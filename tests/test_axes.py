"""Tests for axes functionality."""

import matplotlib.pyplot as plt

from tueplots import axes


def test_lines():
    config = axes.lines(
        line_base_ratio=2.0,
        tick_major_base_ratio=1.0,
        tick_minor_base_ratio=0.5,
        tick_size_width_ratio=3.0,
        tick_major_size_min=1.5,
        tick_minor_size_min=1.0,
        axisbelow=True,
    )
    plt.rcParams.update(config)


def test_color():
    plt.rcParams.update(axes.color(face="red", base="red"))


def test_legend():
    plt.rcParams.update(axes.legend(shadow=False, frameon=True, fancybox=False))


def test_spines():
    plt.rcParams.update(axes.spines(right=False, left=True, top=False, bottom=False))


def test_tick_direction():
    plt.rcParams.update(axes.tick_direction(x="in", y="out"))


def test_grid():
    plt.rcParams.update(
        axes.grid(
            grid_alpha=0.25,
            grid_linestyle="dashed",
        )
    )
