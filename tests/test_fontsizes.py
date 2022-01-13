"""Tests for font sizes."""

import pytest

from tueplots import fontsizes


def test_icml2022():
    sizes = fontsizes.icml2022()
    assert isinstance(sizes, dict)


def test_neurips2021():
    sizes = fontsizes.icml2022()
    assert isinstance(sizes, dict)
