from preprocess import preprocess
from clusters import init_train
import sys


if __name__ == '__main__':

    NAME_INPUT_DIR = sys.argv[1]

    preprocess(NAME_INPUT_DIR)

    DATA_TRAIN = 'train_gender.csv'
    DATA_MOVIES_SERIES = 'data_titles_processed.csv'

    init_train(DATA_TRAIN, DATA_MOVIES_SERIES)