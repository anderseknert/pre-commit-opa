# pre-commit-opa

![Python application](https://github.com/anderseknert/pre-commit-opa/workflows/build/badge.svg)

[Pre-commit](https://pre-commit.com/) git hooks for Open Policy Agent (OPA) and Rego development

### Using pre-commit-opa with pre-commit

Add the `pre-commit-opa` repo to the `.pre-commit-config.yaml` file in your git root directory, and add any number of the available hooks:

```yaml
- repo: https://github.com/anderseknert/pre-commit-opa
  rev: v1.2.0
  hooks:
  - id: opa-fmt
  - id: opa-check
  - id: opa-test
  - id: conftest-test
  - id: conftest-verify
```

Once saved, run `pre-commit install` to instal git pre-commit hooks.

### Hooks available

#### `opa-fmt`
Runs `opa fmt` on any rego file about to be commited.

#### `opa-check`
Runs `opa check` on any rego file about to be commited.

#### `opa-test`
If rego files are present in commit, runs `opa test` in git root directory.

#### `conftest-test`
Runs `conftest test` on any configuration file format supported by conftest.

#### `conftest-verify`
If rego files are present in commit, runs `conftest verify` in git root directory.
