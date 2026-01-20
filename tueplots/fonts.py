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


def neurips2021(*, family="serif", match_math_font=False):
    """Fonts for Neurips 2021."""
    # NeurIPS' style-files states that it uses Times New Roman
    # font, but includes the 'ptm' package, which implements
    # the 'Times' font.
    # Therefore, refer to 'Times' instead of 'Times New Roman'
    return _times(family=family, match_math_font=match_math_font)


def neurips2021_tex(*, family="serif", match_math_font=False):
    """Fonts for Neurips 2021. LaTeX version."""
    return _times_tex_via_pkg_ptm(family=family, match_math_font=match_math_font)


def neurips2022(*, family="serif", match_math_font=False):
    """Fonts for Neurips 2022."""
    # NeurIPS' style-files states that it uses Times New Roman
    # font, but includes the 'ptm' package, which implements
    # the 'Times' font.
    # Therefore, refer to 'Times' instead of 'Times New Roman'
    return _times(family=family, match_math_font=match_math_font)


def neurips2022_tex(*, family="serif", match_math_font=False):
    """Fonts for Neurips 2022. LaTeX version."""
    return _times_tex_via_pkg_ptm(family=family, match_math_font=match_math_font)


def neurips2023(*, family="serif", match_math_font=False):
    """Fonts for Neurips 2023."""
    # NeurIPS' style-files states that it uses Times New Roman
    # font, but includes the 'ptm' package, which implements
    # the 'Times' font.
    # Therefore, refer to 'Times' instead of 'Times New Roman'
    return _times(family=family, match_math_font=match_math_font)


def neurips2023_tex(*, family="serif", match_math_font=False):
    """Fonts for Neurips 2023. LaTeX version."""
    return _times_tex_via_pkg_ptm(family=family, match_math_font=match_math_font)


def neurips2024(*, family="serif", match_math_font=False):
    """Fonts for Neurips 2024."""
    # NeurIPS' style-files states that it uses Times New Roman
    # font, but includes the 'ptm' package, which implements
    # the 'Times' font.
    # Therefore, refer to 'Times' instead of 'Times New Roman'
    return _times(family=family, match_math_font=match_math_font)


def neurips2024_tex(*, family="serif", match_math_font=False):
    """Fonts for Neurips 2024. LaTeX version."""
    return _times_tex_via_pkg_ptm(family=family, match_math_font=match_math_font)


def iclr2023_tex(*, family="serif", match_math_font=False):
    """Fonts for ICLR 2023. LaTeX version."""
    return _times_tex_via_pkg_times(family=family, match_math_font=match_math_font)


def iclr2024_tex(*, family="serif", match_math_font=False):
    """Fonts for ICLR 2024. LaTeX version."""
    return _times_tex_via_pkg_times(family=family, match_math_font=match_math_font)


def iclr2023(*, family="serif", match_math_font=False):
    """Fonts for ICLR 2023."""
    return _times(family=family, match_math_font=match_math_font)


def iclr2024(*, family="serif", match_math_font=False):
    """Fonts for ICLR 2024."""
    return _times(family=family, match_math_font=match_math_font)


def cvpr2024_tex(*, family="serif", match_math_font=False):
    """Fonts for CVPR 2024. LaTeX version."""
    return _times_tex_via_pkg_ptm(family=family, match_math_font=match_math_font)


def cvpr2024(*, family="serif", match_math_font=False):
    """Fonts for CVPR 2024."""
    return _times(family=family, match_math_font=match_math_font)


def icml2022_tex(*, family="serif", match_math_font=False):
    """Fonts for ICML 2022. LaTeX version."""
    return _times_tex_via_pkg_times(family=family, match_math_font=match_math_font)


def icml2024_tex(*, family="serif", match_math_font=False):
    """Fonts for ICML 2024. LaTeX version."""
    return _times_tex_via_pkg_times(family=family, match_math_font=match_math_font)


def eccv2024_tex(*, family="serif", match_math_font=False):
    """Fonts for ECCV 2024. LaTeX version."""
    return _computer_modern_tex(family=family, match_math_font=match_math_font)


