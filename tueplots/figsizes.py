"""Figure size settings."""

# Some useful constants
_GOLDEN_RATIO = (5.0 ** 0.5 - 1.0) / 2.0
_INCHES_PER_POINT = 1.0 * 72.27

# Double-column formats


def icml2022(
    *, column="full", nrows=1, ncols=1, constrained_layout=True, tight_layout=False
):

    if column == "half":
        figsize = _from_base(
            width_pt=234.8775,
            nrows=nrows,
            ncols=ncols,
            height_per_width=_GOLDEN_RATIO,
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
        height_per_width=_GOLDEN_RATIO / 2.0,
    )
    return {
        "figure.figsize": figsize,
        "figure.constrained_layout.use": constrained_layout,
        "figure.autolayout": tight_layout,
    }


def cvpr2022(
    *, column="full", nrows=1, ncols=1, constrained_layout=True, tight_layout=False
):

    if column == "half":
        figsize = _from_base(
            width_pt=237.13594,
            nrows=nrows,
            ncols=ncols,
            height_per_width=_GOLDEN_RATIO,
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
        height_per_width=_GOLDEN_RATIO / 2.0,
    )
    return {
        "figure.figsize": figsize,
        "figure.constrained_layout.use": constrained_layout,
        "figure.autolayout": tight_layout,
    }


# Single-column formats


def jmlr2001(*, nrows=1, ncols=1, constrained_layout=True, tight_layout=False):
    """JMLR figure size"""

    figsize = _from_base(
        width_pt=433.62,
        nrows=nrows,
        ncols=ncols,
        height_per_width=_GOLDEN_RATIO / 2.0,
    )
    return {
        "figure.figsize": figsize,
        "figure.constrained_layout.use": constrained_layout,
        "figure.autolayout": tight_layout,
    }


def neurips2021(*, nrows=1, ncols=1, constrained_layout=True, tight_layout=False):

    figsize = _from_base(
        width_pt=397.48499,
        nrows=nrows,
        ncols=ncols,
        height_per_width=_GOLDEN_RATIO / 2.0,
    )
    return {
        "figure.figsize": figsize,
        "figure.constrained_layout.use": constrained_layout,
        "figure.autolayout": tight_layout,
    }


def _from_base(*, width_pt, nrows, height_per_width, ncols):
    width_inches = width_pt / _INCHES_PER_POINT
    height_inches = height_per_width * width_inches * nrows / ncols
    return width_inches, height_inches


# Other formats


def beamer_169(
    *, rel_width=1.0, rel_height=0.8, constrained_layout=True, tight_layout=False
):
    """Beamer figure size for `aspectratio=169`."""
    width = 398.3386 / _INCHES_PER_POINT * rel_width
    height = 241.56738 / _INCHES_PER_POINT * rel_height
    return {
        "figure.figsize": (width, height),
        "figure.constrained_layout.use": constrained_layout,
        "figure.autolayout": tight_layout,
    }
