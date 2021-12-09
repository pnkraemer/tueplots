"""Tests for axes functionality."""

import matplotlib.pyplot as plt

from tueplots import axes


def test_lines():
    plt.rcParams.update(
        axes.lines(
            color="red",
            xtick_direction="inout",
        )
    )


def test_face():
    plt.rcParams.update(axes.face(color="red"))
