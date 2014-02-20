"""
General configuration for Lex project.
"""
import os

DEBUG = os.environ.get('LEX_DEBUG') or True
PORT = os.environ.get('LEX_PORT') or 8888

HTML_PATH = os.environ.get('PROJECT_HTML') or 'docs/build/html'
STATIC_PATH = os.environ.get('PROJECT_STATIC') or "{0}/_static".format(HTML_PATH)
