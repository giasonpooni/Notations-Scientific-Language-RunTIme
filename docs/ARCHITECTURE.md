# Architecture

NSL Runtime is a parser/compiler, not a workflow engine.

V1 grammar is line-oriented and intentionally small. It compiles directly to the
public `nise.query.v1` data contract established by NISE.

The compiler retains a SHA-256 identity of the exact source and records that it
performed no semantic retrieval, provider execution, or physical inference.

The language does not contain engine names. A user asks for semantic capabilities
such as `signal.spectrum.v1`; later systems decide which qualified engine, if any,
implements that meaning.

## Why separate this from NISE?

Keeping language parsing separate means:

- NISE can accept queries produced by GUIs, agents, APIs or files;
- language syntax can evolve without changing schematic construction;
- NISE traversal remains deterministic and testable;
- a language parser cannot silently acquire evidence/truth authority.
