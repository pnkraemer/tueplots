"""Font settings for conference papers and journals."""


def neurips2021(*, family="serif"):
    """Fonts for Neurips 2021."""
    return {
        "text.usetex": False,
        "font.serif": ["Times New Roman"],
        "mathtext.fontset": "stix",  # free ptmx replacement, for ICML and NeurIPS
        "mathtext.rm": "Times New Roman",
        "mathtext.it": "Times New Roman:italic",
        "mathtext.bf": "Times New Roman:bold",
        "font.family": family,
    }


def neurips2021_tex(*, family="serif"):
    """Fonts for Neurips 2021. LaTeX version."""
    preamble = r"\renewcommand{\rmdefault}{ptm}\renewcommand{\sfdefault}{phv}"
    if family == "serif":
        return {
            "text.usetex": True,
            "font.family": "serif",
            "text.latex.preamble": preamble,
        }
    preamble += (
        r"\renewcommand{\familydefault}{\sfdefault} \usepackage{sansmath} \sansmath"
    )
    return {
        "text.usetex": True,
        "font.family": "sans-serif",
        "text.latex.preamble": preamble,
    }


def icml2022(*, family="serif"):
    """Fonts for ICML 2022."""

    return {
        "text.usetex": False,
        "font.serif": ["Times"],
        "mathtext.fontset": "stix",  # free ptmx replacement, for ICML and NeurIPS
        "mathtext.rm": "Times",
        "mathtext.it": "Times:italic",
        "mathtext.bf": "Times:bold",
        "font.family": family,
    }


def icml2022_tex(*, family="serif"):
    """Fonts for ICML 2022. LaTeX version."""

    preamble = r"\usepackage{times} "
    if family == "serif":
        return {
            "text.usetex": True,
            "font.family": "serif",
            "text.latex.preamble": preamble,
        }
    preamble += (
        r"\renewcommand{\familydefault}{\sfdefault} \usepackage{sansmath} \sansmath"
    )
    return {
        "text.usetex": True,
        "font.family": "sans-serif",
        "text.latex.preamble": preamble,
    }


def jmlr2001_tex(*, family="serif"):
    """Fonts for JMLR. LaTeX version."""
    return _tex_computer_modern(family=family)


def aistats2022_tex(*, family="serif"):
    """Fonts for AISTATS 2022. LaTeX version."""
    return _tex_computer_modern(family=family)


def _tex_computer_modern(*, family="serif"):
    if family == "serif":
        return {
            "text.usetex": True,
            "font.family": "serif",
            "text.latex.preamble": "",
        }
    preamble = (
        r"\renewcommand{\familydefault}{\sfdefault} \usepackage{sansmath} \sansmath"
    )
    return {
        "text.usetex": True,
        "font.family": "sans-serif",
        "text.latex.preamble": preamble,
    }


def beamer_moml():
    """Fonts that are compatible with the beamer template of the method-of-machine-learning group in Tübingen."""
    return {
        "text.usetex": False,
        "font.serif": ["Roboto Condensed"],
        "font.family": "serif",
        "font.weight": "light",
        "axes.labelweight": "light",
        "axes.titleweight": "light",
    }


def beamer_moml_dark_bg():
    """Fonts for :func:`beamer_moml` with dark background."""
    return {
        "text.usetex": False,
        "font.serif": ["Roboto Condensed"],
        "font.family": "serif",
        "font.weight": "light",
        "axes.labelweight": "light",
        "axes.titleweight": "light",
    }
