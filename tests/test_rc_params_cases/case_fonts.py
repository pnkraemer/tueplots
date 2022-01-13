"""Test cases for font settings."""


from tueplots import fonts


def case_fonts_icml2022_default():
    return fonts.icml2022()


def case_fonts_icml2022_custom():
    return fonts.icml2022(family="serif")


def case_fonts_icml2022_tex_default():
    return fonts.icml2022_tex()


def case_fonts_icml2022_tex_custom():
    return fonts.icml2022_tex(family="serif")


def case_fonts_neurips2021_default():
    return fonts.neurips2021()


def case_fonts_neurips2021_custom():
    return fonts.neurips2021(family="serif")


def case_fonts_neurips2021_tex_default():
    return fonts.neurips2021_tex()


def case_fonts_neurips2021_tex_custom():
    return fonts.neurips2021_tex(family="serif")


def case_fonts_jmlr2001_tex_default():
    return fonts.jmlr2001_tex()


def case_fonts_jmlr2001_tex_custom():
    return fonts.jmlr2001_tex(family="serif")


def case_fonts_aistats2022_tex_default():
    return fonts.aistats2022_tex()


def case_fonts_aistats2022_tex_custom():
    return fonts.aistats2022_tex(family="serif")
