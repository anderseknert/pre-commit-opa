#!/usr/bin/env python3
"""OPA fmt pre-commit hook"""

import sys
import subprocess


def main():
    """Runs 'opa test' in git root directory or one provided in args"""
    print(sys.argv)
    process = subprocess.run(
        ['opa', 'test'] + sys.argv[1:], capture_output=True
    )

    if process.returncode > 0:
        sys.exit(process.stderr.decode('utf-8'))


if __name__ == '__main__':
    main()
