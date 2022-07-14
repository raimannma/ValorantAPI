import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "Valorant API Wrapper"
copyright = "2022, Valorant API Wrappr"
author = "Manuel Raimann"

version = "1.0.1"
release = "1.0.1"

language = None

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "autodocsumm",
]

add_module_names = False
templates_path = ["templates"]
source_suffix = ".rst"
html_extra_path = []
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
pygments_style = "sphinx"
todo_include_todos = True
html_codeblock_linenos_style = "table"
html_theme = "sphinx_rtd_theme"

autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "undoc-members": True,
    "private-members": True,
}
