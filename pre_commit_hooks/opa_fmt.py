#!/usr/bin/env python3
"""OPA fmt pre-commit hook"""

import sys
import subprocess


def main():
    """Runs 'opa fmt -w' on any files provided as arguments"""
    process = subprocess.run(
        ['opa', 'fmt', '-w'] + sys.argv[1:],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )

    if process.returncode > 0:
        message = process.stdout.decode('utf-8')

        sys.exit(message)


if __name__ == '__main__':
    main()
