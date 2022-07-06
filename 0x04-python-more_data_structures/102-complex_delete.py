#!/usr/bin/python3
# 102-complex_delete.py
# Linet Muchunu <linetnyambura27@gmail.com>


def complex_delete(a_dictionary, value):
    """Delete keys with a specific value in a dictionary."""
    while value in a_dictionary.values():
        for k, v in a_dictionary.items():
            if v == value:
                del a_dictionary[k]
                break

    return (a_dictionary)
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
