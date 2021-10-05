import pandas as pd
from sklearn.model_selection import train_test_split
from src.utils import open_train_data, open_test_data
from src.featurescreation import FeaturesCreation


class MainWorkflow:

    def run(self):
        # Open train data and extract features
        raw_train = open_train_data()
        train = FeaturesCreation.add_features(raw_train)
        # Open test data and extract features
        raw_test = open_test_data()
        test = FeaturesCreation.add_features(raw_test)
        # Getting features and labels for data during training (train and validation)
        X, y = train.drop('pressure', axis=1), train['pressure']
        X_train, X_val, y_train, y_val = train_test_split(X, y, random_state=0)
        # Getting features and labels for test data
        X_test, y_test = test.drop('pressure', axis=1), test['pressure']
        return train, test


if __name__ == '__main__':
    MainWorkflow().run()