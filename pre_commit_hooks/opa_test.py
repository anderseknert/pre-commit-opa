#!/usr/bin/env python3
"""OPA fmt pre-commit hook"""

import sys
import subprocess


def main():
    """Runs 'opa test' in git root directory"""
    process = subprocess.run(
        ['opa', 'test', '.'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )

    if process.returncode > 0:
        message = process.stdout.decode('utf-8')

        sys.exit(message)


if __name__ == '__main__':
    main()
