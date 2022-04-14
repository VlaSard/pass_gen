import random
from string import ascii_letters, digits


def password_gen(length):
    chars = ascii_letters + digits
    pass_str = ' '
    for x in range(length):
        pass_str = pass_str + random.choice(chars)
    return pass_str


password_len = int(input('Длинна пароля '))
password = password_gen(password_len)
print(password)
