"""Local checks for the Pitch-Off entry.

Run with: python3 -m pytest test_entry.py
(or plain python3 test_entry.py)
"""

import os
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from main import LINE


def run_once(out_dir: str) -> str:
    env = dict(os.environ, MAKEFUN_OUTPUT_DIR=out_dir)
    subprocess.run(
        [sys.executable, "-P", "-s", "main.py"],
        cwd=os.path.dirname(os.path.abspath(__file__)),
        env=env,
        check=True,
    )
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as fh:
        return fh.read()


def test_window() -> None:
    # The sealed scorer accepts UTF-8 text of 1 to 200 characters.
    assert 1 <= len(LINE) <= 200


def test_one_sentence_one_line() -> None:
    assert "\n" not in LINE
    assert LINE.count(".") == 1 and LINE.endswith("dodged.")


def test_deterministic() -> None:
    with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
        assert run_once(a) == run_once(b) == LINE


if __name__ == "__main__":
    test_window()
    test_one_sentence_one_line()
    test_deterministic()
    print("all checks passed")
