"""``tueplots`` package.

``tueplots`` is a Python package that helps you create plots that match the styles and guidelines of different conferences and journals.
Each module in TUEplots provides specific settings like fonts, figure sizes, axes behavior, and bundled configurations for specific conferences.

Examples
--------

.. plot::
    :include-source: True

    >>> import matplotlib.pyplot as plt
    >>> from tueplots import bundles
    >>>
    >>> # Select a style bundle
    >>> style = bundles.icml2024(usetex=False)
    >>>
    >>> # Apply the style to matplotlib
    >>> plt.rcParams.update(style)
    >>>
    >>> # Create a plot
    >>> fig, ax = plt.subplots()
    >>> ax.plot([0, 1, 2], [2, 1, 3])
    >>> ax.set_xlabel("$x$ label")
    >>> ax.set_ylabel("$y$ label")
    >>> plt.show()
"""

from ._version import version as __version__
