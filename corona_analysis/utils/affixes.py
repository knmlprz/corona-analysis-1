"""
This file is made to make changes quicker
"""


def remove_prefix(string, prefix):
    """
    Removes unwanted prefix from string
    :param string string to edit
    :param prefix patter for prefix
    """
    if prefix in string[:len(prefix)]:
        return string[len(prefix):]
    return string


def remove_suffix(string, suffix):
    """
    Removes unwanted suffix from string
    :param string string to edit
    :param suffix patter for suffix
    """
    if suffix in string[:len(suffix)]:
        return string[len(suffix):]
    return string
