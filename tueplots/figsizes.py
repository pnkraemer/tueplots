"""Figure size settings."""

# Some useful constants
_GOLDEN_RATIO = (5.0**0.5 - 1.0) / 2.0
_POINTS_PER_INCH = 72.27

# Double-column formats


def icml2022_half(**kwargs):
    """Double-column (half-width) figures for ICML 2022."""
    return _icml2022_and_aistats2022_half(**kwargs)


def icml2022_full(**kwargs):
    """Single-column (full-width) figures for ICML 2022."""
    return _icml2022_and_aistats2022_full(**kwargs)


def aistats2022_half(**kwargs):
    """Double-column (half-width) figures for AISTATS 2022."""
    return _icml2022_and_aistats2022_half(**kwargs)


def aistats2022_full(**kwargs):
    """Single-column (full-width) figures for AISTATS 2022."""
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
        base_width_in=3.25,
        rel_width=1.0,
        height_to_width_ratio=height_to_width_ratio,
        nrows=nrows,
        ncols=ncols,
    )
    return _figsize_to_output_dict(
        figsize=figsize,
        constrained_layout=constrained_layout,
        tight_layout=tight_layout,
    )


def _icml2022_and_aistats2022_full(
    *,
    rel_width=1.0,
    nrows=1,
    ncols=2,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
):
    figsize = _from_base_in(
        base_width_in=6.75,
        rel_width=rel_width,
        height_to_width_ratio=height_to_width_ratio,
        nrows=nrows,
        ncols=ncols,
    )
    return _figsize_to_output_dict(
        figsize=figsize,
        constrained_layout=constrained_layout,
        tight_layout=tight_layout,
    )


def cvpr2022_half(
    *,
    nrows=1,
    ncols=1,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
):
    """Double-column (half-width) figures for CVPR 2022."""

    figsize = _from_base_pt(
        base_width_pt=237.13594,
        rel_width=1.0,
        height_to_width_ratio=height_to_width_ratio,
        nrows=nrows,
        ncols=ncols,
    )
    return _figsize_to_output_dict(
        figsize=figsize,
        constrained_layout=constrained_layout,
        tight_layout=tight_layout,
    )


def cvpr2022_full(
    *,
    rel_width=1.0,
    nrows=1,
    ncols=2,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
):
    """Single-column (full-width) figures for CVPR 2022."""

    figsize = _from_base_pt(
        base_width_pt=496.85625,
        rel_width=rel_width,
        height_to_width_ratio=height_to_width_ratio,
        nrows=nrows,
        ncols=ncols,
    )
    return _figsize_to_output_dict(
        figsize=figsize,
        constrained_layout=constrained_layout,
        tight_layout=tight_layout,
    )


# Single-column formats


def jmlr2001(
    *,
    rel_width=1.0,
    nrows=1,
    ncols=2,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
):
    """JMLR figure size.

    Source: https://www.jmlr.org/format/format.html

    The present format is for US letter format.
    """

    figsize = _from_base_in(
        base_width_in=6.0,
        rel_width=rel_width,
        height_to_width_ratio=height_to_width_ratio,
        nrows=nrows,
        ncols=ncols,
    )
    return _figsize_to_output_dict(
        figsize=figsize,
        constrained_layout=constrained_layout,
        tight_layout=tight_layout,
    )


def neurips2021(
    *,
    rel_width=1.0,
    nrows=1,
    ncols=2,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
):
    """Neurips 2021 figure size."""
    return _neurips_common(
        rel_width=rel_width,
        nrows=nrows,
        ncols=ncols,
        constrained_layout=constrained_layout,
        tight_layout=tight_layout,
        height_to_width_ratio=height_to_width_ratio,
    )


def neurips2022(
    *,
    rel_width=1.0,
    nrows=1,
    ncols=2,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
):
    """Neurips 2022 figure size."""
    return _neurips_common(
        rel_width=rel_width,
        nrows=nrows,
        ncols=ncols,
        constrained_layout=constrained_layout,
        tight_layout=tight_layout,
        height_to_width_ratio=height_to_width_ratio,
    )


def _neurips_common(
    *,
    rel_width=1.0,
    nrows=1,
    ncols=2,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
):
    """Neurips figure size defaults."""

    figsize = _from_base_in(
        base_width_in=5.5,
        rel_width=rel_width,
        height_to_width_ratio=height_to_width_ratio,
        nrows=nrows,
        ncols=ncols,
    )
    return _figsize_to_output_dict(
        figsize=figsize,
        constrained_layout=constrained_layout,
        tight_layout=tight_layout,
    )


def _from_base_pt(*, base_width_pt, **kwargs):
    base_width_in = base_width_pt / _POINTS_PER_INCH
    return _from_base_in(base_width_in=base_width_in, **kwargs)


def _from_base_in(*, base_width_in, rel_width, height_to_width_ratio, nrows, ncols):
    width_in = base_width_in * rel_width
    subplot_width_in = width_in / ncols
    subplot_height_in = height_to_width_ratio * subplot_width_in
    height_in = subplot_height_in * nrows
    return width_in, height_in


# Other formats


def beamer_169(
    *,
    rel_width=0.9,
    rel_height=0.6,
    constrained_layout=True,
    tight_layout=False,
):
    """Beamer figure size for `aspectratio=169`."""
    figsize = _from_base_pt(
        base_width_pt=398.3386,  # via '\showthe\textwidth' in latex
        rel_width=rel_width,
        height_to_width_ratio=(9 / 16) * (rel_height / rel_width),
        nrows=1,
        ncols=1,
    )

    return _figsize_to_output_dict(
        figsize=figsize,
        constrained_layout=constrained_layout,
        tight_layout=tight_layout,
    )


def _figsize_to_output_dict(*, figsize, constrained_layout, tight_layout):
    return {
        "figure.figsize": figsize,
        "figure.constrained_layout.use": constrained_layout,
        "figure.autolayout": tight_layout,
    }
