# Notations Scientific Language Runtime

**A bounded declarative language front end for Notation Systems scientific workflows.**

The runtime compiles concise scientific intent into typed machine-readable
contracts. Its first target is NISE:

```text
scientific intent
      ↓
NSL Runtime
      ↓
nise.query.v1
      ↓
NISE
      ↓
candidate inference schematic
```

It deliberately does **not** own graph traversal, evidence ranking, state
estimation, provider execution, or physical truth.

## NSL V1

Example:

```text
query bearing-vibration-investigation
question "What information and instruments are relevant to investigating elevated vibration at bearing_04?"
focus bearing_04
use signal.spectrum.v1
use state.estimate.v1
use fault.classify.v1
hops 2
budget 32
hypotheses off
```

Compile it:

```sh
python -m pip install -e '.[dev]'
nsl compile examples/bearing.nsl --output query-compilation.json
python -m pytest
```

The output is `nslr.compilation.v1` containing an exact `nise.query.v1`.
The language never accepts Python/Julia/C++/shell source, executable paths,
provider IDs, container images, or release/actuation authority.

### Statements

| Statement | Meaning |
|---|---|
| `query ID` | stable query identity |
| `question "TEXT"` | retained human question |
| `focus NODE_ID` | explicit NISE focus identity |
| `use capability.v1` | explicit requested semantic capability |
| `hops N` | NISE graph traversal bound, 0..6 |
| `budget N` | selected-node budget, 1..256 |
| `hypotheses on/off` | explicit hypothesis inclusion policy |

The question text is **not interpreted semantically by this runtime**. Future
language extensions may propose structured terms, but execution and truth
authority remain outside the language compiler.

## Boundary

- **Scientific Language Runtime**: intent → typed contract.
- **NISE**: typed query + catalog → candidate schematic.
- **NET**: qualified execution/composition.
- **Specialist instruments**: numerical/domain computation.

MPL-2.0.

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
