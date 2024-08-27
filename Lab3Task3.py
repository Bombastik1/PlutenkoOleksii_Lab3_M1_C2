import random
import string

min_x = 1
max_x = 20
words_length = random.randint(min_x, max_x)
finish_line = ''
max_line_length = 0

for i in range(words_length):
    letters_length = random.randint(min_x, max_x)
    line = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=letters_length))
    finish_line += line + " "
    if len(line) > max_line_length:
        max_line_length = len(line)

print(finish_line)
if max_line_length > 10:
    print("Найдовше слово речення містить більше 10 символів")
else:
    print("Найдовше слово речення не містить більше 10 символів")