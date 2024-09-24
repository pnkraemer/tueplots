"""Test that the functions in tueplots.bundles raise good errors when misused."""

import pytest
import pytest_cases

from tueplots import bundles


def case_multicol_bundle_aistats2023():
    return bundles.aistats2023


def case_multicol_bundle_aistats2025():
    return bundles.aistats2025


@pytest_cases.parametrize_with_cases("multicol_bundle", cases=".")
def test_column_neither_half_nor_full_raises_value_error(multicol_bundle):
    # Sanity checks
    _ = multicol_bundle(column="half")
    _ = multicol_bundle(column="full")

    with pytest.raises(ValueError, match="expected"):
        _ = multicol_bundle(column="anything-but-half")
