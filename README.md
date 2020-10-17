# pre-commit-opa

![Python application](https://github.com/anderseknert/pre-commit-opa/workflows/build/badge.svg)

[Pre-commit](https://pre-commit.com/) git hooks for Open Policy Agent (OPA) and Rego development

<img src="assets/pre-commit.svg" width=150><img src="assets/opa.png" width=150>

### Using pre-commit-opa with pre-commit

Add the `pre-commit-opa` repo to the `.pre-commit-config.yaml` file in your git root directory, and add any number of the available hooks:

```yaml
repos:
- repo: https://github.com/anderseknert/pre-commit-opa
  rev: v1.3.0
  hooks:
  - id: opa-fmt
  - id: opa-check
  - id: opa-test
  - id: conftest-test
  - id: conftest-verify
```

Once saved, run `pre-commit install` to install git pre-commit hooks.

### Hooks available

#### `opa-fmt`
Runs `opa fmt` on any rego file about to be commited.

Note that any files changed by this hook will need to be re-added (`git add`) to be included in the commit.

#### `opa-check`
Runs `opa check` on any rego file about to be commited.

#### `opa-test`
If rego files are present in commit, runs `opa test` in git root directory.

Since it doesn't make sense to only provide `opa test` with the files changed (as these might not include tests), the default is to run `opa test .` in the project root directory. If you keep your policies, tests and data in a specific directory, you'll likely want to change this by pointing out the location of that, like:

```yaml
- id: opa-test
  args: ['my/policies', 'my/other/policies/']
```

#### `conftest-test`
Runs `conftest test` on any configuration file format supported by conftest.

Just like with `opa-test` you'll likely want to specify the location of your conftest policies, and possibly what type of files changed should trigger the hook:

```yaml
- id: conftest-test
  args: ['--policy', 'conftest/policy']
  files: conftest/.*\.yaml$
```

#### `conftest-verify`
If rego files are present in commit, runs `conftest verify` in git root directory.
