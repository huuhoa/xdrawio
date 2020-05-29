__version_info__ = (0, 4, 0)
__version__ = '.'.join([str(__value) for __value in __version_info__])
__copyright__ = '2020, NGUYEN Huu Hoa'
__license__ = 'MIT'

from .experiment import experiment


def _load_team(path):
    from xdrawio.features.layout import create_layout, layout_workgroup
    from xdrawio.features.datatypes import Page
    import xdrawio.features

    mdls, d = xdrawio.features.read_data(path)

    wgs_byteam = layout_workgroup(d.workgroups)

    page = Page()
    page.initialize(mdls, d, wgs_byteam)

    create_layout(page, wgs_byteam, d)
    # flat out
    all_items = page.flatten_tree()

    return 'corepayment.tmpl', all_items, d.configurations


def _load_bank_status(path):
    import xdrawio.bstatus

    data = xdrawio.bstatus.read_data(path)
    all_items = xdrawio.bstatus.flatten_data(data)
    return 'bank_status.tmpl', all_items, data.configurations


def _load_roadmap(path, init_config):
    import xdrawio.roadmap

    data = xdrawio.roadmap.read_data(path)
    data.configurations.update(init_config)
    all_items = xdrawio.roadmap.flatten_data(data)
    return 'roadmap.tmpl', all_items, data.configurations


def render(t, data_path, page_info):
    from jinja2 import Environment, FileSystemLoader, select_autoescape

    init_config = {}
    init_config.update(page_info)
    if t == 'features':
        template_name, items, configs = _load_team(data_path)

    if t == 'status':
        template_name, items, configs = _load_bank_status(data_path)

    if t == 'roadmap':
        template_name, items, configs = _load_roadmap(data_path, init_config)

    if init_config['debug']:
        return

    env = Environment(
        loader=FileSystemLoader('./templates'),
        autoescape=select_autoescape(['html', 'xml']),
        trim_blocks=True,
        lstrip_blocks=True,
        line_statement_prefix='#',
    )

    template = env.get_template(template_name)

    print(template.render(
        items=items,
        configs=configs,
        page=page_info))
