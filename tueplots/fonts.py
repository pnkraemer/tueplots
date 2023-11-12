"""Font settings for conference papers and journals."""


def neurips2021(*, family="serif"):
    """Fonts for Neurips 2021."""
    return _neurips_and_iclr_common(family=family)


def neurips2021_tex(*, family="serif"):
    """Fonts for Neurips 2021. LaTeX version."""
    return _neurips_and_iclr_tex_common(family=family)


def neurips2022(*, family="serif"):
    """Fonts for Neurips 2022."""
    return _neurips_and_iclr_common(family=family)


def neurips2022_tex(*, family="serif"):
    """Fonts for Neurips 2022. LaTeX version."""
    return _neurips_and_iclr_tex_common(family=family)


def neurips2023(*, family="serif"):
    """Fonts for Neurips 2023."""
    return _neurips_and_iclr_common(family=family)


def neurips2023_tex(*, family="serif"):
    """Fonts for Neurips 2023. LaTeX version."""
    return _neurips_and_iclr_tex_common(family=family)


def iclr2023_tex(*, family="serif"):
    """Fonts for ICLR 2023. LaTeX version."""
    return _neurips_and_iclr_tex_common(family=family)


def iclr2024_tex(*, family="serif"):
    """Fonts for ICLR 2024. LaTeX version."""
    return _neurips_and_iclr_tex_common(family=family)


def iclr2023(*, family="serif"):
    """Fonts for ICLR 2023. LaTeX version."""
    return _neurips_and_iclr_common(family=family)


def iclr2024(*, family="serif"):
    """Fonts for ICLR 2024. LaTeX version."""
    return _neurips_and_iclr_common(family=family)


def cvpr2024_tex(*, family="serif"):
    """Fonts for CVPR 2024. LaTeX version."""
    return _neurips_and_iclr_tex_common(family=family)


def cvpr2024(*, family="serif"):
    """Fonts for CVPR 2024. LaTeX version."""
    return _neurips_and_iclr_common(family=family)


def _neurips_and_iclr_common(*, family="serif"):
    """Default fonts for Neurips."""
    return {
        "text.usetex": False,
        "font.serif": ["Times New Roman"],
        "mathtext.fontset": "stix",  # free ptmx replacement, for ICML and NeurIPS
        "mathtext.rm": "Times New Roman",
        "mathtext.it": "Times New Roman:italic",
        "mathtext.bf": "Times New Roman:bold",
        "font.family": family,
    }


def _neurips_and_iclr_tex_common(*, family="serif"):
    """Default fonts for Neurips. LaTeX version."""
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
    return _tex_times(family=family)


def jmlr2001_tex(*, family="serif"):
    """Fonts for JMLR. LaTeX version."""
    return _tex_computer_modern(family=family)


def tmlr2023_tex(*, family="serif"):
    """Fonts for TMLR. LaTeX version."""
    return _tex_computer_modern(family=family)


def aistats2022_tex(*, family="serif"):
    """Fonts for AISTATS 2022. LaTeX version."""
    return _tex_computer_modern(family=family)


def aistats2023_tex(*, family="serif"):
    """Fonts for AISTATS 2023. LaTeX version."""
    return _tex_times(family=family)


def uai2023_tex(*, family="serif"):
    """Fonts for UAI 2023. LaTeX version."""
    return _tex_times(family=family)


def aaai2024_tex(*, family="serif"):
    """Fonts for AAAI 2024. LaTeX version."""
    return _tex_times(family=family)


def _tex_times(*, family):
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


def _tex_computer_modern(*, family):
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
        "mathtext.fontset": "custom",
        "mathtext.it": "sans:italic",
        "font.sans-serif": ["Roboto Condensed"],
        "font.family": "sans-serif",
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
