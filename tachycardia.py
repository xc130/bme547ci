import re


def is_tachycardic(string_in):
    if isinstance(string_in, str):
        string = string_in.lower()
    else:
        return False
    if re.search('tachycardic', string):
        return True
    else:
        return False
