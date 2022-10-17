from importlib.metadata import version

from . import uncertain

__version__ = version("numcertain")

__all__ = ["__version__", "uncertain"]
