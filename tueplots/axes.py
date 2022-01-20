"""Axes behaviour."""


def lines(
    *,
    base_width=0.5,
    line_base_ratio=2.0,
    tick_major_base_ratio=1.0,
    tick_minor_base_ratio=0.5,
    tick_size_width_ratio=3.0,
    tick_major_size_min=3.0,
    tick_minor_size_min=2.0,
    axisbelow=True,
):
    """Adjust linewidth(s) according to a base width."""

    tick_major_width = tick_major_base_ratio * base_width
    tick_minor_width = tick_minor_base_ratio * base_width
    tick_major_size = max(tick_major_size_min, tick_size_width_ratio * tick_major_width)
    tick_minor_size = max(tick_minor_size_min, tick_size_width_ratio * tick_minor_width)
    return {
        # Set the line-widths appropriately (including the grid)
        "axes.linewidth": base_width,
        "lines.linewidth": line_base_ratio * base_width,
        "xtick.major.width": tick_major_width,
        "ytick.major.width": tick_major_width,
        "xtick.minor.width": tick_minor_width,
        "ytick.minor.width": tick_minor_width,
        "xtick.major.size": tick_major_size,
        "ytick.major.size": tick_major_size,
        "xtick.minor.size": tick_minor_size,
        "ytick.minor.size": tick_minor_size,
        "grid.linewidth": base_width,
        # Legend frame linewidth
        "patch.linewidth": base_width,
        "legend.edgecolor": "inherit",  # inherit color from axes. passing 'color' leads to awkward future warnings.
        # Control the zorder of the ticks and gridlines
        # This is somewhat out of place in this function, but creating a new function
        # seems a bit unnecessary here... suggestions welcome!
        "axes.axisbelow": axisbelow,
    }


def grid(*, grid_alpha=0.2, grid_linestyle="solid"):
    """Adjust the grid-style."""
    return {
        # Update the linestyle of the grid
        # (it shares a color with the frame, and needs to be distinguishable)
        "grid.linestyle": grid_linestyle,
        "grid.alpha": grid_alpha,
    }


def legend(*, shadow=False, frameon=True, fancybox=False):
    """Adjust the legend-style."""

    return {
        "legend.shadow": shadow,
        "legend.frameon": frameon,
        "legend.fancybox": fancybox,
    }


def color(*, base="black", face="none"):
    """Adjust the axes' color."""

    return {
        "text.color": base,
        "axes.edgecolor": base,
        "axes.labelcolor": base,
        "xtick.color": base,
        "ytick.color": base,
        "grid.color": base,
        "axes.facecolor": face,
    }


def spines(*, left=True, right=True, top=True, bottom=True):
    """Adjust the visibility of the axes' spines."""
    return {
        "axes.spines.left": left,
        "axes.spines.right": right,
        "axes.spines.top": top,
        "axes.spines.bottom": bottom,
    }


def tick_direction(*, x="inout", y="inout"):
    """Adjust the tick direction."""
    return {
        "xtick.direction": x,
        "ytick.direction": y,
    }
