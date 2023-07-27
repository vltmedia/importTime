import time
import json

startTime = time.time()
startImportTime = time.time()
endTime = time.time()
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
            

