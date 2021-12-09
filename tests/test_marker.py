"""Tests for marker styles."""

import matplotlib.pyplot as plt

from tueplots import marker


def test_with_edge():
    plt.rcParams.update(marker.with_edge())


def test_inverted():
    plt.rcParams.update(marker.inverted())
