# imports
import os
from importlib import import_module
import imp
# Main execution

class Main:
    # Get module
    modName = input("Enter module: ")

    module = imp.load_source( modName, os.path.join('rules', modName + ".py"))
    modFormatString = getattr( module, "formatString")

    # Get filename
    fileLoc = input("Enter complete full filename: ")
    print("File: " + fileLoc)
    # Read the file
    with open (fileLoc, "r") as fileId:
        dataList = fileId.readlines()
    # Iterate over the list generated from the file
    count = 0
    for i in dataList:
        count += 1
        print("(" + str(count) + ")" + ": " + modFormatString(i))