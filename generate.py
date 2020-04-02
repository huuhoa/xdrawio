#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader, select_autoescape

import xdrawio

def get_page_dimention(page_size, page_orientation):
    sizes = {
        'A0': (9933, 14043),
        'A1': (7016, 9933),
        'A2': (4961, 7016),
        'A3': (3508, 4961),
        'A4': (2480, 3508),
        'A5': (1754, 2480),
        'A6': (1240, 1754),
    }

    ps = sizes[page_size]
    if page_orientation == 'portrait':
        return ps[0], ps[1]
    elif page_orientation == 'landscape':
        return ps[1], ps[0]
    else:
        return 0, 0


def load_team(path):
    from xdrawio.layout import create_layout, layout_workgroup
    from xdrawio.datatypes import Page

    env = Environment(
        loader=FileSystemLoader('./templates'),
        autoescape=select_autoescape(['html', 'xml']),
        trim_blocks = True,
        lstrip_blocks = True,
        line_statement_prefix='#',
    )

    template = env.get_template('corepayment.tmpl')

    mdls, d = xdrawio.read_data(path)

    wgs_byteam = layout_workgroup(d.workgroups)

    page = Page()
    page.initialize(mdls, d, wgs_byteam)

    create_layout(page, wgs_byteam, d)
    # flat out
    all_items = page.flatten_tree()

    return template, all_items, d.configurations

def load_bank_status(path):
    import bstatus

    env = Environment(
        loader=FileSystemLoader('./templates'),
        autoescape=select_autoescape(['html', 'xml']),
        trim_blocks = True,
        lstrip_blocks = True,
        line_statement_prefix='#',
    )

    template = env.get_template('bank_status.tmpl')

    data = bstatus.read_data(path)
    all_items = bstatus.flatten_data(data)
    return template, all_items, data.configurations


def main():
    import argparse


    parser = argparse.ArgumentParser(
        description='Render team structure to drawio file format.',
        epilog='Enjoy!'
        )
    parser.version = "1.0"
    parser.add_argument('path', metavar='path', type=str,
                        help='path to xlsx file that contains team structure')
    parser.add_argument(
        '-d',
        '--debug',
        type=bool,
        help='debug flag, when enable only print debug data, not print drawio data'
    )

    parser.add_argument(
        '-ps',
        '--page-size',
        type=str,
        help='page size, possible values: A0, A1, A2, A3, A4',
        default='A3'
    )

    parser.add_argument(
        '-po',
        '--page-orientation',
        type=str,
        help='page orientation, possible values: portrait, landscape',
        default='portrait'
    )

    parser.add_argument(
        '-t',
        '--type',
        type=str,
        help='draw type, possible values: team, roadmap, bank_status',
        default='team'
    )

    args = parser.parse_args()

    w, h = get_page_dimention(args.page_size, args.page_orientation)
    page = {
        "width": w,
        "height": h
    }

    if args.type == 'team':
        template, items, configs = load_team(args.path)

    if args.type == 'bank_status':
        template, items, configs = load_bank_status(args.path)

    if not args.debug:
        print(template.render(
                items=items,
                configs=configs,
                page=page))


if __name__ == "__main__":
    main()
