"""Tests for color cycles."""

from tueplots.color import cycler
import matplotlib.pyplot as plt


def test_bright():
    cy = cycler.bright()
    plt.rcParams.update(cy)


def test_high_contrast():
    cy = cycler.high_contrast()
    plt.rcParams.update(cy)

def test_probnum():
    cy = cycler.probnum()
    plt.rcParams.update(cy)

def test_muted():
    cy = cycler.muted()
    plt.rcParams.update(cy)
