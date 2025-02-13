# Example application: ICML 2022

If you're getting ready to submit your paper to ICML 2022, plug either of the following into your preamble.

## In a nutshell
The minimal amount of code required to fit your figure to the ICML 2022 style (source: https://media.icml.cc/Conferences/ICML2022/Styles/example_paper.pdf)
is `plt.rcParams.update(bundles.icml2022())`:
```python
>>> import matplotlib.pyplot as plt
>>> from tueplots import bundles
>>> bundles.icml2022()
{'text.usetex': True, 'font.family': 'serif', 'text.latex.preamble': '\\usepackage{times} ', 'figure.figsize': (3.25, 2.0086104634371584), 'figure.constrained_layout.use': True, 'figure.autolayout': False, 'savefig.pad_inches': 0.015, 'font.size': 8, 'axes.labelsize': 8, 'legend.fontsize': 6, 'xtick.labelsize': 6, 'ytick.labelsize': 6, 'axes.titlesize': 8}
>>> bundles.icml2022(family="sans-serif", usetex=False, column="full", nrows=2)
{'text.usetex': False, 'font.serif': ['Times'], 'mathtext.fontset': 'stix', 'mathtext.rm': 'Times', 'mathtext.it': 'Times:italic', 'mathtext.bf': 'Times:bold', 'font.family': 'sans-serif', 'figure.figsize': (6.75, 8.343458848123582), 'figure.constrained_layout.use': True, 'figure.autolayout': False, 'savefig.pad_inches': 0.015, 'font.size': 8, 'axes.labelsize': 8, 'legend.fontsize': 6, 'xtick.labelsize': 6, 'ytick.labelsize': 6, 'axes.titlesize': 8}
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
{'figure.figsize': (6.75, 2.0858647120308955), 'figure.constrained_layout.use': True, 'figure.autolayout': False, 'savefig.pad_inches': 0.015}
>>> figsizes.icml2022_half(nrows=2, constrained_layout=True, tight_layout=False)
{'figure.figsize': (3.25, 4.017220926874317), 'figure.constrained_layout.use': True, 'figure.autolayout': False, 'savefig.pad_inches': 0.015}
>>> fontsizes.icml2022()
{'font.size': 8, 'axes.labelsize': 8, 'legend.fontsize': 6, 'xtick.labelsize': 6, 'ytick.labelsize': 6, 'axes.titlesize': 8}
>>> fonts.icml2022()
{'text.usetex': False, 'font.serif': ['Times'], 'mathtext.fontset': 'stix', 'mathtext.rm': 'Times', 'mathtext.it': 'Times:italic', 'mathtext.bf': 'Times:bold', 'font.family': 'serif'}
>>> fonts.icml2022(family="serif")
{'text.usetex': False, 'font.serif': ['Times'], 'mathtext.fontset': 'stix', 'mathtext.rm': 'Times', 'mathtext.it': 'Times:italic', 'mathtext.bf': 'Times:bold', 'font.family': 'serif'}
>>> fonts.icml2022_tex(family="sans-serif")
{'text.usetex': True, 'font.family': 'sans-serif', 'text.latex.preamble': '\\usepackage{times} \\renewcommand{\\familydefault}{\\sfdefault} \\usepackage{sansmath} \\sansmath'}

```

and if you want to give your plots a makeover (albeit a slightly opinionated one) with a single line of code,
consider the `axes.lines()` setting.

```python
>>> from tueplots import axes
>>> axes.lines()
{'axes.linewidth': 0.5, 'lines.linewidth': 1.0, 'xtick.major.width': 0.5, 'ytick.major.width': 0.5, 'xtick.minor.width': 0.25, 'ytick.minor.width': 0.25, 'xtick.major.size': 3.0, 'ytick.major.size': 3.0, 'xtick.minor.size': 2.0, 'ytick.minor.size': 2.0, 'grid.linewidth': 0.5, 'patch.linewidth': 0.5, 'legend.edgecolor': 'inherit', 'axes.axisbelow': True}
>>> axes.lines(base_width=0.5)
{'axes.linewidth': 0.5, 'lines.linewidth': 1.0, 'xtick.major.width': 0.5, 'ytick.major.width': 0.5, 'xtick.minor.width': 0.25, 'ytick.minor.width': 0.25, 'xtick.major.size': 3.0, 'ytick.major.size': 3.0, 'xtick.minor.size': 2.0, 'ytick.minor.size': 2.0, 'grid.linewidth': 0.5, 'patch.linewidth': 0.5, 'legend.edgecolor': 'inherit', 'axes.axisbelow': True}

```
