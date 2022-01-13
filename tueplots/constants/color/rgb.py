"""RGB color constants."""

import numpy as np

# the color palette of the university of Tuebingen:

# primary colors:
tue_red = np.array([141.0, 45.0, 57.0]) / 255.0
tue_dark = np.array([55.0, 65.0, 74.0]) / 255.0
tue_gray = np.array([175.0, 179.0, 183.0]) / 255.0
tue_gold = np.array([174.0, 159.0, 109.0]) / 255.0
tue_lightgold = np.array([239.0, 236.0, 226.0]) / 255.0

# secondary colors
tue_darkblue = np.array([65.0, 90.0, 140.0]) / 255.0
tue_blue = np.array([0.0, 105.0, 170.0]) / 255.0
tue_lightblue = np.array([80.0, 170.0, 200.0]) / 255.0
tue_lightgreen = np.array([130.0, 185.0, 160.0]) / 255.0
tue_green = np.array([125.0, 165.0, 75.0]) / 255.0
tue_darkgreen = np.array([50.0, 110.0, 30.0]) / 255.0
tue_ocre = np.array([200.0, 80.0, 60.0]) / 255.0
tue_violet = np.array([175.0, 110.0, 150.0]) / 255.0
tue_mauve = np.array([180.0, 160.0, 150.0]) / 255.0
tue_lightorange = np.array([215.0, 180.0, 105.0]) / 255.0
tue_orange = np.array([210.0, 150.0, 0.0]) / 255.0
tue_brown = np.array([145.0, 105.0, 70.0]) / 255.0

# ProbNum's primary colors: www.probabilistic-numerics.org
pn_green = np.array([40, 186, 180]) / 255.0
pn_blue = np.array([41, 68, 165]) / 255.0

# ProbNum-matching secondary colors
# (made up slightly ad-hoc, please criticise!)
pn_orange = np.array([255, 153, 51]) / 255.0
pn_gray = tue_gray
pn_red = tue_red

# the Corporate-ID colors of the Max Planck Society:
mpg_green = np.array([17, 102, 86]) / 255.0
mpg_lightgreen = mpg_green + 0.5 * (255.0 - mpg_green)  # 50% version
mpg_gray = np.array([221, 222, 214]) / 255.0
mpg_lightgray = mpg_gray + 0.5 * (255.0 - mpg_gray)  # 50% version
