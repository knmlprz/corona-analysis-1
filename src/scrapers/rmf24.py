import json
import pandas as pd
import os
import re
from bs4 import BeautifulSoup as bs
from urllib import request

url = "https://www.rmf.fm/inc/outer/korona-wykres/wykres.html"


def remove_prefix(string, prefix):
    """
    Removes unwanted prefix from string
    :param string string to edit
    :param prefix patter for prefix
    """
    if prefix in string[:len(prefix)]:
        return string[len(prefix):]
    else:
        return string


def remove_suffix(string, suffix):
    """
    Removes unwanted suffix from string
    :param string string to edit
    :param suffix patter for suffix
    """
    if suffix in string[:len(suffix)]:
        return string[len(suffix):]
    else:
        return string

