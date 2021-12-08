"""Tests for color constants."""

import numpy as np

from tueplots.color.constants import rgb


def test_tue_dark():
    assert isinstance(rgb.tue_dark, np.ndarray)


def test_tue_gray():
    assert isinstance(rgb.tue_gray, np.ndarray)


def test_tue_colors():
    colorlist = [
        rgb.tue_red,
        rgb.tue_dark,
        rgb.tue_gray,
        rgb.tue_gray,
        rgb.tue_gold,
        rgb.tue_lightgold,
        rgb.tue_secondary1,
        rgb.tue_secondary2,
        rgb.tue_secondary3,
        rgb.tue_secondary4,
        rgb.tue_secondary5,
        rgb.tue_secondary6,
        rgb.tue_secondary7,
        rgb.tue_secondary8,
        rgb.tue_secondary9,
        rgb.tue_secondary10,
        rgb.tue_secondary11,
        rgb.tue_secondary12,
    ]
    for c in colorlist:
        assert isinstance(c, np.ndarray)

    assert (rgb.tue_darkblue == rgb.tue_secondary1).all()
    assert (rgb.tue_blue == rgb.tue_secondary2).all()
    assert (rgb.tue_lightblue == rgb.tue_secondary3).all()
    assert (rgb.tue_lightgreen == rgb.tue_secondary4).all()
    assert (rgb.tue_green == rgb.tue_secondary5).all()
    assert (rgb.tue_darkgreen == rgb.tue_secondary6).all()
    assert (rgb.tue_ocre == rgb.tue_secondary7).all()
    assert (rgb.tue_violet == rgb.tue_secondary8).all()
    assert (rgb.tue_mauve == rgb.tue_secondary9).all()
    assert (rgb.tue_lightorange == rgb.tue_secondary10).all()
    assert (rgb.tue_orang == rgb.tue_secondary11).all()
    assert (rgb.tue_brown == rgb.tue_secondary12).all()
