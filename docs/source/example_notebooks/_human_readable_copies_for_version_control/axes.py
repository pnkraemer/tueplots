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
# # Styling figure axes

# %%
import matplotlib.pyplot as plt

from tueplots import axes

# Increase the resolution of all the plots below
plt.rcParams.update({"figure.dpi": 150})

# %% [markdown]
# We can change the axes behaviour via `tueplots.axes`.

# %%
axes.lines()

# %%
fig, ax = plt.subplots()
ax.plot([1.0, 2.0], [3.0, 4.0])
plt.show()

# %%
plt.rcParams.update(axes.lines())
fig, ax = plt.subplots()
ax.plot([1.0, 2.0], [3.0, 4.0])
ax.set_xlabel("xlabel")
ax.set_ylabel("ylabel")
ax.set_title("title")
plt.show()

# %%
plt.rcParams.update(axes.tick_direction(x="inout", y="in"))
fig, ax = plt.subplots()
ax.plot([1.0, 2.0], [3.0, 4.0])
ax.set_xlabel("xlabel")
ax.set_ylabel("ylabel")
ax.set_title("title")
plt.show()

# %%
plt.rcParams.update(axes.color(base="red"))
fig, ax = plt.subplots()
ax.plot([1.0, 2.0], [3.0, 4.0], label="ABC")
ax.set_xlabel("xlabel")
ax.set_ylabel("ylabel")
ax.set_title("title")
plt.grid()
plt.show()

# %%
plt.rcParams.update(axes.grid())
fig, ax = plt.subplots()
ax.plot([1.0, 2.0], [3.0, 4.0], label="ABC")
ax.set_xlabel("xlabel")
ax.set_ylabel("ylabel")
ax.set_title("title")
plt.grid()
plt.show()

# %%
plt.rcParams.update(axes.spines(bottom=False, right=False))
fig, ax = plt.subplots()
ax.plot([1.0, 2.0], [3.0, 4.0])
ax.set_xlabel("xlabel")
ax.set_ylabel("ylabel")
ax.set_title("title")
plt.show()

# %%
plt.rcParams.update(axes.color(face="darkslategray", base="red"))
fig, ax = plt.subplots()
ax.plot([1.0, 2.0], [3.0, 4.0])
ax.set_xlabel("xlabel")
ax.set_ylabel("ylabel")
ax.set_title("title")
plt.show()

# %%
