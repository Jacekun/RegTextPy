import re

def formatString(str):
    # Get the string after the first occurence of 'target'
    try:
        target = ':'
        str = str[str.index(target) + len(target):]
    except:
        str = str
    
    # Remove some characters
    str = re.sub("[;,!?.~*\"]", " ", str)
    str = str.replace("[", " ")
    str = str.replace("]", " ")
    return str