"""
OSR: Operating System Release Parser Tool
"""

# Version mapping for your source code tracking
__version__ = "0.0.0"

# Explicitly expose the main function or classes from your internal modules
# This allows users to do: from osr import main
from .osr import main

# Define exactly what gets exported when someone types: from osr import *
__all__ = [
    "main",
    "__version__",
]

