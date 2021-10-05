from pathlib import Path
import pandas as pd

test_path = Path('../data/test.csv')
train_path = Path('../data/train.csv')


def open_train_data():
    train_data = pd.read_csv(train_path, index_col=0)
    return train_data


def open_test_data():
    test_data = pd.read_csv(test_path, index_col=0)
    return test_data

