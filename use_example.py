#!/usr/bin/env python3

from sys import argv, path
path.insert(0, "example")

from demo_mod import loaded_fun
from demo_mod import mod_b
from demo_mod.inner.mod_a import inner_mod_fun

print("Script has been run as '{}'".format(argv[0]))

loaded_fun()

mod_b.mod_b_fun()

inner_mod_fun()
