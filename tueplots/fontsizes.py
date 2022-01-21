"""Fontsize settings."""


def icml2022():
    r"""Font size for ICML 2022.

    Source: https://media.icml.cc/Conferences/ICML2022/Styles/example_paper.pdf
    """
    # ICML text size is 10, but captions are in size 9.
    # Therefore, we use base 9 instead of 10.
    return _from_base(base=9)


def neurips2021():
    """Font size for Neurips 2021."""
    return _from_base(base=10)


def aistats2022():
    """Font size for AISTATS 2022."""
    return _from_base(base=10)


def jmlr2001():
    """Font size for JMLR 2021."""
    return _from_base(base=10.95)


def beamer_moml():
    """Font size for a beamer slide in aspectratio 16:9 with 10pt font."""
    return _from_base(base=10)


def _from_base(*, base):
    return {
        "font.size": base - 1,
        "axes.labelsize": base - 1,
        "legend.fontsize": base - 3,
        "xtick.labelsize": base - 3,
        "ytick.labelsize": base - 3,
        "axes.titlesize": base - 1,
    }
