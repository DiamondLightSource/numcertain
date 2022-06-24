import subprocess
import sys

from numcertain import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "numcertain", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
