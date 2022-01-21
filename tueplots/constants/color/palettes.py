"""Color palettes."""

import numpy as np

from tueplots.constants.color import rgb

tue_primary = np.array(
    [
        rgb.tue_red,
        rgb.tue_dark,
        rgb.tue_gray,
        rgb.tue_gold,
        rgb.tue_lightgold,
    ]
)
"""Primary corporate colors of the University of Tübingen."""

tue_secondary = np.array(
    [
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
    ]
)
"""Secondary corporate colors of the University of Tübingen."""

tue_plot = np.array(
    [
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
    ]
)
"""A mix of the primary and secondary colors from tue TUE color palette(s), ordered in a way that provides okay(ish) color contrast."""

tue_plot_dark_bg = np.array(
    [
        rgb.tue_lightgold,
        rgb.tue_red,
        rgb.tue_lightblue,
        rgb.tue_gray,
        rgb.tue_lightgreen,
        rgb.tue_ocre,
        rgb.tue_violet,
        rgb.tue_mauve,
        rgb.tue_brown,
    ]
)
"""A mix of the primary and secondary colors from tue TUE color palette(s), ordered in a way that provides okay(ish) color contrast when plotting on dark background."""

pn = np.array(
    [
        rgb.pn_blue,
        rgb.pn_green,
        rgb.pn_orange,
        rgb.pn_gray,
        rgb.pn_red,
    ]
)
"""Colors of ProbNum: probnum.org."""

bright = np.array(
    [
        "4477AA",
        "EE6677",
        "228833",
        "CCBB44",
        "66CCEE",
        "AA3377",
        "BBBBBB",
    ]
)
"""Bright colors.

From Paul Tot's website: https://personal.sron.nl/~pault/.
"""

high_contrast = np.array(["004488", "DDAA33", "BB5566"])
"""High-contrast colors.

From Paul Tot's website: https://personal.sron.nl/~pault/.
"""

muted = np.array(
    [
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
    ]
)
"""Muted colors.

From Paul Tot's website: https://personal.sron.nl/~pault/.
"""
