"""Test cases for bundles."""

from tueplots import bundles


def case_bundles_icml2022():
    return bundles.icml2022(nrows=2, ncols=2, family="serif", column="full")


def case_bundles_icml2022_tex():
    return bundles.icml2022_tex(nrows=2, ncols=2, family="serif", column="full")


def case_bundles_jmlr2001_tex():
    return bundles.jmlr2001_tex(nrows=2, ncols=2, family="serif")


def case_bundles_aistats2022_tex():
    return bundles.aistats2022_tex(column="full", nrows=2, ncols=2, family="serif")


def case_bundles_neurips2021():
    return bundles.neurips2021(nrows=2, ncols=2, family="serif")


def case_bundles_neurips2021_tex():
    return bundles.neurips2021_tex(nrows=2, ncols=2, family="serif")


def case_bundles_beamer_moml_tex():
    return bundles.beamer_moml(rel_width=0.9, rel_height=0.9)


def case_bundles_beamer_moml_dark_bg_tex():
    return bundles.beamer_moml(rel_width=0.9, rel_height=0.9)
