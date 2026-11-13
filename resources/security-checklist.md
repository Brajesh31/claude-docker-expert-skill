# Docker Security Checklist

- [ ] Base images are maintained and versioned deliberately.
- [ ] Dependency versions are reproducible.
- [ ] Build context excludes secrets and irrelevant local files.
- [ ] No credentials are embedded in image layers, ARG, or ENV.
- [ ] Runtime process uses a non-root identity where feasible.
- [ ] Privileged mode is avoided.
- [ ] Linux capabilities are minimized.
- [ ] Writable paths and volumes are explicit.
- [ ] Host ports are limited to required services.
- [ ] Images are scanned with an approved vulnerability scanner.
- [ ] Logs do not expose secrets or personal data.
- [ ] Container shutdown handles termination signals.
- [ ] Backup and restore behavior is documented.

A static review cannot prove a container is secure. Record scanner results, runtime assumptions, and unresolved risks separately.