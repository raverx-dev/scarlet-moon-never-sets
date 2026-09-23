# Inert deployment notes

Nothing in this directory is installed. Do not copy the unit into `/etc` or start it from this tree.

`scarlet-qa.service` matches the offline-source implementation in this commit. The browser-execution unit has localhost-only address filtering because a QA request no longer runs `git fetch`. Provision commit `d7054d2b9b111ff711f44cc3ee5b71268aca6ed8` separately, as root, into `/opt/scarlet-qa/pinned-source` and leave that directory mode `0555` root-owned. Keep writable runs in `/var/lib/scarlet-qa`, which is the systemd state directory. Do not put the pin inside the state directory: `ProtectSystem=strict` plus `StateDirectory=scarlet-qa` would make that whole directory writable.

The unit starts `/usr/bin/node` directly. It does not call a wrapper script. systemd loads the bearer with `LoadCredential=qa-secret:` and exposes it only as `$CREDENTIALS_DIRECTORY/qa-secret`. The unit does not contain the secret.

Chromium still runs as `scarlet-qa`. `NoNewPrivileges=yes` prevents the setuid `chrome-sandbox` helper from gaining privileges. On this host, headless Chromium activated its seccomp sandbox under `setpriv --no-new-privs` for the current unconfined user. That has not been repeated as `scarlet-qa` under this unit. `MemoryDenyWriteExecute=yes` is omitted until that restricted-user smoke exists.

The same-user credential limitation is unchanged: hiding the secret from the child environment does not stop a process with the service uid from opening `$CREDENTIALS_DIRECTORY/qa-secret`. This unit does not give Chromium a separate mount namespace or user from the Node process. That separation is still required and is not claimed here.

Local tests of this commit did not enable the unit, create the user, or apply firewall, SELinux, or cgroup policy.
