# don't run twice on same directory causes sata loss !!!!
# important to run this before augumenting the images with augumentor
# this renames images according to to the class name ie.
# className_i where i is a number where 0 <= i < n where n is number of images in that class
# every image gets a unique name

import os



def renameImages(workingDir):

    first_itr = True
    for dirpath, dirnames, files in os.walk(workingDir):
        if first_itr:
            first_itr = False
        else:
            for im_dirpath, im_dirnames, im_files in os.walk(dirpath):
                j = 0
                for file in im_files :
                    oldPath = dirpath + "/" + file
                    folder = dirpath.replace(workingDir, "")
                    newPath = dirpath + "/" + folder + "_" + str(j) + ".jpg"
                    os.rename(oldPath,newPath)
                    print(newPath)
                    j += 1

WorkingDir = 'trainSetStd(copy)/'
print(" do you really want to run rename images on " + WorkingDir + "If run on the same dir twice it can cause data loss beware")
print("enter y to proceed esle enter enter anyting else to abort")
choice = input()
if choice == 'y':
    renameImages(workingDir= WorkingDir)
    print("renaming done")
else:
    print("aborted")