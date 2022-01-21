"""Bundled configurations."""

from tueplots import axes, cycler, figsizes, fonts, fontsizes
from tueplots.constants.color import palettes, rgb


def icml2022(*, column="half", nrows=1, ncols=1, usetex=True, family="sans-serif"):
    """ICML 2022 bundle."""
    if column == "half":
        size = figsizes.icml2022_half(nrows=nrows, ncols=ncols)
    elif column == "full":
        size = figsizes.icml2022_full(nrows=nrows, ncols=ncols)
    if usetex is True:
        font_config = fonts.icml2022_tex(family=family)
    elif usetex is False:
        font_config = fonts.icml2022(family=family)
    fontsize_config = fontsizes.icml2022()
    return {**font_config, **size, **fontsize_config}


def aistats2022(*, column="half", nrows=1, ncols=1, family="sans-serif"):
    """AISTATS 2022 bundle."""
    if column == "half":
        size = figsizes.aistats2022_half(nrows=nrows, ncols=ncols)
    elif column == "full":
        size = figsizes.aistats2022_full(nrows=nrows, ncols=ncols)
    font_config = fonts.aistats2022_tex(family=family)
    fontsize_config = fontsizes.aistats2022()
    return {**font_config, **size, **fontsize_config}


def jmlr2001(*, nrows=1, ncols=1, family="sans-serif"):
    """JMLR 2001 bundle."""
    size = figsizes.jmlr2001(nrows=nrows, ncols=ncols)
    font_config = fonts.jmlr2001_tex(family=family)
    fontsize_config = fontsizes.jmlr2001()
    return {**font_config, **size, **fontsize_config}


def neurips2021(*, usetex=True, nrows=1, ncols=1, family="sans-serif"):
    """Neurips 2021 bundle."""
    if usetex is True:
        font_config = fonts.neurips2021_tex(family=family)
    elif usetex is False:
        font_config = fonts.neurips2021(family=family)
    size = figsizes.neurips2021(nrows=nrows, ncols=ncols)
    fontsize_config = fontsizes.neurips2021()
    return {**font_config, **size, **fontsize_config}


def beamer_moml(*, rel_width=1.0, rel_height=0.8):
    """Beamer bundle that matches the template of the method-of-machine-learning group in Tübingen."""
    size = figsizes.beamer_169(rel_width=rel_width, rel_height=rel_height)
    font_config = fonts.beamer_moml()
    axes_config_line = axes.lines()
    axes_config_grid = axes.grid()
    axes_config_color = axes.color(base=rgb.tue_dark)
    cycler_config = cycler.cycler(color=palettes.tue_plot)
    fontsize_config = fontsizes.beamer_moml()
    return {
        **size,
        **font_config,
        **fontsize_config,
        **axes_config_line,
        **axes_config_grid,
        **axes_config_color,
        **cycler_config,
    }


def beamer_moml_dark_bg(*, rel_width=1.0, rel_height=0.8):
    """Dark version of :func:`beamer_moml`."""
    size = figsizes.beamer_169(rel_width=rel_width, rel_height=rel_height)
    font_config = fonts.beamer_moml_dark_bg()
    axes_config_line = axes.lines()
    axes_config_grid = axes.grid()
    axes_config_color = axes.color(face=rgb.tue_dark, base="w")
    cycler_config = cycler.cycler(color=palettes.tue_plot_dark_bg)
    fontsize_config = fontsizes.beamer_moml()
    return {
        **size,
        **font_config,
        **fontsize_config,
        **axes_config_line,
        **axes_config_grid,
        **axes_config_color,
        **cycler_config,
    }
