slovar = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
password = str(input('Введите пароль: ')).lower()
word = str(input('Введите фразу для шифрования: ')).lower()
k = (len(word) % len(password)) # Количество символов которые нужно дополнить
password_len = '' + password * (len(word) // len(password)) + password[:k]
print(word, password_len, sep='\n')
slovar_visinera = []
slovar_i = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
for i in range(len(slovar)):
    slovar_visinera.append(slovar_i)
    new = slovar_i[1:] + slovar_i[0]
    slovar_i = new
print("Квадрат вижинера:", slovar_visinera)
message = ''
for i in range(len(word)):
    f_index1 = slovar.find(word[i])
    f_index2 = slovar.find(password_len[i])
    message += slovar_visinera[f_index1][f_index2]
print(f'Защифрованное сообщение: {message}')
