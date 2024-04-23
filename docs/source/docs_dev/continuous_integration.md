# Continuous integration


Install `tueplots` with all ci-related dependencies via
```
pip install .[ci]
```


## Tox
Run all checks via
```
tox
```
or only run the tests via
```
tox -e test
```
or only run the linter via
```commandline
tox -e format-and-lint
```

## Pre-commit hook
The CI checks for compliance of the code with black and isort, and runs the tests and the notebooks.
To automatically satisfy the former, there is a pre-commit that can be used (do this once):
```
pip install pre-commit
pre-commit install
```
From then on, your code will be checked for isort and black compatibility automatically.


Both the pre-commit hook and tox point to isort, black, and so on.
We do our best to match their versions. If you run into version conflicts
between those two tools, please let us know!
