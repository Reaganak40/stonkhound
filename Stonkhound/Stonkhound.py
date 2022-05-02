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
    
    print("No sampling method:")
    run_diagnotics(trials = 10, sampling='normal')

    print("Oversampling:")
    run_diagnotics(trials = 10, sampling='oversampling')

    print("Undersampling:")
    run_diagnotics(trials = 10, sampling='undersampling')

    
def run_diagnotics(trials = 10, sampling = "normal"):
    accuracy = 0
    precision = 0
    recall = 0
    F1_Score = 0
    for i in range(trials):
        t_accuracy, t_precision, t_recall, t_F1_score = run_diagnostics_helper(sampling = sampling)
        accuracy += t_accuracy
        precision += t_precision
        recall += t_recall
        F1_Score += t_F1_score
    
    # divide by # of trials to get average of each metric
    accuracy /= trials
    precision /= trials
    recall /= trials
    F1_Score /= trials

    print("Avg accuracy of ensemble: {}".format(accuracy))
    print("Avg precision of ensemble: {}".format(precision))
    print("Avg recall of ensemble: {}".format(recall))
    print("Avg F1 Score of ensemble: {}\n".format(F1_Score))

# ======================================================================
# Function: run_diagnostics_helper
# Date Modified: 5/1/2022
# Details: Returns accuracy of clf on
# ======================================================================
def run_diagnostics_helper(sampling = "normal"):
    clf = ensemble_stonks()
    X_train, y_train, X_test, y_test = train_test_split(get_dataset(sampling=sampling), 0.9)

    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)

    tp = 0 # true positives
    fp = 0 # false positives
    tn = 0 # true negatives
    fn = 0 # false negatives

    for i in range(len(predictions)):
        if(y_test[i] == 1.0):
            if(y_test[i] == predictions[i]): # positive guessed positive
                tp += 1
            else:
                fn += 1 # positive guessed negative
        elif(y_test[i] == 0.0):
            if(y_test[i] == predictions[i]): # negative guessed negative
                tn += 1
            else:
                fp += 1 # negative guessed positive

    precision = (tp * 1.0) / (tp + fp)
    recall = (tp * 1.0) / (tp + fn)
    F1_Score = (2.0 * precision * recall) / (precision + recall)
    return accuracy_score(y_test, predictions), precision, recall, F1_Score
if __name__ == "__main__":
    main()