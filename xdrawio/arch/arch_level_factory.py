from xdrawio.arch.dataloader import read_data
from xdrawio.arch.datatypes import Page
from xdrawio.arch.layout import layout_workgroup

from .arch_level0 import generate_layout_spec_level_0
from .arch_level1 import generate_layout_spec_level_1
from .arch_level2 import generate_layout_spec_level_2
from .arch_level3 import generate_layout_spec_level_3


def generate_layout_spec(path: str, level: int):
    mapping = {
        0: generate_layout_spec_level_0,
        1: generate_layout_spec_level_1,
        2: generate_layout_spec_level_2,
        3: generate_layout_spec_level_3,
    }

    d = read_data(path)

    wgs_byteam = layout_workgroup(d.workgroups)

    page = Page()
    page.initialize(d, wgs_byteam)

    return mapping[level](d, page)
