from xdrawio.xutils import encode_name
from xdrawio.xutils import transform_table_to_dict, transform_table_to_frame
from xdrawio.xutils import read_configuration_data, read_table_from_wb


def read_domain_data(wb):
    data = read_table_from_wb(wb, 'Teams', 'Teams')
    td = transform_table_to_dict(data)
    for k, v in td.items():
        v['Domain Name'] = encode_name(v['Domain Name'])
    return td


def read_group_data(wb):
    data = read_table_from_wb(wb, 'Teams', 'Groups')
    d = transform_table_to_dict(data)
    for k, v in d.items():
        v['Group Name'] = encode_name(v['Group Name'])

    return d


class Data(object):
    def __init__(self):
        super().__init__()
        self.domains = {}
        self.groups = {}
        self.workgroups = {}
        self.configurations = {}
        self.layoutspec = {}
        self.modules = []


def read_layout_specification(wb):
    def kv_transform(headers, columns):
        return columns[0], columns[1]

    data = read_table_from_wb(wb, 'Teams', 'LayoutSpecs')
    return transform_table_to_dict(data, kv_transform)


def read_workgroup_data(wb):
    data = read_table_from_wb(wb, 'Teams', 'WorkGroups')
    wgs = transform_table_to_dict(data)
    for k, v in wgs.items():
        members = v['Members']
        if members is None:
            members = ''
        v['Members'] = members.split(',')

    return wgs


def read_module_data(wb, workgroups):
    def module_transform(headers, columns):
        from xdrawio.arch.datatypes import Module

        mdl = Module(columns[2], columns[4], columns[6])
        mdl.team = columns[0]
        mdl.group = columns[1]
        mdl.wg_type = columns[3]
        mdl.sub_group = columns[5]
        mdl.wg_stype = "WGStyle%d" % (workgroups[mdl.wg_type]['Type'])
        return None, mdl

    data = read_table_from_wb(wb, 'Modules', 'Modules')
    mdls = transform_table_to_frame(data, module_transform)
    return mdls


def read_data(file_path):
    import openpyxl

    wb = openpyxl.load_workbook(file_path)

    d = Data()
    d.configurations = read_configuration_data(wb)
    d.domains = read_domain_data(wb)
    d.workgroups = read_workgroup_data(wb)
    d.groups = read_group_data(wb)
    d.layoutspec = read_layout_specification(wb)
    d.modules = read_module_data(wb, d.workgroups)

    return d
