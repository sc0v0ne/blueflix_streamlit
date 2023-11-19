import os
import joblib
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans


def init_train(path_input, data_train, all_data):
    
    print('Initialize Train')
    print('-' * 80)
    
    path_train = os.path.join(path_input, 'data', 'processed',  data_train)
    X_train = np.array(pd.read_csv(path_train))

    kmeans_model = KMeans(n_clusters=277, random_state=123456)
    y_clusters = kmeans_model.fit_predict(X_train)
    
    print('Prepare new Dataframe')
    path_dataset = os.path.join(path_input, 'data', 'processed', all_data)
    dataset = pd.read_csv(path_dataset)
    dataset['clusters_genre_type'] = y_clusters
    
    print('Save outputs')
    OUTPUT= os.path.join(path_input, 'data', 'final')
    
    if not os.path.exists(OUTPUT):
        os.mkdir(OUTPUT)

    path_dataset = os.path.join(OUTPUT, 'dataset_titles_final')
    dataset.to_csv(f'{path_dataset}.csv', index=False)
    print('Sucefully data final')

    
    OUTPUT_MODEL = os.path.join(path_input, 'data', 'models')

    if not os.path.exists(OUTPUT_MODEL):
        os.mkdir(OUTPUT_MODEL)

    model_path = os.path.join(OUTPUT_MODEL, 'model_kmeans_20231119')
    joblib.dump(kmeans_model, f'{model_path}.pkl')
