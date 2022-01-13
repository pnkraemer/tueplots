"""Tests for font settings."""

import matplotlib.pyplot as plt
import pytest_cases

from tueplots import fonts


def case_icml2022_default_arguments():
    return fonts.icml2022()


def case_icml2022_all_arguments_set():
    return fonts.icml2022(family="serif")


def case_icml2022_tex_default_arguments():
    return fonts.icml2022_tex()


def case_icml2022_tex_all_arguments_set():
    return fonts.icml2022_tex(family="serif")


def case_neurips2021_default_arguments():
    return fonts.neurips2021()


def case_neurips2021_all_arguments_set():
    return fonts.neurips2021(family="serif")


def case_neurips2021_tex_default_arguments():
    return fonts.neurips2021_tex()


def case_neurips2021_tex_all_arguments_set():
    return fonts.neurips2021_tex(family="serif")


def case_jmlr2001_tex_default_arguments():
    return fonts.jmlr2001_tex()


def case_jmlr2001_tex_all_arguments_set():
    return fonts.jmlr2001_tex(family="serif")


@pytest_cases.parametrize_with_cases("font_config", cases=".")
def test_update_rcParams(font_config):
    plt.rcParams.update(font_config)
