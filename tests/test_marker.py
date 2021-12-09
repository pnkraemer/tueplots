"""Tests for marker styles."""

from tueplots import markers
import matplotlib.pyplot as plt

def test_dark_edge():
    plt.rcParams.update(markers.dark_edge())

def test_inverted():
    plt.rcParams.update(markers.inverted())

def test_cycler():
    plt.rcParams.update(markers.cycler())
