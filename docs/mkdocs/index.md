# Introduction

Unix `ls`, `find`, and `tree` commands combined into a Python module.

!!! warning

    Not yet done (has not reached version 0.1.0), no commitment to finish.

`lsutil` combines commonly used functionalities of the `ls`, `find`, and `tree` commands.
The functionality is approximately similar to

    find <find options> -exec ls <ls options> \{\} \;

with perhaps better performance and ease of use. Some unique functionalities are:

- ignore files

## Installation

The package is available on `pypi.org`. Install the package by

    pip install lsutil

## Command line

The command `lsutil` is available as a script.


## Python module

``` python
import lsutil

lsutil.ls()
```

## Developments

- Source code on github:  [https://github.com/koobedoc/lsutil](https://github.com/koobedoc/lsutil)
- Package on PyPI: [https://pypi.org/search/?q=lsutil](https://pypi.org/search/?q=lsutil)

