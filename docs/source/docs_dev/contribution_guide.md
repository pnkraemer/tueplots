# Contribution guide

Install `tueplots` with all ci-related dependencies via
```
pip install .[ci]
```
Run all checks via
```
tox
```
or only run the tests via
```
tox -e pytest
```
or use tox (which also runs the linter, and the python-code-snippets in this readme).
```
tox
```
The CI checks for compliance of the code with black and isort, and runs the tests and the notebooks.
To automatically satisfy the former, there is a pre-commit that can be used (do this once):
```
pip install pre-commit
pre-commit install
```
From then on, your code will be checked for isort and black compatibility automatically.
