import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')


def is_NumOrDot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))

def is_Valid_number (string: str):
    valid = False
    try: 
        float(string)
        valid = True

    except ValueError:
        print(f'"{string}" não é um número válido!')
        valid = False
    return valid


def is_Empty(string: str):
    return len(string) == 0

