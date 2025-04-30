# python-extension-project
Clean c++ and nanobind python project base using VSCode, vcpkg, pyproject.toml, uv, ruff

Currently the workflow is through a wheel so this takes much longer
than desired.  Need to implement an in-situ dev cycle for the extension.

Build the full wheel in powershell tyerminal with active venv:
> pip install -e .

The execute python tests with:
> pytest
