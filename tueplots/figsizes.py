"""Figure size presets (:mod:`tueplots.figsizes`).

Provides standard figure dimensions for publications, ensuring
proper scaling in papers.

Examples
--------

.. plot::
    :include-source: True

    >>> import matplotlib.pyplot as plt
    >>> from tueplots import figsizes, fontsizes
    >>>
    >>> # Select a style bundle: fontsize + figsize
    >>> style = figsizes.aistats2025_half() | fontsizes.aistats2025()
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

# Some useful constants
_GOLDEN_RATIO = (5.0**0.5 - 1.0) / 2.0
"""Default height-to-width ratio for subplots."""

_POINTS_PER_INCH = 72.27
"""Translate pt to inches and back."""


_PAD_INCHES = 0.015
"""Default whitespace around figures when saving."""


# Double-column formats


def icml2022_half(**kwargs):
    """Double-column (half-width) figures for ICML 2022."""
    return _icml_and_aistats_common_half(**kwargs)


def icml2022_full(**kwargs):
    """Single-column (full-width) figures for ICML 2022."""
    return _icml_and_aistats_common_full(**kwargs)


def icml2024_half(**kwargs):
    """Double-column (half-width) figures for ICML 2024."""
    return _icml_and_aistats_common_half(**kwargs)


def icml2024_full(**kwargs):
    """Single-column (full-width) figures for ICML 2024."""
    return _icml_and_aistats_common_full(**kwargs)


def aistats2022_half(**kwargs):
    """Double-column (half-width) figures for AISTATS 2022."""
    return _icml_and_aistats_common_half(**kwargs)


def aistats2022_full(**kwargs):
    """Single-column (full-width) figures for AISTATS 2022."""
    return _icml_and_aistats_common_full(**kwargs)


def aistats2023_half(**kwargs):
    """Double-column (half-width) figures for AISTATS 2023."""
    return _icml_and_aistats_common_half(**kwargs)


def aistats2023_full(**kwargs):
    """Single-column (full-width) figures for AISTATS 2023."""
    return _icml_and_aistats_common_full(**kwargs)


def aistats2025_half(**kwargs):
    """Double-column (half-width) figures for AISTATS 2025."""
    return _icml_and_aistats_common_half(**kwargs)


def aistats2025_full(**kwargs):
    """Single-column (full-width) figures for AISTATS 2025."""
    return _icml_and_aistats_common_full(**kwargs)


def _icml_and_aistats_common_half(
    *,
    nrows=1,
    ncols=1,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
    pad_inches=_PAD_INCHES,
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
        pad_inches=pad_inches,
    )


def _icml_and_aistats_common_full(
    *,
    rel_width=1.0,
    nrows=1,
    ncols=2,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
    pad_inches=_PAD_INCHES,
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
        pad_inches=pad_inches,
    )


def aaai2024_half(
    *,
    nrows=1,
    ncols=1,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
    pad_inches=_PAD_INCHES,
    rel_width=1.0,
):
    """Double-column (half-width) figures for AAAI 2024."""

    figsize = _from_base_in(
        base_width_in=3.3,
        rel_width=rel_width,
        height_to_width_ratio=height_to_width_ratio,
        nrows=nrows,
        ncols=ncols,
    )
    return _figsize_to_output_dict(
        figsize=figsize,
        constrained_layout=constrained_layout,
        tight_layout=tight_layout,
        pad_inches=pad_inches,
    )


def aaai2024_full(
    *,
    nrows=1,
    ncols=1,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
    pad_inches=_PAD_INCHES,
    rel_width=1.0,
):
    """Double-column (full-width) figures for AAAI 2024."""

    figsize = _from_base_in(
        base_width_in=6.975,
        rel_width=rel_width,
        height_to_width_ratio=height_to_width_ratio,
        nrows=nrows,
        ncols=ncols,
    )
    return _figsize_to_output_dict(
        figsize=figsize,
        constrained_layout=constrained_layout,
        tight_layout=tight_layout,
        pad_inches=pad_inches,
    )


def uai2023_half(
    *,
    nrows=1,
    ncols=1,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
    pad_inches=_PAD_INCHES,
):
    """Double-column (half-width) figures for UAI 2023."""

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
        pad_inches=pad_inches,
    )


def uai2023_full(
    *,
    nrows=1,
    ncols=1,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
    pad_inches=_PAD_INCHES,
):
    """Double-column (full-width) figures for UAI 2023."""

    figsize = _from_base_in(
        base_width_in=6.75,
        rel_width=1.0,
        height_to_width_ratio=height_to_width_ratio,
        nrows=nrows,
        ncols=ncols,
    )
    return _figsize_to_output_dict(
        figsize=figsize,
        constrained_layout=constrained_layout,
        tight_layout=tight_layout,
        pad_inches=pad_inches,
    )


def cvpr2022_half(
    *,
    nrows=1,
    ncols=1,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
    pad_inches=_PAD_INCHES,
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
        pad_inches=pad_inches,
    )


def cvpr2022_full(
    *,
    rel_width=1.0,
    nrows=1,
    ncols=2,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
    pad_inches=_PAD_INCHES,
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
        pad_inches=pad_inches,
    )


def cvpr2024_half(
    *,
    nrows=1,
    ncols=1,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
    pad_inches=_PAD_INCHES,
):
    """Double-column (half-width) figures for CVPR 2024."""

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
        pad_inches=pad_inches,
    )


def cvpr2024_full(
    *,
    rel_width=1.0,
    nrows=1,
    ncols=2,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
    pad_inches=_PAD_INCHES,
):
    """Single-column (full-width) figures for CVPR 2024."""

    figsize = _from_base_in(
        base_width_in=6.875,
        rel_width=rel_width,
        height_to_width_ratio=height_to_width_ratio,
        nrows=nrows,
        ncols=ncols,
    )
    return _figsize_to_output_dict(
        figsize=figsize,
        constrained_layout=constrained_layout,
        tight_layout=tight_layout,
        pad_inches=pad_inches,
    )


def probnum2025_half(
    *,
    nrows=1,
    ncols=1,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
    pad_inches=_PAD_INCHES,
):
    """Single-column (half-width) figures for ProbNum 2025."""
    figsize = _from_base_pt(
        base_width_pt=240,
        rel_width=1.0,
        height_to_width_ratio=height_to_width_ratio,
        nrows=nrows,
        ncols=ncols,
    )
    return _figsize_to_output_dict(
        figsize=figsize,
        constrained_layout=constrained_layout,
        tight_layout=tight_layout,
        pad_inches=pad_inches,
    )


def probnum2025_full(
    *,
    rel_width=1.0,
    nrows=1,
    ncols=2,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
    pad_inches=_PAD_INCHES,
):
    """Full-page (full-width) figures for ProbNum 2025."""
    figsize = _from_base_pt(
        base_width_pt=500,
        rel_width=rel_width,
        height_to_width_ratio=height_to_width_ratio,
        nrows=nrows,
        ncols=ncols,
    )
    return _figsize_to_output_dict(
        figsize=figsize,
        constrained_layout=constrained_layout,
        tight_layout=tight_layout,
        pad_inches=pad_inches,
    )


# Single-column formats


def eccv2024(
    *,
    rel_width=1.0,
    nrows=1,
    ncols=2,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
    pad_inches=_PAD_INCHES,
):
    """ECCV figure size.

    Source: https://eccv2024.ecva.net/Conferences/2024/SubmissionPolicies
    """

    figsize = _from_base_in(
        base_width_in=4.8,  # corresponds to 122mm in ECCV template
        rel_width=rel_width,
        height_to_width_ratio=height_to_width_ratio,
        nrows=nrows,
        ncols=ncols,
    )
    return _figsize_to_output_dict(
        figsize=figsize,
        constrained_layout=constrained_layout,
        tight_layout=tight_layout,
        pad_inches=pad_inches,
    )


def jmlr2001(
    *,
    rel_width=1.0,
    nrows=1,
    ncols=2,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
    pad_inches=_PAD_INCHES,
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
        pad_inches=pad_inches,
    )


def tmlr2023(
    *,
    rel_width=1.0,
    nrows=1,
    ncols=2,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
    pad_inches=_PAD_INCHES,
):
    """TMLR figure size.

    Source: https://www.jmlr.org/tmlr/author-guide.html"""

    figsize = _from_base_in(
        base_width_in=6.5,
        rel_width=rel_width,
        height_to_width_ratio=height_to_width_ratio,
        nrows=nrows,
        ncols=ncols,
    )
    return _figsize_to_output_dict(
        figsize=figsize,
        constrained_layout=constrained_layout,
        tight_layout=tight_layout,
        pad_inches=pad_inches,
    )


