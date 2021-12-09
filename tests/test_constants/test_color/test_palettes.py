"""Tests for color palettes."""

import numpy as np
import pytest

from tueplots.constants.color import palettes

all_palettes = [
    palettes.tue_primary,
    palettes.tue_secondary,
    palettes.pn,
]


@pytest.mark.parametrize("palette", all_palettes)
def test_is_array(palette):
    assert isinstance(palette, tuple)
