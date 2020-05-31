import json
import yoga
import xdrawio.xutils
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader
from jinja2.utils import select_autoescape
import argparse
import sys

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


def add_flex(yn, node):
    if 'flex' not in node:
        return
    yn.set_flex(node['flex'])


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


def add_max_height(yn, node):
    if 'max-height' not in node:
        return
    yn.max_height = node['max-height']


def add_min_width(yn, node):
    if 'min-width' not in node:
        return
    yn.min_width = node['min-width']


def add_min_height(yn, node):
    if 'min-height' not in node:
        return
    yn.min_height = node['min-height']


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
        add_flex,
        add_flex_direction,
        add_flex_wrap,
        add_margin,
        add_padding,
        add_width,
        add_height,
        add_max_width,
        add_max_height,
        add_min_width,
        add_min_height,
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


def flatten_tree(root, parent_id=''):
    result = []
    context = root.context
    if context is None:
        # print("None CONTEXT")
        value = "NONE"
        id = xdrawio.xutils.random_string()
        xclass = 'undefined'
        style = None
        extra = None
    else:
        value = root.context.get('display_name', '')
        id = context['id']
        xclass = root.context.get('class', None)
        if xclass is None:
            xclass = root.context.get('type', '')
        style = root.context.get('style', None)
        extra = root.context.get('extra', None)

    result.append({
        'x': root.calculated_left,
        'y': root.calculated_top,
        'w': root.calculated_width,
        'h': root.calculated_height,
        'id': id,
        'parent_id': parent_id,
        'value': value,
        'class': xclass,
        'style': style,
        'extra': extra,
    })
    for child in root.children:
        children = flatten_tree(child, id)
        result = result + children

    return result


def generate_drawio(ls_tree):
    yn = create_node(ls_tree)
    yn.calculate_layout()

    all_items = flatten_tree(yn, '3')
    return all_items


def render_drawio(all_items, args, configs):
    env = Environment(
        loader=FileSystemLoader('./templates'),
        autoescape=select_autoescape(['html', 'xml']),
        trim_blocks=True,
        lstrip_blocks=True,
        line_statement_prefix='#',
    )

    template = env.get_template(configs['template'])

    args.output.write(template.render(
        items=all_items,
        page=configs))
