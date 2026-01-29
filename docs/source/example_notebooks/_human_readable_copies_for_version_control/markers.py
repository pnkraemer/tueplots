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
# # Create custom markers

# %%
import matplotlib.pyplot as plt
import numpy as np

from tueplots import cycler, markers
from tueplots.constants import markers as marker_constants
from tueplots.constants.color import palettes

# Increase the resolution of all the plots below
plt.rcParams.update({"figure.dpi": 150})

# %% [markdown]
# There are a few marker styles to choose from. (Setup taken from https://matplotlib.org/stable/tutorials/intermediate/color_cycle.html). There are rcParam dictionaries including specific marker styles and full marker cycles.
#

# %%
markers.with_edge()

# %% [markdown]
# Compare the default options to the specialised markers.

# %%
x = np.linspace(0, np.pi, 25)
offsets = np.linspace(0, 2 * np.pi, 7, endpoint=False)
yy = [np.sin(x + phi) for phi in offsets]

# %%
fig, ax = plt.subplots()
for y in yy:
    ax.plot(x, y, "o-", linewidth=1)
plt.show()

# %%
plt.rcParams.update(markers.inverted())

fig, ax = plt.subplots()
for y in yy:
    ax.plot(x, y, "o-", linewidth=1)
plt.show()

# %%
plt.rcParams.update(markers.with_edge())

fig, ax = plt.subplots()
for y in yy:
    ax.plot(x, y, "o-", linewidth=1)
plt.show()

# %%
plt.rcParams.update(
    cycler.cycler(marker=marker_constants.o_sized[:5], color=palettes.pn[:5])
)

fig, ax = plt.subplots()
for y in yy:
    ax.plot(x, y, linewidth=1)
plt.show()

# %%
plt.rcParams.update(markers.with_edge(edgecolor="green", edgewidth=1.0))

fig, ax = plt.subplots()
for y in yy:
    ax.plot(x, y, linewidth=1)
plt.show()

# %%
