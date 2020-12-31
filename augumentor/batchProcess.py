import os
import random
from subprocess import call

# working dir is the dir containing class subdirs
def feedImages(workingDir,programPath):

    first_itr = True
    for dirpath, dirnames, files in os.walk(workingDir):
        if first_itr:
            first_itr = False
        else:
            for im_dirpath, im_dirnames, im_files in os.walk(dirpath):

                # we don't augument all the images in the class instead we only augument 3 >= images per class
                # so that classes are relatively balanced
                # if class has more tha 3 images then we we select 3 random images from the class
                if len(im_files) > 3 :
                    imagesToProcess = random.sample(im_files,3)
                    for image in imagesToProcess:
                        imagePath = dirpath + "/" + image
                        call(["python", programPath, imagePath])

                else:
                    for image in im_files:
                        imagePath = dirpath + "/" + image
                        call(["python", programPath, imagePath])


WorkingDir =  "/home/bhatakti-atama/PycharmProjects/internHack/trainSetStd(copy)"
ProgramPath = "/home/bhatakti-atama/PycharmProjects/augumentor/demo.py"

feedImages(WorkingDir, ProgramPath)