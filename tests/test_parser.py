from pathlib import Path
import json
import subprocess
import sys

import pytest

from nslr.parser import compile_source, parse_source

ROOT = Path(__file__).resolve().parents[1]
SOURCE = (ROOT / "examples" / "bearing.nsl").read_text()


def test_canonical_source_compiles_to_nise_query():
    result = compile_source(SOURCE)
    query = result["query"]
    assert result["output_schema"] == "nise.query.v1"
    assert query["query_id"] == "bearing-vibration-investigation"
    assert query["focus_node_ids"] == ["bearing_04"]
    assert query["requested_capabilities"] == [
        "signal.spectrum.v1", "state.estimate.v1", "fault.classify.v1"]
    assert query["max_hops"] == 2
    assert query["node_budget"] == 32
    assert query["include_hypotheses"] is False
    assert result["claims"]["semantic_retrieval_performed"] is False
    assert result["claims"]["provider_execution"] is False


def test_comments_and_blank_lines_do_not_change_query():
    left = parse_source(SOURCE)
    right = parse_source("\n# another comment\n" + SOURCE + "\n")
    assert left == right


@pytest.mark.parametrize("source", [
    "query q\nquestion \"x\"\n",
    "query q\nquestion \"x\"\nfocus a\nunknown thing\n",
    "query q\nquestion \"x\"\nfocus a\nuse bad\n",
    "query q\nquestion \"x\"\nfocus a\nhops 7\n",
    "query q\nquestion \"x\"\nfocus a\nbudget 0\n",
    "query q\nquestion \"x\"\nfocus a\nhypotheses maybe\n",
    "query q\nquery q2\nquestion \"x\"\nfocus a\n",
    "query q\nquestion \"x\"\nfocus a\nfocus a\n",
])
def test_invalid_language_refuses(source):
    with pytest.raises(ValueError):
        parse_source(source)


def test_cli_create_only_output(tmp_path):
    output = tmp_path / "query.json"
    subprocess.run([
        sys.executable, "-m", "nslr.cli", "compile",
        str(ROOT / "examples" / "bearing.nsl"),
        "--output", str(output),
    ], check=True, cwd=tmp_path)
    value = json.loads(output.read_text())
    assert value["schema"] == "nslr.compilation.v1"
    second = subprocess.run([
        sys.executable, "-m", "nslr.cli", "compile",
        str(ROOT / "examples" / "bearing.nsl"),
        "--output", str(output),
    ], text=True, capture_output=True, cwd=tmp_path)
    assert second.returncode == 1
