"""Test that the functions in tueplots.bundles raise good errors when misused."""

import pytest
import pytest_cases

from tueplots import bundles


@pytest_cases.case(tags=["multicol", "tex_or_not"])
def case_bundle_cvpr2024():
    return bundles.cvpr2024


@pytest_cases.case(tags=["multicol", "tex_or_not"])
def case_bundle_icml2022():
    return bundles.icml2022


@pytest_cases.case(tags=["multicol", "tex_or_not"])
def case_bundle_icml2024():
    return bundles.icml2024


@pytest_cases.case(tags=["multicol"])
def case_bundle_aistats2022():
    return bundles.aistats2022


@pytest_cases.case(tags=["multicol"])
def case_bundle_aistats2023():
    return bundles.aistats2023


@pytest_cases.case(tags=["multicol"])
def case_bundle_aistats2025():
    return bundles.aistats2025


@pytest_cases.case(tags=["multicol"])
def case_bundle_aaai2024():
    return bundles.aaai2024


@pytest_cases.case(tags=["multicol"])
def case_bundle_uai2024():
    return bundles.uai2023


@pytest_cases.case(tags=["tex_or_not"])
def case_bundle_neurips2021():
    return bundles.neurips2021


@pytest_cases.case(tags=["tex_or_not"])
def case_bundle_neurips2022():
    return bundles.neurips2022


@pytest_cases.case(tags=["tex_or_not"])
def case_bundle_neurips2023():
    return bundles.neurips2023


@pytest_cases.case(tags=["tex_or_not"])
def case_bundle_neurips2024():
    return bundles.neurips2024


@pytest_cases.case(tags=["tex_or_not"])
def case_bundle_iclr2023():
    return bundles.iclr2023


@pytest_cases.case(tags=["tex_or_not"])
def case_bundle_iclr2024():
    return bundles.iclr2024


@pytest_cases.parametrize_with_cases("bundle_fun", cases=".", has_tag=["multicol"])
def test_column_neither_half_nor_full_raises_value_error(bundle_fun):
    # Sanity checks
    _ = bundle_fun(column="half")
    _ = bundle_fun(column="full")

    with pytest.raises(ValueError, match="expected"):
        _ = bundle_fun(column="anything-but-half")


@pytest_cases.parametrize_with_cases("bundle_fun", cases=".", has_tag=["tex_or_not"])
def test_usetex_must_be_bool_otherwise_type_error(bundle_fun):
    # Sanity checks
    _ = bundle_fun(usetex=True)
    _ = bundle_fun(usetex=False)

    with pytest.raises(ValueError, match="expected"):
        _ = bundle_fun(usetex=2)
