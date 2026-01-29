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
# # Matching fontsizes

# %%
import matplotlib.pyplot as plt

from tueplots import figsizes, fontsizes

# Increase the resolution of all the plots below
plt.rcParams.update({"figure.dpi": 150})

# "Better" figure size to display the font-changes
plt.rcParams.update(figsizes.icml2022_half())

# %% [markdown]
# Fontsizes are dictionaries that can be passed to `matplotlib.pyplot.rcParams.update()`.

# %%
fontsizes.icml2022()

# %% [markdown]
# Compare the default font-sizes to, e.g., the ICML style. (To make differences more obvious, we increase the `dpi` value.)

# %%
fig, ax = plt.subplots()
ax.plot([1.0, 2.0], [3.0, 4.0])
ax.set_title("Title")
ax.set_xlabel("xlabel")
ax.set_ylabel("ylabel")
plt.show()

# %%
plt.rcParams.update(fontsizes.icml2022())
fig, ax = plt.subplots()
ax.plot([1.0, 2.0], [3.0, 4.0])
ax.set_title("Title")
ax.set_xlabel("xlabel")
ax.set_ylabel("ylabel")

plt.show()

# %%
plt.rcParams.update(fontsizes.neurips2021())
fig, ax = plt.subplots()
ax.plot([1.0, 2.0], [3.0, 4.0])
ax.set_title("Title")
ax.set_xlabel("xlabel")
ax.set_ylabel("ylabel")

plt.show()

# %%
plt.rcParams.update(fontsizes.aistats2022())
fig, ax = plt.subplots()
ax.plot([1.0, 2.0], [3.0, 4.0])
ax.set_title("Title")
ax.set_xlabel("xlabel")
ax.set_ylabel("ylabel")

plt.show()

# %%

# %%

# %%
