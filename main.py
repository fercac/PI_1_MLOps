from fastapi import FastAPI
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

app = FastAPI()

@app.get("/cantidad_peliculas_idioma/{Idioma}")
def peliculas_idioma( Idioma: str ): 
    #Se ingresa un idioma (como están escritos en el dataset, no hay que traducirlos!). Debe devolver la cantidad de películas producidas en ese idioma.
    df = pd.read_csv("Dataset_generados/idiomas.csv")     
    cantidad = df.loc[df.original_language == Idioma]
    cantidad = cantidad.cantidad_peliculas.to_list()
    
    return f"{cantidad[0]} películas fueron estrenadas en idioma {Idioma}"

@app.get("/cantidad_peliculas_duracion/{Pelicula}")
def peliculas_duracion( Pelicula: str ):
    #Se ingresa una pelicula. Debe devolver la la duracion y el año.
    df = pd.read_csv("Dataset_generados/duracion.csv") 
    titulo = df.loc[df.title == Pelicula]
    duracion = titulo.runtime.to_list()
    año = titulo.release_year.to_list()

    return f"La pelicula {Pelicula} dura {duracion[0]} min y se estreno el año {año[0]}"

@app.get("/cantidad_franquicia/{Franquicia}")
def franquicia( Franquicia: str ):
    #Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio
    df = pd.read_csv("Dataset_generados/franquicia.csv")
    franquicia_ingresada = df.loc[df.belongs_to_collection == Franquicia]
    cantidad = franquicia_ingresada.cantidad_peliculas.to_list()
    ganancia_total = franquicia_ingresada.ganancia_total.to_list()
    ganancia_promedio = franquicia_ingresada.promedio_ganancia.to_list()
                    
    return f"La franquicia {Franquicia} posee {cantidad[0]} peliculas, una ganancia total de {ganancia_total[0]} y una ganancia promedio de {ganancia_promedio[0]}"

@app.get("/cantidad_peliculas_pais/{Pais}")
def peliculas_pais( Pais: str ): 
    #Se ingresa un país (como están escritos en el dataset, no hay que traducirlos!), retornando la cantidad de peliculas producidas en el mismo.
    df = pd.read_csv("Dataset_generados/pais.csv")
    pais_ingresado = df.loc[df.pais == Pais]
    cantidad_peliculas = pais_ingresado.cantidad_peliculas.to_list()

    return f"Se produjeron {cantidad_peliculas[0]} películas en el país {Pais}"

@app.get("/productora_revenue_cantidad/{Productora}")
def productoras_exitosas( Productora: str ):
    #Se ingresa la productora, entregandote el revunue total y la cantidad de peliculas que realizo.
    df = pd.read_csv("Dataset_generados/productoras.csv")
    productora_ingresada = df.loc[df.production_companies == Productora]
    revenue = productora_ingresada.revenue.to_list()
    cantidad_peliculas = productora_ingresada.cantidad_peliculas.to_list()
    
    return f"La productora {Productora} ha tenido un revenue total de {revenue[0]} y realizo {cantidad_peliculas[0]} peliculas"

@app.get("/get_director/{nombre_director}")
def get_director( nombre_director ):
    #Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno.
    #Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma, en formato lista.
    df1 = pd.read_csv("Dataset_generados/director_1.csv")
    df2 = pd.read_csv("Dataset_generados/director_2.csv")
    director_buscado = df1.loc[df1.director == nombre_director]
    r = director_buscado["return_total"].to_list()

    director_buscado_2 = df2[(df2["crew"]== nombre_director) & (df2["return"].notnull())]
    g = director_buscado_2["title"].to_list()
    a = director_buscado_2["release_year"].to_list()
    rr = director_buscado_2["return"].to_list()
    bd = director_buscado_2["budget"].to_list()
    rv = director_buscado_2["revenue"].to_list()
    return {"director":nombre_director, "retorno_total_director":r, "peliculas":g, "anio":a,
            "retorno_pelicula": rr, "budget_pelicula":bd, "revenue_pelicula":rv}

@app.get("/recomendacion/{titulo}")
def recomendacion(titulo):
    """Ingresas un nombre de pelicula y te recomnienda las similares en una lista"""
    i = pd.read_csv("Dataset_generados/titulos.csv")
    tfidf = TfidfVectorizer(stop_words="english")
    i["overview"] = i["overview"].fillna("")

    tfidf_matriz = tfidf.fit_transform(i["overview"])
    coseno_sim = linear_kernel(tfidf_matriz, tfidf_matriz)

    indices = pd.Series(i.index, index=i["title"]).drop_duplicates()
    idx = indices[titulo]
    simil = list(enumerate(coseno_sim[idx]))
    simil = sorted(simil, key=lambda x: x[1], reverse=True)
    simil = simil[1:11]
    movie_index = [i[0] for i in simil]

    lista = i["title"].iloc[movie_index].to_list()[:5]
    
    return f"Lista recomendada: {lista}"