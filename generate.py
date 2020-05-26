#!/usr/bin/env python3

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



def main():
    import argparse


    parser = argparse.ArgumentParser(
        description='Render data to drawio file format.',
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
        metavar="size",
        help='page size, possible values: A0, A1, A2, A3, A4, A5, A6',
        default='A3'
    )

    parser.add_argument(
        '-po',
        '--page-orientation',
        metavar="orientation",
        type=str,
        help='page orientation, possible values: portrait, landscape',
        default='portrait'
    )

    parser.add_argument(
        '-t',
        '--type',
        type=str,
        help='draw type, possible values: features, roadmap, status, arch',
        default='features'
    )

    args = parser.parse_args()

    w, h = get_page_dimention(args.page_size, args.page_orientation)
    page = {
        "width": w,
        "height": h,
        'debug': args.debug,
    }

    xdrawio.render(args.type, args.path, page)


if __name__ == "__main__":
    main()
