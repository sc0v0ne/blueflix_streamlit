import pandas as pd
from components.responses import response_markdown, response_recommends

def recommends(
                dataset:pd.DataFrame,
                name: str,
                top_n: int
                ) -> pd.DataFrame:
    rename = name.upper()
    exists_title = len(dataset[dataset['title'].str.contains(rename)])
    
    if exists_title == 0:
        return response_markdown('This title not exists')

    try:
        top_n = int(top_n)
    except Exception as e:
        print('Exception', e)
        return response_markdown('This is not number')

    new_search = name.upper()
    movie = dataset[dataset['title'] == new_search][['clusters_genre_type']]
    reset_movie = movie.reset_index()
    reset_movie = reset_movie.at[0, 'clusters_genre_type']
    k_id = int(reset_movie)
    result = dataset[dataset['clusters_genre_type'] == k_id][['title', 'gender_type']][:int(top_n)]
    result.set_index('title')

    return response_recommends(result)