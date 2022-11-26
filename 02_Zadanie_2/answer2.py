import random


def get_random(number=3):
    numbers = []
    for sign in range(number):
        numbers.append(random.randint(1, 100))
    numbers.sort()
    print(numbers)


print(get_random(9))