def jmlr2001_tex(*, family="serif", match_math_font=False):
    """Fonts for JMLR. LaTeX version."""
    return _computer_modern_tex(family=family, match_math_font=match_math_font)


def tmlr2023_tex(*, family="serif", match_math_font=False):
    """Fonts for TMLR. LaTeX version."""
    return _computer_modern_tex(family=family, match_math_font=match_math_font)


def aistats2022_tex(*, family="serif", match_math_font=False):
    """Fonts for AISTATS 2022. LaTeX version."""
    return _computer_modern_tex(family=family, match_math_font=match_math_font)


def aistats2023_tex(*, family="serif", match_math_font=False):
    """Fonts for AISTATS 2023. LaTeX version."""
    return _computer_modern_tex(family=family, match_math_font=match_math_font)


def aistats2025_tex(*, family="serif", match_math_font=False):
    """Fonts for AISTATS 2025. LaTeX version."""
    return _computer_modern_tex(family=family, match_math_font=match_math_font)


def uai2023_tex(*, family="serif", match_math_font=False):
    """Fonts for UAI 2023. LaTeX version."""
    return _times_tex_via_pkg_times(family=family, match_math_font=match_math_font)


def aaai2024_tex(*, family="serif", match_math_font=False):
    """Fonts for AAAI 2024. LaTeX version."""
    return _times_tex_via_pkg_times(family=family, match_math_font=match_math_font)


def icml2022(*, family="serif", match_math_font=False):
    """Fonts for ICML 2022."""
    return _times(family=family, match_math_font=match_math_font)


def icml2024(*, family="serif", match_math_font=False):
    """Fonts for ICML 2024."""
    return _times(family=family, match_math_font=match_math_font)


def probnum2025_tex(*, family="serif", match_math_font=False):
    """Fonts for ProbNum 2025. LaTeX version."""
    return _computer_modern_tex(family=family, match_math_font=match_math_font)


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


# Helper functions below


def _times(*, family="serif", match_math_font=False):
    """Times font.

    Used, e.g., for ICML 2022.
    """
    config = {
        "text.usetex": False,
        "font.serif": ["Times"],
        "font.family": family,
    }
    if match_math_font:
        config.update(
            {
                "mathtext.fontset": "stix",  # free ptmx replacement, for ICML and NeurIPS
                "mathtext.rm": "Times",
                "mathtext.it": "Times:italic",
                "mathtext.bf": "Times:bold",
            }
        )
    return config


def _times_tex_via_pkg_ptm(*, family, match_math_font=False):
    """Times font, implemented in Latex via the ptm-package.

    Default fonts for Neurips.
    """
    preamble = r"\renewcommand{\rmdefault}{ptm}\renewcommand{\sfdefault}{phv}"
    if family == "serif":
        return {
            "text.usetex": True,
            "font.family": "serif",
            "text.latex.preamble": preamble,
        }
    preamble += r"\renewcommand{\familydefault}{\sfdefault}"
    if match_math_font:
        preamble += r" \usepackage{sansmath} \sansmath"
    return {
        "text.usetex": True,
        "font.family": "sans-serif",
        "text.latex.preamble": preamble,
    }


def _times_tex_via_pkg_times(*, family, match_math_font=False):
    preamble = r"\usepackage{times} "
    if family == "serif":
        return {
            "text.usetex": True,
            "font.family": "serif",
            "text.latex.preamble": preamble,
        }
    preamble += r"\renewcommand{\familydefault}{\sfdefault}"
    if match_math_font:
        preamble += r" \usepackage{sansmath} \sansmath"
    return {
        "text.usetex": True,
        "font.family": "sans-serif",
        "text.latex.preamble": preamble,
    }


def _computer_modern_tex(*, family, match_math_font=False):
    if family == "serif":
        return {
            "text.usetex": True,
            "font.family": "serif",
            "text.latex.preamble": "",
        }
    preamble = r"\renewcommand{\familydefault}{\sfdefault}"
    if match_math_font:
        preamble += r" \usepackage{sansmath} \sansmath"
    return {
        "text.usetex": True,
        "font.family": "sans-serif",
        "text.latex.preamble": preamble,
    }
