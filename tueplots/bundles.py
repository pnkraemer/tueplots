"""Context managers for plots."""

import matplotlib.pyplot as plt

from tueplots import axes, cycler, figsize, fonts
from tueplots.constants.color import palettes, rgb


def icml2022():
    size = figsize.icml2022()
    font_config = fonts.icml2022()
    return {**font_config, **size}


def neurips2021():
    size = figsize.neurips2021()
    font_config = fonts.neurips2021()
    return {**font_config, **size}


def beamer_moml():
    size = figsize.beamer()
    font_config = fonts.beamer_moml()
    axes_config = axes.lines(color=rgb.tue_dark)
    cycler_config = cycler.cycler(color=palettes.tue_plot)
    return {**font_config, **axes_config, **cycler_config, **size}


def beamer_moml_dark_bg():
    size = figsize.beamer()
    font_config = fonts.beamer_moml_dark_bg()
    axes_config_line = axes.lines(color="w")
    axes_config_face = axes.face(color=rgb.tue_dark)
    cycler_config = cycler.cycler(color=palettes.tue_plot_dark_bg)
    return {
        **font_config,
        **cycler_config,
        **axes_config_line,
        **axes_config_face,
        **size,
    }
