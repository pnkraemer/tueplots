"""Test cases for axes."""


from tueplots import axes


def case_axes_lines():
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


def case_axes_color():
    return axes.color(face="red", base="red")


def case_axes_legend():
    return axes.legend(shadow=True, frameon=False, fancybox=True)


def case_axes_spines():
    return axes.spines(right=False, left=False, top=False, bottom=False)


def case_axes_tick_direction():
    return axes.tick_direction(x="in", y="out")


def case_axes_grid():
    return axes.grid(
        grid_alpha=0.25,
        grid_linestyle="dashed",
    )
