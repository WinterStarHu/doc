#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reassemble split CHM parts back into .chm files.
Run inside G/chm/. Output goes to reassembled/ (local-only, gitignored).
"""
import glob, re, os, sys

OUTDIR = "reassembled"
os.makedirs(OUTDIR, exist_ok=True)

parts = [p for p in glob.glob("*.part*") if re.search(r"\.part\d+$", p)]
bases = {}
for p in parts:
    b = re.sub(r"\.part\d+$", "", p)
    bases.setdefault(b, []).append(p)

if not parts:
    # also handle already-whole small chms: copy them through
    for f in glob.glob("*.chm"):
        dst = os.path.join(OUTDIR, f)
        if not os.path.exists(dst):
            import shutil; shutil.copyfile(f, dst)
            print("copied whole:", f)

for b, ps in bases.items():
    ps.sort()
    dst = os.path.join(OUTDIR, b)
    if os.path.exists(dst):
        print("skip (exists):", b); continue
    with open(dst, "wb") as out:
        for p in ps:
            out.write(open(p, "rb").read())
    n = len(ps)
    sz = os.path.getsize(dst)
    print(f"reassembled: {b}  ({n} parts -> {sz//1048576}M)")

print("\nDone. Reassembled .chm files are in", OUTDIR + "/ (gitignored, local-only).")
print("To view: open the .chm in a CHM reader, or run 7z x / extract to HTML.")
