# pkg-resources-removal-hook
git pre-commit hook for removing pkg-resources from requirements.txt

**Update:** `requirements-txt-fixer` from [`pre-commit-hooks`](https://github.com/pre-commit/pre-commit-hooks)
has the same functionality as this hook along with sorting the requirements. 
So the only reason for using this is if you just want pkg-resources to be 
removed without sorting the requirements file. 

## About
In some cases when using `virtualenv` on ubuntu pip freeze may return 
`pkg-resources` as a result of bad metadata provided by ubuntu to `pip`. If we 
use freeze to generate `requrements.txt` file the presence of `pkg-resources` 
may break the installation using the requirements file. This hook checks for 
presence of `pkg-resources` within the requirements file and removes it before
committing the changes.

## Usage
You can use the hook by renaming the `remove.py` file to `pre-commit` and moving
it to `.git/hooks/`. Assuming you are in the root of your project and have 
already initialized a git repo you can use the following command:
```shell script
wget https://raw.githubusercontent.com/AleksaC/pkg-resources-removal-hook/master/pkg_resources_removal/remove.py -O .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
``` 
### With [pre-commit](https://pre-commit.com/)
Add the following lines to `.pre-commit-config.yaml`
```yaml
repos:
  - repo: https://github.com/AleksaC/pkg-resources-removal-hook
    rev: master
    hooks:
      - id: pkg-resources-removal
        args: [--auto-add]
```
