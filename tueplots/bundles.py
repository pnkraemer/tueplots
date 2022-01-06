"""Context managers for plots."""

from tueplots import axes, cycler, figsize, fonts, fontsizes
from tueplots.constants.color import palettes, rgb


def icml2022(*, column="half", nrows=1, family="sans-serif"):
    size = figsize.icml2022(column=column, nrows=nrows)
    font_config = fonts.icml2022(family=family)
    fontsize_config = fontsizes.icml2022()
    return {**font_config, **size, **fontsize_config}


def icml2022_tex(*, column="half", nrows=1, family="sans-serif"):
    size = figsize.icml2022(column=column, nrows=nrows)
    font_config = fonts.icml2022_tex(family=family)
    fontsize_config = fontsizes.icml2022()
    return {**font_config, **size, **fontsize_config}


def neurips2021(*, nrows=1, family="sans-serif"):
    size = figsize.neurips2021(nrows=nrows)
    font_config = fonts.neurips2021(family=family)
    fontsize_config = fontsizes.neurips2021()
    return {**font_config, **size, **fontsize_config}


def neurips2021_tex(*, nrows=1, family="sans-serif"):
    size = figsize.neurips2021(nrows=nrows)
    font_config = fonts.neurips2021_tex(family=family)
    fontsize_config = fontsizes.neurips2021()
    return {**font_config, **size, **fontsize_config}


def beamer_moml(*, rel_width=1, rel_height=1):
    size = figsize.beamer(rel_width=rel_width, rel_height=rel_height)
    font_config = fonts.beamer_moml()
    axes_config = axes.lines(color=rgb.tue_dark)
    cycler_config = cycler.cycler(color=palettes.tue_plot)
    fontsize_config = fontsizes.beamer_moml()
    return {**font_config, **axes_config, **cycler_config, **size, **fontsize_config}


def beamer_moml_dark_bg(*, rel_width=1, rel_height=1):
    size = figsize.beamer(rel_width=rel_width, rel_height=rel_height)
    font_config = fonts.beamer_moml_dark_bg()
    axes_config_line = axes.lines(color="w")
    axes_config_face = axes.face(color=rgb.tue_dark)
    cycler_config = cycler.cycler(color=palettes.tue_plot_dark_bg)
    fontsize_config = fontsizes.beamer_moml()
    return {
        **font_config,
        **cycler_config,
        **axes_config_line,
        **axes_config_face,
        **size,
        **fontsize_config,
    }
