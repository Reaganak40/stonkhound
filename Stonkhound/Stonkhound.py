# ======================================================================
# Stonkhound (Cpts 437 Term Project)
# Coded By: Reagan Kelley
# Last Modified: 4/26/2022
#
# This code takes in historical stock data to learn and predict stock
# growth. This was done by means of classification via nueral networks
# ======================================================================
from format_data import *
from stocks_learning_algorithm import *


# ======================================================================
# Function: Main
# Date Modified: 4/26/2022
# Details: Execution function for Stonkhound
# ======================================================================
def main():
    print("=========================================")
    print("         WELCOME TO STONKHOUND!")
    print("=========================================")

    # clf = ensemble_stonks()
    # X_train, y_train, X_test, y_test = train_test_split(get_dataset(), 0.9)
    # clf.fit(X_train, y_train)
    # predictions = clf.predict(X_test)
    # print(accuracy_score(y_test, predictions))

    avg = 0
    trials = 100
    for i in range(trials):
        avg += run_diagnostics()
    avg /= trials
    print("Avg accuracy of ensemble: {}".format(avg))

    dataset = get_dataset()
    n_1 = 0
    n_0 = 0
    for dp in dataset:
        if(dp[-1] == 1.0):
            n_1 += 1
        elif(dp[-1] == 0.0):
            n_0 += 1
        else:
            print("faulty data!")
    print("n1 = {}, n0 = {}".format(n_1, n_0))
    print("percentage of postive values: {}".format(n_1/(n_1 + n_0)))
    

# ======================================================================
# Function: run_diagnostics
# Date Modified: 4/26/2022
# Details: Returns accuracy of clf on
# ======================================================================
def run_diagnostics():
    clf = ensemble_stonks()
    X_train, y_train, X_test, y_test = train_test_split(get_dataset(), 0.9)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    return accuracy_score(y_test, predictions)

if __name__ == "__main__":
    main()