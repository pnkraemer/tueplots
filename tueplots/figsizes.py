"""Figure size settings."""

# Some useful constants
_GOLDEN_RATIO = (5.0 ** 0.5 - 1.0) / 2.0
_INCHES_PER_POINT = 1.0 * 72.27

# Double-column formats


def icml2022(
    *,
    column="full",
    nrows=1,
    ncols=1,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
):

    if column == "half":
        figsize = _from_base(
            width_pt=234.8775,
            nrows=nrows,
            ncols=ncols,
            height_to_width_ratio=height_to_width_ratio,
        )
        return {
            "figure.figsize": figsize,
            "figure.constrained_layout.use": constrained_layout,
            "figure.autolayout": tight_layout,
        }

    figsize = _from_base(
        width_pt=487.8225,
        nrows=nrows,
        ncols=ncols,
        height_to_width_ratio=height_to_width_ratio / 2.0,
    )
    return {
        "figure.figsize": figsize,
        "figure.constrained_layout.use": constrained_layout,
        "figure.autolayout": tight_layout,
    }


def aistats2022(
    *,
    column="full",
    nrows=1,
    ncols=1,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
):

    if column == "half":
        figsize = _from_base(
            width_pt=3.25 * _INCHES_PER_POINT,
            nrows=nrows,
            ncols=ncols,
            height_to_width_ratio=height_to_width_ratio,
        )
        return {
            "figure.figsize": figsize,
            "figure.constrained_layout.use": constrained_layout,
            "figure.autolayout": tight_layout,
        }

    figsize = _from_base(
        width_pt=6.75 * _INCHES_PER_POINT,
        nrows=nrows,
        ncols=ncols,
        height_to_width_ratio=height_to_width_ratio / 2.0,
    )
    return {
        "figure.figsize": figsize,
        "figure.constrained_layout.use": constrained_layout,
        "figure.autolayout": tight_layout,
    }


def cvpr2022(
    *,
    column="full",
    nrows=1,
    ncols=1,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
):

    if column == "half":
        figsize = _from_base(
            width_pt=237.13594,
            nrows=nrows,
            ncols=ncols,
            height_to_width_ratio=height_to_width_ratio,
        )
        return {
            "figure.figsize": figsize,
            "figure.constrained_layout.use": constrained_layout,
            "figure.autolayout": tight_layout,
        }

    figsize = _from_base(
        width_pt=496.85625,
        nrows=nrows,
        ncols=ncols,
        height_to_width_ratio=height_to_width_ratio / 2.0,
    )
    return {
        "figure.figsize": figsize,
        "figure.constrained_layout.use": constrained_layout,
        "figure.autolayout": tight_layout,
    }


# Single-column formats


def jmlr2001(
    *,
    nrows=1,
    ncols=2,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
):
    """JMLR figure size"""

    figsize = _from_base(
        width_pt=433.62,
        nrows=nrows,
        ncols=ncols,
        height_to_width_ratio=height_to_width_ratio,
    )
    return {
        "figure.figsize": figsize,
        "figure.constrained_layout.use": constrained_layout,
        "figure.autolayout": tight_layout,
    }


def neurips2021(
    *,
    nrows=1,
    ncols=2,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
):

    figsize = _from_base(
        width_pt=397.48499,
        nrows=nrows,
        ncols=ncols,
        height_to_width_ratio=height_to_width_ratio,
    )
    return {
        "figure.figsize": figsize,
        "figure.constrained_layout.use": constrained_layout,
        "figure.autolayout": tight_layout,
    }


def _from_base(*, width_pt, nrows, height_to_width_ratio, ncols):
    width_inches = width_pt / _INCHES_PER_POINT
    height_inches = height_to_width_ratio * width_inches * nrows / ncols
    return width_inches, height_inches


# Other formats


def beamer_169(
    *, rel_width=0.9, rel_height=0.6, constrained_layout=True, tight_layout=False
):
    """Beamer figure size for `aspectratio=169`."""
    textwidth_169_pt = 398.3386  # via '\showthe\textwidth' in latex
    textwidth_169_in = textwidth_169_pt / _INCHES_PER_POINT
    textheight_169_in = textwidth_169_in / 16.0 * 9.0

    figsize = (textwidth_169_in * rel_width, textheight_169_in * rel_height)
    return {
        "figure.figsize": figsize,
        "figure.constrained_layout.use": constrained_layout,
        "figure.autolayout": tight_layout,
    }
