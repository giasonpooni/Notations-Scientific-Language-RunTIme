# Notations Scientific Language Runtime

A small declarative language front end for Notation Systems scientific workflows.

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
