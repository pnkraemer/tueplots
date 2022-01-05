"""Tests for font settings."""

import matplotlib.pyplot as plt
import pytest

from tueplots import fonts

all_font_families = pytest.mark.parametrize("family", ["serif", "sans-serif"])


@all_font_families
def test_icml2022(family):
    font = fonts.icml2022(family=family)
    plt.rcParams.update(font)


@all_font_families
def test_icml2022_tex(family):
    font = fonts.icml2022_tex(family=family)
    plt.rcParams.update(font)


@all_font_families
def test_neurips2021(family):
    font = fonts.neurips2021(family=family)
    plt.rcParams.update(font)


@all_font_families
def test_jmlr2001_tex(family):
    font = fonts.jmlr2001_tex(family=family)
    plt.rcParams.update(font)
