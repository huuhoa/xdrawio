from xdrawio.arch.dataloader import Data
from xdrawio.arch.layout.stacklayout import FixLayout, GridLayout, Layout
from xdrawio.arch.layout.stacklayout import HStack, VStack
from xdrawio.arch.layout.layoutparser import parseLayoutSpec
from xdrawio.arch.datatypes import Domain, Group, Page
from typing import Dict
import xdrawio.arch.layout


def generate_layout_spec_level_0(d: Data, page: Page):
    # Step 1: layout spec for root
    spec = d.layoutspec.get("ROOT", None)
    if spec is not None:
        ls = parseLayoutSpec(spec)
    else:
        # default layout
        ls = HStack()
        for team in page.domains.values():
            ls.items.append(FixLayout(team.code, 0, 0))

    # Step 2: layout spec for team
    for team in page.domains.values():
        team_info = d.domains[team.code]
        # 2.1 layout spec for team, result a layout tree
        ltree = FixLayout(team.code, 0, 0)
        # 2.2 add team spec for layout tree
        ltree.add_attribute({
            'padding': {'top': 100, 'left': 10, 'bottom': 10, 'right': 10},
            'margin': {'all': 10},
            'min-width': 500,
            'min-height': 300,
            'display_name': team_info['Domain Name'],
            'class': 'domain',
            'style': d.configurations[team_info['Style']]
        })

        # 2.3 replace layout tree with team node in root
        replace_node(ls, team.code, ltree)

    return ls.dumps()


def replace_node(root: Layout, code: str, new_node: Layout):
    root.replace(code, new_node)

