# Notations Scientific Language Runtime

A small declarative language front end for Notation Systems Inc scientific workflows.

The runtime's first responsibility is intentionally narrow:

> Compile concise scientific investigation intent into typed machine-readable contracts.

For NISE, that means:

```text
scientific intent
    ↓
Notations Scientific Language Runtime
    ↓
nise.query.v1
    ↓
NISE schematic construction
```

The Scientific Language Runtime does **not** own NISE graph traversal, evidence ranking, state estimation, provider execution, or physical truth.

Implementation work proceeds on reviewable branches.

## Organization

**Notation Systems Inc** is the parent organization.

| Division | Focus |
| --- | --- |
| **Notations Gaming** | Games, graphics and interactive worlds. |
| **Notations Manufacturing** | Industrial design, materials and manufacturing systems. |
| **Notations Laboratories** | Research, scientific computing, simulation and experimental validation. |

This repository is shared **Notation Systems Inc** tooling for declarative scientific workflows, supporting all three divisions.
