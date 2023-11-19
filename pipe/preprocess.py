import os
import pandas as pd


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

    df_split = data_titles['gender_type'].str.split(',', expand=True)

    df_split = df_split.fillna('-')

    for x in df_split.columns:
        df_split[x] = df_split[x].apply(lambda i: i.strip())

    group_dummies = [df_split[d] for d in df_split.columns]

    for x in group_dummies:
        print('Type dummies', type(x))

    group_dummies = [pd.get_dummies(d, dtype='int') for d in group_dummies]
    
    print('Amount dummies:', len(group_dummies))
    
    group_dummies = pd.concat(group_dummies, axis=1)
    
    group_dummies = group_dummies.fillna(0).astype('uint8')
    
    group_dummies.drop(columns=['-'], axis=1, inplace=True)
    
    data_titles['title'] = data_titles['title'].apply(lambda x: x.lower())

    OUTPUT= os.path.join(PATTERN_PATH, 'processed')
    if not os.path.exists(OUTPUT):
        os.mkdir(OUTPUT)
    
    path_data_titles = os.path.join(OUTPUT, 'data_titles_processed')
    data_titles.to_csv(f'{path_data_titles}.csv', index=False)
    print('Sucefully Data Titles')

    path_data_dummies = os.path.join(OUTPUT, 'train_gender')
    group_dummies.to_csv(f'{path_data_dummies}.csv', index=False)
    print('Sucefully group_dummies')

    print('-' * 80)

