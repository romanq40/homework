file = open('text.txt','r', encoding="utf-8")
rr = file.read()
# print(rr)
file2 = rr.split('.')
# print(file2)
max_len = 0
for s in file2:
    if len(s) > max_len:
        max_text = s
        max_len = len(s)
print(max_text)

import re
word =input('Введите слово котрое хотите найти ')
print(re.findall(word, rr)) #писал слово 'вышла'

file_2 = open('text2.txt','w',encoding="utf-8")
text = ['это', 'начало', 'большого', 'рассказа']
for i in text:
    file_2.write(i+'\n')

filename = open("shopping_list.txt",'a',encoding="utf-8")

while True:
    print("\nВыберите действие:")
    print("1. Показать список покупок")
    print("2. Добавить пункт")
    print("3. Выход")
    choice = input("> ")
    if choice == "1":
        filename = open('shopping_list.txt','r', encoding="utf-8")
        print(filename.read())
    elif choice == "2":
        filename.write(input('Введите продукт')+'\n')
    elif choice == "3":
        break
    else:
        print("Некорректный выбор.")          

filename.close()
file_2.close()
file.close()