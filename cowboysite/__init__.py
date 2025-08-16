"""
Cowboy Django - ASCII art cowboys with Kubernetes jokes.
"""

try:
    from ._version import version as __version__
except ImportError:
    # Fallback if not built with setuptools_scm
    __version__ = "unknown"