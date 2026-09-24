"""Run the Unix-oriented paper workflow on Windows without patching the repo."""

from __future__ import annotations

import os
import runpy


if not hasattr(os, "fchmod"):
    os.fchmod = lambda _fd, _mode: None  # type: ignore[attr-defined]

runpy.run_module("scripts.paper_contribution", run_name="__main__")
