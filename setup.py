from setuptools import setup

setup(
    name="pyproj",
    version="0.1",
    py_modules=["pyproj"],
    install_requires=[
        "Click",
    ],
    entry_points="""
        [console_scripts]
        pyproj=pyproj:dir_file_create
    """
)