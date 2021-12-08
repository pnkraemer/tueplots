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
tue_secondary1 = _np.array([65,90,140]) / 255.0   % dark blue
tue_secondary2 = _np.array([0,105,170]) / 255.0   % blue
tue_secondary3 = _np.array([80,170,200]) / 255.0  % light blue 
tue_secondary4 = _np.array([130,185,160]) / 255.0 % light green
tue_secondary5 = _np.array([125,165,75]) / 255.0  % green
tue_secondary6 = _np.array([50,110,30]) / 255.0   % dark green
tue_secondary7 = _np.array([200,80,60]) / 255.0   % ocre 
tue_secondary8 = _np.array([175,110,150]) / 255.0 % violet
tue_secondary9 = _np.array([180,160,150]) / 255.0 % mauve
tue_secondary10 = _np.array([215,180,105]) / 255.0% light orange
tue_secondary11 = _np.array([210,150,0]) / 255.0  % orange
tue_secondary12 = _np.array([145,105,70]) / 255.0 % brown

# speaking aliases for the secondary colors
tue_darkblue = tue_secondary1
tue_blue = tue_secondary2
tue_lightblue = tue_secondary3
tue_lightgreen = tue_secondary4
tue_green = tue_secondary5
tue_darkgreen = tue_secondary6
tue_ocre = tue_secondary7
tue_violet = tue_secondary8
tue_mauve = tue_secondary9
tue_lightorange = tue_secondary10
tue_orange = tue_secondary11
tue_brown = tue_secondary12