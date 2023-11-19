import os
import pandas as pd
from components.responses import response_markdown, response_recommends
import joblib as jl
import streamlit as st

def recommends(
                dataset:pd.DataFrame,
                name: str,
                top_n: int,
                extra_cols: dict,
                ) -> st.dataframe:
    """Generate recommends

    Args:
        dataset (pd.DataFrame): Datatset input
        name (str):  name movie or tv show
        top_n (int):  number of recommendations for return
        extra_cols (dict):  Extra columns for return 

    Returns:
        st.dataframe: component st.dataframe
    """

    rename = name.lower()
    exists_title = len(dataset[dataset['title'].str.contains(rename)])
    
    if exists_title == 0:
        return response_markdown('This title not exists')

    try:
        top_n = int(top_n)
    except Exception as e:
        print('Exception', e)
        return response_markdown('This is not number')

    extra_cols = [x for x, y in extra_cols.items() if y]

    movie = dataset[dataset['title'] == rename][['clusters_gender']]
    reset_movie = movie.reset_index()
    reset_movie = reset_movie.at[0, 'clusters_gender']
    k_id = int(reset_movie)
    cols_view = ['title', 'gender_type'] + extra_cols
    result = dataset[dataset['clusters_gender'] == k_id][cols_view][:int(top_n)]
    result.set_index('title')

    return response_recommends(result)


def recommender_by_gender(
                        dataset: pd.DataFrame,
                        options: list,
                        cols: list
                        ) -> st.dataframe:
    """Generate recommends by genre

    Args:
        dataset (pd.DataFrame): Dataset input
        options (list): list genres
        cols (list): list names genres

    Returns:
        st.dataframe: component st.dataframe
    """

    if options == 0:
        return response_markdown('Empty')
    
    input_group = {x: [0] for x in cols}
    for x in options:
        input_group[x] = [1]
    y_input = pd.DataFrame(input_group)
    path_model =  os.path.join('./src/data', 'models', 'model_kmeans_20231118')
    model = jl.load(f'{path_model}.pkl')
    
    pred_test = model.predict(y_input)
    pred_test[0]
    
    result = dataset[dataset['clusters_gender'] == pred_test[0] ][['title', 'gender_type', 'channel_streaming']]
    result.set_index('title')
    
    return response_recommends(result)