"""Marker styles and sizes (:mod:`tueplots.markers`).

Provides predefined marker shapes and sizes for scatter plots
and line charts.

Examples
--------

.. plot::
    :include-source: True

    >>> import matplotlib.pyplot as plt
    >>> from tueplots import markers
    >>>
    >>> # Select a style bundle
    >>> style = markers.with_edge()
    >>>
    >>> # Apply the style to matplotlib
    >>> plt.rcParams.update(style)
    >>>
    >>> # Create a plot
    >>> fig, ax = plt.subplots()
    >>> ax.plot([0, 1, 2], [2, 1, 3], "o-")
    >>> ax.set_xlabel("$x$ label")
    >>> ax.set_ylabel("$y$ label")
    >>> plt.show()


"""


def with_edge(*, edgecolor="black", edgewidth=0.5):
    """Create markers with an edge.

    The facecolor matches the linecolor and the edgecolor is changed.
    """
    return {
        "lines.markeredgecolor": edgecolor,
        "lines.markerfacecolor": "auto",
        "lines.markeredgewidth": edgewidth,
    }


def inverted(*, facecolor="white", edgewidth=0.75):
    """Create inverted markers.

    The edgecolor matches the linecolor and the facecolor is changed.
    """
    return {
        "lines.markeredgecolor": "auto",
        "lines.markerfacecolor": facecolor,
        "lines.markeredgewidth": edgewidth,
    }
