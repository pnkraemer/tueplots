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
# # Choosing the correct fonts

# %%
import matplotlib.pyplot as plt

from tueplots import figsizes, fonts

# Increase the resolution of all the plots below
plt.rcParams.update({"figure.dpi": 150})

# "Better" figure size to display the font-changes
plt.rcParams.update(figsizes.icml2022_half())

# %% [markdown]
# Fonts in `tueplots` follow the same interface as the other settings.
#
# There are some pre-defined font recipes for a few journals, and they return dictionaries that are compatible with `matplotlib.pyplot.rcParams.update()`.

# %%
fonts.neurips2021()

# %% [markdown]
# Compare the following default font to some of the alternatives that we provide:

# %%
fig, ax = plt.subplots()
ax.plot([1.0, 2.0], [3.0, 4.0])
ax.set_title("Title")
ax.set_xlabel(r"xlabel $\int f(x) dx$")
ax.set_ylabel(r"ylabel $x \sim \mathcal{N}(x)$")
plt.show()

# %%
with plt.rc_context(fonts.jmlr2001_tex(family="serif")):
    fig, ax = plt.subplots()
    ax.plot([1.0, 2.0], [3.0, 4.0])
    ax.set_title("Title")
    ax.set_xlabel(r"xlabel $\int_a^b f(x) dx$")
    ax.set_ylabel(r"ylabel $x \sim \mathcal{N}(x)$")
    plt.show()

# %%
with plt.rc_context(fonts.jmlr2001_tex(family="sans-serif")):
    fig, ax = plt.subplots()
    ax.plot([1.0, 2.0], [3.0, 4.0])
    ax.set_title("Title")
    ax.set_xlabel(r"xlabel $\int_a^b f(x) dx$")
    ax.set_ylabel(r"ylabel $x \sim \mathcal{N}(x)$")
    plt.show()

# %%
with plt.rc_context(fonts.neurips2021_tex(family="sans-serif")):
    fig, ax = plt.subplots()
    ax.plot([1.0, 2.0], [3.0, 4.0])
    ax.set_title("Title")
    ax.set_xlabel(r"xlabel $\int_a^b f(x) dx$")
    ax.set_ylabel(r"ylabel $x \sim \mathcal{N}(x)$")
    plt.show()

# %%
with plt.rc_context(fonts.neurips2021(family="sans-serif")):
    fig, ax = plt.subplots()
    ax.plot([1.0, 2.0], [3.0, 4.0])
    ax.set_title("Title")
    ax.set_xlabel(r"xlabel $\int_a^b f(x) dx$")
    ax.set_ylabel(r"ylabel $x \sim \mathcal{N}(x)$")
    plt.show()

# %%
with plt.rc_context(fonts.icml2022()):
    fig, ax = plt.subplots()
    ax.plot([1.0, 2.0], [3.0, 4.0])
    ax.set_title("Title")

    ax.set_xlabel(r"xlabel $\int_a^b f(x) dx$")
    ax.set_ylabel(r"ylabel $x \sim \mathcal{N}(x)$")
    plt.show()

# %%
with plt.rc_context(fonts.icml2022_tex(family="sans-serif")):
    fig, ax = plt.subplots()
    ax.plot([1.0, 2.0], [3.0, 4.0])
    ax.set_title("Title")
    ax.set_xlabel(r"xlabel $\int_a^b f(x) dx$")
    ax.set_ylabel(r"ylabel $x \sim \mathcal{N}(x)$")
    plt.show()

# %%
with plt.rc_context(fonts.icml2022_tex(family="serif")):
    fig, ax = plt.subplots()
    ax.plot([1.0, 2.0], [3.0, 4.0])
    ax.set_title("Title")
    ax.set_xlabel(r"xlabel $\int_a^b f(x) dx$")
    ax.set_ylabel(r"ylabel $x \sim \mathcal{N}(x)$")
    plt.show()

# %%
plt.rcParams.update(fonts.aistats2022_tex(family="serif"))
fig, ax = plt.subplots()
ax.plot([1.0, 2.0], [3.0, 4.0])
ax.set_title("Title")
ax.set_xlabel(r"xlabel $\int_a^b f(x) dx$")
ax.set_ylabel(r"ylabel $x \sim \mathcal{N}(x)$")
plt.show()

# %%
with plt.rc_context(fonts.aistats2022_tex(family="sans-serif")):
    fig, ax = plt.subplots()
    ax.plot([1.0, 2.0], [3.0, 4.0])
    ax.set_title("Title")
    ax.set_xlabel(r"xlabel $\int_a^b f(x) dx$")
    ax.set_ylabel(r"ylabel $x \sim \mathcal{N}(x)$")
    plt.show()
