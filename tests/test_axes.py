"""Tests for axes functionality."""

import matplotlib.pyplot as plt

from tueplots import axes


def test_lines():
    plt.rcParams.update(axes.lines(base_width=0.5, color="red", facecolor="none"))
