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

## Instrument role

[NET](https://github.com/atomtrapping/Notations-Systems-Terminal) retains composition and execution history. [NISE](https://github.com/atomtrapping/Notations-Inference-Schematics-Engine) constructs bounded candidate schematics; specialist instruments retain their mathematics; governed evidence and creative game state keep their separate authorities.

[Current organization](#organization) · [Historical research protocol](https://github.com/atomtrapping/Notations-Systems-Terminal/blob/b41b84922d4963a9206202029afd1e78b9451f9c/RESEARCH_PROGRAMME.md)

## Research profile

**Question:** what user intent can a bounded notation express without losing the semantics required by the receiving instrument?

Evaluate parser acceptance/refusal, round-trip meaning, source identity, NISE contract compatibility and preservation of unresolved capabilities. Compare user effort and error rates against direct contract authoring on fixed tasks. Mathematical sufficiency and practical usability are distinct tests.

Extend the existing contracts and workbench rather than creating a second universal IR or scheduler. Python, Julia, Rust and C++ may implement future bindings; CUDA is a provider-specific execution choice, not a language property. A typecheck or successful parse is not a proof of the scientific model.
