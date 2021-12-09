"""Marker styles."""

import itertools

import matplotlib.pyplot as plt
from matplotlib import cycler as mpl_cycler


def with_edge(*, edgecolor="black", edgewidth=0.5):
    return {
        "lines.markeredgecolor": edgecolor,
        "lines.markerfacecolor": "auto",
        "lines.markeredgewidth": edgewidth,
    }


def inverted(*, facecolor="white", edgewidth=0.75):
    return {
        "lines.markeredgecolor": "auto",
        "lines.markerfacecolor": facecolor,
        "lines.markeredgewidth": edgewidth,
    }


def cycler():
    cycle_current = plt.rcParams["axes.prop_cycle"]
    cycle_marker = mpl_cycler("marker", ["o", "^", "*", "P", "X", "d"])

    # We need to repeat the shortest of the cycles to match both lengts.
    # Otherwise cycle iterations are thrown away.
    if len(cycle_marker) <= len(cycle_current):
        num_fills = len(cycle_current) // len(cycle_marker) + 1
        cycle_marker_addon = (num_fills * cycle_marker)[: len(cycle_current)]
    else:
        num_fills = len(cycle_marker) // len(cycle_current) + 1
        cycle_marker_addon = (num_fills * cycle_current)[: len(cycle_marker)]
    return {"axes.prop_cycle": cycle_current + cycle_marker_addon}
