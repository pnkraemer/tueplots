from tueplots import colors


def test_tue_dark():
    color = colors.tue_dark()
    assert isinstance(color, tuple)
