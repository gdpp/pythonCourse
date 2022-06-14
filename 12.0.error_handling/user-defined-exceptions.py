class NegativeNumbersError(Exception):
    """ One or more inputs are negatives """
    pass


def add_sum(a, b):
    try:
        if a <= 0 or b <= 0:
            raise NegativeNumbersError
    except NegativeNumbersError:
        return "Not valid!"

print(add_sum(-5, -2))