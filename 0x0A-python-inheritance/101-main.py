#!/usr/bin/python3
"""defin class"""


add_attribute = __import__('101-add_attribute').add_attribute


class MyClass():
    """MyClass"""
    pass


mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name)

try:
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
