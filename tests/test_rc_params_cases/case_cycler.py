"""Test cases for the cycler."""

from tueplots import cycler


def case_cycler_cycler():
    return cycler.cycler(color=["red", "blue"], marker=["x", "+"])
