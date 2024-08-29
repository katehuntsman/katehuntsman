print("starting project 2")
"""Start a Data Analytics Project."""

import pathlib


def create_project_directory(directory_proj2: str): # add type hinting to params
    """Creates a project sub-directory."""
    pathlib.Path(directory_proj2).mkdir(exist_ok=True)


def main():
    """Scaffold a project."""
    create_project_directory(directory_proj2='test') # name the param
    create_project_directory(directory_proj2='docs') # name the param


if__name__=="__main__": 
main()