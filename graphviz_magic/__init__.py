"""Graphviz magics"""
__version__ = '0.0.1'

from .graphviz import GraphvizMagics

def load_ipython_extension(ipython):
    ipython.register_magics(GraphvizMagics)