#!/usr/bin/env python3

import json
import yoga
import xdrawio.xutils
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader
from jinja2.utils import select_autoescape

config = yoga.Config.create()
config.use_web_defaults = True

def add_flex_direction(yn, node):
    if 'flex-direction' not in node:
        return
    fd = node['flex-direction']
    mapping = {
        'row': yoga.FlexDirection.Row,
        'column': yoga.FlexDirection.Column,
        'row-reverse': yoga.FlexDirection.RowReverse,
        'column-reverse': yoga.FlexDirection.ColumnReverse,
    }
    yn.flex_direction = mapping[fd]

def add_flex_wrap(yn, node):
    if 'flex-wrap' not in node:
        return
    fd = node['flex-wrap']
    mapping = {
        'nowrap': yoga.Wrap.NoWrap,
        'wrap': yoga.Wrap.Wrap,
        'wrap-reverse': yoga.Wrap.WrapReverse,
    }
    yn.flex_wrap = mapping[fd]

def add_width(yn, node):
    if 'width' not in node:
        return
    yn.width = node['width']

def add_height(yn, node):
    if 'height' not in node:
        return
    yn.height = node['height']

def add_max_width(yn, node):
    if 'max-width' not in node:
        return
    yn.max_width = node['max-width']

def add_padding(yn, node):
    if 'padding' not in node:
        return
    padding = node['padding']
    mapping = {
        'left': yoga.Edge.Left,
        'right': yoga.Edge.Right,
        'bottom': yoga.Edge.Bottom,
        'top': yoga.Edge.Top,
        'horizontal': yoga.Edge.Horizontal,
        'vertical': yoga.Edge.Vertical,
        'all': yoga.Edge.All,
    }
    for key, value in mapping.items():
        if key in padding:
            yn.set_padding(value, padding[key])

def add_margin(yn, node):
    if 'margin' not in node:
        return
    margin = node['margin']
    mapping = {
        'left': yoga.Edge.Left,
        'right': yoga.Edge.Right,
        'bottom': yoga.Edge.Bottom,
        'top': yoga.Edge.Top,
        'horizontal': yoga.Edge.Horizontal,
        'vertical': yoga.Edge.Vertical,
        'all': yoga.Edge.All,
    }
    for key, value in mapping.items():
        if key in margin:
            yn.set_margin(value, margin[key])

def add_align_items(yn, node):
    if 'align-items' not in node:
        return
    mapping = {
        'auto': yoga.Align.Auto,
        'flex-start': yoga.Align.FlexStart,
        'flex-end': yoga.Align.FlexEnd,
        'center': yoga.Align.Center,
        'stretch': yoga.Align.Stretch,
        'baseline': yoga.Align.Baseline,
        'space-between': yoga.Align.SpaceBetween,
        'space-around': yoga.Align.SpaceAround,
    }
    yn.align_items = mapping[node['align-items']]

def add_align_self(yn, node):
    if 'align-self' not in node:
        return
    mapping = {
        'auto': yoga.Align.Auto,
        'flex-start': yoga.Align.FlexStart,
        'flex-end': yoga.Align.FlexEnd,
        'center': yoga.Align.Center,
        'stretch': yoga.Align.Stretch,
        'baseline': yoga.Align.Baseline,
        'space-between': yoga.Align.SpaceBetween,
        'space-around': yoga.Align.SpaceAround,
    }
    yn.align_self = mapping[node['align-self']]

def add_justify_content(yn, node):
    if 'justify-content' not in node:
        return
    mapping = {
        'flex-start': yoga.Justify.FlexStart,
        'flex-end': yoga.Justify.FlexEnd,
        'center': yoga.Justify.Center,
        'space-between': yoga.Justify.SpaceBetween,
        'space-around': yoga.Justify.SpaceAround,
        'space-evenly': yoga.Justify.SpaceEvenly,
    }
    yn.justify_content = mapping[node['justify-content']]

def add_align_content(yn, node):
    if 'align-content' not in node:
        return
    mapping = {
        'auto': yoga.Align.Auto,
        'flex-start': yoga.Align.FlexStart,
        'flex-end': yoga.Align.FlexEnd,
        'center': yoga.Align.Center,
        'stretch': yoga.Align.Stretch,
        'baseline': yoga.Align.Baseline,
        'space-between': yoga.Align.SpaceBetween,
        'space-around': yoga.Align.SpaceAround,
    }
    yn.align_content = mapping[node['align-content']]

def create_node(node):
    yn = yoga.Node.create_with_config(config)
    yn.context = node
    operators = [
        add_flex_direction,
        add_flex_wrap,
        add_margin,
        add_padding,
        add_width,
        add_height,
        add_max_width,
        add_align_content,
        add_align_items,
        add_align_self,
        add_justify_content,

    ]

    for op in operators:
        op(yn, node)

    for index, child in enumerate(node.get('children', [])):
        yn.insert_child(create_node(child), index)

    return yn


def dump_node(root, indent=0):
    suffix = ''
    if root.child_count > 0:
        suffix = ', children: ['
    else:
        suffix = '}'
    ident_str = ''.join([' ' for i in range(indent*2)])
    print("%s{left: %d, top: %d, width: %d, height: %d%s" % (ident_str,
        root.calculated_left, root.calculated_top,
        root.calculated_width, root.calculated_height,
        suffix))

    for child in root.children:
        dump_node(child, indent+1)
    if root.child_count > 0:
        print(']}')

def flatten_tree(root, parent_id=''):
    result = []
    context = root.context
    if context is None:
        # print("None CONTEXT")
        value = "NONE"
        id = xdrawio.xutils.randomString()
        xclass = 'undefined'
    else:
        value = root.context.get('display_name', '')
        id = context['id']
        xclass = root.context.get('class', None)
        if xclass is None:
            xclass = root.context.get('type', '')
    
    result.append({
        'x': root.calculated_left,
        'y': root.calculated_top,
        'w': root.calculated_width,
        'h': root.calculated_height,
        'id': id,
        'parent_id': parent_id,
        'value': value,
        'class': xclass,
    })
    for child in root.children:
        children = flatten_tree(child, id)
        result = result + children

    return result

input = 'layout.json'
template_name = 'generic.tmpl'

with open(input, 'r') as fi:
    data = json.load(fi)


yn = create_node(data)
yn.calculate_layout()
# dump_node(yn)

all_items = flatten_tree(yn, '3')
# print(all_items)
# print(data)

env = Environment(
    loader=FileSystemLoader('./templates'),
    autoescape=select_autoescape(['html', 'xml']),
    trim_blocks = True,
    lstrip_blocks = True,
    line_statement_prefix='#',
)

template = env.get_template(template_name)

page_info = {
    'width': 9933,
    'height': 7016
}
configs = {}

print(template.render(
        items=all_items,
        configs=configs,
        page=page_info))