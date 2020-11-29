# imports
import os
from importlib import import_module
import imp
# Main execution

class Main:
    # Get module
    modName = input("Enter module: ")

    module = imp.load_source( modName, os.path.join('rules', modName + ".py"))
    modsplitFile = getattr( module, "splitFile")
    modFormatString = getattr( module, "formatString")

    # Get filename
    fileLoc = input("Enter complete full filename: ")

    # Get List of Strings
    dataList = modsplitFile(fileLoc)

    # Iterate over the list generated from the file
    count = 0
    for i in dataList:
        count += 1
        print("(" + str(count) + ")" + ": " + modFormatString(i))