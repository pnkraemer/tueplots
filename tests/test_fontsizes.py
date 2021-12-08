"""Tests for font sizes."""

import pytest

from tueplots import fontsizes


def test_icml2022():
    sizes = fontsizes.icml2022()
    assert isinstance(sizes, dict)


def test_neurips2021():
    sizes = fontsizes.icml2022()
    assert isinstance(sizes, dict)


@pytest.mark.parametrize("base", [9, 10])
def test_from_base(base):
    r"""
    Turn a base-size into font-sizes.

    For a paper that uses size 10pt fonts for \normalsize, do
    7pt for \scriptsize and
    9pt for \footnotesize and
    9pt for \small
    Figure captions are set in \small, so that's what we're using here.
    """
    sizes = fontsizes.from_base(base=base)
    assert isinstance(sizes, dict)
