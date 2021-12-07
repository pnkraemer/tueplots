

def jmlr():
    """JMLR figure size """
    width = 433.62
    height = 0.5 * width * golden_ratio()
    return width, height

def icml(*, column="half"):
    height_per_width = golden_ratio()
    if column == "half":
        width = 234.8775
        height = height_per_width * width
        return width, height
    width = 487.8225
    height = width * height_per_width / 2.0
    return width, height


def golden_ratio():
    return  (5. ** 0.5 - 1.) / 2.

def inches_per_point():
    return 1. / 72.27