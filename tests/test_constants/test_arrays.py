"""Array-type tests."""

import numpy as np
import pytest_cases

CASE_MODULES = (
    ".test_arrays_cases.case_markers",
    ".test_arrays_cases.color_cases.case_palettes",
    ".test_arrays_cases.color_cases.case_rgb",
)


@pytest_cases.parametrize_with_cases("arr", cases=CASE_MODULES)
def test_is_array(arr):
    """Assert compatibiity with matplotlib.pyplot.rcParams.update()."""
    assert isinstance(arr, np.ndarray)
