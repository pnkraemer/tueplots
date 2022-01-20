"""Figure size settings."""

# Some useful constants
_GOLDEN_RATIO = (5.0 ** 0.5 - 1.0) / 2.0
_INCHES_PER_POINT = 1.0 * 72.27

# Double-column formats


def icml2022_half(**kwargs):
    return _icml2022_and_aistats2022_half(**kwargs)


def icml2022_full(**kwargs):
    return _icml2022_and_aistats2022_full(**kwargs)


def aistats2022_half(**kwargs):
    return _icml2022_and_aistats2022_half(**kwargs)


def aistats2022_full(**kwargs):
    return _icml2022_and_aistats2022_full(**kwargs)


def _icml2022_and_aistats2022_half(
    *,
    nrows=1,
    ncols=1,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
):
    figsize = _from_base_in(
        width_in=3.25,
        nrows=nrows,
        ncols=ncols,
        height_to_width_ratio=height_to_width_ratio,
    )
    return {
        "figure.figsize": figsize,
        "figure.constrained_layout.use": constrained_layout,
        "figure.autolayout": tight_layout,
    }


def _icml2022_and_aistats2022_full(
    *,
    nrows=1,
    ncols=1,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
):
    figsize = _from_base_in(
        width_in=6.75,
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
        figsize = _from_base_pt(
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

    figsize = _from_base_pt(
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

    figsize = _from_base_pt(
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

    figsize = _from_base_pt(
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


def _from_base_pt(*, width_pt, **kwargs):
    width_in = width_pt / _INCHES_PER_POINT
    return _from_base_in(width_in=width_in, **kwargs)


def _from_base_in(*, width_in, nrows, height_to_width_ratio, ncols):
    height_in = height_to_width_ratio * width_in * nrows / ncols
    return width_in, height_in


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
