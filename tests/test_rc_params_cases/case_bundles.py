"""Test cases for bundles."""

from tueplots import bundles


def case_bundles_icml2022_default():
    return bundles.icml2022()


def case_bundles_icml2022_custom():
    return bundles.icml2022(nrows=2, ncols=2, family="serif", column="full")


def case_bundles_icml2022_tex_default():
    return bundles.icml2022_tex()


def case_bundles_icml2022_tex_custom():
    return bundles.icml2022_tex(nrows=2, ncols=2, family="serif", column="full")


def case_bundles_jmlr2001_tex_default():
    return bundles.jmlr2001_tex()


def case_bundles_jmlr2001_tex_custom():
    return bundles.jmlr2001_tex(nrows=2, ncols=2, family="serif")


def case_bundles_neurips2021_default():
    return bundles.neurips2021()


def case_bundles_neurips2021_custom():
    return bundles.neurips2021(nrows=2, ncols=2, family="serif")


def case_bundles_neurips2021_tex_default():
    return bundles.neurips2021_tex()


def case_bundles_neurips2021_tex_custom():
    return bundles.neurips2021_tex(nrows=2, ncols=2, family="serif")


def case_bundles_beamer_moml_default():
    return bundles.beamer_moml()


def case_bundles_beamer_moml_tex_custom():
    return bundles.beamer_moml(rel_width=0.9, rel_height=0.9)


def case_bundles_beamer_moml_dark_bg_default():
    return bundles.beamer_moml()


def case_bundles_beamer_moml_dark_bg_tex_custom():
    return bundles.beamer_moml(rel_width=0.9, rel_height=0.9)
