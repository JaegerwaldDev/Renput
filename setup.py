from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0.0'
DESCRIPTION = 'Tab-completion for inputs'
LONG_DESCRIPTION = 'A simple Python library for Windows, which replaces the default input function in order to add the functionality to automatically complete an input using the tab key.'

# Setting up
setup(
    name="renput",
    version=VERSION,
    author="Jaegerwald (JaegerwaldDev)",
    author_email="<jaegerwald.dev@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['tab', 'completion', 'auto-completion', 'tab-completion', 'input', 'modified input', 'windows', 'easy-to-use'],
    classifiers=[
        "Development Status :: Released",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)
