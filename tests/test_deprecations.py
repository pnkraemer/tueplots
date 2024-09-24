"""Test that deprecations are announced appropriately."""

import pytest

from tueplots import fontsizes


def test_fontsize_beamer_function_renamed():
    with pytest.deprecated_call(match="renamed"):
        _ = fontsizes.beamer_moml()
