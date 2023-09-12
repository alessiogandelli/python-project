import random
import string

def get_random_string(length):
    """
    This function returns a random string of length length.
    """
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return result_str