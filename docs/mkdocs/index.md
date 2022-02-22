# Introduction


Unix `ls` and `find` commands combined into a Python module.

!!! warning

    Not yet done, not yet released, no commitment to finish.

`lsutil` combines commonly used functionalities of the `ls` and `find` command
into a single command and Python methods. The functionality is approximately similar to

    find <find options> -exec ls <ls options> \{\} \;

with perhaps better performance and ease of use.

## Python module

```
import lsutil

lsutil.ls()
```

## Installation

The package will be available on `pypi.org`. Run the following to install the package.

    pip install lsutil


