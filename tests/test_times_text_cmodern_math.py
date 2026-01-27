"""Tests for the _times_text_cmodern_math() function behavior.

Non-TeX font functions should use Times text with Computer Modern math,
mirroring the TeX behavior of usepackage{times} and usepackage{ptm}.
"""

import pytest

from tueplots import fonts


@pytest.mark.parametrize("font_func", [
    fonts.icml2022,
    fonts.icml2024,
    fonts.neurips2021,
    fonts.neurips2022,
    fonts.neurips2023,
    fonts.neurips2024,
    fonts.iclr2023,
    fonts.iclr2024,
    fonts.cvpr2024,
])
def test_times_text_cmodern_math(font_func):
    """Non-TeX functions should use Times text with Computer Modern math."""
    config = font_func()
    assert config["mathtext.fontset"] == "cm"
    assert config["font.serif"] == ["Times"]
    assert config["text.usetex"] is False
