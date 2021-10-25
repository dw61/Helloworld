# test electronvolt.py with atom script
# python -i electronvolt.py
# update README.md
# update version number in setuptools.setup
# rm -r __pycache__
# python setup.py sdist bdist_wheel
# twine upload dist/*
# rm -r build dist *.egg-info
# pip install electronvolt -U
# git commit and push
# pypi.org/project/electronvolt
# github.com/dw61/electronvolt
# test module in home directory or on mybinder.org

import setuptools

setuptools.setup(
    name="hbar",
    version="0.0.9",
    author_email="xx@virginia.edu",
    description="A Project.",
    long_description="no description hahaha surprise",
    long_description_content_type="text/markdown",
    url="https://github.com/dw61/helloworld",
    py_modules=["fourspacetab"],
    python_requires='>=3.6',
)
