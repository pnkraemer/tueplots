"""Context managers for plots."""

import matplotlib.pyplot as plt

from tueplots import axes, figsize, fonts
from tueplots.color.constants import rgb


def icml2022():
    size = figsize.icml2022()
    font_config = fonts.icml2022()
    return plt.rc_context({**font_config, "figure.figsize": size})


def neurips2021():
    size = figsize.neurips2021()
    font_config = fonts.neurips2021()
    return plt.rc_context({**font_config, "figure.figsize": size})


def beamer_moml():
    size = figsize.beamer()
    font_config = fonts.beamer_moml()
    axes_config = axes.lines(color=rgb.tue_dark)
    return plt.rc_context({**font_config, **axes_config, "figure.figsize": size})


def beamer_moml_dark_bg():
    size = figsize.beamer()
    font_config = fonts.beamer_moml_dark_bg()
    axes_config_line = axes.lines(color="w")
    axes_config_face = axes.face(color=rgb.tue_dark)
    return plt.rc_context(
        {**font_config, **axes_config_line, **axes_config_face, "figure.figsize": size}
    )
