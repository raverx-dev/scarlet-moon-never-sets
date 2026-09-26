# Inert deployment notes

Nothing in this directory is installed. Do not copy the unit into `/etc` or start it from this tree.

The service launches Chromium through `qa/service/chromium-confine.sh`. Bubblewrap must be installed at `/usr/bin/bwrap`, and the Chromium binary must resolve under `/usr`. The launcher fails closed when either is missing, when `--no-sandbox` is requested, or when the browser profile is outside `/tmp` or `/dev/shm`. It uses a new pid namespace and a fresh `/proc`, closes inherited file descriptors above stderr, and does not mount `/home` or `/run`. Local tests observed that this hides a fake credential, denies ptrace and `/proc/<parent>` access, and still lets Chromium's own seccomp sandbox start. Those tests ran as the current unprivileged user. They are not a dedicated-user or SELinux qualification.

`LoadCredential=qa-secret:/etc/scarlet-qa/qa-secret` is the root-controlled source. Do not create that file in this tree, and do not place the secret under `/var/lib/scarlet-qa`. systemd presents the loaded bytes as `$CREDENTIALS_DIRECTORY/qa-secret`. The launcher's temporary `/run` is what keeps that loaded file out of the browser's mount namespace. A process that is not inside the launcher can still read it if it shares the service uid.

Provision commit `d7054d2b9b111ff711f44cc3ee5b71268aca6ed8` with `stage-pinned-source.mjs` into a path that does not yet exist, then keep `/opt/scarlet-qa/pinned-source` root-owned and read-only. The command refuses an existing destination and does not delete one. Replacing a pin later is a separate reviewed procedure.

The unit's `IPAddressDeny=any` and `IPAddressAllow=localhost` lines are proposed only. The launcher deliberately shares the host network so the existing loopback game server remains reachable, and that shared network still allows external TCP until an OS policy denies it. Dedicated-user execution, SELinux domain, resource limits, and any trusted ingress are UNQUALIFIED until they are tested on the actual host. This unit has not been installed.
