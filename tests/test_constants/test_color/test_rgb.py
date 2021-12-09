"""Tests for color constants."""

import numpy as np
import pytest

from tueplots.constants.color import rgb

all_colors = [
    # Tuebingen primary colors
    rgb.tue_red,
    rgb.tue_dark,
    rgb.tue_gray,
    rgb.tue_gray,
    rgb.tue_gold,
    rgb.tue_lightgold,
    # Tuebingen secondary colors
    rgb.tue_darkblue,
    rgb.tue_blue,
    rgb.tue_lightblue,
    rgb.tue_lightgreen,
    rgb.tue_green,
    rgb.tue_darkgreen,
    rgb.tue_ocre,
    rgb.tue_violet,
    rgb.tue_mauve,
    rgb.tue_lightorange,
    rgb.tue_orange,
    rgb.tue_brown,
    # ProbNum colors
    rgb.pn_green,
    rgb.pn_blue,
    rgb.pn_orange,
    rgb.pn_gray,
    rgb.pn_red,
]


@pytest.mark.parametrize("color", all_colors)
def test_is_array(color):
    assert isinstance(color, np.ndarray)
