.. tueplots documentation master file, created by
   sphinx-quickstart on Thu Jan 20 15:36:42 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

TUEplots reference documentation
================================

TUEplots is a light-weight matplotlib extension
that adapts your figure sizes to formats more suitable for scientific publications.
It produces configurations that are compatible with matplotlib's `rcParams`,
and provides fonts, figure sizes, font sizes, color schemes, and more, for a number of publication formats.


Supported Venues
----------------

The following venues are currently supported by TUEplots out of the box as pre-configured bundles:

- Conference on Neural Information Processing Systems (NeurIPS)
- International Conference on Artificial Intelligence and Statistics (AISTATS)
- International Conference on Learning Representations (ICLR)
- International Conference on Machine Learning (ICML)
- Conference on Uncertainty in Artificial Intelligence (UAI)
- Journal of Machine Learning Research (JMLR)

For further details on the available bundles, check out the `tueplots.bundles API documentation <docs_api/tueplots.bundles.rst>`_.


.. toctree::
   :maxdepth: 1
   :caption: Getting started

   getting_started/installation
   getting_started/usage_example
   getting_started/application_icml2022
   getting_started/troubleshooting


.. toctree::
   :maxdepth: 1
   :caption: Example notebooks

   example_notebooks/axes
   example_notebooks/bundles
   example_notebooks/color-cycles
   example_notebooks/figsizes
   example_notebooks/fonts
   example_notebooks/fontsizes
   example_notebooks/markers


.. toctree::
   :maxdepth: 4
   :caption: API documentation

   docs_api/tueplots


.. toctree::
   :maxdepth: 1
   :caption: Developer documentation

   docs_dev/contribution_guide
   docs_dev/examples



.. toctree::
   :maxdepth: 1
   :caption: Other

   GitHub Repository <https://github.com/pnkraemer/tueplots>
