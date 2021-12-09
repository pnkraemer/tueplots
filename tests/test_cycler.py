"""Tests for color cycles."""

import matplotlib.pyplot as plt

from tueplots import cycler
from tueplots.constants.color import palettes


def test_cycler():
    cy = cycler.cycler(color_palette=palettes.tue_primary)
    plt.rcParams.update(cy)
