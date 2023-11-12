"""Bundled configurations."""

from tueplots import axes, cycler, figsizes, fonts, fontsizes
from tueplots.constants.color import palettes, rgb


def cvpr2024(*, column="half", nrows=1, ncols=1, usetex=True, family="serif"):
    """CVPR 2024 bundle."""
    if column == "half":
        size = figsizes.cvpr2024_half(nrows=nrows, ncols=ncols)
    elif column == "full":
        size = figsizes.cvpr2024_full(nrows=nrows, ncols=ncols)
    if usetex is True:
        font_config = fonts.cvpr2024_tex(family=family)
    elif usetex is False:
        font_config = fonts.cvpr2024(family=family)
    fontsize_config = fontsizes.cvpr2024()
    return {**font_config, **size, **fontsize_config}


def icml2022(*, column="half", nrows=1, ncols=1, usetex=True, family="serif"):
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


def aistats2022(*, column="half", nrows=1, ncols=1, family="serif"):
    """AISTATS 2022 bundle."""
    if column == "half":
        size = figsizes.aistats2022_half(nrows=nrows, ncols=ncols)
    elif column == "full":
        size = figsizes.aistats2022_full(nrows=nrows, ncols=ncols)
    font_config = fonts.aistats2022_tex(family=family)
    fontsize_config = fontsizes.aistats2022()
    return {**font_config, **size, **fontsize_config}


def aistats2023(*, column="half", nrows=1, ncols=1, family="serif"):
    """AISTATS 2023 bundle."""
    if column == "half":
        size = figsizes.aistats2023_half(nrows=nrows, ncols=ncols)
    elif column == "full":
        size = figsizes.aistats2023_full(nrows=nrows, ncols=ncols)
    font_config = fonts.aistats2023_tex(family=family)
    fontsize_config = fontsizes.aistats2023()
    return {**font_config, **size, **fontsize_config}


def aaai2024(*, column="half", nrows=1, ncols=1, family="serif", rel_width=1.0):
    """AAAI 2024 bundle.

    Source: https://aaai.org/wp-content/uploads/2023/06/AuthorKit24.zip
    """
    if column == "half":
        size = figsizes.aaai2024_half(nrows=nrows, ncols=ncols, rel_width=rel_width)
    elif column == "full":
        size = figsizes.aaai2024_full(nrows=nrows, ncols=ncols, rel_width=rel_width)
    font_config = fonts.aaai2024_tex(family=family)
    fontsize_config = fontsizes.aaai2024()
    return {**font_config, **size, **fontsize_config}


def uai2023(*, column="half", nrows=1, ncols=1, family="serif"):
    """UAI 2023 bundle."""
    if column == "half":
        size = figsizes.uai2023_half(nrows=nrows, ncols=ncols)
    elif column == "full":
        size = figsizes.uai2023_full(nrows=nrows, ncols=ncols)
    font_config = fonts.uai2023_tex(family=family)
    fontsize_config = fontsizes.uai2023()
    return {**font_config, **size, **fontsize_config}


def jmlr2001(*, rel_width=1.0, nrows=1, ncols=1, family="serif"):
    """JMLR 2001 bundle."""
    size = figsizes.jmlr2001(rel_width=rel_width, nrows=nrows, ncols=ncols)
    font_config = fonts.jmlr2001_tex(family=family)
    fontsize_config = fontsizes.jmlr2001()
    return {**font_config, **size, **fontsize_config}


def tmlr2023(*, rel_width=1.0, nrows=1, ncols=1, family="serif"):
    """TMLR 2023 bundle."""
    size = figsizes.tmlr2023(rel_width=rel_width, nrows=nrows, ncols=ncols)
    font_config = fonts.tmlr2023_tex(family=family)
    fontsize_config = fontsizes.tmlr2023()
    return {**font_config, **size, **fontsize_config}


def neurips2021(*, usetex=True, rel_width=1.0, nrows=1, ncols=1, family="serif"):
    """Neurips 2021 bundle."""
    if usetex is True:
        font_config = fonts.neurips2021_tex(family=family)
    elif usetex is False:
        font_config = fonts.neurips2021(family=family)
    size = figsizes.neurips2021(rel_width=rel_width, nrows=nrows, ncols=ncols)
    fontsize_config = fontsizes.neurips2021()
    return {**font_config, **size, **fontsize_config}


def neurips2022(*, usetex=True, rel_width=1.0, nrows=1, ncols=1, family="serif"):
    """Neurips 2022 bundle."""
    if usetex is True:
        font_config = fonts.neurips2022_tex(family=family)
    elif usetex is False:
        font_config = fonts.neurips2022(family=family)
    size = figsizes.neurips2022(rel_width=rel_width, nrows=nrows, ncols=ncols)
    fontsize_config = fontsizes.neurips2022()
    return {**font_config, **size, **fontsize_config}


def neurips2023(*, usetex=True, rel_width=1.0, nrows=1, ncols=1, family="serif"):
    """Neurips 2023 bundle."""
    if usetex is True:
        font_config = fonts.neurips2023_tex(family=family)
    elif usetex is False:
        font_config = fonts.neurips2023(family=family)
    size = figsizes.neurips2023(rel_width=rel_width, nrows=nrows, ncols=ncols)
    fontsize_config = fontsizes.neurips2023()
    return {**font_config, **size, **fontsize_config}


def iclr2023(*, usetex=True, rel_width=1.0, nrows=1, ncols=1, family="serif"):
    """ICLR 2023 bundle."""
    if usetex is True:
        font_config = fonts.iclr2023_tex(family=family)
    elif usetex is False:
        font_config = fonts.iclr2023(family=family)
    size = figsizes.iclr2023(rel_width=rel_width, nrows=nrows, ncols=ncols)
    fontsize_config = fontsizes.iclr2023()
    return {**font_config, **size, **fontsize_config}


def iclr2024(*, usetex=True, rel_width=1.0, nrows=1, ncols=1, family="serif"):
    """ICLR 2024 bundle."""
    if usetex is True:
        font_config = fonts.iclr2024_tex(family=family)
    elif usetex is False:
        font_config = fonts.iclr2024(family=family)
    size = figsizes.iclr2024(rel_width=rel_width, nrows=nrows, ncols=ncols)
    fontsize_config = fontsizes.iclr2024()
    return {**font_config, **size, **fontsize_config}


def beamer_moml(
    *,
    rel_width=1.0,
    rel_height=0.8,
):
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
