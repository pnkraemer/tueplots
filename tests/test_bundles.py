"""Test for context managers for plots."""

import matplotlib.pyplot as plt

from tueplots import bundles


def test_icml2022():
    with plt.rc_context(bundles.icml2022(family="sans-serif", column="half")):
        pass


def test_icml2022_tex():
    with plt.rc_context(bundles.icml2022_tex()):
        pass


def test_jmlr2001_tex():
    with plt.rc_context(bundles.jmlr2001_tex()):
        pass


def test_neurips2021():
    with plt.rc_context(bundles.neurips2021(nrows=2)):
        pass


def test_neurips2021_tex():
    with plt.rc_context(bundles.neurips2021_tex()):
        pass


def test_beamer_moml():
    with plt.rc_context(bundles.beamer_moml()):
        pass


def test_beamer_moml_dark_bg():
    with plt.rc_context(bundles.beamer_moml_dark_bg()):
        pass
