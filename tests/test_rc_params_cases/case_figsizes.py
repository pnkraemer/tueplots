"""Test-cases for figsizes."""


from tueplots import figsizes


def case_figsizes_icml2022_full():
    return figsizes.icml2022_full(nrows=2, ncols=3, height_to_width_ratio=1.0)


def case_figsizes_icml2022_half():
    return figsizes.icml2022_half(nrows=2, ncols=3, height_to_width_ratio=1.0)


def case_figsizes_aistats2022_full():
    return figsizes.aistats2022_full(nrows=2, ncols=3, height_to_width_ratio=1.0)


def case_figsizes_aistats2022_half():
    return figsizes.aistats2022_half(nrows=2, ncols=3, height_to_width_ratio=1.0)


def case_figsizes_aistats2023_full():
    return figsizes.aistats2023_full(nrows=2, ncols=3, height_to_width_ratio=1.0)


def case_figsizes_aistats2023_half():
    return figsizes.aistats2023_half(nrows=2, ncols=3, height_to_width_ratio=1.0)


def case_figsizes_cvpr2022_half():
    return figsizes.cvpr2022_half(nrows=2, ncols=3, height_to_width_ratio=1.0)


def case_figsizes_cvpr2022_full():
    return figsizes.cvpr2022_full(nrows=2, ncols=3, height_to_width_ratio=1.0)


def case_figsizes_cvpr2024_half():
    return figsizes.cvpr2024_half(nrows=2, ncols=3, height_to_width_ratio=1.0)


def case_figsizes_cvpr2024_full():
    return figsizes.cvpr2024_full(nrows=2, ncols=3, height_to_width_ratio=1.0)


def case_figsizes_neurips2021():
    return figsizes.neurips2021(nrows=2, ncols=3, height_to_width_ratio=1.0)


def case_figsizes_neurips2022():
    return figsizes.neurips2022(nrows=2, ncols=3, height_to_width_ratio=1.0)


def case_figsizes_neurips2023():
    return figsizes.neurips2023(nrows=2, ncols=3, height_to_width_ratio=1.0)


def case_figsizes_iclr2023():
    return figsizes.iclr2023(nrows=2, ncols=3, height_to_width_ratio=1.0)


def case_figsizes_iclr2024():
    return figsizes.iclr2024(nrows=2, ncols=3, height_to_width_ratio=1.0)


def case_figsizes_aaai2024_half():
    return figsizes.aaai2024_half(nrows=2, ncols=3, height_to_width_ratio=1.0)


def case_figsizes_aaai2024_full():
    return figsizes.aaai2024_full(nrows=2, ncols=3, height_to_width_ratio=1.0)


def case_figsizes_uai2023_half():
    return figsizes.uai2023_half(nrows=2, ncols=3, height_to_width_ratio=1.0)


def case_figsizes_uai2023_full():
    return figsizes.uai2023_full(nrows=2, ncols=3, height_to_width_ratio=1.0)


def case_figsizes_jmlr2001():
    return figsizes.jmlr2001(nrows=2, ncols=3, height_to_width_ratio=1.0)


def case_beamer_169():
    return figsizes.beamer_169(rel_width=0.5, rel_height=0.1)
