"""Tests for color constants."""

import numpy as np

from tueplots.color.constants import rgb


def test_tue_dark():
    assert isinstance(rgb.tue_dark, np.ndarray)


def test_tue_gray():
    assert isinstance(rgb.tue_gray, np.ndarray)
