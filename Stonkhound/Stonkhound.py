from format_data import *
from stocks_learning_algorithm import *
from sklearn.neural_network import MLPClassifier

def main():
    print("=========================================")
    print("         WELCOME TO STONKHOUND!")
    print("=========================================")

    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)

    avg = 0
    num_trials = 10000
    for i in range(num_trials):
        avg += run_diagnostics(clf, get_dataset())
    avg /= num_trials
    print("average accuracy: {} from {} trials".format(round(avg, 3), num_trials))

def run_diagnostics(clf, data):
    X_train, y_train, X_test, y_test = train_test_split(data, 0.9)
    clf.fit(X_train, y_train.ravel())
    return clf.score(X_test, y_test)

if __name__ == "__main__":
    main()