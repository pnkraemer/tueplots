"""Tests for rc params."""

import matplotlib.pyplot as plt
import pytest_cases

CASE_MODULES = (
    ".test_rc_params_cases.case_fonts",
    ".test_rc_params_cases.case_axes",
    ".test_rc_params_cases.case_bundles",
    ".test_rc_params_cases.case_cycler",
    ".test_rc_params_cases.case_figsizes",
    ".test_rc_params_cases.case_fontsizes",
    ".test_rc_params_cases.case_markers",
)


@pytest_cases.parametrize_with_cases("config", cases=CASE_MODULES)
def test_update_rcParams(config):
    """Assert compatibility with matplotlib.pyplot.rcParams.update()."""
    plt.rcParams.update(config)


@pytest_cases.parametrize_with_cases("config", cases=CASE_MODULES)
def test_rc_context(config):
    """Assert compatibility with matplotlib.pyplot.rc_context()."""
    with plt.rc_context(config):
        pass
