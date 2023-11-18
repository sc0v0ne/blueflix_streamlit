import pandas as pd
from components.responses import response_markdown, response_recommends

def recommends(
                dataset:pd.DataFrame,
                name: str,
                top_n: int,
                extra_cols: dict,
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

    extra_cols = [x for x, y in extra_cols.items() if y]
    
    movie = dataset[dataset['title'] == rename][['clusters_genre_type']]
    reset_movie = movie.reset_index()
    reset_movie = reset_movie.at[0, 'clusters_genre_type']
    k_id = int(reset_movie)
    cols_review = ['title', 'gender_type'] + extra_cols
    result = dataset[dataset['clusters_genre_type'] == k_id][cols_review][:int(top_n)]
    result.set_index('title')

    return response_recommends(result)