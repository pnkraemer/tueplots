"""Fontsize settings."""

import warnings


def icml2022(*, default_smaller=1):
    r"""Font size for ICML 2022.

    Source: https://media.icml.cc/Conferences/ICML2022/Styles/example_paper.pdf
    """
    # ICML text size is 10, but captions are in size 9.
    # Therefore, we use base 9 instead of 10.
    return _from_base(base=9 - default_smaller)


def icml2024(*, default_smaller=1):
    r"""Font size for ICML 2024.

    Source: https://media.icml.cc/Conferences/ICML2024/Styles/example_paper.pdf
    """
    # ICML text size is 10, but captions are in size 9.
    # Therefore, we use base 9 instead of 10.
    return _from_base(base=9 - default_smaller)


def cvpr2024(*, default_smaller=1):
    """Font size for CVPR 2024."""
    # CVPR text size is 10, but captions are in size 9.
    # Therefore, we use base 9 instead of 10.
    return _from_base(base=9 - default_smaller)


def neurips2021(*, default_smaller=1):
    """Font size for Neurips 2021."""
    return _from_base(base=10 - default_smaller)


def neurips2022(*, default_smaller=1):
    """Font size for Neurips 2022."""
    return _from_base(base=10 - default_smaller)


def neurips2023(*, default_smaller=1):
    """Font size for Neurips 2023."""
    return _from_base(base=10 - default_smaller)


def neurips2024(*, default_smaller=1):
    """Font size for Neurips 2024."""
    return _from_base(base=10 - default_smaller)


def iclr2023(*, default_smaller=1):
    """Font size for ICLR 2023."""
    return _from_base(base=10 - default_smaller)


def iclr2024(*, default_smaller=1):
    """Font size for ICLR 2024."""
    return _from_base(base=10 - default_smaller)


def aistats2022(*, default_smaller=1):
    """Font size for AISTATS 2022."""
    return _from_base(base=10 - default_smaller)


def aistats2023(*, default_smaller=1):
    """Font size for AISTATS 2023."""
    return _from_base(base=10 - default_smaller)


def aistats2025(*, default_smaller=1):
    """Font size for AISTATS 2025."""
    return _from_base(base=10 - default_smaller)


def aaai2024(*, default_smaller=1):
    """Font size for AAAI 2024."""
    return _from_base(base=10 - default_smaller)


def uai2023(*, default_smaller=1):
    """Font size for UAI 2023."""
    return _from_base(base=10 - default_smaller)


def eccv2024(*, default_smaller=1):
    """Font size for ECCV 2024."""
    # ECCV text size is 10, but captions are in size 9.
    # Therefore, we use base 9 instead of 10.
    return _from_base(base=9 - default_smaller)


def jmlr2001(*, default_smaller=1):
    """Font size for JMLR 2021."""
    return _from_base(base=10.95 - default_smaller)


def tmlr2023(*, default_smaller=1):
    """Font size for TMLR 2023."""
    return _from_base(base=10 - default_smaller)


def beamer_moml(**kwargs):
    """Font size for a beamer slide in aspectratio 16:9 with 10pt font.

    Deprecated in v0.0.16. Use 'fontsizes.beamer' instead.
    """
    msg = "'fontsizes.beamer_moml' has been renamed to 'fontsizes.beamer' in v0.0.16."
    msg += " The old API will be removed any time after January 1st, 2025."
    warnings.warn(msg, DeprecationWarning)
    return beamer(**kwargs)


def beamer(*, default_smaller=1):
    """Font size for a beamer slide (in aspectratio 16:9 with 10pt font)."""
    return _from_base(base=10 - default_smaller)


def _from_base(*, base, small_offset=2):
    """Set all font-sizes based on a base-size.

    "small_offset" is the amount by which
    the small elements of the figure should be smaller than "base".
    This affects legends, xticks, yticks, etc.
    """
    return {
        "font.size": base,
        "axes.labelsize": base,
        "legend.fontsize": base - small_offset,
        "xtick.labelsize": base - small_offset,
        "ytick.labelsize": base - small_offset,
        "axes.titlesize": base,
    }
