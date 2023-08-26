import os

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans


def pipeline_clusters(path_input, data_train, all_data):
    path_train = os.path.join(path_input, data_train)

    X_train = np.array(pd.read_csv(path_train))

    kmeans_model = KMeans(n_clusters=20, random_state=0)
    y_clusters = kmeans_model.fit_predict(X_train)

    path_dataset = os.path.join(path_input, all_data)
    dataset = pd.read_csv(path_dataset)
    dataset['clusters_genre_type'] = y_clusters

    dataset.to_csv('data/final/dataset_titles_final.csv', index=False)


