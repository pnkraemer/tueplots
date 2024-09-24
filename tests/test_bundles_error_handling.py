"""Test that the functions in tueplots.bundles raise good errors when misused."""

import pytest
import pytest_cases

from tueplots import bundles


def case_multicol_bundle_cvpr2024():
    return bundles.cvpr2024


def case_multicol_bundle_icml2022():
    return bundles.icml2022


def case_multicol_bundle_icml2024():
    return bundles.icml2024


def case_multicol_bundle_aistats2022():
    return bundles.aistats2022


def case_multicol_bundle_aistats2023():
    return bundles.aistats2023


def case_multicol_bundle_aistats2025():
    return bundles.aistats2025


def case_multicol_bundle_aaai2024():
    return bundles.aaai2024


def case_multicol_bundle_uai2024():
    return bundles.uai2023


@pytest_cases.parametrize_with_cases("multicol_bundle", cases=".")
def test_column_neither_half_nor_full_raises_value_error(multicol_bundle):
    # Sanity checks
    _ = multicol_bundle(column="half")
    _ = multicol_bundle(column="full")

    with pytest.raises(ValueError, match="expected"):
        _ = multicol_bundle(column="anything-but-half")
