# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Creating color-cycles

# %%
import matplotlib.pyplot as plt
import numpy as np

from tueplots import cycler
from tueplots.constants import markers
from tueplots.constants.color import palettes

# Increase the resolution of all the plots below
plt.rcParams.update({"figure.dpi": 150})

# %% [markdown]
# `cycler` objects define the default color choices in matplotlib (e.g., blue-orange-red-...).
# Like most other settings provided in `tueplots`, the outputs of `cycler` are directly compatible with `plt.rcParams.update()` (which is different to the `cycler` object in matplotlib in that it wraps them into a dictionary).
#
# We can control the cyclers through the constants in `tueplots.constants`.
# To see this, let us generate some lines to be plotted. (Setup taken from https://matplotlib.org/stable/tutorials/intermediate/color_cycle.html).

# %%
x = np.linspace(0, np.pi, 20)
offsets = np.linspace(0, 2 * np.pi, 8, endpoint=False)
yy = [np.sin(x + phi) for phi in offsets]

# %% [markdown]
# The following are the default colors:

# %%
for y in yy:
    plt.plot(x, y, linewidth=3)
plt.show()

# %% [markdown]
# Through the dictionaries provided by `tueplots`, we can change the default color behaviour as follows.

# %%
plt.rcParams.update(cycler.cycler(color=palettes.tue_plot))
for y in yy:
    plt.plot(x, y, linewidth=3)
plt.show()

# %%
plt.rcParams.update(cycler.cycler(color=palettes.paultol_muted))
for y in yy:
    plt.plot(x, y, linewidth=3)
plt.show()

# %%
plt.rcParams.update(cycler.cycler(color=palettes.paultol_high_contrast))
for y in yy:
    plt.plot(x, y, linewidth=3)
plt.show()

# %%
plt.rcParams.update(cycler.cycler(color=palettes.pn))
for y in yy:
    plt.plot(x, y, linewidth=3)
plt.show()

# %% [markdown]
# We can also cycle linestyles and markers.
#
#

# %%
plt.rcParams.update(cycler.cycler(color=palettes.pn[:3], marker=markers.o_sized[:3]))
for y in yy:
    plt.plot(x, y, linewidth=3, markersize=10)
plt.show()

# %%
plt.rcParams.update(
    cycler.cycler(color=palettes.paultol_vibrant[:3], marker=markers.x_like_bold[:3])
)
for y in yy:
    plt.plot(x, y, linewidth=3, markersize=10)
plt.show()

# %%
plt.rcParams.update(
    cycler.cycler(
        color=palettes.paultol_medium_contrast[:3], marker=markers.x_like_bold[:3]
    )
)
for y in yy:
    plt.plot(x, y, linewidth=3, markersize=10)
plt.show()

# %%
