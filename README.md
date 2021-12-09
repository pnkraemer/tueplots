# TUEplots

Plot-configurations for scientific publications, purely based on matplotlib.

## Usage

`tueplots` provides some recipes for scientific plotting. 
For example, figure sizes can be tailored straightforwardly to some common journal page layouts:
```python
>>> from tueplots import figsize
>>> figsize.jmlr2001()
(6.0, 1.8541019662496847)
```
within one module, the functions have a unified interface (wherever possible)
```python
>>> figsize.jmlr2001(nrows=2)
(6.0, 3.7082039324993694)
>>> 
>>> figsize.neurips2021(nrows=3)
(5.499999861629998, 5.098780278910587)
>>> 
>>> figsize.icml2022(nrows=4)
(6.75, 8.343458848123582)
```

There are also predefined color constants. For example, those based on the corporate design of the University of Tuebingen:
```python
>>> from tueplots.constants.color import rgb 
>>> 
>>> rgb.tue_dark
array([0.21568627, 0.25490196, 0.29019608])
>>>
>>> rgb.tue_gray
array([0.68627451, 0.70196078, 0.71764706])
```

Most of the output types of functions in `tueplots` are dictionaries that are directly compatible with matplotlib's `rcParam` language.
```python
>>> from tueplots import axes 
>>> 
>>> axes.lines()
{'axes.edgecolor': 'black',
 'axes.labelcolor': 'black',
 'axes.linewidth': 1.0,
 'axes.spines.bottom': True,
 'axes.spines.left': True,
 'axes.spines.right': True,
 'axes.spines.top': True,
 'grid.alpha': 0.75,
 'grid.color': 'black',
 'grid.linestyle': 'dotted',
 'grid.linewidth': 1.0,
 'text.color': 'black',
 'xtick.color': 'black',
 'xtick.direction': 'out',
 'xtick.major.size': 4.5,
 'xtick.major.width': 1.0,
 'xtick.minor.size': 3.3,
 'xtick.minor.width': 0.6,
 'ytick.color': 'black',
 'ytick.direction': 'out',
 'ytick.major.size': 4.5,
 'ytick.major.width': 1.0,
 'ytick.minor.size': 3.3,
 'ytick.minor.width': 0.6}

>>> import matplotlib.pyplot as plt

>>> # Use them as context managers:
>>> with plt.rc_context(rc=axes.lines()):
...     pass # do your plotting...

>>> # Or change your global configuration
>>> plt.rcParams.update(axes.lines())
```

For more detailed tutorials, please have a look at the examples in the `examples/` directory.

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
