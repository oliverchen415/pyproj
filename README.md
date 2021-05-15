# pyproj
Basic setup of a simple Python project

## ARCHIVED
I'm not working on this anymore, so choose either one of the alternatives below!

## ALTERNATIVES
I kinda realize that this version's a bit of a pain to use, so I've now built it in Go. [Check it out here!](../../../go_pyproj)

If you were looking for a GUI version, there's one now! [Check it out here!](../../../projmake_qt)

## Requirements
Requires Python 3.6+ and [`Click`](https://click.palletsprojects.com/en/7.x/)

## Installation
The easiest way to use `pyproj` is to install it into a Python environment.
1. Open a Python environment.
   * Use `venv` ([guide here](https://realpython.com/python-virtual-environments-a-primer/#using-virtual-environments)) or `conda` ([guide here](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment))
2. Download both `pyproj.py` and `setup.py` to a folder, e.g. `C:\Users\<username>\Downloads\pyproj` if you're on Windows.
3. Open the folder in a terminal, e.g.:
```
cd C:\Users\<username>\Downloads\pyproj
```
4. To install it into the current Python environment:
```
pip install -e .
```
  * **Don't forget the dot after `-e`**.

## Usage
Now, from anywhere on your computer, you can simply call
```
pyproj --name <project_name>
```
or
```
pyproj -n <project_name>
```

This creates a new folder named `<project_name>` with the following folder structure:
```
<project_name>
├── .gitignore
├── <project_name>.py
└── README.md
```
