"""Tests for axes functionality."""

import matplotlib.pyplot as plt

from tueplots import axes


def test_lines():
    config = axes.lines(color="red", xtick_direction="inout", line_base_ratio=2.0)
    plt.rcParams.update(config)


def test_face():
    plt.rcParams.update(axes.face(color="red"))


def test_legend():
    plt.rcParams.update(axes.legend(shadow=False, frameon=True, fancybox=False))
