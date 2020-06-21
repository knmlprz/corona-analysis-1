"""
Manage paths to directories in project
"""
from pathlib import Path
import os

DATA_DIR = "data"


def get_path(directory=DATA_DIR, subdir="", abs_path=os.getcwd()):
    """
    Returns Path to directory in cwd.
    ...

    Attributes
    ----------
    directory : str
        Name of directory
    subdir : str
        Name of subdirectory
    abs_path : Path
        Absolute path to project, cwd by default.
    """

    path = abs_path
    path = Path(path, directory, subdir)

    if not path.exists():
        path.mkdir(parents=True)
    return path
