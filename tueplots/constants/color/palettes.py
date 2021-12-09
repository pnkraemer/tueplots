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

tue_plot = (
    rgb.tue_red,
    rgb.tue_dark,
    rgb.tue_gold,
    rgb.tue_blue,
    rgb.tue_gray,
    rgb.tue_green,
    rgb.tue_ocre,
    rgb.tue_violet,
    rgb.tue_mauve,
    rgb.tue_brown,
)
"""A mix of the primary and secondary colors from tue TUE color palette(s), ordered in a way that provides okay(ish) color contrast."""

tue_plot_dark_bg = (
    rgb.tue_lightgold,
    rgb.tue_red,
    rgb.tue_lightblue,
    rgb.tue_gray,
    rgb.tue_lightgreen,
    rgb.tue_ocre,
    rgb.tue_violet,
    rgb.tue_mauve,
    rgb.tue_brown,
)
"""A mix of the primary and secondary colors from tue TUE color palette(s), ordered in a way that provides okay(ish) color contrast when plotting on dark background."""

pn = (
    rgb.pn_blue,
    rgb.pn_orange,
    rgb.pn_green,
    rgb.pn_gray,
    rgb.pn_red,
)

bright = (
    "4477AA",
    "EE6677",
    "228833",
    "CCBB44",
    "66CCEE",
    "AA3377",
    "BBBBBB",
)
"""From Paul Tot's website: https://personal.sron.nl/~pault/."""

high_contrast = ("004488", "DDAA33", "BB5566")
"""From Paul Tot's website: https://personal.sron.nl/~pault/."""

muted = (
    "CC6677",
    "332288",
    "DDCC77",
    "117733",
    "88CCEE",
    "882255",
    "44AA99",
    "999933",
    "AA4499",
    "DDDDDD",
)

"""From Paul Tot's website: https://personal.sron.nl/~pault/."""
