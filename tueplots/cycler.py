"""Color cycler."""

from matplotlib import cycler as mpl_cycler


def cycler(**kwargs):
    """Wrap a matplotlib.cycler object into a parameter-dictionary compatible with plt.rcParams.

    Please refer to
        https://matplotlib.org/cycler/
    and
        https://matplotlib.org/stable/tutorials/intermediate/color_cycle.html
    for information about how to use cyclers.
    """
    return {"axes.prop_cycle": mpl_cycler(**kwargs)}
