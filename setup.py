import os
import setuptools


setuptools.setup(
    name="eulogy",
    version="0.0.2",
    author="roganjosh",
    author_email="",
    description="A logger for atexit debugging",
    url="",
    packages=setuptools.find_packages('src'),
    package_dir={"": "src"},
    python_requires='>=3.7'
)