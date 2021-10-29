# python -i electronvolt.py
# update README.md
# update version number in setuptools.setup
# git commit and push
# pip install electronvolt -U
# pypi.org/project/electronvolt
# github.com/dw61/electronvolt
# test module in home directory or on mybinder.org

import setuptools

setuptools.setup(
    name="hbar",
    version="0.0.41",
    author_email="xx@virginia.edu",
    description="A Project.",
    long_description="no description hahaha surprise",
    long_description_content_type="text/markdown",
    url="https://github.com/dw61/helloworld",
    py_modules=["hbar"],
    python_requires='>=3.6',
)
