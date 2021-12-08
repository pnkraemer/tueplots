"""Fontsize settings."""


def icml2022():
    return from_base(base=10)


def neurips2021():
    return from_base(base=10)


def jmlr2001():
    return from_base(base=10.95)


def from_base(*, base=10):
    return {
        "axes.labelsize": base - 1,
        "font.size": base - 1,
        "legend.fontsize": base - 3,
        "xtick.labelsize": base - 3,
        "ytick.labelsize": base - 3,
        "axes.titlesize": "medium",
    }
