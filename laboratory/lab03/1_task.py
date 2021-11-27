# Вводим алфавит и ключ
word_to_encode = input("Введите фразу для шифрования: ").upper()
key_word = input("Введите ключ: ").upper()
# Растягиваем ключ на длину слова
if len(key_word) < len(word_to_encode):
    k = (len(word_to_encode) % len(key_word))
    key_word = '' + key_word * (len(word_to_encode) // len(key_word)) + key_word[:k]
# Формируем алфвавит и порядковый словарь
alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alp_dict = {letter: idx + 1 for idx, letter in enumerate(alphabet)}
print(alp_dict.keys())
# процесс кодировки
encoded_word = ''
for word_letter, key_letter in zip(word_to_encode, key_word):
    encoded_word += list(alp_dict.keys()) [(alp_dict[word_letter] + alp_dict[key_letter] % (len(alphabet)+1)) % (len(alphabet)+1)-1]
print("Зашифрованное сообщение: ", encoded_word)
# процесс декодировки
word_to_decode = input("Введите фразу для дешифрования: ").upper()
decoded_word = ''
for word_letter, key_letter in zip(word_to_decode, key_word):
    decoded_word += list(alp_dict.keys())[(alp_dict[word_letter] - alp_dict[key_letter] % (len(alphabet)+1)) % (len(alphabet)+1)-1]
print("Расшифрованное сообщение: ", decoded_word)