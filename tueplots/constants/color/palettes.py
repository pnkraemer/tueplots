"""Color palettes."""


# _np instead of "np", because we dont want to expose numpy through
# `rgb.np`. This is not a bulletproof solution, but "saver" options
# would require a lot more import logic and that feels a bit pointless.
import numpy as _np

from tueplots.constants.color import rgb

tue_primary = (
    rgb.tue_red,
    rgb.tue_dark,
    rgb.tue_gray,
    rgb.tue_gold,
    rgb.tue_lightgold,
)

tue_secondary = (
    rgb.tue_darkblue,
    rgb.tue_blue,
    rgb.tue_lightblue,
    rgb.tue_lightgreen,
    rgb.tue_green,
    rgb.tue_darkgreen,
    rgb.tue_ocre,
    rgb.tue_violet,
    rgb.tue_mauve,
    rgb.tue_lightorange,
    rgb.tue_orange,
    rgb.tue_brown,
)

pn = (
    rgb.pn_blue,
    rgb.pn_orange,
    rgb.pn_green,
    rgb.pn_gray,
    rgb.pn_red,
)
