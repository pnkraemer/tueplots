"""Marker shape presets (:mod:`tueplots.constants.markers`).

Defines commonly used marker styles for plots.
"""

import numpy as np

o_sized = np.array(["o", "*", "v", "p", "<", "P", ">", "X", "^", "D"])
r"""All markers that have a size roughly similar to 'o', '^', etc.."""


x_like = np.array(["x", "p", "*"])
r"""All markers that look roughly like the bold `X` (i.e. bold `+`, `*`, etc.)"""

x_like_bold = np.array(["X", "P", "*"])
r"""All markers that look roughly like X (i.e. `+`, `*`, etc.)"""

triangles = np.array(["^", "v", "<", ">"])
r"""All triangular markers."""
