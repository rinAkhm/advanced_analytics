import pandas as pd 


columns = ['user_id', 'movie_id','rating','timestamp']
ratings = pd.read_csv('ml-latest-small/ratings.csv', sep=',', header =None, names = columns)

movies = ['movie_id' , 'movie_title' , 'release date' , 'video release date' ,
                 'IMDb URL' , 'unknown' , 'Action' , 'Adventure' , 'Animation' ,
                 "Children's" , 'Comedy' , 'Crime' , 'Documentary' , 'Drama' , 'Fantasy' ,
                 'Film-Noir' , 'Horror' , 'Musical' , 'Mystery' , 'Romance' , 'Sci-Fi' ,
                 'Thriller' , 'War' , 'Western']
df_movie = pd.read_csv('ml-latest-small/movies.csv', sep=',', encoding= 'koi8_r', header=None, names= movies, ) 

#фильтруем таблицу с фильмами 
movie = df_movie[ ['movie_id', 'movie_title'] ] 

#соедниям таблицы 
rating_name = ratings.merge(movie, on ='movie_id', how = 'left')

#находим список уникальных фильмов с макс суммой значений рейтинга, далее выбираем индекс 0 строки с названием фильма  
film_name = rating_name['movie_title'].value_counts().index.values[0]

# по аналогии с прошлой строкой, но только выдаем значение 
max_ = rating_name['movie_title'].value_counts().values[0]

#результат
print(f'Название фильма {film_name} с наибольшим рейтингом {max_}')


data = pd.read_csv('files/power.csv', encoding = 'utf-8')
#смотрим слова которые закачиваются на 'ia'
country = data [ data['country'].str.contains('ia', case = False)] ['country'].unique()

# Запрос по городам Estonia, Latvia, Lithuania с категорией 4,12,21 в период 2005 по 2010. Почитать сумму столбца quantity
filtred_country = data.quantity [ ((data['country']=='Lithuania') | (data['country']=='Latvia') | (data['country']=='Estonia')) 
                            & ((data.category == 4) | (data.category ==12) | (data.category ==21)) 
                            & ((data['year'] >= 2005) & (data['year'] <= 2010)) & (data['quantity'] > 0) ].sum()
print(filtred_country)