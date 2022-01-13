"""Tests for tueplots.

Essentially, there are only two kinds of tests.

    1) The return types of anything in tueplots' main module should be a dictionary
       that is compatible with plt.rcParams.update()-style functions.
    2) The return types of anything in tueplots.constants should be a numpy array.

These two tests make up most of the test suite.
"""
