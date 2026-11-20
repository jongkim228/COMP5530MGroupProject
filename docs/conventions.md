# Conventions

## Coordinate frames

- The world origin is `(0, 0, 0)` at the centre of the MuJoCo ground plane.
- World axes follow MuJoCo: positive X is right/forward in the model view, positive Y is left, and positive Z is up.
- The left arm is mounted on negative X; the right arm is mounted on positive X.
- Every function must document whether a pose is expressed in world, base, or arm frame.

## Units

- Length: metres
- Angles: radians
- Time: seconds
- Force: newtons
- Torque: newton-metres
- Velocities: metres per second or radians per second

## Timing

- Shared model timestep: `0.002` seconds.
- Control code must use the shared timestep unless a documented high-level controller has a lower frequency.
- Integrators must not silently change timestep or control frequency.

## Naming

- Python modules and functions use `snake_case`.
- Python classes use `PascalCase`.
- XML bodies, geoms, joints and sites use `snake_case`.
- Arm names are `left` and `right`.
- Task folders correspond to task numbers and subsystem names.

## Git

- Branches use `taskN/short-description`.
- Commit messages use `taskN: short description`.
- Fix broken `main` before starting unrelated work.
