"""
General configuration for Lex project.
"""
import os

DEBUG = os.environ.get('LEX_DEBUG') or True
PORT = os.environ.get('LEX_PORT') or 8888
