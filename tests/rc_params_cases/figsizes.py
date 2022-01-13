"""Test-cases for figsizes."""


from tueplots import figsizes


def case_figsizes_icml2022_default():
    return figsizes.icml2022()


def case_figsizes_icml2022_custom():
    return figsizes.icml2022(column="full", nrows=2, ncols=3, height_to_width_ratio=1.0)


def case_figsizes_cvpr2022_default():
    return figsizes.cvpr2022()


def case_figsizes_cvpr2022_custom():
    return figsizes.cvpr2022(column="full", nrows=2, ncols=3, height_to_width_ratio=1.0)


def case_figsizes_neurips2021_default():
    return figsizes.neurips2021()


def case_figsizes_neurips2021_custom():
    return figsizes.neurips2021(nrows=2, ncols=3, height_to_width_ratio=1.0)


def case_figsizes_jmlr2001_default():
    return figsizes.jmlr2001()


def case_figsizes_jmlr2001_custom():
    return figsizes.jmlr2001(nrows=2, ncols=3, height_to_width_ratio=1.0)


def case_beamer_169_default():
    return figsizes.beamer_169()


def case_beamer_169_custom():
    return figsizes.beamer_169(rel_width=0.5, rel_height=0.1)
