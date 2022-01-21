"""RGB color constants."""

import numpy as np

# Uni Tuebingen corporate colors: primary


tue_red = np.array([141.0, 45.0, 57.0]) / 255.0
"""Color associated with the University of Tübingen. Red."""

tue_dark = np.array([55.0, 65.0, 74.0]) / 255.0
"""Color associated with the University of Tübingen. Dark gray."""

tue_gray = np.array([175.0, 179.0, 183.0]) / 255.0
"""Color associated with the University of Tübingen. Gray."""

tue_gold = np.array([174.0, 159.0, 109.0]) / 255.0
"""Color associated with the University of Tübingen. Gold."""

tue_lightgold = np.array([239.0, 236.0, 226.0]) / 255.0
"""Color associated with the University of Tübingen. Light gold."""

# Uni Tuebingen corporate colors: secondary

tue_darkblue = np.array([65.0, 90.0, 140.0]) / 255.0
"""Color associated with the University of Tübingen. Dark blue."""

tue_blue = np.array([0.0, 105.0, 170.0]) / 255.0
"""Color associated with the University of Tübingen. Blue."""

tue_lightblue = np.array([80.0, 170.0, 200.0]) / 255.0
"""Color associated with the University of Tübingen. Light blue."""

tue_lightgreen = np.array([130.0, 185.0, 160.0]) / 255.0
"""Color associated with the University of Tübingen. Light green."""

tue_green = np.array([125.0, 165.0, 75.0]) / 255.0
"""Color associated with the University of Tübingen. Green."""

tue_darkgreen = np.array([50.0, 110.0, 30.0]) / 255.0
"""Color associated with the University of Tübingen. Dark green."""

tue_ocre = np.array([200.0, 80.0, 60.0]) / 255.0
"""Color associated with the University of Tübingen. Ocre."""

tue_violet = np.array([175.0, 110.0, 150.0]) / 255.0
"""Color associated with the University of Tübingen. Violet."""

tue_mauve = np.array([180.0, 160.0, 150.0]) / 255.0
"""Color associated with the University of Tübingen. Mauve."""

tue_lightorange = np.array([215.0, 180.0, 105.0]) / 255.0
"""Color associated with the University of Tübingen. Light orange."""

tue_orange = np.array([210.0, 150.0, 0.0]) / 255.0
"""Color associated with the University of Tübingen. Orange."""

tue_brown = np.array([145.0, 105.0, 70.0]) / 255.0
"""Color associated with the University of Tübingen. Brown."""


# ProbNum's primary colors: www.probabilistic-numerics.org
pn_green = np.array([40, 186, 180]) / 255.0
"""Color associated with ProbNum: probnum.org. Green."""

pn_blue = np.array([41, 68, 165]) / 255.0
"""Color associated with ProbNum: probnum.org. Blue."""

# ProbNum-matching secondary colors
# (made up slightly ad-hoc, please criticise!)

pn_orange = np.array([255, 153, 51]) / 255.0
"""Color associated with ProbNum: probnum.org. Orange."""

pn_gray = tue_gray
"""Color associated with ProbNum: probnum.org. Gray."""

pn_red = tue_red
"""Color associated with ProbNum: probnum.org. Red."""

# the Corporate-ID colors of the Max Planck Society:

mps_green = np.array([17, 102, 86]) / 255.0
"""Color associated with the Max Planck Society. Green."""

mps_lightgreen = mps_green + 0.5 * (255.0 - mps_green)  # 50% version
"""Color associated with the Max Planck Society. Light green. 50% version."""

mps_gray = np.array([221, 222, 214]) / 255.0
"""Color associated with the Max Planck Society. Gray."""

mps_lightgray = mps_gray + 0.5 * (255.0 - mps_gray)  # 50% version
"""Color associated with the Max Planck Society. Light gray. 50% version."""
