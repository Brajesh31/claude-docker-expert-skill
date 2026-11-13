# Production Compose Guidance

## Service definition
For each service, document its purpose, image/build source, startup command, exposed ports, dependencies, and persistence needs.

## Networking
Use named networks to isolate service groups. Containers should communicate through service names and internal ports. Publish only ports that must be reachable from outside the Compose network.

## Persistence
Use named volumes for durable application data. Bind mounts are useful for development but require careful host-path permissions in production.

## Configuration
Keep non-secret configuration in environment files or deployment configuration. Inject secrets through an approved runtime secret mechanism. Never commit populated secret files.

## Health and startup
A depends_on relationship alone does not prove that a dependency is ready. Use health checks and supported condition syntax where appropriate, and make applications resilient to temporary dependency failures.

## Operations
Define logging expectations, backup and restore procedures, resource limits, restart policy, upgrade steps, and rollback procedure. Validate the rendered Compose model before deployment.