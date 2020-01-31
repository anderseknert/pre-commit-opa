#!/usr/bin/env bash

set -e

for file in "$@"; do
  opa fmt "./$(dirname "$file")"
done