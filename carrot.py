import random
import carrot


def random_number_generator():
    number = random.randint(1, 1000)
    print(number)

def randomnumber():
    random_number_generator()


def randomletters(length=1):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(letters) for _ in range(length))
