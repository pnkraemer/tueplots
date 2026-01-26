"""Tests for the _times_text_cmodern_math() function behavior.

This tests that non-TeX font functions now mirror TeX behavior:
- Times text with Computer Modern math (no STIX)
- This matches what usepackage{times} and usepackage{ptm} do in LaTeX
"""

from tueplots import fonts


class TestTimesTextCmodernMath:
    """Test that non-TeX functions use Times text with Computer Modern math."""

    def test_icml2022_no_stix(self):
        """ICML 2022 non-TeX should NOT use STIX fontset."""
        config = fonts.icml2022()
        assert "mathtext.fontset" not in config
        assert config["font.serif"] == ["Times"]
        assert config["text.usetex"] is False

    def test_icml2024_no_stix(self):
        """ICML 2024 non-TeX should NOT use STIX fontset."""
        config = fonts.icml2024()
        assert "mathtext.fontset" not in config
        assert config["font.serif"] == ["Times"]

    def test_neurips2024_no_stix(self):
        """NeurIPS 2024 non-TeX should NOT use STIX fontset."""
        config = fonts.neurips2024()
        assert "mathtext.fontset" not in config
        assert config["font.serif"] == ["Times"]

    def test_iclr2024_no_stix(self):
        """ICLR 2024 non-TeX should NOT use STIX fontset."""
        config = fonts.iclr2024()
        assert "mathtext.fontset" not in config
        assert config["font.serif"] == ["Times"]

    def test_cvpr2024_no_stix(self):
        """CVPR 2024 non-TeX should NOT use STIX fontset."""
        config = fonts.cvpr2024()
        assert "mathtext.fontset" not in config
        assert config["font.serif"] == ["Times"]


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

        # Neither should force math font to match (for serif)
        assert "mathtext.fontset" not in non_tex_config
        # TeX version uses default LaTeX math (Computer Modern)
