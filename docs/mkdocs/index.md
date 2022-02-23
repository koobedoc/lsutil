# Introduction

Unix `ls`, `find`, and `tree` commands combined into a Python module.

!!! warning

    Not yet done, not yet released, no commitment to finish.

`lsutil` combines commonly used functionalities of the `ls`, `find`, and `tree` commands.
The functionality is approximately similar to

    find <find options> -exec ls <ls options> \{\} \;

with perhaps better performance and ease of use.


## Installation

The package will be available on `pypi.org`. Run the following to install the package.

    pip install lsutil


## Command line


The command `lsutil` is available as a script.


## Python module


    import lsutil


    lsutil.ls()


