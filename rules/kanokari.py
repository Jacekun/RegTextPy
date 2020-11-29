import re

# Return List of strings
def splitFile(filename):
    # Read the file
    with open (filename, "r") as fileId:
        return fileId.readlines()

# Return string, formatted
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

    # Lowercase
    str = str.lower()

    # Remove double whitespaces
    while "  " in str:
        str = str.replace("  ", " ")

    # Trim
    str = str.strip()

    # If starts with 'chapter' or 'page'
    if str.startswith('chapter') or str.startswith('page'):
        str = "\n" + str + "\n"

    # Return str
    return str