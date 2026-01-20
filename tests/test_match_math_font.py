"""Tests for the match_math_font parameter behavior."""

import pytest

from tueplots import fonts


class TestMatchMathFontNonTex:
    """Test match_math_font for non-TeX functions (STIX fontset)."""

    def test_times_match_math_font_false_no_stix(self):
        """When match_math_font=False, STIX fontset should NOT be applied."""
        config = fonts.icml2022(match_math_font=False)
        assert "mathtext.fontset" not in config

    def test_times_match_math_font_true_has_stix(self):
        """When match_math_font=True, STIX fontset should be applied."""
        config = fonts.icml2022(match_math_font=True)
        assert config["mathtext.fontset"] == "stix"
        assert config["mathtext.rm"] == "Times"
        assert config["mathtext.it"] == "Times:italic"
        assert config["mathtext.bf"] == "Times:bold"

    def test_neurips_match_math_font_false_no_stix(self):
        """When match_math_font=False, STIX fontset should NOT be applied."""
        config = fonts.neurips2024(match_math_font=False)
        assert "mathtext.fontset" not in config

    def test_neurips_match_math_font_true_has_stix(self):
        """When match_math_font=True, STIX fontset should be applied."""
        config = fonts.neurips2024(match_math_font=True)
        assert config["mathtext.fontset"] == "stix"


class TestMatchMathFontTex:
    """Test match_math_font for TeX functions (sansmath package)."""

    def test_times_tex_ptm_serif_no_sansmath(self):
        """Serif family should never have sansmath regardless of match_math_font."""
        config_false = fonts.neurips2024_tex(family="serif", match_math_font=False)
        config_true = fonts.neurips2024_tex(family="serif", match_math_font=True)
        # Neither should have sansmath for serif
        assert "sansmath" not in config_false["text.latex.preamble"]
        assert "sansmath" not in config_true["text.latex.preamble"]

    def test_times_tex_ptm_sans_match_math_font_false_no_sansmath(self):
        """Sans-serif with match_math_font=False should NOT have sansmath."""
        config = fonts.neurips2024_tex(family="sans-serif", match_math_font=False)
        assert "sansmath" not in config["text.latex.preamble"]
        assert r"\renewcommand{\familydefault}{\sfdefault}" in config["text.latex.preamble"]

    def test_times_tex_ptm_sans_match_math_font_true_has_sansmath(self):
        """Sans-serif with match_math_font=True should have sansmath."""
        config = fonts.neurips2024_tex(family="sans-serif", match_math_font=True)
        assert r"\usepackage{sansmath}" in config["text.latex.preamble"]
        assert r"\sansmath" in config["text.latex.preamble"]

    def test_times_tex_times_sans_match_math_font_false_no_sansmath(self):
        """Sans-serif with match_math_font=False should NOT have sansmath."""
        config = fonts.icml2022_tex(family="sans-serif", match_math_font=False)
        assert "sansmath" not in config["text.latex.preamble"]

    def test_times_tex_times_sans_match_math_font_true_has_sansmath(self):
        """Sans-serif with match_math_font=True should have sansmath."""
        config = fonts.icml2022_tex(family="sans-serif", match_math_font=True)
        assert r"\usepackage{sansmath}" in config["text.latex.preamble"]
        assert r"\sansmath" in config["text.latex.preamble"]

    def test_computer_modern_sans_match_math_font_false_no_sansmath(self):
        """Sans-serif with match_math_font=False should NOT have sansmath."""
        config = fonts.aistats2025_tex(family="sans-serif", match_math_font=False)
        assert "sansmath" not in config["text.latex.preamble"]

    def test_computer_modern_sans_match_math_font_true_has_sansmath(self):
        """Sans-serif with match_math_font=True should have sansmath."""
        config = fonts.aistats2025_tex(family="sans-serif", match_math_font=True)
        assert r"\usepackage{sansmath}" in config["text.latex.preamble"]
        assert r"\sansmath" in config["text.latex.preamble"]


class TestDefaultBehavior:
    """Test that default behavior matches LaTeX templates (no sansmath/stix)."""

    def test_default_is_false(self):
        """Default match_math_font should be False."""
        # Non-tex: no STIX by default
        config = fonts.icml2022()
        assert "mathtext.fontset" not in config

        # Tex with sans-serif: no sansmath by default
        config_tex = fonts.icml2022_tex(family="sans-serif")
        assert "sansmath" not in config_tex["text.latex.preamble"]
