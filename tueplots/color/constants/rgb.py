"""RGB color constants."""

# _np instead of "np", because we dont want to expose numpy through
# `rgb.np`. This is not a bulletproof solution, but "saver" options
# would require a lot more import logic and that feels a bit pointless.
import numpy as _np

tue_dark = _np.array([55.0 / 255.0, 65.0 / 255.0, 74.0 / 255.0])
tue_gray = _np.array([175.0 / 255.0, 179.0 / 255.0, 183.0 / 255.0])
