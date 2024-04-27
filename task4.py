# tesadufu sozleri secir

import random

with open("api.txt", "r") as f:
    lines = f.readlines()
random_line = random.choice(lines)
words = random_line.split()
random_word = random.choice(words)
print(random_word)
