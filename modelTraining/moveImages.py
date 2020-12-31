# program to copy images from augumentor's output folder to the the data folder
# first run renameImage.py else this would not work
# it finds the proper dir for the image through it's name

import os
from shutil import copyfile


def copyFiles(sourceDir, targetDir):

    firstItr = True
    for dirpath, driname, files in os.walk(sourceDir):

        if firstItr:
            firstItr= False
        else:
            for file in files:
                # class names have 12 characters verified by dataAnalysis.py
                targetSubDIr = file[0:12]
                source = dirpath + "/" + file
                target = targetDir + "/" + targetSubDIr + "/" + file
                copyfile(source,target)
                print("copied " + file)




SourceDir = "/home/bhatakti-atama/PycharmProjects/augumentor/output"
TargetDir = "trainSetStdTrialWork"
print("copying files form " + SourceDir + " to " + TargetDir )
print("Do you want to continue ? enter y to proceed anything else to abort")
choice = input()
if choice == 'y' :
    copyFiles(sourceDir=SourceDir, targetDir=TargetDir)
else:
    print("aborted")