"""
Manage paths to directories in project
"""
from pathlib import Path

DATA_DIR = "data"


def get_path(directory=DATA_DIR, subdir=""):
    """
    Get relative path to /directory/subdir

    ...

    Attributes
    ----------
    subdir : str
        name of subdirectory
    """

    path = Path(__file__).parents[2]
    path = Path(path, directory, subdir)

    if not path.exists():
        path.mkdir(parents=True)
    return path
