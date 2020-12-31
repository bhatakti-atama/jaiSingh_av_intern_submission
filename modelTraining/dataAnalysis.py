import os
import matplotlib.pyplot as plt


# working dir is the all the class dirs
# dir structure doens't matter if class dirs only contain images and no dirs
def averageImagesPerClass(workingDir):

    numberClasses = 0
    numberImages = 0

    for dirpath, dirnames, files in os.walk(workingDir):
        if len(files) != 0:
            numberImages += len(files)
            numberClasses += 1

    imagesPerClass = numberImages / numberClasses
    print("number of images " + str(numberImages))
    print("Average images per Class " + str(imagesPerClass))


def minMaxImgPerClass(workingDIr):

    min = None
    max = 1

    for dirpath, dirnames, files in os.walk(workingDIr):
        if len(files) != 0:
            if min == None :
                min = len(files)
            else:
                if min > len(files):
                    min = len(files)

            if max < len(files):
                max = len(files)
    print("Minimum number of images per class is " + str(min))
    print("Maximum number of images per class is " + str(max))

# Working dir must have have dirs inside for each class no intermediate folder structure for this function to work properly
def lenghtOfClassNames(workingDir):
    #intial values of min max taken from lenght of first class
    min = 12
    max = 12
    for dirpath, dirnames, files in os.walk(workingDir):
        if len(dirnames) != 0:
            for x in dirnames:
                if len(x) > max :
                    max = len(x)
                if len(x) < min :
                    min = len(x)
    print("max lenght of class names is " + str(max))
    print("min lenght of class names is " + str(min))


# dir structure doens't matter if class dirs only contain images and no sub dirs
def plotClassBalance(workingDir):
    distribution = []
    for dirpath, dirnames, files in os.walk(workingDir):
        if len(files) != 0:
            distribution.append(len(files))
    plt.hist(distribution, density= False, bins=10)
    plt.ylabel('occurences')
    plt.xlabel('size of class')
    plt.show()


WorkingDir = ""  # enter the path to workin dir

averageImagesPerClass(WorkingDir)
minMaxImgPerClass(WorkingDir)
lenghtOfClassNames(WorkingDir)
plotClassBalance(workingDir= WorkingDir)