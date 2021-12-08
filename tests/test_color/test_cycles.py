"""Tests for color cycles."""

from tueplots.color import cycler
import matplotlib.pyplot as plt

def test_bright():
    cy = cycler.bright()
    plt.rcParams.update(cy)

