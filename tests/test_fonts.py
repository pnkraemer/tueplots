"""Tests for font settings."""

import matplotlib.pyplot as plt
import pytest

from tueplots import fonts


@pytest.mark.parametrize("family", ["serif", "sans-serif"])
def test_icml(family):
    font = fonts.icml(family=family)
    plt.rcParams.update(font)


@pytest.mark.parametrize("family", ["serif", "sans-serif"])
def test_neurips(family):
    font = fonts.neurips(family=family)
    plt.rcParams.update(font)
