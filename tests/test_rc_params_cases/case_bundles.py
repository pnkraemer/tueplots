"""Test cases for bundles."""

import pytest_cases

from tueplots import bundles


@pytest_cases.parametrize(column=["full", "half"])
@pytest_cases.parametrize(usetex=[True, False])
def case_bundles_cvpr2024(column, usetex):
    return bundles.cvpr2024(
        nrows=2, ncols=2, family="serif", column=column, usetex=usetex
    )


@pytest_cases.parametrize(column=["full", "half"])
@pytest_cases.parametrize(usetex=[True, False])
def case_bundles_icml2022(column, usetex):
    return bundles.icml2022(
        nrows=2, ncols=2, family="serif", column=column, usetex=usetex
    )


@pytest_cases.parametrize(column=["full", "half"])
def case_bundles_aistats2022(column):
    return bundles.aistats2022(column=column, nrows=2, ncols=2, family="serif")


@pytest_cases.parametrize(column=["full", "half"])
def case_bundles_aistats2023(column):
    return bundles.aistats2023(column=column, nrows=2, ncols=2, family="serif")


@pytest_cases.parametrize(usetex=[True, False])
def case_bundles_neurips2021(usetex):
    return bundles.neurips2021(usetex=usetex, nrows=2, ncols=2, family="serif")


@pytest_cases.parametrize(usetex=[True, False])
def case_bundles_neurips2022(usetex):
    return bundles.neurips2022(usetex=usetex, nrows=2, ncols=2, family="serif")


@pytest_cases.parametrize(usetex=[True, False])
def case_bundles_neurips2023(usetex):
    return bundles.neurips2023(usetex=usetex, nrows=2, ncols=2, family="serif")


@pytest_cases.parametrize(usetex=[True, False])
def case_bundles_iclr2023(usetex):
    return bundles.iclr2023(usetex=usetex, nrows=2, ncols=2, family="serif")


@pytest_cases.parametrize(usetex=[True, False])
def case_bundles_iclr2024(usetex):
    return bundles.iclr2024(usetex=usetex, nrows=2, ncols=2, family="serif")


@pytest_cases.parametrize(column=["full", "half"])
def case_bundles_aaai2024(column):
    return bundles.aaai2024(column=column, nrows=2, ncols=2, family="serif")


@pytest_cases.parametrize(column=["full", "half"])
def case_bundles_uai2023(column):
    return bundles.uai2023(column=column, nrows=2, ncols=2, family="serif")


def case_bundles_jmlr2001():
    return bundles.jmlr2001(nrows=2, ncols=2, family="serif")


def case_bundles_tmlr2023():
    return bundles.tmlr2023(nrows=2, ncols=2, family="serif")


def case_bundles_beamer_moml():
    return bundles.beamer_moml(rel_width=0.9, rel_height=0.9)


def case_bundles_beamer_moml_dark_bg():
    return bundles.beamer_moml(rel_width=0.9, rel_height=0.9)
