import random
import my_module
random_int = random.randint(1, 10)
random_float = random.random() * 5

print(random_int)
print(random_float)
print(my_module.name)

love_score = random.randint(1, 100)

print(f"Your Love score is {love_score}")