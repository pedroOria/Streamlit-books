# ESTE SERA EL ARCHIVO DONDE CREAREMOS EL MODELO PARA PREDECIR LOS LIBROS POR SU DESCRIPCION
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def get_recomendations(titulo: str):
    i = pd.read_csv('data_limpia.csv')
    tfidf = TfidfVectorizer(stop_words='english')
    i['descritpion'] = i["description"].fillna("")
    tfidf_matrix = tfidf.fit_transform(i['description'])
    coseno_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    indices = pd.Series(i.index, index=i['title'].str.lower()).drop_duplicates()
    idx = indices[titulo.lower()]
    simil = list(enumerate(coseno_sim[idx]))
    simil = sorted(simil, key=lambda x: x[1], reverse=True)
    simil = simil[1:11]
    movie_indices = [i[0] for i in simil]
    lista = i['title'].iloc[movie_indices].to_list()[:10]
    return {'lista recomendada': lista}

