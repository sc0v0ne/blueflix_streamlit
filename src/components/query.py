def query_name_title(dataset, nome, top_n):
    nome_pesquisa = nome.upper()
    # Recebe o valor da id K-Classes
    filme = dataset[dataset['title'] == nome_pesquisa][['clusters_genre_type']]
    # resetar o index, como possui apenas um linha, acessar mais rápido
    reseta_filme = filme.reset_index()
    # Adicionar a célula da K-Classes, a uma variável
    resetado_filme = reseta_filme.at[0, 'clusters_genre_type']
    # Transforma variável string em inteiro
    k_id = int(resetado_filme)
    # Procura filmes com semelhança usando a k-id = K-Classes
    recomendacoes = dataset[dataset['clusters_genre_type'] == k_id][['title', 'gender_type']][:int(top_n)]
    recomendacoes.set_index('title')
    return recomendacoes