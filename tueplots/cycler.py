"""Color cycler."""

from matplotlib import cycler as mpl_cycler


def cycler(*, color_palette):
    """Set a linestyle-cycler by promoting each cycler to the longest length."""
    color_cycler = mpl_cycler("color", color_palette)
    return {"axes.prop_cycle": color_cycler}
