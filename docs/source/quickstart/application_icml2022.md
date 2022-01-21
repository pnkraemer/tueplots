# Example application: ICML 2022

If you're getting ready to submit your paper to ICML 2022, plug either of the following into your preamble.

## In a nutshell

```python
>>> import matplotlib.pyplot as plt
>>> from tueplots import bundles
>>> bundles.icml2022()
{'axes.labelsize': 8,
 'axes.titlesize': 8,
 'figure.autolayout': False,
 'figure.constrained_layout.use': True,
 'figure.figsize': (3.25, 2.0086104634371584),
 'font.family': 'sans-serif',
 'font.size': 8,
 'legend.fontsize': 6,
 'text.latex.preamble': '\\usepackage{times} '
                        '\\renewcommand{\\familydefault}{\\sfdefault} '
                        '\\usepackage{sansmath} \\sansmath',
 'text.usetex': True,
 'xtick.labelsize': 6,
 'ytick.labelsize': 6}
>>> bundles.icml2022(family="sans-serif", usetex=False, column="full", nrows=2)
{'axes.labelsize': 8,
 'axes.titlesize': 8,
 'figure.autolayout': False,
 'figure.constrained_layout.use': True,
 'figure.figsize': (6.75, 8.343458848123582),
 'font.family': 'sans-serif',
 'font.serif': ['Times'],
 'font.size': 8,
 'legend.fontsize': 6,
 'mathtext.bf': 'Times:bold',
 'mathtext.fontset': 'stix',
 'mathtext.it': 'Times:italic',
 'mathtext.rm': 'Times',
 'text.usetex': False,
 'xtick.labelsize': 6,
 'ytick.labelsize': 6}
>>>
>>> # Plug any of those into either the rcParams or into an rc_context:
>>> plt.rcParams.update(bundles.icml2022())
>>> with plt.rc_context(bundles.icml2022()):
...     pass
```

## Some customisation

If you don't want a pre-packaged solution, at least fix your figure- and font-sizes as follows.
```python
>>> from tueplots import figsizes, fontsizes, fonts
>>> figsizes.icml2022_full()
{'figure.autolayout': False,
 'figure.constrained_layout.use': True,
 'figure.figsize': (6.75, 2.0858647120308955)}
>>> figsizes.icml2022_half(nrows=2, constrained_layout=True, tight_layout=False)
{'figure.autolayout': False,
 'figure.constrained_layout.use': True,
 'figure.figsize': (3.25, 4.017220926874317)}
>>> fontsizes.icml2022()
{'axes.labelsize': 8,
 'axes.titlesize': 8,
 'font.size': 8,
 'legend.fontsize': 6,
 'xtick.labelsize': 6,
 'ytick.labelsize': 6}
>>> fonts.icml2022()
{'font.family': 'serif',
 'font.serif': ['Times'],
 'mathtext.bf': 'Times:bold',
 'mathtext.fontset': 'stix',
 'mathtext.it': 'Times:italic',
 'mathtext.rm': 'Times',
 'text.usetex': False}
>>> fonts.icml2022(family="serif")
{'font.family': 'serif',
 'font.serif': ['Times'],
 'mathtext.bf': 'Times:bold',
 'mathtext.fontset': 'stix',
 'mathtext.it': 'Times:italic',
 'mathtext.rm': 'Times',
 'text.usetex': False}
>>> fonts.icml2022_tex(family="sans-serif")
{'font.family': 'sans-serif',
 'text.latex.preamble': '\\usepackage{times} '
                        '\\renewcommand{\\familydefault}{\\sfdefault} '
                        '\\usepackage{sansmath} \\sansmath',
 'text.usetex': True}
```
and if you want to give your plots a makeover (albeit a slightly opinionated one) with a single line of code,
consider the `axes.lines()` setting.
```python
>>> from tueplots import axes
>>> axes.lines()
{'axes.axisbelow': True,
 'axes.linewidth': 0.5,
 'grid.linewidth': 0.5,
 'legend.edgecolor': 'inherit',
 'lines.linewidth': 1.0,
 'patch.linewidth': 0.5,
 'xtick.major.size': 3.0,
 'xtick.major.width': 0.5,
 'xtick.minor.size': 2.0,
 'xtick.minor.width': 0.25,
 'ytick.major.size': 3.0,
 'ytick.major.width': 0.5,
 'ytick.minor.size': 2.0,
 'ytick.minor.width': 0.25}
>>> axes.lines(base_width=0.5)
{'axes.axisbelow': True,
 'axes.linewidth': 0.5,
 'grid.linewidth': 0.5,
 'legend.edgecolor': 'inherit',
 'lines.linewidth': 1.0,
 'patch.linewidth': 0.5,
 'xtick.major.size': 3.0,
 'xtick.major.width': 0.5,
 'xtick.minor.size': 2.0,
 'xtick.minor.width': 0.25,
 'ytick.major.size': 3.0,
 'ytick.major.width': 0.5,
 'ytick.minor.size': 2.0,
 'ytick.minor.width': 0.25}
```
