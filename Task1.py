import random
import string

min_x = 0
max_x = 100

length = random.randint(min_x, max_x)
if length < 21:
    print("Довжина рядку недостатня для виконання операції зрізу. Спробуйте ще раз")
    exit()
line = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
mod_line = line[0:20:5]
print(mod_line)
