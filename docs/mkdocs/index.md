# Introduction

Unix command line 'ls' command in a Python module.

```
import lsutil

lsutil.ls()
```

## Installation

The package is available on `test.pypi.org`. Run the following to install the package.

    pip install --index-url https://test.pypi.org/simple/ --no-deps --upgrade lsutil


Notice that `--no-deps` prevents the installation of dependencies because they may not be available on
`test.pypi.org`. Install the dependencies separately by:


    pip install fastapi jinja2 uvicorn




