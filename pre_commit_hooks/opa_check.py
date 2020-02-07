#!/usr/bin/env python3
"""OPA check pre-commit hook"""

import sys
import subprocess


def main():
    """Runs 'opa check' on any files provided as arguments"""
    process = subprocess.run(
        ['opa', 'check'] + sys.argv[1:], capture_output=True
    )

    if process.returncode > 0:
        sys.exit(process.stdout.decode('utf-8'))


if __name__ == '__main__':
    main()
