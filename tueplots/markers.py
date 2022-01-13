"""Marker styles."""


def with_edge(*, edgecolor="black", edgewidth=0.5):
    """The facecolor is set to the linecolor, the edgecolor is changed."""
    return {
        "lines.markeredgecolor": edgecolor,
        "lines.markerfacecolor": "auto",
        "lines.markeredgewidth": edgewidth,
    }


def inverted(*, facecolor="white", edgewidth=0.75):
    """The edgecolor is set to the linecolor, the facecolor is changed."""
    return {
        "lines.markeredgecolor": "auto",
        "lines.markerfacecolor": facecolor,
        "lines.markeredgewidth": edgewidth,
    }
