import numpy as np
import random
from numpy import linalg



def reverse_arr(num):
    '''func can revese can doing array list'''
    return np.arange(num-1, 0, -1)

rez = reverse_arr(10)
# print(rez)


def create_diagonal_matrix(num):
    ''' Создает диоганальную матрицу размеоности N со значениями от N до 0'''
    return np.diag(np.arange(num-1, 0, -1), k=0)

rez = create_diagonal_matrix(10)
#подсчет значений диагонали
line = 0 
for i, k in enumerate(rez):
    line+=k[i]
# print(line)


'''
example
4x + 2y + z = 4
x + 3y = 12
5y + 4z = -3'''

left = np.array([[4,2,1],[1,3,0],[0,5,4]])
right = np.array([4,12,-3])

rez = linalg.solve(left, right)
answer = np.allclose(np.dot(left,rez),right)
# print(rez, answer)


def calc_cos(a,b):
    ''' подсчет косинуса угла между векторами'''
    aLength = np.linalg.norm(a)
    bLength = np.linalg.norm(b)

    return np.dot(a,b) / (aLength*bLength)

users_stats = np.array(
    [
        [2, 1, 0, 0, 0, 0],
        [1, 1, 2, 1, 0, 0],
        [2, 0, 1, 0, 0, 0],
        [1, 1, 2, 1, 0, 1],
        [0, 0, 1, 2, 0, 0],
        [0, 0, 0, 0, 0, 5],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 3],
        [1, 0, 0, 2, 1, 4]
    ], 
    np.int32
)

new_user_stats = np.array([0,1,2,0,0,0])
list_solution  = {}
for i, line in enumerate(users_stats):
    like_user  = calc_cos(line, new_user_stats)
    list_solution[i+1] = like_user

rez = max(list_solution.items(), key = lambda x:x[1])
print(f'similar buyer is user{rez[0]}')

