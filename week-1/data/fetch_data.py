#!/usr/bin/env python3
"""Download the Week 1 dataset.

    python fetch_data.py

Puts three CSV files next to this script. Re-run it any time; it overwrites.
No account, no login, no API key needed.
"""
import pathlib
import urllib.request

BASE = "https://hypha.aicell.io/ddls-course/artifacts/2026-week1/files"
FILES = ["compounds.csv", "screen_wells.csv", "followup_assays.csv"]

here = pathlib.Path(__file__).parent
for name in FILES:
    dest = here / name
    print(f"downloading {name} ... ", end="", flush=True)
    urllib.request.urlretrieve(f"{BASE}/{name}", dest)
    print(f"{dest.stat().st_size / 1e6:.1f} MB")

print(f"\nDone. {len(FILES)} files in {here.resolve()}")
