import time
import json

startTime = time.time()
startImportTime = time.time()
outData = []

def startImport():
    """
    Call this function at the start of the import to start the timer.
    
    Returns:
        None
    
    """
    global startImportTime
    startImportTime = time.time()
    
def endImport(description):
    """
    Call this function at the end of the import to end the timer and print the time.
    
    Args:
        description (str): Description or name of the import.
    
    Returns:
        None
    
    """
    global endImportTime
    global outData
    outData.append({"description":description, "time": time.time() - startImportTime})
    print("Time to Import {0}: {1}".format(description,  time.time() - startImportTime))


def startTotal():
    """
    Call this function at the when you want to start the total timer.
    
    Returns:
        None
    
    """
    global startTime
    startTime = time.time()
    
def endTotal():
    """
    Call this function at the end of the import to end the timer and print the time.
    
    Args:
        description (str): Description or name of the import.
    
    Returns:
        None
    
    """
    global endImportTime
    global outData
    outData.append({"description":"total", "time": time.time() - startTime})
    print("Total time to Import: {0}".format( time.time() - startTime))

def saveCSV(filepath):
    """
    Save the data to a CSV file.
    
    Args:
        filepath (str): Path to the CSV file.
    
    Returns:
        None
    """
    global outData
    with open(filepath, 'w') as f:
        for item in outData:
            f.write("{0},{1}\n".format(item["description"], item["time"]))
            
def saveJSON(filepath):
    """
    Save the data to a JSON file.
    
    Args:
        filepath (str): Path to the JSON file.
    
    Returns:
        None
    """
    global outData
    open(filepath, 'w').write(json.dumps(outData, indent=4))
            

def debugImportTimes(modules = [], description = "modules"):
    """
    Debug the import times of the modules.
    
    Args:
        modules (list[str]): List of modules to import.
    
    Returns:
        None
        
    """
    outText = "import "
    for module in modules:
        outText += "{0} ".format(module)
        
    startImport()
    exec(outText)
    endImport(description)