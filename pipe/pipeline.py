from preprocess import preprocess
from clusters import init_train
import sys
import os
if __name__ == '__main__':

    NAME_INPUT_DIR = sys.argv[1]

    preprocess(NAME_INPUT_DIR)
    
    PATH_PROCESSED = os.path.join('/preprocess')
    DATA_TRAIN = 'train_gender.csv'
    DATA_MOVIES_SERIES = 'data_titles_processed.csv'

    init_train(PATH_PROCESSED, DATA_TRAIN, DATA_MOVIES_SERIES)