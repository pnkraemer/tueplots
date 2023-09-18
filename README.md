
<p align="center">
<img src="./docs/source/img/logo.png" width="400"/>
</p>

# TUEplots: Extend matplotlib for scientific publications

[![PyPi Version](https://img.shields.io/pypi/v/tueplots.svg?style=flat-square)](https://pypi.org/project/tueplots/)
[![Docs](https://readthedocs.org/projects/pip/badge/?version=latest&style=flat-square)](https://github.com/pnkraemer/tueplots)
[![GitHub stars](https://img.shields.io/github/stars/pnkraemer/tueplots.svg?style=flat-square&logo=github&label=Stars&logoColor=white)](https://github.com/pnkraemer/tueplots)
[![gh-actions](https://img.shields.io/github/actions/workflow/status/pnkraemer/tueplots/ci.yaml?branch=main&style=flat-square)](https://github.com/pnkraemer/tueplots/actions?query=workflow%3Aci)
<a href="https://github.com/pnkraemer/tueplots/blob/master/LICENSE"><img src="https://img.shields.io/github/license/pnkraemer/tueplots?style=flat-square&color=2b9348" alt="License Badge"/></a>



## Why?

`tueplots` helps you to create scientific plots that can be used in papers, presentations, posters, or other publications.
`tueplots` does not try to make your plots as beautiful as possible (who are we to judge your favourite color).
Instead, it makes it effortless to avoid common issues like too-small figures, inappropriate fontsizes, or inconsistencies among figures.
Because good-looking figures _are_ important. 

For example, consider the style tailored to the ICML2022 template.
(Left: default matplotlib, middle: one line of tueplots-code, right: two lines of tueplots-code)

<p align="center">
<img src="https://raw.githubusercontent.com/pnkraemer/tueplots/main/docs/img_for_readme/before.png" width="200"/>
<img src="https://raw.githubusercontent.com/pnkraemer/tueplots/main/docs/img_for_readme/after1.png" width="200"/>
<img src="https://raw.githubusercontent.com/pnkraemer/tueplots/main/docs/img_for_readme/after2.png" width="200"/>
</p>


## Principles

**`tueplots` has no internal state:**
It only passes around dictionaries, whose key-value pairs match those that matplotlib uses.
Instead of updating global state, it makes it easy for you to do it yourself! 
If you want to globally change settings, pass them to `matplotlib.pyplot.rcParams.update()`.
If you only need them for specific contexts, pass them to `matpltlib.pyplot.rc_context()`.
`tueplots` makes the change easy, so you can make the easy change. This should make `tueplots` naturally compatible with other matplotlib extensions.
Usage examples are given below.


**`tueplots` has no opinions:**
It does not tell you what your figures should look like in the end, but helps you to tailor your plots to your own needs.
We like all the colors, frame-styles, markers, or linewidths.
But we _do_ think that figure sizes should match the text-width in your publication, 
and that the font-size in the plot should be readable, and similar to the rest of the paper/presentation/....

## Getting started 

Installing `tueplots` is explained [**here**](https://tueplots.readthedocs.io/en/latest/getting_started/installation.html).
Some usage examples are given [**at this url**](https://tueplots.readthedocs.io/en/latest/getting_started/usage_example.html).
A more specific tutorial, applying `tueplots` to figures intended for ICML 2022, is [**on this page**](https://tueplots.readthedocs.io/en/latest/getting_started/application_icml2022.html).
If something is not working as promised, please refer to the [**troubleshooting**](https://tueplots.readthedocs.io/en/latest/getting_started/troubleshooting.html) site.
For more advanced tutorials, you may refer to the example notebooks.

## Related packages
There are similar packages to `tueplots` (with different foci, respectively):
* Seaborn: https://seaborn.pydata.org/index.html
* ProPlot: https://proplot.readthedocs.io/en/latest/cycles.html
* SciencePlots: https://github.com/garrettj403/SciencePlots
* MatplotX: https://github.com/nschloe/matplotx
* Themepy: https://github.com/petermckeeverPerform/themepy

The [**matplotlib third-party plots**](https://matplotlib.org/mpl-third-party/) contains a more comprehensive list.
If you know of any others, please feel invited to open an issue/PR. 


# Miscellaneous

`tueplots`has been developed at the University of Tübingen (hence the name).
