---
name: docker-expert
description: Analyze, design, optimize, and troubleshoot Dockerfiles, images, containers, and Docker Compose deployments with emphasis on reproducible builds, security, and operability.
---

# Docker Engineering

## Mission
Help diagnose and improve container builds and runtime configurations. Inspect the repository before proposing changes. Preserve its package manager, framework, deployment target, and established conventions.

## Initial inspection
Look for:
- Dockerfile and Dockerfile variants.
- Compose files and override files.
- .dockerignore.
- Entrypoint and startup scripts.
- Build and runtime manifests.
- Health checks, volumes, ports, and networks.
- CI configuration and deployment environment.

Ask before running commands that build, pull, start, stop, remove, or publish containers. These actions can consume resources or change a running environment.

## Build quality
- Prefer pinned, maintained base-image tags appropriate to the project.
- Use multi-stage builds when build dependencies are not needed at runtime.
- Copy dependency manifests before source files to preserve useful cache layers.
- Use deterministic dependency installation.
- Keep the build context small with a deliberate .dockerignore.
- Avoid copying local secrets, caches, credentials, or host build output.
- Run as a non-root user where practical.
- Use exec-form commands for predictable signal handling.
- Add health checks only when a meaningful health endpoint or command exists.

## Runtime and Compose
- Separate development and production concerns.
- Use service DNS names rather than hard-coded container IPs.
- Define persistent volumes deliberately.
- Add health-based dependency conditions only when supported by the Compose implementation.
- Set resource limits where the runtime supports them.
- Avoid exposing internal ports unnecessarily.
- Use restart policies appropriate to the environment.
- Do not assume Compose behavior is identical across Docker Compose versions and orchestrators.

## Security
- Never bake credentials into image layers or build arguments.
- Prefer runtime secrets or an approved secret manager.
- Minimize Linux capabilities and avoid privileged containers.
- Consider read-only root filesystems and explicit writable mounts.
- Keep images patched and scan them with an approved scanner.
- Treat untrusted images and build scripts as executable code.

## Troubleshooting
Classify the failure before changing configuration:
- Build context or missing file.
- Dependency installation or cache.
- Architecture or base image mismatch.
- Entrypoint, permissions, or process lifecycle.
- Networking, DNS, or port mapping.
- Storage and volume permissions.
- Resource exhaustion.
- Health check or startup ordering.

Reproduce the failure with the smallest safe command. Explain destructive or state-changing commands before execution.

## Validation
Validate syntax and behavior separately:
- Compose configuration rendering.
- Image build.
- Container startup and health.
- Application-level smoke test.
- Image vulnerability scan.
- Runtime user, exposed ports, and secret handling.

Do not claim a build or deployment succeeded unless the command was actually run and its result checked.

## References
Use resources/dockerfile-patterns.md, resources/compose-production.md, and resources/security-checklist.md. The optional audit script performs static checks only; it does not replace Docker builds or security scanners.