from sysconfig import get_paths

from numpy import get_include
from numpy.distutils.core import Extension, setup

ext_modules = [
    Extension(
        "numcertain.uncertain",
        [
            "src/numcertain/uncertain.c",
            "src/numcertain/uncertaindtype.c",
            "src/numcertain/npyuncertain.c",
        ],
        include_dirs=[get_paths()["include"], get_include()],
    ),
]

setup(ext_modules=ext_modules)
