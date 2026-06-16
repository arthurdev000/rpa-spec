# SPDX-FileCopyrightText: Copyright 2026 RPA Architecture Team
# SPDX-License-Identifier: CC-BY-SA-4.0

# RPA Specification documentation build configuration file

# -- Project information -----------------------------------------------------

project = 'RPA Specification'
author = 'RPA Architecture Team'
copyright = '2026, RPA Architecture Team'

# The short X.Y version
version = '0.1'
# The full version, including alpha/beta/rc tags
release = '0.1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.intersphinx',      # Cross-referencing
    'sphinx.ext.autodoc',          # Auto documentation from code
    'sphinx.ext.viewcode',         # View source code links
    'sphinx.ext.graphviz',         # Graphviz diagrams
    'sphinxcontrib.plantuml',      # PlantUML diagrams
    'sphinx_rtd_theme',            # Read the Docs theme
]

# PlantUML configuration
plantuml_output_format = 'svg'
plantuml_latex_output_format = 'pdf'

# Graphviz configuration
graphviz_output_format = 'svg'

# Add any paths that contain templates here
templates_path = ['_templates']

# List of patterns, relative to source directory, to ignore
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
}

html_static_path = ['_static']

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'figure_align': 'htbp',
    'preamble': r'''
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{bytefield}  % For bit-field diagrams like MMU page tables
''',
}

# Grouping the document tree into LaTeX files
latex_documents = [
    (master_doc, 'rpa-spec.tex', 'RPA Specification',
     'RPA Architecture Team', 'manual'),
]

# -- Options for PDF output (via LaTeX) --------------------------------------

pdf_documents = [
    ('index', 'rpa-spec', 'RPA Specification', 'RPA Architecture Team'),
]

# -- Intersphinx configuration -----------------------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

# -- Custom substitutions ----------------------------------------------------

rst_prolog = """
.. |RPA| replace:: RPA Specification
.. |API| replace:: API
"""