"""
Initialisation module.

This is the entrypoint for the module when loaded as a library.
"""

from sys import argv

from .mod_b import mod_b_fun
from . import mod_b
from .inner.mod_a import inner_mod_fun

print("Module has been loaded as '{}'".format(__name__))

def loaded_fun():
    print("This function was loaded as '{}'".format(loaded_fun.__name__))

def main():
    print("Binary has been run as '{}'".format(argv[0]))
    loaded_fun()
    mod_b.mod_b_fun()
    inner_mod_fun()
