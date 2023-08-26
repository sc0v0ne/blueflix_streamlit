from preprocess import preprocess
from clusters import pipeline_clusters
import sys
import os
if __name__ == '__main__':

    NAME_INPUT_DIR = sys.argv[1]

    preprocess(NAME_INPUT_DIR)
    
    PATH_PROCESSED = os.path.join('/preprocess/data')
    DATA_TRAIN = 'train_genger.csv'
    DATA_MOVIES_SERIES = 'data_titles_processed.csv'

    pipeline_clusters(PATH_PROCESSED, DATA_TRAIN, DATA_MOVIES_SERIES)