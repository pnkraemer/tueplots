"""Font settings for plots (:mod:`tueplots.fonts`).

Configures fonts to match LaTeX documents.


Examples
--------

.. plot::
    :include-source: True

    >>> import matplotlib.pyplot as plt
    >>> from tueplots import fonts
    >>>
    >>> # Select a style bundle
    >>> style = fonts.neurips2021()
    >>>
    >>> # Apply the style to matplotlib
    >>> plt.rcParams.update(style)
    >>>
    >>> # Create a plot
    >>> fig, ax = plt.subplots()
    >>> ax.plot([0, 1, 2], [2, 1, 3])
    >>> ax.set_xlabel("$x$ label")
    >>> ax.set_ylabel("$y$ label")
    >>> plt.show()


"""


def neurips2021(*, family="serif"):
    """Fonts for Neurips 2021."""
    # NeurIPS' style-files states that it uses Times New Roman
    # font, but includes the 'ptm' package, which implements
    # the 'Times' font.
    # Therefore, refer to 'Times' instead of 'Times New Roman'
    return _times_text_cmodern_math(family=family)


def neurips2021_tex(*, family="serif"):
    """Fonts for Neurips 2021. LaTeX version."""
    return _times_tex_via_pkg_ptm(family=family)


def neurips2022(*, family="serif"):
    """Fonts for Neurips 2022."""
    # NeurIPS' style-files states that it uses Times New Roman
    # font, but includes the 'ptm' package, which implements
    # the 'Times' font.
    # Therefore, refer to 'Times' instead of 'Times New Roman'
    return _times_text_cmodern_math(family=family)


def neurips2022_tex(*, family="serif"):
    """Fonts for Neurips 2022. LaTeX version."""
    return _times_tex_via_pkg_ptm(family=family)


def neurips2023(*, family="serif"):
    """Fonts for Neurips 2023."""
    # NeurIPS' style-files states that it uses Times New Roman
    # font, but includes the 'ptm' package, which implements
    # the 'Times' font.
    # Therefore, refer to 'Times' instead of 'Times New Roman'
    return _times_text_cmodern_math(family=family)


def neurips2023_tex(*, family="serif"):
    """Fonts for Neurips 2023. LaTeX version."""
    return _times_tex_via_pkg_ptm(family=family)


def neurips2024(*, family="serif"):
    """Fonts for Neurips 2024."""
    # NeurIPS' style-files states that it uses Times New Roman
    # font, but includes the 'ptm' package, which implements
    # the 'Times' font.
    # Therefore, refer to 'Times' instead of 'Times New Roman'
    return _times_text_cmodern_math(family=family)


def neurips2024_tex(*, family="serif"):
    """Fonts for Neurips 2024. LaTeX version."""
    return _times_tex_via_pkg_ptm(family=family)


def iclr2023_tex(*, family="serif"):
    """Fonts for ICLR 2023. LaTeX version."""
    return _times_tex_via_pkg_times(family=family)


def iclr2024_tex(*, family="serif"):
    """Fonts for ICLR 2024. LaTeX version."""
    return _times_tex_via_pkg_times(family=family)


def iclr2023(*, family="serif"):
    """Fonts for ICLR 2023."""
    return _times_text_cmodern_math(family=family)


def iclr2024(*, family="serif"):
    """Fonts for ICLR 2024."""
    return _times_text_cmodern_math(family=family)


def cvpr2024_tex(*, family="serif"):
    """Fonts for CVPR 2024. LaTeX version."""
    return _times_tex_via_pkg_ptm(family=family)


def cvpr2024(*, family="serif"):
    """Fonts for CVPR 2024."""
    return _times_text_cmodern_math(family=family)


def icml2022_tex(*, family="serif"):
    """Fonts for ICML 2022. LaTeX version."""
    return _times_tex_via_pkg_times(family=family)


def icml2024_tex(*, family="serif"):
    """Fonts for ICML 2024. LaTeX version."""
    return _times_tex_via_pkg_times(family=family)


def eccv2024_tex(*, family="serif"):
    """Fonts for ECCV 2024. LaTeX version."""
    return _computer_modern_tex(family=family)


def jmlr2001_tex(*, family="serif"):
    """Fonts for JMLR. LaTeX version."""
    return _computer_modern_tex(family=family)


def tmlr2023_tex(*, family="serif"):
    """Fonts for TMLR. LaTeX version."""
    return _computer_modern_tex(family=family)


def aistats2022_tex(*, family="serif"):
    """Fonts for AISTATS 2022. LaTeX version."""
    return _computer_modern_tex(family=family)


def aistats2023_tex(*, family="serif"):
    """Fonts for AISTATS 2023. LaTeX version."""
    return _computer_modern_tex(family=family)


def aistats2025_tex(*, family="serif"):
    """Fonts for AISTATS 2025. LaTeX version."""
    return _computer_modern_tex(family=family)


def uai2023_tex(*, family="serif"):
    """Fonts for UAI 2023. LaTeX version."""
    return _times_tex_via_pkg_times(family=family)


def aaai2024_tex(*, family="serif"):
    """Fonts for AAAI 2024. LaTeX version."""
    return _times_tex_via_pkg_times(family=family)


def icml2022(*, family="serif"):
    """Fonts for ICML 2022."""
    return _times_text_cmodern_math(family=family)


def icml2024(*, family="serif"):
    """Fonts for ICML 2024."""
    return _times_text_cmodern_math(family=family)


def probnum2025_tex(*, family="serif"):
    """Fonts for ProbNum 2025. LaTeX version."""
    return _computer_modern_tex(family=family)


def tue_ai_thesis_tex(*, family="serif"):
    """Fonts for Tübingen AI Center thesis."""
    return _computer_modern_tex(family=family)


def roboto_condensed():
    """Robot fonts, typically used with the beamer templates."""
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


# Helper functions below

_TIMES_LIKE = ["Times New Roman", "Times", "TeX Gyre Termes", "Nimbus Roman"]
_HELVET_LIKE = [
    "Helvetica",
    "Helvetica Neue",
    "TeX Gyre Heros",
    "Nimbus Sans",
    "Nimbus Sans L",
]


def _times_text_cmodern_math(*, family="serif"):
    r"""Choose a Times text font with Computer Modern math.

    Mirrors the TeX behavior of \usepackage{times} and \usepackage{ptm},
    which use Times for text but Computer Modern for math.
    Used for non-TeX versions of NeurIPS, ICML, ICLR, CVPR, etc.
    """
    return {
        "text.usetex": False,
        "font.serif": _TIMES_LIKE,
        "font.sans-serif": _HELVET_LIKE,
        "font.family": family,
        "mathtext.fontset": "cm",
    }


def _times_tex_via_pkg_ptm(*, family):
    """Choose the Times font, implemented in Latex via the ptm-package.

    Default fonts for Neurips.
    """
    preamble = r"\renewcommand{\rmdefault}{ptm}\renewcommand{\sfdefault}{phv}"
    if family == "serif":
        return {
            "text.usetex": True,
            "font.family": "serif",
            "text.latex.preamble": preamble,
        }
    preamble += r" \renewcommand{\familydefault}{\sfdefault}"
    preamble += r" \usepackage{sansmath} \sansmath"
    return {
        "text.usetex": True,
        "font.family": "sans-serif",
        "text.latex.preamble": preamble,
    }


def _times_tex_via_pkg_times(*, family):
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


def _computer_modern_tex(*, family):
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
