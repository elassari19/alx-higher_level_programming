#!/usr/bin/python3
"""defin module"""


def append_after(filename="", search_string="", new_string=""):
    """fappend_after
    Args:
        filename: filename
        search_string: search_string
        new_string: new_string
    """
    with open(filename, "r") as f:
        file_content = f.readlines()

    with open(filename, "w") as fo:
        line_content = ""
        for file_line in file_content:
            line_content += file_line
            if search_string in file_line:
                line_content += new_string
        fo.write(line_content)
