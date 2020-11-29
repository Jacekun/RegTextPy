# imports
import os
import imp

# Main execution
class Main:
    # Get module
    modName = input("Enter module: ")

    module = imp.load_source( modName, os.path.join('rules', modName + ".py"))
    modsplitFile = getattr( module, "splitFile")
    modFormatString = getattr( module, "formatString")

    # Get filename
    fileLoc = input("Enter filename (in the same folder): ")

    # Get List of Strings
    dataList = modsplitFile(fileLoc)

    # Open file for appending
    resFile = open(fileLoc + "_output.txt", "a")

    # Iterate over the list generated from the file
    count = 0
    countMax = len(dataList)
    result = ""

    for i in dataList:
        count += 1
        result = modFormatString(i)
        if result:
            resFile.write(result + "\n")

        print(str(count), " out of ", str(countMax), " done! Percentage: ", str((count/countMax)*100), "%")
    
    resFile.close()