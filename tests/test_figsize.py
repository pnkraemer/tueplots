import pytest
from tueplots import figsize


full_and_half_columns = pytest.mark.parametrize("column", ["full", "half"])
nrows_all = pytest.mark.parametrize("nrows", [1, 2])


@full_and_half_columns
@nrows_all
def test_icml(column, nrows):
    size = figsize.icml(column=column, nrows=nrows)
    assert isinstance(size, tuple)


@full_and_half_columns
@nrows_all
def test_cvpr(column, nrows):
    size = figsize.cvpr(column=column, nrows=nrows)
    assert isinstance(size, tuple)


@nrows_all
def test_neurips(nrows):
    size = figsize.neurips(nrows=nrows)
    assert isinstance(size, tuple)


@nrows_all
def test_jmlr(nrows):
    size = figsize.jmlr(nrows=nrows)
    assert isinstance(size, tuple)


def test_golden_ratio():
    ratio = figsize.golden_ratio()
    assert abs(ratio - 1 / 1.61) < 0.1, ratio


def test_inches_per_point():
    in_per_pt = figsize.inches_per_point()
    assert in_per_pt > 0.0
