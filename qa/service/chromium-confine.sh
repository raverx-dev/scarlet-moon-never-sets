#!/bin/bash
# Fail-closed Chromium launcher. Playwright invokes this as the browser executable.
# Shared networking is intentional and is not an egress control.
set -euo pipefail

if [ "${QA_BROWSER_CONFINEMENT:-required}" = "off" ]; then
  echo "chromium-confine.sh does not provide an unrestricted browser" >&2
  exit 69
fi

bwrap_bin="${QA_BWRAP:-/usr/bin/bwrap}"
if [ ! -x "$bwrap_bin" ]; then
  echo "browser confinement unavailable: bubblewrap is required" >&2
  exit 69
fi

# Playwright's Chromium transport uses descriptors 3 and 4. Close every other
# inherited descriptor so a leaked credential file cannot be read.
for n in $(seq 5 255); do
  eval "exec ${n}>&-" || true
done

for arg in "$@"; do
  case "$arg" in
    --no-sandbox|--no-sandbox=*|--disable-setuid-sandbox|--disable-setuid-sandbox=*)
      echo "refusing to disable the Chromium sandbox" >&2
      exit 69
      ;;
  esac
done

resolve_chrome() {
  local candidate real stripped
  local -a candidates=()
  if [ -n "${BROWSER_BIN:-}" ]; then
    candidates+=("$BROWSER_BIN")
  fi
  candidates+=(
    /usr/lib64/chromium-browser/chromium-browser
    /usr/lib/chromium-browser/chromium-browser
    /usr/bin/chromium
    /usr/bin/google-chrome-stable
    /usr/bin/google-chrome
  )
  for candidate in "${candidates[@]}"; do
    [ -e "$candidate" ] || continue
    real=$(readlink -f "$candidate") || continue
    case "$real" in
      /usr/*) ;;
      *)
        echo "refusing Chromium executable outside /usr" >&2
        exit 69
        ;;
    esac
    case "$real" in
      *.sh)
        stripped="${real%.sh}"
        if [ -x "$stripped" ]; then real=$stripped; fi
        ;;
    esac
    if [ -f "$real" ] && [ -x "$real" ]; then
      printf '%s\n' "$real"
      return 0
    fi
  done
  echo "no confined Chromium executable is available" >&2
  exit 69
}

user_data=""
previous=""
for arg in "$@"; do
  case "$arg" in
    --user-data-dir=*) user_data="${arg#--user-data-dir=}" ;;
  esac
  if [ "$previous" = "--user-data-dir" ]; then user_data=$arg; fi
  previous=$arg
done
if [ -n "$user_data" ]; then
  case "$user_data" in
    /tmp/*|/dev/shm/*) ;;
    *)
      echo "refusing user-data-dir outside /tmp or /dev/shm" >&2
      exit 69
      ;;
  esac
  case "$user_data" in
    *..*)
      echo "refusing user-data-dir with parent segments" >&2
      exit 69
      ;;
  esac
  if [ -e "$user_data" ]; then
    real_data=$(readlink -f "$user_data")
    case "$real_data" in
      /tmp/*|/dev/shm/*) ;;
      *)
        echo "refusing user-data-dir that escapes its temporary directory" >&2
        exit 69
        ;;
    esac
  fi
fi

saved_lang="${LANG:-}"
saved_lc_all="${LC_ALL:-}"
probe="${QA_CONFINE_PROBE:-}"
probe_script="${QA_CONFINE_PROBE_SCRIPT:-}"
host_pid="${HOST_PID:-}"
secret_path="${SECRET_PATH:-}"

wrap=(
  --ro-bind /usr /usr
  --ro-bind /lib64 /lib64
  --ro-bind-try /lib /lib
  --ro-bind-try /etc/fonts /etc/fonts
  --ro-bind-try /etc/ssl /etc/ssl
  --ro-bind-try /etc/pki /etc/pki
  --proc /proc
  --dev /dev
  --tmpfs /tmp
  --tmpfs /dev/shm
  --tmpfs /home
  --tmpfs /run
  --die-with-parent
  --unshare-user
  --unshare-pid
  --unshare-uts
  --unshare-ipc
  --share-net
  --clearenv
  --setenv PATH /usr/bin:/bin
  --setenv HOME /tmp
)
if [ -n "$saved_lang" ]; then wrap+=(--setenv LANG "$saved_lang"); fi
if [ -n "$saved_lc_all" ]; then wrap+=(--setenv LC_ALL "$saved_lc_all"); fi

if [ "$probe" = "1" ]; then
  case "$probe_script" in
    /tmp/*) ;;
    *)
      echo "refusing confinement probe script outside /tmp" >&2
      exit 69
      ;;
  esac
  [ -f "$probe_script" ] || { echo "confinement probe script is missing" >&2; exit 69; }
  wrap+=(--ro-bind "$probe_script" /tmp/probe.py)
  if [ -n "$host_pid" ]; then wrap+=(--setenv HOST_PID "$host_pid"); fi
  if [ -n "$secret_path" ]; then wrap+=(--setenv SECRET_PATH "$secret_path"); fi
  exec "$bwrap_bin" "${wrap[@]}" -- /usr/bin/python3 /tmp/probe.py
fi

chrome=$(resolve_chrome)
if [ -n "$user_data" ]; then
  wrap+=(--bind "$user_data" "$user_data")
fi
exec "$bwrap_bin" "${wrap[@]}" -- "$chrome" "$@"
