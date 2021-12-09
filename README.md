# TUEplots

Scientific plotting made easy, purely based on matplotlib.


## Why?

`tueplots` helps you to create scientific plots that can be used in papers, presentations, posters, or other publications.
`tueplots` does not try to make your plots as beautiful as possible (who are we to judge your favourite color).
Instead, it makes it effortless to avoid common issues like too-small figures, inappropriate fontsizes, or inconsistencies among figures.
Because good-looking figures _are_ important. 

The code adheres to the following principles.

_**`tueplots` has no internal state:**_
It only passes around dictionaries, whose key-value pairs match those that matplotlib uses.
Instead of updating global state, it makes it easy for you to do it yourself! 
If you want to globally change settings, pass them to `matplotlib.pyplot.rcParams.update()`.
If you only need them for specific contexts, pass them to `matpltlib.pyplot.rc_context()`.
`tueplots` makes the change easy, so you can make the easy change. This should make `tueplots` naturally compatible with other matplotlib extensions.
Usage examples are given below.


**_`tueplots` has no opinions:_**
It does not tell you what your figures should like like in the end, but helps you to tailor your plots to your own needs.
We like all the colors, frame-styles, markers, or linewidths.
But we _do_ think that figure sizes should match the text-width in your publication, 
and that the font-size in the plot should be readable, and similar to the rest of the paper/presentation/....




## Usage examples

`tueplots` provides some recipes for scientific plotting. 
For example, figure sizes can be tailored straightforwardly to some common journal page layouts:
```python
>>> from tueplots import figsize
>>> figsize.jmlr2001()["figure.figsize"]
(6.0, 1.8541019662496847)
```
within one module, the functions have a unified interface (wherever possible)
```python
>>> figsize.jmlr2001(nrows=2)["figure.figsize"]
(6.0, 3.7082039324993694)
>>> 
>>> figsize.neurips2021(nrows=3)["figure.figsize"]
(5.499999861629998, 5.098780278910587)
>>> 
>>> # The full output:
>>> figsize.icml2022(nrows=4)
{'figure.autolayout': False,
 'figure.constrained_layout.use': True,
 'figure.figsize': (6.75, 8.343458848123582)}
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
>>> from tueplots import marker
>>> 
>>> marker.inverted()
{'lines.markeredgecolor': 'auto',
 'lines.markeredgewidth': 0.75,
 'lines.markerfacecolor': 'white'}


>>> import matplotlib.pyplot as plt

>>> # Use them as context managers:
>>> with plt.rc_context(marker.inverted()):
...     pass # do your plotting...

>>> # Or change your global configuration
>>> plt.rcParams.update(marker.inverted())
```

For more detailed tutorials, please have a look at the examples in the `examples/` directory.

## Contribution

Tests are run with pytest.
You can use tox (you only have to install tox once):
```commandline
pip install tox 
tox -e py3  # for the tests (via pytest)
tox -e isort  # for linting (isort)
tox -e black  # for linting (black)
tox -e byexample  # to run the python snippets in the readme
```

The CI checks for compliance of the code with black and isort, and runs the tests and the notebooks.
To automatically satisfy the former, there is a pre-commit that can be used (do this once):
```commandline
pip install pre-commit
pre-commit install
```
From then on, your code will be checked for isort and black compatibility automatically. 



# Miscellanous

tueplots`has been developed at the University of Tübingen (hence the name).
