# Adding Python Packages

* `setup.py` = contains the list of Python packages used (with version numbers if necessary).
* `requirements.txt` = a pinned list of the Python packages and used for deployment.

In development:

1. Add or remove required packages in `pyproject.toml`.
2. Freeze the package list using `python -m piptools compile -o requirements.txt pyproject.toml && echo "-e ." >> requirements.txt`.
The local files are added using a relative path with `-e .` so they can be accessed
in development, test and production environments.
3. Run `pip install -Ur requirements.txt` to install the packages.
to generate the frozen list of packages and their dependencies for testing and deployment.

## Why?

This approach answers the questions:

* *What do we want?*: the packages specified in `setup.py`.
together with comments about the reasons for their inclusion.
If need be the package can be pinned to a specific version.
* *What are we using?*: the packages specified in `requirements.txt`,
which is generated via `pip-compile` (part of [pip-tools](https://github.com/jazzband/pip-tools))
to ensure that the correct
dependent packages are used.
* *How do we upgrade?* Using `pip-compile` to regenerate `requirements.txt`
keeps the upgrade process under out control
and `pip-compile` resolves dependencies between requested packages.
Changes to the `requirements.txt` file are automatically picked up
in the `git diff` before committing.

## Keeping Up To Date

Where development environments are long lived
if is possible for the installed packages to drift away from the list in `requirements.txt`.
So a Git `post-merge` hook is provided
in the Ansible `cloud_controller` role
(see below)
to ensure that the installed packages in the remote development environment
are kept up to date with the list in `requirements.txt`.

```bash
# Ensure that the installed packages are up to date and the developer docs are available.
pip install -r requirements.txt
mkdocs build
```