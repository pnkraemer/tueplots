"""Tests for font settings."""

import matplotlib.pyplot as plt
import pytest

from tueplots import fonts


@pytest.mark.parametrize("family", ["serif", "sans-serif"])
def test_icml2022(family):
    font = fonts.icml2022(family=family)
    plt.rcParams.update(font)


@pytest.mark.parametrize("family", ["serif", "sans-serif"])
def test_neurips2021(family):
    font = fonts.neurips2021(family=family)
    plt.rcParams.update(font)
