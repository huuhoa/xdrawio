
def encode_name(name):
    '''
    encode_name does encode special characters to be xml-compatible entities
    '''

    if name is None:
        return name

    return name.replace("&", "&amp;")


def encode_identity(name):
    import re
    pattern = re.compile('[^a-zA-Z]+')
    return re.sub(pattern, '', name)


def randomString(stringLength=10):
    import random
    import string

    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
