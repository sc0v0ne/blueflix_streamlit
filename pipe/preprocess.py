import os
import pandas as pd
import numpy as np


def clear_cols(x):

    x = (
        x
        .replace('&', ',')
        .replace('-', ',')
        .replace('tv shows', ',')
        .replace('movies', ',')
        .replace('/', ',')
        .replace('tv', ',')
        )
    return x


def transform_binary(x):
    if x > 1:
        return  1
    else:
        return x

def preprocess(input_dir):
    
    print('Initialize preprocess')
    print('-' * 80)

    PATTERN_PATH = os.path.join('/pipe', 'data')

    path_data = os.path.join(PATTERN_PATH,  input_dir)
    datasets_names = os.listdir(path_data)

    print('Data name: ', datasets_names)

    all_data = []
    for dir_ in datasets_names:
        path_file_csv = os.path.join(path_data, dir_)
        read_pd = pd.read_csv(path_file_csv)
        read_pd['channel_streaming'] = dir_.split('_')[0]
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
        print('Shape data: ', data.shape)

    data_titles = pd.concat(all_data, axis=0)

    data_titles['gender_type'] = data_titles['gender_type'].str.lower()

    data_titles['gender_type'] = data_titles['gender_type'].apply(lambda x: clear_cols(str(x)))

    df_split = data_titles['gender_type'].str.split(',', expand=True)

    df_split = df_split.fillna('-').drop(columns=[3,4, 5, 6, 7, 8, 9], axis=1)


    for x in df_split.columns:
        df_split[x] = df_split[x].apply(lambda i: i.strip())

    group_dummies = [df_split[d] for d in df_split.columns]

    for x in group_dummies:
        print('Type dummies', type(x))

    group_dummies = [pd.get_dummies(d, dtype='int') for d in group_dummies]
    
    print('Amount dummies:', len(group_dummies))

    A1 = group_dummies[0]
    A2 = group_dummies[1]
    A3 = group_dummies[2]
    
    AU  = list(A1.columns) + list(A2.columns)+ list(A3.columns)
    AU1 = list(set(AU))

    make_dataframe = {x: np.zeros(shape=(A1.shape[0],), dtype=int) for x in AU1}

    dataframe_make = pd.DataFrame(make_dataframe)
    
    for dummie in [A1, A2, A3]:
        for col in dummie.columns:
            dataframe_make[col] = list((dataframe_make[col] + dummie[col]).dropna())

    for col in dataframe_make.columns:
        dataframe_make[col] = dataframe_make[col].apply(lambda x: transform_binary(x))


    dataframe_make = dataframe_make.fillna(0).astype('uint8')
    
    dataframe_make.drop(columns=['-'], axis=1, inplace=True)
    
    data_titles['title'] = data_titles['title'].apply(lambda x: x.lower())

    OUTPUT= os.path.join(PATTERN_PATH, 'processed')
    if not os.path.exists(OUTPUT):
        os.mkdir(OUTPUT)
    
    path_data_titles = os.path.join(OUTPUT, 'data_titles_processed')
    data_titles.to_csv(f'{path_data_titles}.csv', index=False)
    print('Sucefully Data Titles')

    path_data_dummies = os.path.join(OUTPUT, 'train_gender')
    dataframe_make.to_csv(f'{path_data_dummies}.csv', index=False)
    print('Sucefully group_dummies')

    print('-' * 80)

