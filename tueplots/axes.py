"""Axes behaviour."""


def lines(
    *,
    base_width=0.5,
    color="black",
    line_base_ratio=1.5,
    grid_alpha=0.25,
    grid_linestyle="solid",
    axisbelow=True,
):
    return {
        # Set the line-widths appropriately (including the grid)
        "axes.linewidth": base_width,
        "lines.linewidth": line_base_ratio * base_width,
        "xtick.major.width": base_width,
        "ytick.major.width": base_width,
        "xtick.minor.width": 0.5 * base_width,
        "ytick.minor.width": 0.5 * base_width,
        "xtick.major.size": 1.5 + 3 * base_width,
        "ytick.major.size": 1.5 + 3 * base_width,
        "xtick.minor.size": 1.0 + 3 * 0.5 * base_width,
        "ytick.minor.size": 1.0 + 3 * 0.5 * base_width,
        "grid.linewidth": base_width,
        # Legend frame linewidth
        "patch.linewidth": base_width,
        # Change the text color
        "text.color": color,
        "axes.edgecolor": color,
        "axes.labelcolor": color,
        "xtick.color": color,
        "ytick.color": color,
        "grid.color": color,
        "legend.edgecolor": "inherit",  # inherit color from axes. passing 'color' leads to awkward future warnings.
        # Update the linestyle of the grid
        # (it shares a color with the frame, and needs to be distinguishable)
        "grid.linestyle": grid_linestyle,
        "grid.alpha": grid_alpha,
        # Control the zorder of the ticks and gridlines
        "axes.axisbelow": axisbelow,
    }


def legend(*, shadow=False, frameon=True, fancybox=False):
    return {
        "legend.shadow": shadow,
        "legend.frameon": frameon,
        "legend.fancybox": fancybox,
    }


def face(*, color="none"):
    return {"axes.facecolor": color}


def spines(*, left=True, right=True, top=True, bottom=True):
    return {
        "axes.spines.left": left,
        "axes.spines.right": right,
        "axes.spines.top": top,
        "axes.spines.bottom": bottom,
    }


def tick_direction(*, x="inout", y="inout"):
    return {
        "xtick.direction": x,
        "ytick.direction": y,
    }
