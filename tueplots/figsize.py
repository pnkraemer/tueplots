"""Figure size settings."""

# Double-column formats


def icml2022(*, column="full", nrows=1):

    height_per_width = golden_ratio()
    if column == "half":
        width = 234.8775 / 72.27
        height = height_per_width * width * nrows
        return {"figure.figsize": (width, height)}

    width = 487.8225 / 72.27
    height = width * height_per_width / 2.0 * nrows
    return {"figure.figsize": (width, height)}


def cvpr2022(*, column="full", nrows=1):
    height_per_width = golden_ratio()
    if column == "half":
        width = 237.13594 / 72.27
        height = height_per_width * width * nrows
        return {"figure.figsize": (width, height)}
    width = 496.85625 / 72.27
    height = width * height_per_width / 2.0 * nrows
    return {"figure.figsize": (width, height)}


# Single-column formats
def beamer(*, nrows=1):
    """Beamer figure size for `aspectratio=169`."""
    width = 398.3386 / 72.27
    height = 0.8 * 241.56738 / 72.27 * nrows
    return {"figure.figsize": (width, height)}


def jmlr2001(*, nrows=1):
    """JMLR figure size"""
    width = 433.62 / 72.27
    height = 0.5 * width * golden_ratio() * nrows
    return {"figure.figsize": (width, height)}


def neurips2021(*, nrows=1):
    width = 397.48499 / 72.27
    height = 0.5 * golden_ratio() * width * nrows
    return {"figure.figsize": (width, height)}


def golden_ratio():
    return (5.0 ** 0.5 - 1.0) / 2.0


def inches_per_point():
    return 1.0 / 72.27
