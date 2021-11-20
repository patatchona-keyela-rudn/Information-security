import numpy as np
import random

my_word = ''.join(str(input('Введите фразу:')).split())
# делаем k целым
while (len(my_word) / 4) ** 0.5 % 1 != 0:
    my_word = my_word + 'a'
k = int((len(my_word) / 4) ** 0.5)
print(my_word)
print('k = ', k)

matrix_1 = np.reshape(np.arange(1, k ** 2 + 1), (k, k))
matrix_2 = np.rot90(matrix_1, -1)
matrix_4 = np.rot90(matrix_2, -1)
matrix_3 = np.rot90(matrix_4, -1)
mat_1 = np.concatenate((matrix_1, matrix_2), axis=1)
mat_2 = np.concatenate((matrix_3, matrix_4), axis=1)
mat = np.concatenate((mat_1, mat_2), axis=0)
print(mat)

str_mat = mat.astype('|S1').tobytes().decode('utf-8')
dic = {}
for i in range(1, k ** 2 + 1):
    index = []
    for j in range(len(str_mat)):
        if str(i) == str_mat[j]:
            index.append(j)
    dic[i] = index
print(dic)

chouse_pos = []
for i in dic:
    value = dic[i]
    chouse_val = random.choice(value)
    i_index = chouse_val // (k * 2)
    j_index = chouse_val % (k * 2)
    chouse_pos.append([i_index, j_index])
print(chouse_pos)

key_matrix = np.zeros((2 * k, 2 * k), dtype=int)
val = 1
for i, j in chouse_pos:
    key_matrix[i][j] = val
    val += 1
print(key_matrix)

matrix_end = np.copy(key_matrix)
for i in range(3):
    key_matrix = np.rot90(key_matrix, -1)
    for j in range(2 * k):
        for q in range(2 * k):
            if key_matrix[j][q] != 0:
                key_matrix[j][q] += k ** 2
    print(f'после {i} шага')
    matrix_end = matrix_end + key_matrix
    print(matrix_end)
while True:
    password = str(input(f'Введите пароль длиной {2 * k}: '))
    if len(password) == 2 * k:
        break
    else:
        print('Не выполнены условия ввода пароля')
password_sort = ''.join(sorted(password))

index_list = []
for i in range (len(password)):
    f_index = password.find(password_sort[i])
    index_list.append(f_index)

new_word = []
for i in index_list:
    for j in range(matrix_end.shape[0]):
        new_word.append(matrix_end[j][i])
print(new_word)

kod_word = ''
for i in range(len(new_word)):
    kod_word += my_word[new_word[i]-1]
print(kod_word)
