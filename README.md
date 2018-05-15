# Python Packager

This tool packages a Python package structure into a single executable
and loadable file.

## Packaging

```bash
pypack path/to/package path/to/binary
```

## Executing

Any of the following will work for the package

```bash
/path/to/binary
python path/to/binary
```

## Including Modules

```python
# Add the binary package to the search path
import sys
sys.path.insert(0, 'path/to/binary')

# Import the module from within the package
import submodule_from_binary
```

## Directory Structure

The root directory must contain an `__init__.py` which is the entrypoint
into the package when it is loaded as package set. Only **submodules**
within the package can be loaded from the package by adding the package
file to `sys.path`.

The root directory can alternatively contain a `__main__.py` which is
the entrypoint into the package when it is executed as a binary. This
will not be loaded if the package is loaded as a module.

Both may be provided.

It is recommended that relative module imports are used to
cross-reference modules within the package. Relative imports will not
work up to the root of the package but only up to submodules within the
package. For this reason, it is recommended to have an empty
`__init__.py` in the root of the package along with a `__main__.py` to
execute the program and then place everything that should be accessible
as part of the library inside a submodule within the package which can
then be included.

## Example

Look at the `example_pkg` directory to see such a file structure. It can be
built into a module that can be run or imported with:

```bash
pypack example_pkg example
```

`use_example.py` is an example demonstrating how the binary can be used
as a module.

## Known Issues

When using the recommended directory structure, the module cannot be run
direclty with the `-m` option of `python3`. That is to say, from the
root of this repository, **all** of the following **will** work:

* `python -m example_pkg`
* `./pypack example_pkg example && ./example`
* `./pypack example_pkg example && python2 ./example`
* `./pypack example_pkg example && python3 ./example`
* `./pypack example_pkg example && python2 use-example.py`
* `./pypack example_pkg example && python3 use-example.py`

However, the following will not work:

* `python3 -m example_pkg`
