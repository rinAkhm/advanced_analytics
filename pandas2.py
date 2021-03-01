import pandas as pd 
import numpy as np

''' Хотим определить количество оценок по пользователяю с id = 2'''
ratings = pd.read_csv('ml-latest-small/ratings.csv')
movies = pd.read_csv('ml-latest-small/movies.csv')
rating = ratings[ratings['userId']==2].groupby('rating').count()[['userId']]
# print(rating.head())
# Входе решения получили, что пользователь с id = 2 ставит чаще всего оценку 4. 

''' Способ номер 2'''
# rating = ratings[ratings['userId']==2].ratings['rating'].value_counts()
# print(rating)


'''Делаем сводную таблицу 
столбцы это райтинги, строки это юзеры, ячйки это количество тех или иных оценок'''
rating = ratings.pivot_table(index = 'userId', columns = 'rating', values = 'movieId', aggfunc = 'count', 
                                fill_value = '-', margins = True)
# print(rating.tail())

''' Методы фильтрации таблиц при помощи loc'''
rez = ratings.loc[:, ['userId', 'rating']].head()

'''фильтрация по номеру строки'''
rez = ratings.iloc[:, [0,1,2]].head()

'''Добавления нового столбца'''
rez = ratings.loc [ratings.movieId == 1, 'NAME'] = 'Taxi 1'

''' Склеить 2 таблицы, добавить колонку с жанром Приключение, где содержится значение вывести помощи фильтра необходимые столбцы'''
merge_table = ratings.merge(movies, how = 'left', on = 'movieId')
merge_table['Adventure'] = merge_table.apply(lambda row: row.rating if 'Adventure' in row.genres else None, axis= 1).head(5)  
# print(merge_table.iloc[:, [0,5,6,7]].head())

''' Способ номер 2'''
columnAdd = ratings.merge(movies,how = 'left', on = 'movieId')
columnAdd['Adventure'] = columnAdd.loc [columnAdd.genres.str.contains('Adventure'), 'rating']
# print(columnAdd.head())

'''созадать dataframe и вывести не пустые значения'''
df = pd.DataFrame({'value' : [123, 11, None, np.NaN, np.nan, 345]})
# print(df.loc[~pd.isnull(df.value), :])

'''Заполнить пустые поля нулями'''
# print(df['value'].fillna(0))

'''перевести колонку datestamp в формат обычного числа'''
ratings['date'] = pd.to_datetime(ratings['timestamp'], unit='s')
# print(ratings.head())

ratings['date'] = pd.to_datetime(ratings['timestamp'], format='%Y-%m-%d')
print(ratings.head())


