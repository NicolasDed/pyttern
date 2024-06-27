# read the contents of your README file
from pathlib import Path

from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='pyttern',
    version='0.1.3',
    packages=['pyttern', 'pyttern.antlr'],
    package_dir={'': 'src'},
    url='https://github.com/JulienLie/pyttern',
    license='MIT',
    author='Julien Lienard',
    author_email='julien.lienard@uclouvain.be',
    description="Python package to build code patterns using a dedicated language.",
    install_requires=[
        "pytest",
        "antlr4-python3-runtime==4.7.2",
        "pytest-timeout"
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
