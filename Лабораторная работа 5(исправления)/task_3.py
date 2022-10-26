import string
from random import sample


def get_random_password(length=8, digits=True, punctuation=True) -> str:
    chars = string.ascii_letters
    if digits:
        chars += string.digits
    if punctuation:
        chars += string.punctuation
    return ''.join(sample(chars, length))


print(get_random_password(30))
