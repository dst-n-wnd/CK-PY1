import string
from random import sample


def get_random_password(n=8) -> str:
    chars = f"{string.ascii_letters}{string.digits}{string.punctuation}"
    password = f"{''.join(sample(chars, n))}"
    return password


print(get_random_password(30))
