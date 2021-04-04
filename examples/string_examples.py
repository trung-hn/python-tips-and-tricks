import string


def not_in_s(s: str) -> set:
    """
    Return set of letters not in s

    Parameters:
    s (str): input only contains letters (both uppercase and lowercase)

    Returns:
    set: set of letters not in s
    """
    return set(string.ascii_letters) - set(s)


print(not_in_s(string.ascii_lowercase))

# Output:
# {'U', 'O', 'C', 'M', 'Y', 'A', 'T', 'Q', 'B', 'Z', 'W', 'E', 'F', 'D', 'P', 'X', 'J', 'K', 'V', 'H', 'N', 'G', 'L', 'R', 'S', 'I'}
