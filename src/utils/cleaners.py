import re
import pandas as pd
import unicodedata


def fix_numerical(text: str):
    """
    Fixes numerical value in text so that it can be parsed by pandas

    Parameters
    ----------
    text : str

    """
    match = re.match(r"[0-9]+(,*.*[0-9][0-9]?)?", str(text))
    text = match[0].replace(" ", "")
    text = re.sub(r"\s+", "", text)
    text = re.sub(r",", ".", text)
    return text


def strip_accents(text):
    """
    Strips accents from text

    Parameters
    ----------
    text : str
        text to strip accents from

    """
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode(
        "utf8")
