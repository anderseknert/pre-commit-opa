#!/usr/bin/env python3

import os
import sys
import subprocess

def main():
    command = ['opa', 'check'] + sys.argv[1:]
    process = subprocess.Popen(command)

    if process:
        if process.returncode > 0:
            sys.exit(process.stderr)
    else:
        sys.exit('Failed to start OPA - please ensure it is installed and on $PATH')

if __name__ == '__main__':
    main()

