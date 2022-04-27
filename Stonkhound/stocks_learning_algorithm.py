
import random
import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import GradientBoostingClassifier

from sklearn.metrics import accuracy_score

class ensemble_stonks:
    # Ensemble classifiers
    dt = DecisionTreeClassifier()
    mlp = MLPClassifier(random_state=0, max_iter=10000)
    svm = make_pipeline(StandardScaler(), SVC(gamma='auto'))
    reg = LinearRegression()
    logistic = LogisticRegression(solver='lbfgs', max_iter=1000, random_state=0)
    neigh = KNeighborsClassifier(n_neighbors=3)
    gnb = GaussianNB()
    p = Perceptron(tol=1e-3, random_state=0)
    bag = BaggingClassifier(base_estimator=SVC(), n_estimators=10, random_state=0)
    gbc = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)
    
    def fit(self, X, y):
        self.dt.fit(X,y)
        self.mlp.fit(X,y)
        self.svm.fit(X,y)
        self.reg.fit(X,y)
        self.logistic.fit(X,y)
        self.neigh .fit(X,y)
        self.gnb.fit(X,y)
        self.p.fit(X,y)
        self.bag.fit(X,y)
        self.gbc.fit(X,y)
    
    def predict(self, X_test):
        predictions = []
        voting = []
        # get predictions from 10 classification methods (8 classifiers, 1 bagging, 1 boosting)
        predictions.append(self.dt.predict(X_test))
        predictions.append(self.mlp.predict(X_test))
        predictions.append(self.svm.predict(X_test))
        predictions.append(self.reg.predict(X_test))
        predictions.append(self.logistic.predict(X_test))
        predictions.append(self.neigh.predict(X_test))
        predictions.append(self.gnb.predict(X_test))
        predictions.append(self.p.predict(X_test))
        predictions.append(self.bag.predict(X_test))
        predictions.append(self.gbc.predict(X_test))

        # predict through voting
        for i in range(len(X_test)):
            set_of_predictions = []
            for j in range(len(predictions)):
                set_of_predictions.append(predictions[j][i])
            voting.append(most_frequent(set_of_predictions))
        return voting

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
    
    return np.reshape(X_train, (-1, 8)), np.reshape(y_train, (-1, 1)).ravel(), np.reshape(X_test, (-1, 8)), np.reshape(y_test, (-1, 1))

def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
    return num