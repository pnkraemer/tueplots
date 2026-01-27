"""Tests for the _times_text_cmodern_math() function behavior.

This tests that non-TeX font functions now mirror TeX behavior:
- Times text with Computer Modern math (no STIX)
- This matches what usepackage{times} and usepackage{ptm} do in LaTeX
"""

import pytest

from tueplots import fonts


class TestTimesTextCmodernMath:
    """Test that non-TeX functions use Times text with Computer Modern math."""

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
    def test_uses_cm_math(self, font_func):
        """Non-TeX functions should use Computer Modern math."""
        config = font_func()
        assert config["mathtext.fontset"] == "cm"
        assert config["font.serif"] == ["Times"]
        assert config["text.usetex"] is False


class TestTexVersionsUnchanged:
    """Test that TeX versions still work correctly with sansmath for sans-serif."""

    def test_icml2022_tex_serif_no_sansmath(self):
        """Serif TeX should not have sansmath."""
        config = fonts.icml2022_tex(family="serif")
        assert "sansmath" not in config["text.latex.preamble"]

    def test_icml2022_tex_sans_has_sansmath(self):
        """Sans-serif TeX should have sansmath."""
        config = fonts.icml2022_tex(family="sans-serif")
        assert r"\usepackage{sansmath}" in config["text.latex.preamble"]
        assert r"\sansmath" in config["text.latex.preamble"]

    def test_neurips2024_tex_serif_no_sansmath(self):
        """Serif TeX should not have sansmath."""
        config = fonts.neurips2024_tex(family="serif")
        assert "sansmath" not in config["text.latex.preamble"]

    def test_neurips2024_tex_sans_has_sansmath(self):
        """Sans-serif TeX should have sansmath."""
        config = fonts.neurips2024_tex(family="sans-serif")
        assert r"\usepackage{sansmath}" in config["text.latex.preamble"]
        assert r"\sansmath" in config["text.latex.preamble"]


class TestTexNonTexConsistency:
    """Test that TeX and non-TeX versions are now consistent."""

    def test_icml2022_consistency(self):
        """Both TeX and non-TeX should use Times text without forcing math font."""
        tex_config = fonts.icml2022_tex(family="serif")
        non_tex_config = fonts.icml2022()

        # Both should use Times for text
        assert tex_config["text.usetex"] is True
        assert non_tex_config["text.usetex"] is False
        assert non_tex_config["font.serif"] == ["Times"]

        # Both use Computer Modern for math
        assert non_tex_config["mathtext.fontset"] == "cm"
