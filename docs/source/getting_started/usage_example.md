
# Usage examples

`tueplots` provides some recipes for scientific plotting.
For example, figure sizes can be tailored straightforwardly to some common journal page layouts:
```python
>>> from tueplots import figsizes
>>> figsizes.jmlr2001()["figure.figsize"]
(6.0, 1.8541019662496847)

```

within one module, the functions have a unified interface (wherever possible)
```python
>>> figsizes.jmlr2001(nrows=2)["figure.figsize"]
(6.0, 3.7082039324993694)
>>>
>>> figsizes.neurips2021(nrows=3)["figure.figsize"]
(5.5, 5.0987804071866325)
>>>
>>> # The full output:
>>> figsizes.icml2022_full(nrows=4)
{'figure.figsize': (6.75, 8.343458848123582), 'figure.constrained_layout.use': True, 'figure.autolayout': False, 'savefig.bbox': 'tight', 'savefig.pad_inches': 0.015}

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
>>> from tueplots import markers
>>>
>>> markers.inverted()
{'lines.markeredgecolor': 'auto', 'lines.markerfacecolor': 'white', 'lines.markeredgewidth': 0.75}

>>> import matplotlib.pyplot as plt

>>> # Use them as context managers:
>>> with plt.rc_context(markers.inverted()):
...     pass # do your plotting...

>>> # Or change your global configuration
>>> plt.rcParams.update(markers.inverted())

```

For more detailed tutorials, please have a look at the examples in the `examples/` directory.
