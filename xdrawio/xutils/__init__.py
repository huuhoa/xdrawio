__version_info__ = (0,1,0)
__version__ = '.'.join([str(__value) for __value in __version_info__])
__copyright__ = '2020, NGUYEN Huu Hoa'
__license__ = 'MIT'


def read_configuration_data(wb):
    ws = wb["Configuration"]
    for tbl in ws._tables:
        if tbl.name == "Configuration":
            data = ws[tbl.ref]
            break

    cfg = {}
    header = None
    for row in data:
        # Get a list of all columns in each row
        cols = []
        for col in row:
            cols.append(col.value)

        if header is None:
            header = cols
        else:
            cfg[cols[0]] = cols[1]

    return cfg


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
