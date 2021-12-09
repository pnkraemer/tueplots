"""RGB color constants."""

# _np instead of "np", because we dont want to expose numpy through
# `rgb.np`. This is not a bulletproof solution, but "saver" options
# would require a lot more import logic and that feels a bit pointless.
import numpy as _np

# the color palette of the university of Tuebingen:

# primary colors:
tue_red = _np.array([141.0, 45.0, 57.0]) / 255.0
tue_dark = _np.array([55.0, 65.0, 74.0]) / 255.0
tue_gray = _np.array([175.0, 179.0, 183.0]) / 255.0
tue_gold = _np.array([174.0, 159.0, 109.0]) / 255.0
tue_lightgold = _np.array([239.0, 236.0, 226.0]) / 255.0

# secondary colors
tue_darkblue = _np.array([65.0, 90.0, 140.0]) / 255.0
tue_blue = _np.array([0.0, 105.0, 170.0]) / 255.0
tue_lightblue = _np.array([80.0, 170.0, 200.0]) / 255.0
tue_lightgreen = _np.array([130.0, 185.0, 160.0]) / 255.0
tue_green = _np.array([125.0, 165.0, 75.0]) / 255.0
tue_darkgreen = _np.array([50.0, 110.0, 30.0]) / 255.0
tue_ocre = _np.array([200.0, 80.0, 60.0]) / 255.0
tue_violet = _np.array([175.0, 110.0, 150.0]) / 255.0
tue_mauve = _np.array([180.0, 160.0, 150.0]) / 255.0
tue_lightorange = _np.array([215.0, 180.0, 105.0]) / 255.0
tue_orange = _np.array([210.0, 150.0, 0.0]) / 255.0
tue_brown = _np.array([145.0, 105.0, 70.0]) / 255.0

# ProbNum's primary colors: www.probabilistic-numerics.org
pn_green = _np.array([40, 186, 180]) / 255.0
pn_blue = _np.array([41, 68, 165]) / 255.0

# ProbNum-matching secondary colors
# (made up slightly ad-hoc, please criticise!)
pn_orange = _np.array([255, 153, 51]) / 255.0
pn_gray = tue_gray
pn_red = tue_red
