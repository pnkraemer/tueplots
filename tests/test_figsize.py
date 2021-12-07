
from momlplots import figsize


def test_jmlr():

    size = figsize.jmlr()
    assert isinstance(size, tuple)

def test_golden_ratio():
    ratio = figsize.golden_ratio()
    assert abs(ratio - 1/1.61) < 0.1, ratio