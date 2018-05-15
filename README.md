# Python Packager

This tool packages a Python package structure into a single executable
and loadable file.

## Packaging

```bash
pypack path/to/package > binary
```

## Directory Structure

The root directory must contain an `__init__.py` which is the entrypoint
into the package when it is loaded as a module. This file will not be
loaded if the package is executed as a binary.

The root directory can alternatively contain a `__main__.py` which is
the entrypoint into the package when it is executed as a binary. This
will not be loaded if the package is loaded as a module.

Both may be provided.

It is recommended that relative module imports are used to
cross-reference modules within the package.

## Including as Module

The file can be imported as a module into both Python 2 and 3 using the
following:

```python
# Add the binary package to the search path
import sys
sys.path.insert(0, "path/to/binary")

# Import the module from within the package
import binary_name
```

## Example

Look at the `example` package to see such a file structure. It can be
built into a module that can be run or imported with:

```bash
pypack example-py > example
```

`use-example.py` is an example demonstrating how the binary can be used
as a module.
