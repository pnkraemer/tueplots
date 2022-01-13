"""Tests for rc params."""

import matplotlib.pyplot as plt
import pytest_cases


@pytest_cases.parametrize_with_cases("config", cases=".rc_params_cases.fonts")
def test_update_rcParams(config):
    plt.rcParams.update(config)


@pytest_cases.parametrize_with_cases("config", cases=".rc_params_cases.fonts")
def test_rc_context(config):
    with plt.rc_context(config):
        pass
