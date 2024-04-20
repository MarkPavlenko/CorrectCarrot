import random
import carrot

# Lines of code to display random numbers
def random_number_generator():
    number = random.randint(1, 1000)
    print(number)

def randomnumber():
    carrot.random_number_generator()

# Lines of code to display random letters
def random_letters_generator(length=1):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(letters) for _ in range(length))

def randomletters():
    carrot.random_letters_generator()