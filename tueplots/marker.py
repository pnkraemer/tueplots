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
