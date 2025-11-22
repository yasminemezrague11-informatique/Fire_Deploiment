# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import django 
sys.path.insert(0, os.path.abspath('../'))  # Chemin vers le répertoire principal du projet Django

os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'  # Remplacez par le chemin de votre fichier settings.py
django.setup()


# Choisissez un thème (optionnel, mais recommandé)
html_theme = 'sphinx_rtd_theme'


project = 'myproject'
copyright = '2025, yasmine'
author = 'yasmine'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',  # Extraction automatique de la documentation des docstrings
    'sphinx.ext.viewcode',  # Lien vers le code source dans la documentation
    'sphinx_rtd_theme',     # Thème pour la documentation
]


templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

