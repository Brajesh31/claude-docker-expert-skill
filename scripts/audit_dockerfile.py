#!/usr/bin/env python3
"""Run conservative static checks against a Dockerfile; does not build images."""

from __future__ import annotations
import argparse
import re
from pathlib import Path

CHECKS = [
    ("floating-latest", re.compile(r"^\s*FROM\s+\S+:latest\b", re.I), "Base image uses the floating latest tag."),
    ("root-user", re.compile(r"^\s*USER\s+root\s*$", re.I), "Dockerfile explicitly switches to root."),
    ("add-instead-copy", re.compile(r"^\s*ADD\s+https?://", re.I), "Remote URL is fetched with ADD; prefer a verified download step."),
    ("secret-env", re.compile(r"^\s*ENV\s+\w*(TOKEN|PASSWORD|SECRET|API_KEY)\w*\s*=", re.I), "Possible secret is declared in ENV."),
    ("shell-cmd", re.compile(r"^\s*CMD\s+[^\[]", re.I), "CMD uses shell form; review signal handling."),
]

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dockerfile", type=Path)
    args = parser.parse_args()
    if not args.dockerfile.is_file():
        parser.error(f"File not found: {args.dockerfile}")
    lines = args.dockerfile.read_text(encoding="utf-8", errors="replace").splitlines()
    findings = []
    for number, line in enumerate(lines, 1):
        for code, pattern, message in CHECKS:
            if pattern.search(line):
                findings.append((number, code, message))
    if not any(re.match(r"^\s*USER\s+", line, re.I) for line in lines):
        findings.append((0, "no-user-directive", "No USER directive found; verify runtime identity."))
    if not any(re.match(r"^\s*HEALTHCHECK\s+", line, re.I) for line in lines):
        findings.append((0, "no-healthcheck", "No HEALTHCHECK directive found; add one only if a meaningful probe exists."))
    if findings:
        for number, code, message in findings:
            location = f"line {number}" if number else "file"
            print(f"{location}: [{code}] {message}")
    else:
        print("No configured static checks were triggered.")
    print("Static checks only. Review context and run real build/security validation separately.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
