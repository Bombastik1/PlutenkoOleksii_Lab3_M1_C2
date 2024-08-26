import random
import string

def contains_numbers(l):
    return any(char.isdigit() for char in l)

min_x = 0
max_x = 5

length = random.randint(min_x, max_x)
line = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

print(line)

if contains_numbers(line):
    print("В цьому рядку є цифри")
else:
    print("В цьому рядку цифри відсутні")