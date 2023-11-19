import os
import joblib
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans


def init_train(data_train, all_data):
    
    print('-' * 80)
    print('Initialize Train')

    PATTERN_PATH = os.path.join('/pipe', 'data',)
    path_train = os.path.join(PATTERN_PATH, 'processed',  data_train)
    X_train = np.array(pd.read_csv(path_train))

    kmeans_model = KMeans(n_clusters=277, random_state=123456, n_init='auto')
    y_clusters = kmeans_model.fit_predict(X_train)
    print('-' * 80)
    print()
    print('Prepare new Dataframe')
    path_dataset = os.path.join(PATTERN_PATH, 'processed', all_data)
    dataset = pd.read_csv(path_dataset)
    dataset['clusters_gender'] = y_clusters
    print('-' * 80)
    print()
    print('Save outputs')
    OUTPUT= os.path.join(PATTERN_PATH, 'final')

    if not os.path.exists(OUTPUT):
        os.mkdir(OUTPUT)

    path_dataset = os.path.join(OUTPUT, 'dataset_titles_final')
    dataset.to_csv(f'{path_dataset}.csv', index=False)
    print('Sucefully data final')

    OUTPUT_MODEL = os.path.join(PATTERN_PATH, 'models')

    if not os.path.exists(OUTPUT_MODEL):
        os.mkdir(OUTPUT_MODEL)

    model_path = os.path.join(OUTPUT_MODEL, 'model_kmeans_20231119')
    joblib.dump(kmeans_model, f'{model_path}.pkl')
    print('Sucefully Model')
    print('-' * 80)
