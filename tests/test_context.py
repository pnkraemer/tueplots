"""Test for context managers for plots."""

import matplotlib.pyplot as plt

from tueplots import context


def test_icml2022():
    with context.icml2022():
        pass


def test_neurips2021():
    with context.neurips2021():
        pass


def test_beamer_moml():
    with context.beamer_moml():
        pass


def test_beamer_moml_dark_bg():
    with context.beamer_moml_dark_bg():
        pass
