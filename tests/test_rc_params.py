"""Tests for rc params."""

import matplotlib.pyplot as plt
import pytest_cases

CASE_MODULES = (
    ".rc_params_cases.fonts",
    ".rc_params_cases.axes",
    ".rc_params_cases.bundles",
    ".rc_params_cases.cycler",
)


@pytest_cases.parametrize_with_cases("config", cases=CASE_MODULES)
def test_update_rcParams(config):
    """Assert compatibiity with matplotlib.pyplot.rcParams.update()."""
    plt.rcParams.update(config)


@pytest_cases.parametrize_with_cases("config", cases=CASE_MODULES)
def test_rc_context(config):
    """Assert compatibiity with matplotlib.pyplot.rc_context()."""
    with plt.rc_context(config):
        pass
