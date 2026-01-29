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
# # Appropriate figure sizes

# %%
import matplotlib.pyplot as plt

from tueplots import figsizes

# Increase the resolution of all the plots below
plt.rcParams.update({"figure.dpi": 150})

# %% [markdown]
# Figure sizes are tuples. They describe the figure sizes in `inches`, just like what matplotlib expects.
#
# Outputs of `figsize` functions are dictionaries that match `rcParams`.
#

# %%
icml_size = figsizes.icml2022_full()
print(icml_size)

# %% [markdown]
# We can use them to make differently sized figures. The height-to-width ratio is (loosely) based on the golden ratio.

# %%
fig, ax = plt.subplots()
ax.plot([1.0, 2.0], [3.0, 4.0])
plt.show()

# %% [markdown]
# ### Figure sizes that match your latex template

# %%
plt.rcParams.update(figsizes.icml2022_full())

fig, ax = plt.subplots()
ax.plot([1.0, 2.0], [3.0, 4.0])
plt.show()

# %%
plt.rcParams.update(figsizes.neurips2021())

fig, ax = plt.subplots()
ax.plot([1.0, 2.0], [3.0, 4.0])
plt.show()

# %%
plt.rcParams.update(figsizes.aistats2022_full())

fig, ax = plt.subplots()
ax.plot([1.0, 2.0], [3.0, 4.0])
plt.show()

# %% [markdown]
# For double-column layouts such as ICML or AISTATS, there is also a single-column (i.e. half-width) version:

# %%
plt.rcParams.update(figsizes.icml2022_half())
fig, ax = plt.subplots()
ax.plot([1.0, 2.0], [3.0, 4.0])
plt.show()

# %%
plt.rcParams.update(figsizes.aistats2022_half())
fig, ax = plt.subplots()
ax.plot([1.0, 2.0], [3.0, 4.0])
plt.show()

# %% [markdown]
# ### Figure sizes that match your subplot layouts
# When working with `plt.subplots`, provide the `nrows` and `ncols` also to the figsize functions to get consistent subplot sizes by adjusting the overall figure height.
# Why? Because each subplot is fixed to a specific format (usually the golden ratio), and the figure width is commonly tied to the specific journal style.
# The remaining degree of freedom, the overall figure height, is adapted to make things look clean.

# %%
plt.rcParams.update(figsizes.neurips2021(nrows=1, ncols=3))

fig, axes = plt.subplots(nrows=1, ncols=3, sharex=True, sharey=True)
for ax in axes.flatten():
    ax.plot([1.0, 2.0], [3.0, 4.0])
plt.show()

# %%
plt.rcParams.update(figsizes.neurips2021(nrows=2, ncols=3))

fig, axes = plt.subplots(nrows=2, ncols=3, sharex=True, sharey=True)
for ax in axes.flatten():
    ax.plot([1.0, 2.0], [3.0, 4.0])
plt.show()

# %% [markdown]
# You can also customize the `height_to_width_ratio`:

# %%
plt.rcParams.update(figsizes.icml2022_half(nrows=2, ncols=2, height_to_width_ratio=1.0))

fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True)
for ax in axes.flatten():
    ax.plot([1.0, 2.0], [3.0, 4.0])
plt.show()

# %%
