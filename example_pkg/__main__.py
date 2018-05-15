"""
Main module.

This is the entrypoint for the module when loaded as an executable.
"""

from sys import argv
from demo_mod import loaded_fun
from demo_mod import mod_b
from demo_mod.inner.mod_a import inner_mod_fun

print("Binary has been run as '{}'".format(argv[0]))

loaded_fun()

mod_b.mod_b_fun()

inner_mod_fun()
