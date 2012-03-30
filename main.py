import os

def getFileInfo(fileList): #Gets the file info from a list of file paths, returns a dictionary with this info
    fileInfo = {}
    for elem in fileList:
        stats = os.stat(elem)
        fileInfo[elem] = stats
    return fileInfo #Dictionary with {path:info}

def readFileData(fileDataPath): #Reads the information from the file data obj file into a dictionary and returns it
    oldDataFile = open(fileDataPath,'r')
    fileBackupList = oldDataFile.readlines()
    oldFileData = {}
    for elem in fileBackupList:
        newData = elem.rstrip('\n').split(' ')
        oldFileData[newData[0]] = float(newData[1])

    oldDataFile.close()
    return oldFileData

def writeFileData(fileDataPath, newFileData): #Makes a new file data log from the data taken from the new files
    newDataFile = open(fileDataPath,'w')
    for path,info in newFileData.items():
        newDataFile.write(path + ' ' + str(info.st_ctime) + '\n')
    newDataFile.close()
    return True

def compareInfo(compFileInfo, oldFileInfo): #Compares the info for each file with the info recorded in the backup changes file, determines whether or not to back it up, and returns a dictionary with this info, along with a dictionary containing files recorded in the backup changes file that are no longer in the source directory
    fileBackupList = {} #Dictionary containing info on whether or not a file needs to be re-backed up
    ghostFiles = [] #List containing files that can be removed because the source file no longer exists

    for path, info in compFileInfo.items():
        try:
            if info.st_ctime == oldFileInfo[path]: #Compares the dates edited
                fileBackupList[path] = False
            else:
                fileBackupList[path] = True
        except KeyError: #If the path wasn't in the old list
            fileBackupList[path] = True
    
    for path, info in oldFileInfo.items():
        try:
            compFileInfo[path]
        except KeyError: #If a file found is no longer there
            ghostFiles.append[path]    

    return (fileBackupList, ghostFiles)

fileInfo = getFileInfo(['/home/gladish2/Documents/USB-Backup/main.py'])
oldFileData = readFileData('filedata.obj')
backupDict = compareInfo(fileInfo, oldFileData)
writeFileData('filedata.obj',fileInfo)
print backupDict
