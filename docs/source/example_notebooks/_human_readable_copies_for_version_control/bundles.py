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
# # Convenient plot-configs with bundles

# %%
import matplotlib.pyplot as plt

from tueplots import axes, bundles

# Increase the resolution of all the plots below
plt.rcParams.update({"figure.dpi": 150})

# %% [markdown]
# `tueplots` provides a few prepackaged bundles that can be plugged right into matplotlib's context manager.

# %%
bundles.icml2022()

# %% [markdown]
# Compare the default plots to the context plots below.

# %%
fig, ax = plt.subplots()
ax.plot([1.0, 2.0], [3.0, 4.0])
ax.set_title("Title")
ax.set_xlabel("xlabel")
ax.set_ylabel("ylabel")
plt.show()

# %%
with plt.rc_context(bundles.neurips2021()):
    fig, ax = plt.subplots()
    ax.plot([1.0, 2.0], [3.0, 4.0])
    ax.set_title("Title")
    ax.set_xlabel("xlabel")
    ax.set_ylabel("ylabel")
    plt.show()

# %%
with plt.rc_context(bundles.jmlr2001(family="serif")):
    fig, ax = plt.subplots()
    ax.plot([1.0, 2.0], [3.0, 4.0])
    ax.set_title("Title")
    ax.set_xlabel("xlabel")
    ax.set_ylabel("ylabel")
    plt.show()

# %% [markdown]
# To get some (subjective) default behaviour, combine the bundles with `axes.lines()` (which is highly customisable, but has some opinionated default arguments).

# %%
with plt.rc_context({**bundles.neurips2021(), **axes.lines()}):
    fig, ax = plt.subplots()
    ax.plot([1.0, 2.0], [3.0, 4.0])
    ax.set_title("Title")
    ax.set_xlabel("xlabel")
    ax.set_ylabel("ylabel")
    plt.grid()
    plt.show()

# %%
with plt.rc_context(bundles.neurips2021(usetex=True, family="serif")):
    fig, ax = plt.subplots()
    ax.plot([1.0, 2.0], [3.0, 4.0])
    ax.set_title("Title")
    ax.set_xlabel(r"xlabel $\int f(x) dx$")
    ax.set_ylabel(r"ylabel $x \sim \mathcal{N}(x)$")
    plt.grid()
    plt.show()

# %%
with plt.rc_context({**bundles.icml2022(), **axes.lines()}):
    fig, ax = plt.subplots()
    ax.plot([1.0, 2.0], [3.0, 4.0], label="p(x)")
    ax.set_title("Title")
    ax.set_xlabel(r"xlabel $\int f(x) dx$")
    ax.set_ylabel(r"ylabel $x \sim \mathcal{N}(x)$")
    plt.grid()
    plt.legend()
    plt.show()

# %%
with plt.rc_context(bundles.aistats2022()):
    fig, ax = plt.subplots()
    ax.plot([1.0, 2.0], [3.0, 4.0], label="p(x)")
    ax.set_title("Title")
    ax.set_xlabel(r"xlabel $\int f(x) dx$")
    ax.set_ylabel(r"ylabel $x \sim \mathcal{N}(x)$")
    plt.grid()
    plt.legend()
    plt.show()

# %%
with plt.rc_context({**bundles.aistats2022(family="serif"), **axes.lines()}):
    fig, ax = plt.subplots()
    ax.plot([1.0, 2.0], [3.0, 4.0], label="p(x)")
    ax.set_title("Title")
    ax.set_xlabel(r"xlabel $\int f(x) dx$")
    ax.set_ylabel(r"ylabel $x \sim \mathcal{N}(x)$")
    plt.grid()
    plt.legend()
    plt.show()

# %%
with plt.rc_context(bundles.beamer_moml()):
    fig, ax = plt.subplots()
    ax.plot([1.0, 2.0], [3.0, 4.0], label="p(x)")
    ax.legend()
    ax.set_title("Title")
    ax.set_xlabel("xlabel")
    ax.set_ylabel("ylabel")
    ax.grid()
    plt.show()

# %%
with plt.rc_context(bundles.beamer_moml_dark_bg()):
    fig, ax = plt.subplots()
    ax.plot([1.0, 2.0], [3.0, 4.0])
    ax.set_title("Title")
    ax.set_xlabel("xlabel")
    ax.set_ylabel("ylabel")
    ax.grid()
    plt.show()

# %%
with plt.rc_context(bundles.iclr2023()):
    fig, ax = plt.subplots()
    ax.plot([1.0, 2.0], [3.0, 4.0])
    ax.set_title("Title")
    ax.set_xlabel("xlabel")
    ax.set_ylabel("ylabel")
    ax.grid()
    plt.show()

# %%
with plt.rc_context(
    bundles.iclr2023(usetex=True, nrows=1, ncols=3, family="smallcaps")
):
    fig, ax = plt.subplots()
    ax.plot([1.0, 2.0], [3.0, 4.0])
    ax.set_title("Title")
    ax.set_xlabel("xlabel")
    ax.set_ylabel("ylabel")
    ax.grid()
    plt.show()
