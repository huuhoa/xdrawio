
def encode_name(name):
    """
    encode_name encodes special characters to be xml-compatible entities
    """

    if name is None:
        return name

    return name.replace("&", "&amp;")


def encode_identity(name):
    import re
    pattern = re.compile('[^a-zA-Z]+')
    return re.sub(pattern, '', name)


def random_string(string_length=10):
    """Generate a random string of fixed length """
    import random
    import string

    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))
