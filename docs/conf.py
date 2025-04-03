"""Documentation configuration."""

import os
import sys

project = "PYthon region geospatial utilities"
author = "Martí Bosch"

__version__ = "0.1.0"
version = __version__
release = __version__

extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "myst_parser"]

autodoc_typehints = "description"
html_theme = "default"

# add module to path
sys.path.insert(0, os.path.abspath(".."))
