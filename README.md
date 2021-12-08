# TUEplots

Plot-configurations for scientific publications, purely based on matplotlib.

## Usage

Please have a look at the examples in the example/ directory.

## Contribution

Tests are run with pytest.
You can use tox (you only have to install tox once):
```commandline
pip install tox 
tox
```

The CI checks for compliance of the code with black and isort, and runs the tests and the notebooks.
To automatically satisfy the former, there is a pre-commit that can be used (do this once):
```commandline
pip install pre-commit
pre-commit install
```
From then on, your code will be checked for isort and black compatibility automatically. 
