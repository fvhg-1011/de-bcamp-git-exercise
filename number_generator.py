import random

random_number = random.randint(1, 6)


def squared_number(x):
    return x**2


squared_random_number = squared_number(random_number)
print(squared_random_number)
