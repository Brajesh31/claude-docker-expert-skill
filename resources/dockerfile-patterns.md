# Dockerfile Patterns

## Cache-friendly build
Copy lockfiles and dependency manifests before application source. Install dependencies using the project's lockfile-preserving command. Copy source only after dependencies are installed.

## Multi-stage build
Use separate stages for dependencies, compilation, and runtime when the toolchain is not needed in production. Copy only required runtime artifacts into the final stage.

## Runtime image
- Use a small maintained base image compatible with native dependencies.
- Set an explicit working directory.
- Copy files with appropriate ownership.
- Run as a non-root user.
- Use exec-form CMD or ENTRYPOINT.
- Document the listening port with EXPOSE when useful.
- Add a health check only if the application has a reliable health probe.

## .dockerignore
Consider excluding:
- Version-control metadata.
- Local dependency directories.
- Build output not needed by the image.
- Test artifacts and coverage.
- Editor and operating-system files.
- Local environment files and credentials.

Review every exclusion against the build requirements. A broad pattern can accidentally remove required source files.

## Anti-patterns
- Using latest for production base images without a deliberate update policy.
- Installing packages without pinning or reproducibility.
- Copying the entire repository before dependency installation.
- Running as root without justification.
- Storing secrets in ARG, ENV, or image layers.
- Using shell-form startup commands when signal handling matters.