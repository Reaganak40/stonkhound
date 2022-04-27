
import random
import numpy as np

# ======================================================================
# Function: train_test_split
# Date Modified: 4/26/2022
# Details: Returns train and test data given a 2D dataset
# ======================================================================
def train_test_split(dataset, train_size):
    num_training = int(train_size * len(dataset))

    train = []
    test = []

    # Get random datapoints to put in training data
    for i in range(num_training):
        random_dp = random.randint(0, (len(dataset)-1))
        train.append(dataset.pop(random_dp))
    
    # Put unchosen datapoints in testing data
    for dp in dataset:
        test.append(dp)

    y_train_ = []
    y_test_ = []
    for i in range(len(train)):
        # removes the label from the features and puts in in y
        y_train_.append(train[i].pop(len(train[i])-1))

    for i in range(len(test)):
        # removes the label from the features and puts in in y
        y_test_.append(test[i].pop(len(test[i])-1))
    
    X_train = np.array(train)
    y_train = np.array(y_train_)
    X_test = np.array(test)
    y_test = np.array(y_test_)
    
    return np.reshape(X_train, (-1, 8)), np.reshape(y_train, (-1, 1)), np.reshape(X_test, (-1, 8)), np.reshape(y_test, (-1, 1))
