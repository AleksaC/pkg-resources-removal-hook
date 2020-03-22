# pkg-resources-removal-hook
git pre-commit hook for removing pkg-resources from requirements.txt

## About
In some cases when using `virtualenv` on ubuntu pip freeze may return 
`pkg-resources` as a result of bad metadata provided by ubuntu to `pip`. If we 
use freeze to generate `requrements.txt` file the presence of `pkg-resources` 
may break the installation using the requirements file. This hook checks for 
presence of `pkg-resources` within the requirements file and removes it before
committing the changes.

## Usage
You can use the hook by renaming the `remove.py` file to `pre-commit` and moving
it to `.git/hooks/`
### With [pre-commit](https://pre-commit.com/)
Add the following lines to `.pre-commit-config.yaml`
```yaml
repos:
  - repo: https://github.com/AleksaC/pkg-resources-removal-hook
    rev: 5727d8f
    hooks:
      - id: pkg-resources-removal
```
