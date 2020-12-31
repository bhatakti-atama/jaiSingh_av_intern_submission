# JaiSingh AV Intern Submission

## Part 1

### Note I was not able to make a testing API in time. So there is no api to test with your own images currently. Please Do read through the document

### Approach 


I didn't have much knowldge of deep learning. I only knew machine learning only till regression. So I started to look for guides on the internet and I found the current dataset inadequate. Also refrencing hands on machine learning I knew the amount of data mattered more than than the nn architecture. So I decided to Drastically Increase the amount of data.

![Importance of Amount of Data](https://github.com/bhatakti-atama/jaiSingh_aw_intern_submission/blob/master/images/handsOn.png)

Also I found the classes to be very unbalanced. Which can be detterent according to this [article](https://towardsdatascience.com/deep-learning-unbalanced-training-data-solve-it-like-this-6c528e9efea6)

![Initial Unblanced Data](https://github.com/bhatakti-atama/jaiSingh_aw_intern_submission/blob/master/images/dataBalancePreAug.png)


### Increasing the amount of data using image augumentation

I chose to augument images based on landmark detection augumentation as it had the most significant according to [this reasearch paper](https://www.sciencedirect.com/science/article/abs/pii/S0925231216315016)

![](https://github.com/bhatakti-atama/jaiSingh_aw_intern_submission/blob/master/images/laFinding.png)


I decided on using [this](https://github.com/iacopomasi/face_specific_augm) augumentor 


### Results from augumentation 

Images in the datset increased from 4192 to 1.3 lakhs !!!!

Also the balance of classes improved

![](https://github.com/bhatakti-atama/jaiSingh_aw_intern_submission/blob/master/images/dbafter.png)

Average images per class increased from 3 to 136


### Training 

As facial features were already extracted in the augumented inages I decided to train and test on these images only


### Architecture of the Neural Network

I based (weight initialization ) my nn on effecientnetb0 as it gave the best performance compared to other nets in the same class

![](https://1.bp.blogspot.com/-oNSfIOzO8ko/XO3BtHnUx0I/AAAAAAAAEKk/rJ2tHovGkzsyZnCbwVad-Q3ZBnwQmCFsgCEwYBhgL/s1600/image3.png)

this is the model info :

Model: "sequential_14"

Layer (type)                 Output Shape              Param #   

efficientnet-b0 (Model)      (None, 5, 5, 1280)        4049564   

conv2d_11 (Conv2D)           (None, 3, 3, 32)          368672    

dropout_11 (Dropout)         (None, 3, 3, 32)          0         

global_max_pooling2d_11 (Glo (None, 32)                0         

dense_15 (Dense)             (None, 1013)              33429     

Total params: 4,451,665
Trainable params: 402,101
Non-trainable params: 4,049,564

### Result 

![](https://github.com/bhatakti-atama/jaiSingh_aw_intern_submission/blob/master/images/result.png)

Accuracy of the model is 64.7 percent although it could have improved a bit further with more epochs as graph of accuracy was still rising but I was contrained by my machine.

### How to run this code 

#### Intial Setup

- Dataset should be stored in directory which contains a a sub directory for each class 
- Names of all the claases should be of same lenght

#### Data formating

- Rename the images using datasrenameImages.py from the modelTraining directory
- make another copy of the dataset folder 
- Remove all images from the copy of dataset while maintaing the directory structure using command ``` find /some/dir -type f -exec rm {} + ```
- Augument the images using batchProcess.py in the augumentor Directory
- Move images to empty dataset folder using moveImages.py from the modelTraining Directory

#### Training
- Run the trainModel notebook to train the new dataset ( that you just created now ). Number of nosed in units in the dense layer should match number of classes


### Requirements to run the code 

#### To run modelTraining
- python 3.7
- tensorflow
- keras
- both running on gpu reccomended 
- Matplotlib

#### To run Augumentor
- python 2.7
- dlib 19.0
- opencv-python 3.1.00
- scikit-learn 0.20.4


### It's reccomended to use pycharm and create a virtual env for each



