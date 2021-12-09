"""Tests for color cycles."""

import matplotlib.pyplot as plt

from tueplots import cycler
from tueplots.constants import markers
from tueplots.constants.color import palettes


def test_cycler():
    cy = cycler.cycler(color=palettes.tue_primary[:3], marker=markers.triangles[:3])
    plt.rcParams.update(cy)
