from momlplots import fonts

def test_icml():
    font = fonts.icml()
    assert isinstance(font, dict)


def test_neurips():
    font = fonts.neurips()
    assert isinstance(font, dict)
