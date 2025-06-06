"""Documentation configuration."""

import os
import sys

import pkg_resources

project = "pyregeon"
author = "Martí Bosch"

release = pkg_resources.get_distribution(project).version
version = ".".join(release.split(".")[:2])

extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "myst_parser"]

autodoc_typehints = "description"
html_theme = "pydata_sphinx_theme"
html_theme_options = {"github_url": "https://github.com/martibosch/pyregeon"}

# add module to path
sys.path.insert(0, os.path.abspath(".."))
