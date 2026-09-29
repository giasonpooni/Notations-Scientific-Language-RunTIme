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
