from .. import mod_b
from ..mod_a import mod_a_fun

def inner_mod_fun():
    mod_b.mod_b_fun()
    mod_a_fun()
    print("This function was loaded as '{}'".format(inner_mod_fun.__name__))

