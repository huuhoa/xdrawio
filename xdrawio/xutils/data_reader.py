def read_table_from_wb(wb, sheet_name, table_name):
    ws = wb[sheet_name]
    for tbl in ws._tables:
        if tbl.name == table_name:
            return ws[tbl.ref]

    return None


def transform_func(headers, columns):
    return columns[0], {headers[i]: columns[i] for i in range(len(columns))}


def transform_table_to_frame(table, row_transform_func=transform_func):
    """ transform input (array of array) to output (array of dict) """
    d = []
    header = None
    for row in table:
        # Get a list of all columns in each row
        cols = []
        for col in row:
            cols.append(col.value)

        if header is None:
            header = cols
            continue

        _, item = row_transform_func(header,  cols)
        d.append(item)
    return d


def transform_table_to_dict(table, row_transform_func=transform_func):
    """ transform input (array of array) to output (dict of dict) """
    d = {}
    header = None
    for row in table:
        # Get a list of all columns in each row
        cols = []
        for col in row:
            cols.append(col.value)

        if header is None:
            header = cols
            continue

        key, item = row_transform_func(header, cols)
        d[key] = item
    return d


def read_configuration_data(wb):
    def config_transform(headers, columns):
        return columns[0], columns[1]

    data = read_table_from_wb(wb, 'Configuration', 'Configuration')
    cfg = transform_table_to_dict(data, config_transform)

    return cfg
