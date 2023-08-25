from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Tab-completion for inputs'
with open('README.md', encoding='utf-8') as readme:
    LONG_DESCRIPTION = readme.read()
    
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
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)
