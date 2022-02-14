# Introduction

This started off with the need for a simple way to list directory contents nicely and
evolved into a learning experience.

*This is a work-in-progress with very few things working.*

Unix command-line 'ls' command in a Python module.

```
import lsutil

lsutil.ls()
```

## Installation

The package is available on `test.pypi.org`. Run the following to install the package.

    pip install --index-url https://test.pypi.org/simple/ --no-deps --upgrade lsutil


Notice that `--no-deps` prevents the installation of dependencies because they may not be available on
`test.pypi.org`. Install the dependencies separately by:

    pip install rich




