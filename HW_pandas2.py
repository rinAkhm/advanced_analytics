from pymystem3 import Mystem
import pandas as pd 
import numpy as np

log = pd.read_csv('ml-latest-small/2/visit_log.csv', sep = ';')
log.loc[log.traffic_source.isin(['yandex', 'google']), 'traffic_type'] = 'organic'
log.loc[(log.traffic_source.isin(['paid', 'email'])) & (log.region == 'Russia'), 'traffic_type'] = 'ad'
log.loc[(log.traffic_source.isin(['paid', 'email'])) & (log.region != 'Russia'), 'traffic_type'] = 'other'
log.loc[(~log.traffic_source.isin(['yandex', 'google'])) & (~log.traffic_source.isin(['paid', 'email'])), 'traffic_type'] = log.traffic_source
# print(log['traffic_type'])
# print(log.head(30))

''' Спарсить ссылки по данным зная, что каждая ссылка начинается из 8 цифр и знака - '''
data = pd.read_csv('ml-latest-small/2/URLs.txt')
data = data[data.url.str.contains('[0-8]-')].head(20)
# print(data)


''' привести столбец keyword слова к единной форме и добавить в новую колонку'''
data = pd.DataFrame({
    'keyword': ['курс гривны к рублю', 'доллары в рубли', '100 долларов в рублях', 'курс рубля'],
    'shows': [125076, 114173, 97534, 53546],
})

def lemma(row):
    m = Mystem()   
    keyword = row['keyword']
    lem = m.lemmatize(keyword)
    return (''.join(lem)).strip()

data['lemmas']= data.apply(lemma, axis=1)
# print(data)

ratings = pd.read_csv('ml-latest-small/ratings.csv')
# переводим колонку timestamp читаемый вид
ratings['timestamp'] = pd.to_datetime(ratings['timestamp'], unit='s')
# создаем сводную таблицу и из неё вытаскиваем пользователей со значением ALL больше 100
users = list(ratings.pivot_table(index='userId', columns= 'rating', values= 'movieId', aggfunc = 'count', 
    fill_value= 0, margins=True).query('All > 100').index[:-1])
#пользователь user 1 просидел в среднем 8д и 13 часов
user1 =[1]
#фильтруем и таблицу по пользователям из списка. Далее группируем по пользователю и добавляем столбцы min и max 
data = ratings.loc[ratings.userId.isin(user1)].groupby(['userId'])['timestamp'].agg(['min', 'max']).reset_index()
#добавляем столбец с разницей 
data['user_life'] = data['max'] - data['min']
# print(data['user_life'].mean())


rzd = pd.DataFrame({
    'client_id': [111, 112, 113, 114, 115],
    'rzd_revenue' : [1093, 2810, 10283, 5774, 981]
})

auto = pd.DataFrame({
    'client_id': [113, 114, 115, 116, 117],
    'auto_revenue' : [57483, 83, 912, 4834, 98]
})

air = pd.DataFrame({
        'client_id': [115, 116, 117, 118],
        'air_revenue': [81, 4, 13, 173]
    })

client_base = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115, 116, 117, 118],
        'address': ['Комсомольская 4', 'Энтузиастов 8а', 'Левобережная 1а', 'Мира 14', 'ЗЖБИиДК 1', 
                    'Строителей 18', 'Панфиловская 33', 'Мастеркова 4']
        })

join_ = rzd.merge(auto, on = 'client_id', how='outer').merge(air, on = 'client_id', how='outer').fillna(0)
join_2 = client_base.merge(rzd, on = 'client_id', how='outer').merge(auto, on = 'client_id', how='outer').merge(air, on = 'client_id', how='outer').fillna(0)
print(join_2)