def neurips2021(
    *,
    rel_width=1.0,
    nrows=1,
    ncols=2,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
    pad_inches=_PAD_INCHES,
):
    """Neurips 2021 figure size."""
    return _neurips_and_iclr_common(
        rel_width=rel_width,
        nrows=nrows,
        ncols=ncols,
        constrained_layout=constrained_layout,
        tight_layout=tight_layout,
        height_to_width_ratio=height_to_width_ratio,
        pad_inches=pad_inches,
    )


def neurips2022(
    *,
    rel_width=1.0,
    nrows=1,
    ncols=2,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
    pad_inches=_PAD_INCHES,
):
    """Neurips 2022 figure size."""
    return _neurips_and_iclr_common(
        rel_width=rel_width,
        nrows=nrows,
        ncols=ncols,
        constrained_layout=constrained_layout,
        tight_layout=tight_layout,
        height_to_width_ratio=height_to_width_ratio,
        pad_inches=pad_inches,
    )


def neurips2023(
    *,
    rel_width=1.0,
    nrows=1,
    ncols=2,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
    pad_inches=_PAD_INCHES,
):
    """Neurips 2023 figure size."""
    return _neurips_and_iclr_common(
        rel_width=rel_width,
        nrows=nrows,
        ncols=ncols,
        constrained_layout=constrained_layout,
        tight_layout=tight_layout,
        height_to_width_ratio=height_to_width_ratio,
        pad_inches=pad_inches,
    )


