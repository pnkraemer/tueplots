"""Tests for font settings."""

import matplotlib.pyplot as plt

from tueplots import fonts


def test_icml():
    font = fonts.icml()
    plt.rcParams.update(font)


def test_neurips():
    font = fonts.neurips()
    plt.rcParams.update(font)
