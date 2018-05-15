from . import mod_a

def mod_b_fun():
    print("This function was loaded as '{}'".format(mod_b_fun.__name__))
    mod_a.mod_a_fun()