def neurips2024(
    *,
    rel_width=1.0,
    nrows=1,
    ncols=2,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
    pad_inches=_PAD_INCHES,
):
    """Neurips 2024 figure size.

    Source: https://nips.cc/Conferences/2024/CallForPapers
    """
    return _neurips_and_iclr_common(
        rel_width=rel_width,
        nrows=nrows,
        ncols=ncols,
        constrained_layout=constrained_layout,
        tight_layout=tight_layout,
        height_to_width_ratio=height_to_width_ratio,
        pad_inches=pad_inches,
    )


def iclr2023(
    *,
    rel_width=1.0,
    nrows=1,
    ncols=2,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
    pad_inches=_PAD_INCHES,
):
    """ICLR 2023 figure size."""
    return _neurips_and_iclr_common(
        rel_width=rel_width,
        nrows=nrows,
        ncols=ncols,
        constrained_layout=constrained_layout,
        tight_layout=tight_layout,
        height_to_width_ratio=height_to_width_ratio,
        pad_inches=pad_inches,
    )


def iclr2024(
    *,
    rel_width=1.0,
    nrows=1,
    ncols=2,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
    pad_inches=_PAD_INCHES,
):
    """ICLR 2024 figure size."""
    return _neurips_and_iclr_common(
        rel_width=rel_width,
        nrows=nrows,
        ncols=ncols,
        constrained_layout=constrained_layout,
        tight_layout=tight_layout,
        height_to_width_ratio=height_to_width_ratio,
        pad_inches=pad_inches,
    )


def _neurips_and_iclr_common(
    *,
    rel_width=1.0,
    nrows=1,
    ncols=2,
    constrained_layout=True,
    tight_layout=False,
    height_to_width_ratio=_GOLDEN_RATIO,
    pad_inches=_PAD_INCHES,
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
        pad_inches=pad_inches,
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
    pad_inches=_PAD_INCHES,
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
        pad_inches=pad_inches,
    )


def _figsize_to_output_dict(
    *,
    figsize,
    constrained_layout,
    tight_layout,
    pad_inches,
):
    return {
        "figure.figsize": figsize,
        "figure.constrained_layout.use": constrained_layout,
        "figure.autolayout": tight_layout,
        "savefig.pad_inches": pad_inches,
    }
