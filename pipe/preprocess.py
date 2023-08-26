import os
import sys

import pandas as pd


def preprocess(path_input):
    PATTERN_PATH = os.path.join('/preprocess', 'data')
    datasets_names = os.listdir(os.path.join(PATTERN_PATH, path_input))
    print('-' * 100)
    print('\nLog preprocess execution\n')
    print(datasets_names)

    all_data = []
    for dir in datasets_names:
        read_pd = pd.read_csv(os.path.join(PATTERN_PATH, path_input, dir))
        read_pd['channel_streaming'] = dir.split('_')[0]
        all_data.append(read_pd)

    try:
        for data in all_data:
            cols = {
                'date_added': 'date_added_platform',
                'duration': 'duration_seconds',
                'listed_in': 'gender_type',
                'type': 'movie_or_serie'
            }
            data.rename(columns=cols, inplace=True)
    except Exception as e:
        print(e)
        pass

    try:
        for data in all_data:
            data.drop(columns=['rating', 'show_id'], axis=1, inplace=True)
    except Exception as e:
        print(e)
        pass

    for data in all_data:
        data['cast'].fillna('uninformed cast', inplace=True)
        data['director'].fillna('uninformed director', inplace=True)
        data['country'].fillna('uninformed country', inplace=True)
        data['gender_type'].apply(lambda x: x.upper())

    for data in all_data:
        print(data.shape, flush=True)

    data_titles = pd.concat(all_data, axis=0)

    df_split = data_titles['gender_type'].str.split(',', expand=True)
    df_split = df_split.fillna('-')

    group_dummies = [
        pd.get_dummies(df_split[y].apply(lambda x: x.strip()), dtype='int')
        for y in df_split.columns
    ]

    group_dummies = pd.concat(group_dummies, axis=1)
    group_dummies = group_dummies.fillna(0).astype('uint8')

    data_titles['title'] = data_titles['title'].apply(lambda x: x.upper())
    
    OUTPUT= os.path.join(PATTERN_PATH, 'processed')
    if not os.path.exists(OUTPUT):
        os.mkdir(OUTPUT)
    
    data_titles.to_csv('/preprocess/data/processed/data_titles_processed.csv', index=False)
    print('Sucefully Data Titles')    
    group_dummies.to_csv('/preprocess/data/processed/train_genger.csv',
                         index=False)
    print('Sucefully train genger')
    print('-' * 100)   

