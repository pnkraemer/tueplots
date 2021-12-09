"""Test for context managers for plots."""

import matplotlib.pyplot as plt

from tueplots import bundles


def test_icml2022():
    with plt.rc_context(bundles.icml2022()):
        pass


def test_neurips2021():
    with plt.rc_context(bundles.neurips2021()):
        pass


def test_beamer_moml():
    with plt.rc_context(bundles.beamer_moml()):
        pass


def test_beamer_moml_dark_bg():
    with plt.rc_context(bundles.beamer_moml_dark_bg()):
        pass
