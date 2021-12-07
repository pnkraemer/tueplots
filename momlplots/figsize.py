

# Double-column formats

def icml(*, column="half"):
    height_per_width = golden_ratio()
    if column == "half":
        width = 234.8775
        height = height_per_width * width
        return width, height
    width = 487.8225
    height = width * height_per_width / 2.0
    return width, height

def cvpr(*, column="half"):
    height_per_width = golden_ratio()
    if column == "half":
        width = 237.13594
        height = height_per_width * width
        return width, height
    width = 496.85625
    height = width * height_per_width / 2.0
    return width, height

# Single-column formats

def jmlr():
    """JMLR figure size """
    width = 433.62
    height = 0.5 * width * golden_ratio()
    return width, height

def neurips():
    width = 397.48499
    height = golden_ratio() * width
    return width, height


def golden_ratio():
    return  (5. ** 0.5 - 1.) / 2.

def inches_per_point():
    return 1. / 72.27