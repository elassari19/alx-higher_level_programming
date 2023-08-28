#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    try:
        response = fct(*args)
    except BaseException as e:
        response = None
        print("Exception: {}".format(e), file=sys.stderr)
    finally:
        return response
