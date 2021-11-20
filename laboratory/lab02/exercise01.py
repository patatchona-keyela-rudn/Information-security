# Мы принимаем пароль и текст на шрифрование
password = str(input('Введите пароль:'))
my_word = ''.join(str(input('Введите фразу:')).split())

# Длина прямоугольника
n = len(password)
# Дополняем если нужно
if len(my_word)%n != 0:
    my_word += 'a'*(n-len(my_word) % n)

# Отсортируем буквуы пароля
password_sort = ''.join(sorted(password))
index_list = []
for i in range (len(password)):
    f_index = password.find(password_sort[i])
    index_list.append(f_index)

# Шифруем наш текст
new_word = ''
for i in index_list:
    for j in range(len(my_word)//n):
        new_word += my_word[j*n+i]

# Выводим отшифрованный текст
print("Шмфроанный текст: ",new_word)
