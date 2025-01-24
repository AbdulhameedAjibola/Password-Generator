import random
import string


def generatePass():
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    num = string.digits
    symbols = string.punctuation

    all_characters = upper + lower + num + symbols

    password = random.choices(all_characters, k=random.randint(16, 20))

    random.shuffle(password)

    return "".join(password)


