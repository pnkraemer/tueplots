"""Tests for marker styles."""

import matplotlib.pyplot as plt

from tueplots import markers


def test_with_edge():
    plt.rcParams.update(markers.with_edge())


def test_inverted():
    plt.rcParams.update(markers.inverted())
