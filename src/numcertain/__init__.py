from importlib.metadata import version

from . import uncertain

__version__ = version("adcorr")

__all__ = ["__version__", "uncertain"]
