# pre-commit-opa

Pre-commit git hooks for Open Policy Agent (OPA) and Rego development

### Using pre-commit-opa with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
- repo: https://github.com/anderseknert/pre-commit-opa
  rev: v1.0.0
  hooks:
  - id: opa-fmt
  - id: opa-check
  - id: opa-test
```
