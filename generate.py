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
    }

    ps = sizes[page_size]
    if page_orientation == 'portrait':
        return ps[0], ps[1]
    elif page_orientation == 'landscape':
        return ps[1], ps[0]
    else:
        return 0, 0

def main():
    import argparse
    from xdrawio.layout import create_layout, layout_workgroup
    from xdrawio.datatypes import Page


    parser = argparse.ArgumentParser(
        description='Render team structure to drawio file format.',
        epilog='Enjoy!'
        )
    parser.version = "1.0"
    parser.add_argument('team_path', metavar='path', type=str,
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

    args = parser.parse_args()

    env = Environment(
        loader=FileSystemLoader('./templates'),
        autoescape=select_autoescape(['html', 'xml']),
        trim_blocks = True,
        lstrip_blocks = True,
        line_statement_prefix='#',
    )

    template = env.get_template('corepayment.tmpl')

    mdls, d = xdrawio.read_data(args.team_path)

    wgs_byteam = layout_workgroup(d.workgroups)

    page = Page()
    page.initialize(mdls, d, wgs_byteam)

    create_layout(page, wgs_byteam, d)
    # flat out
    all_items = page.flatten_tree()

    w, h = get_page_dimention(args.page_size, args.page_orientation)
    page = {
        "width": w,
        "height": h
    }
    if not args.debug:
        print(template.render(
                items=all_items,
                configs=d.configurations,
                page=page))


if __name__ == "__main__":
    main()
