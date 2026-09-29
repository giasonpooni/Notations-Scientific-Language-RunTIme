"""Bounded declarative scientific-intent parser.

V1 compiles text into nise.query.v1 only. It executes no providers and performs
no graph traversal, retrieval, model fitting, evidence admission, or actuation.
"""
from __future__ import annotations

import hashlib
import json
import re
import shlex
from typing import Any

ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:/-]{0,159}$")
CAP = re.compile(r"[a-z][a-z0-9_-]*(?:\.[a-z][a-z0-9_-]*)+\.v[1-9][0-9]*$")
MAX_SOURCE = 64 * 1024
MAX_LINES = 256
MAX_CAPABILITIES = 64
MAX_FOCUS = 64


def _id(value: str) -> str:
    if ID.fullmatch(value) is None:
        raise ValueError("Invalid bounded identifier")
    return value


def _capability(value: str) -> str:
    if CAP.fullmatch(value) is None:
        raise ValueError("Capability must be a versioned semantic identifier")
    return value


def parse_source(source: str) -> dict:
    if type(source) is not str or not source or len(source.encode("utf-8")) > MAX_SOURCE:
        raise ValueError("Scientific source must be nonempty and <=64 KiB")
    lines = source.splitlines()
    if len(lines) > MAX_LINES:
        raise ValueError("Scientific source exceeds line budget")

    query_id = None
    question = None
    focus = []
    capabilities = []
    max_hops = 2
    node_budget = 64
    include_hypotheses = False
    seen_singletons = set()

    for number, raw in enumerate(lines, start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        try:
            parts = shlex.split(line, posix=True)
        except ValueError as exc:
            raise ValueError(f"line {number}: malformed quoting") from exc
        if not parts:
            continue
        command = parts[0]

        if command == "query":
            if len(parts) != 2 or "query" in seen_singletons:
                raise ValueError(f"line {number}: query requires one unique identifier")
            query_id = _id(parts[1])
            seen_singletons.add("query")
        elif command == "question":
            if len(parts) != 2 or "question" in seen_singletons:
                raise ValueError(f"line {number}: question requires one quoted string")
            if not parts[1].strip() or len(parts[1]) > 8192:
                raise ValueError(f"line {number}: question is empty or too long")
            question = parts[1]
            seen_singletons.add("question")
        elif command == "focus":
            if len(parts) != 2:
                raise ValueError(f"line {number}: focus requires one node identity")
            focus.append(_id(parts[1]))
            if len(focus) > MAX_FOCUS:
                raise ValueError("focus count exceeds 64")
        elif command == "use":
            if len(parts) != 2:
                raise ValueError(f"line {number}: use requires one capability")
            capabilities.append(_capability(parts[1]))
            if len(capabilities) > MAX_CAPABILITIES:
                raise ValueError("capability count exceeds 64")
        elif command == "hops":
            if len(parts) != 2 or "hops" in seen_singletons:
                raise ValueError(f"line {number}: hops requires one value")
            try:
                max_hops = int(parts[1])
            except ValueError as exc:
                raise ValueError(f"line {number}: hops must be an integer") from exc
            if not 0 <= max_hops <= 6:
                raise ValueError("hops must be in 0..6")
            seen_singletons.add("hops")
        elif command == "budget":
            if len(parts) != 2 or "budget" in seen_singletons:
                raise ValueError(f"line {number}: budget requires one value")
            try:
                node_budget = int(parts[1])
            except ValueError as exc:
                raise ValueError(f"line {number}: budget must be an integer") from exc
            if not 1 <= node_budget <= 256:
                raise ValueError("budget must be in 1..256")
            seen_singletons.add("budget")
        elif command == "hypotheses":
            if len(parts) != 2 or "hypotheses" in seen_singletons or parts[1] not in {"on", "off"}:
                raise ValueError(f"line {number}: hypotheses must be 'on' or 'off'")
            include_hypotheses = parts[1] == "on"
            seen_singletons.add("hypotheses")
        else:
            raise ValueError(f"line {number}: unsupported statement {command!r}")

    if query_id is None or question is None or not focus:
        raise ValueError("A scientific query requires query, question and at least one focus statement")
    if len(focus) != len(set(focus)):
        raise ValueError("Duplicate focus identity")
    if len(capabilities) != len(set(capabilities)):
        raise ValueError("Duplicate requested capability")

    return {
        "schema": "nise.query.v1",
        "query_id": query_id,
        "question": question,
        "focus_node_ids": focus,
        "requested_capabilities": capabilities,
        "max_hops": max_hops,
        "node_budget": node_budget,
        "include_hypotheses": include_hypotheses,
    }


def compile_source(source: str) -> dict:
    query = parse_source(source)
    source_sha256 = "sha256:" + hashlib.sha256(source.encode("utf-8")).hexdigest()
    return {
        "schema": "nslr.compilation.v1",
        "language": "nsl.v1",
        "source_sha256": source_sha256,
        "output_schema": "nise.query.v1",
        "query": query,
        "claims": {
            "intent_parsed": True,
            "semantic_retrieval_performed": False,
            "provider_execution": False,
            "physical_truth_established": False,
        },
    }
