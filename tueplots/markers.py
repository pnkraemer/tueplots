"""Marker styles."""

from matplotlib import cycler as mpl_cycler
import matplotlib.pyplot as plt
import itertools

def dark_edge(*, edgecolor="black", edgewidth=0.5):
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

    num_fills = len(cycle_current) // len(cycle_marker) + 1
    cycle_marker_addon = (num_fills * cycle_marker)[:len(cycle_current)]

    return {"axes.prop_cycle": cycle_current + cycle_marker_addon}
