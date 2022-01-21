"""Marker collections."""

import numpy as _np

o_sized = _np.array(["o", "*", "v", "p", "<", "P", ">", "X", "^", "D"])
r"""All markers that have a size roughly similar to 'o', '^', etc.."""


x_like = _np.array(["x", "p", "*"])
r"""All markers that look roughly like the bold `X` (i.e. bold `+`, `*`, etc.)"""

x_like_bold = _np.array(["X", "P", "*"])
r"""All markers that look roughly like X (i.e. `+`, `*`, etc.)"""

triangles = _np.array(["^", "v", "<", ">"])
r"""All triangular markers."""
