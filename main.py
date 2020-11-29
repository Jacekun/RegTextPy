# imports
import os
import imp

# define our clear function 
def clear(): 
  
    # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear')

# Main execution
class Main:

    # Open Log File
    logFile = open("AppLog.log", "a")

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
    outputFile = fileLoc + "_output.txt"
    resFile = open(outputFile, "a")

    # Log file name
    logFile.write("Original file: " + fileLoc + "\nOutput file: " + outputFile + "\n\n")

    # Iterate over the list generated from the file
    count = 0
    countMax = len(dataList)
    result = ""

    for i in dataList:
        count += 1
        result = modFormatString(i)
        if result:
            resFile.write(result + "\n")
            logFile.write("Index: " + str(count) + "\nOriginal: "+ i + "Result: " + result + "\n\n")

        clear()
        print(str(count), " out of ", str(countMax), " done! Percentage: ", str((count/countMax)*100), "%")
    
    # Close output file
    resFile.close()
    print("All done! Check file: ", outputFile, " | Located in the same folder")

    # Close Log file
    logFile.close()