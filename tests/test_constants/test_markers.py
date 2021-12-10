"""Tests for marker lists."""


import pytest

from tueplots.constants import markers

all_marker_collections = [
    markers.o_sized,
    markers.x_like,
    markers.x_like_bold,
    markers.triangles,
]


@pytest.mark.parametrize("marker_collection", all_marker_collections)
def test_is_array(marker_collection):
    assert isinstance(marker_collection, tuple)
