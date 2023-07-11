<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>

<hr>  

## **Objetivo:** crear una api consumible desde la web del dataset de peliculas
<hr>

## **Proceso**
## ETL: se hicieron las siguientes transformaciones
1) **Eliminación de columnas innecesarias:** video,imdb_id,adult,original_title,poster_path y homepage.
2) **Desanidado de las columnas:** belongs_to_collection y production_companies
3) **Reemplazar los valores nulos por 0 de los campos:** revenue y budget
4) **Eliminación de los valores nulos del campo:** release date
5) **Establecer el formato AAAA-MM-DD del campo:** release date
6) **Creación de nuevas columna:** release_year apartir de la extración del año de la columna release date y return apartir de la división de la columna revenue/budget (cuando no hay datos disponibles para calcularlo, deberá tomar el valor 0)

## EDA: se obtuvieron las siguientes conclusiones
1) los viernes son los dias donde mas peliculas se estrenaron
2) enero es el mes con mas peliculas estrenadas
3) el director de la pelicula esta relacionado con el retorno de inversion de la pelicula, buen indicio para análisis posteriores

## Machine learning:
- Se utilizo el algoritmo de similitud de coseno para recomendar peliculas parecidas basadas en el overview de las peliculas
- Se redujo el uso de memoria de este algoritmo obteniendo la matriz TF-IDF de una sola película a la vez y calculando la similitud del coseno solo para la película consultada y las 10 películas más similares

## Funciones creadas para la api:
1) **peliculas_idioma( Idioma: str ):** se ingresa un idioma en formato iso_639_1 y retorna la cantidad de peliculas producidas con ese idioma original
<br>**Ejemplo:** peliculas_idioma("ab") --> 32202 películas fueron estrenadas en idioma en (English)<br>
2) **peliculas_duracion( Pelicula: str ):** se ingresa el nombre de una pelicula y retorna la duración y año de estreno de la pelicula
<br>**Ejemplo:** peliculas_duracion("Toy Story") --> La pelicula Toy Story dura 81.0 min y se estreno el año 1995<br>
3) **franquicia( Franquicia: str ):** se ingresa el nombre de la franquicia y retorna la cantidad de peliculas, ganancia total y promedio de la franquicia
<br>**Ejemplo:** franquicia("Ace Ventura Collection") --> La franquicia Ace Ventura Collection posee 2 peliculas, una ganancia total de 319602929.0 y una ganancia promedio de 159801464.5<br>
4) **peliculas_pais( Pais: str ):** se ingresa el nombre de un pais y retorna la cantidad de peliculas producidas en ese pais
<br>**Ejemplo:** peliculas_pais("United States of America") --> Se produjeron 21176 películas en el país United States of America<br>
5) **productoras_exitosas( Productora: str ):** se ingresa el nombre de una productora y retorna el revenue total y cantidad de peliculas de esta productora
<br>**Ejemplo:** productoras_exitosas("20th Century Fox") --> La productora 20th Century Fox ha tenido un revenue total de 51523297.16666667 y realizo 29 peliculas<br>
6) **get_director( nombre_director ):** se ingresa el nombre de un director y retorna el retorno total del director, las peliculas que produjo y sus respectivos años, retorno, presupuesto e ingreso individual de cada pelicula
<br>**Ejemplo:** get_director("John Lasseter") --> {'director': 'John Lasseter', 'retorno_total_director': [21.00525680277778], 'peliculas': ['Toy Story', "A Bug's Life", 'Toy Story 2'], 'anio': [1995, 1998, 1999], 'retorno_pelicula': [12.4518011, 3.027157158333333, 5.526298544444445], 'budget_pelicula': [30000000.0, 120000000.0, 90000000.0], 'revenue_pelicula': [373554033.0, 363258859.0, 497366869.0]}<br>
7) **recomendacion( titulo ):** se ingresa el nombre de una pelicula y retorna una lista de 5 peliculas parecidas
<br>**Ejemplo:** recomendacion("The Dark Knight Rises") --> Lista recomendada: ['The Dark Knight', 'Batman Forever', 'Batman Returns', 'Batman: Under the Red Hood', 'Batman']<br>

## Deployment
https://deployment-pi-1-mlops.onrender.com/docs



