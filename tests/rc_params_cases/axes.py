"""Test cases for axes."""


from pytest_cases import case

from tueplots import axes


def case_axes_lines_default():
    return axes.lines()


def case_axes_lines_custom():
    return axes.lines(
        base_width=0.5,
        line_base_ratio=2.0,
        tick_major_base_ratio=1.0,
        tick_minor_base_ratio=0.5,
        tick_size_width_ratio=3.0,
        tick_major_size_min=1.5,
        tick_minor_size_min=1.0,
        axisbelow=True,
    )


def case_axes_color_default():
    return axes.color()


def case_axes_color_custom():
    return axes.color(face="red", base="red")


def case_axes_legend_default():
    return axes.legend()


def case_axes_legend_custom():
    return axes.legend(shadow=True, frameon=False, fancybox=True)


def case_axes_spines_default():
    return axes.spines()


def case_axes_spines_custom():
    return axes.spines(right=False, left=False, top=False, bottom=False)


def case_axes_tick_direction_default():
    return axes.tick_direction()


def case_axes_tick_direction_custom():
    return axes.tick_direction(x="in", y="out")


def case_axes_grid_default():
    return axes.grid()


def case_axes_grid_custom():
    return axes.grid(
        grid_alpha=0.25,
        grid_linestyle="dashed",
    )
