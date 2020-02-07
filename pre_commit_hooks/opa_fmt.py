#!/usr/bin/env python3
"""OPA fmt pre-commit hook"""

import sys
import subprocess


def main():
    """Runs 'opa fmt -w' on any files provided as arguments"""
    process = subprocess.run(
        ['opa', 'fmt', '-w'] + sys.argv[1:], capture_output=True
    )

    if process.returncode > 0:
        sys.exit(process.stderr)


if __name__ == '__main__':
    main()
