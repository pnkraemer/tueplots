import pytest
from momlplots import figsize


full_and_half_columns = pytest.mark.parametrize("column", ["full", "half"])


@full_and_half_columns
def test_icml(column):
    size = figsize.icml(column=column)
    assert isinstance(size, tuple)


@full_and_half_columns
def test_cvpr(column):
    size = figsize.cvpr(column=column)
    assert isinstance(size, tuple)


def test_neurips():
    size = figsize.neurips()
    assert isinstance(size, tuple)


def test_jmlr():
    size = figsize.jmlr()
    assert isinstance(size, tuple)


def test_golden_ratio():
    ratio = figsize.golden_ratio()
    assert abs(ratio - 1 / 1.61) < 0.1, ratio


def test_inches_per_point():
    in_per_pt = figsize.inches_per_point()
    assert in_per_pt > 0.0
