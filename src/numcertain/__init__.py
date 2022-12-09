from importlib.metadata import version

from numcertain._numcertain import nominal, uncertain, uncertainty

__version__ = version("numcertain")
del version

__all__ = ["__version__", "nominal", "uncertain", "uncertainty"]
