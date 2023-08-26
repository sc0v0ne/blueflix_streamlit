def query_name_title(dataset, nome, top_n):
    new_search = nome.upper()
    movie = dataset[dataset['title'] == new_search][['clusters_genre_type']]
    reset_movie = movie.reset_index()
    reset_movie = reset_movie.at[0, 'clusters_genre_type']
    k_id = int(reset_movie)
    result = dataset[dataset['clusters_genre_type'] == k_id][['title', 'gender_type']][:int(top_n)]
    result.set_index('title')
    return result