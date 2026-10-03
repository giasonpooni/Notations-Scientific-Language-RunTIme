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

**Notation Systems Inc** is the parent organization: a scientific computing and systems engineering company developing computational instruments, software and interactive environments for understanding and building physical and virtual systems.

The company's development direction connects measurement, state estimation and sensor fusion, scientific modelling, simulation and execution, from materials and machines to interactive worlds.

| Division | Focus |
| --- | --- |
| **Notations Gaming** | Games, graphics, world building, interactive environments and gameplay simulation. |
| **Notations Manufacturing** | Design, machinery integration, process development, fabrication and production systems. |
| **Notations Laboratories** | Research and experimental validation in scientific computing, measurement, physics and chemistry modelling, materials and simulation. |

**Repository role:** This repository documents the shared **Notation Systems Inc** declarative front end for compiling scientific investigation intent into typed contracts. Its broader direction connects physical and virtual system investigations to existing instruments; NET retains session composition and execution, and NISE retains schematic construction.
