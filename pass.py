#! /usr/bin/env python
# 
# генератор паролей
# использование: pass.py
# 

import random

# Список символов для пароля
chars = list('1234567890abcdefghijklmnopqrstuvyxwzABCDEFGHIJKLMNOPQRSTUVYXWZ')
# Начальное значения pasw
pasw = ''
# Запрос длинны пароля
length = int(input('Длинна парля '))

random.shuffle(chars) #Перемешиваем список символов для пароля

for x in range(length):
    pasw = pasw + random.choice(chars)

print(pasw)
