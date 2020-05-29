# xdrawio

xdrawio is a script to render data from Excel worksheet to draw.io file format. From that, one can open in draw.io and export to other formats such as pdf, svg, png, ...

Currently, xdrawio support following templates to render data:

* `features`: render all features of a software system, which will be grouped into domains, sub-domains
* `status`: render data in status dashboard, suitable for rendering multi project status, where each project will go through set of same steps.
* `roadmap`: render feature roadmap of a software system

## Install

Need to run following command to install prerequisite python packages:

```bash
$ pip3 install pyparsing openpyxl jinja2
```

Clone and install pyyoga - visit https://github.com/huuhoa/pyyoga


## Usage

```
usage: generate.py [-h] [-d DEBUG] [-ps {A0,A1,A2,A3,A4,A5,A6}]
                   [-po {portrait,landscape}]
                   [-t {arch,features,roadmap,status}]
                   path

Render data to drawio file format.

positional arguments:
  path                  path to xlsx file that contains team structure

optional arguments:
  -h, --help            show this help message and exit
  -d DEBUG, --debug DEBUG
                        debug flag, when enable only print debug data, not
                        print drawio data
  -ps {A0,A1,A2,A3,A4,A5,A6}, --page-size {A0,A1,A2,A3,A4,A5,A6}
                        page size, possible values: A0, A1, A2, A3, A4, A5, A6
  -po {portrait,landscape}, --page-orientation {portrait,landscape}
                        page orientation, possible values: portrait, landscape
  -t {arch,features,roadmap,status}, --type {arch,features,roadmap,status}
                        draw type, possible values: features, roadmap, status,
                        arch

Enjoy!
```

