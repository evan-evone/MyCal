#!/usr/bin/env python

from sys import argv

colors = {
    'black': 30,
    'red': 31,
    'green': 32,
    'yellow': 33,
    'blue': 34,
    'magenta': 35,
    'cyan': 36,
    'white': 37,
    'bright_black': 90,
    'bright_red': 91,
    'bright_green': 92,
    'bright_yellow': 93,
    'bright_blue': 94,
    'bright_magenta': 95,
    'bright_cyan': 96,
    'bright_white': 97
}

if '-c' in argv:
    index = argv.index('-c')
    if len(argv) > index + 2:
        args = argv[index + 1:index + 3]
    elif len(argv) > index + 1:
        args = [argv[index + 1], 'green']
    else:
        args = ['blue', 'green']
else:
    args = ['blue', 'green']

value = []

for x in args:
    if x in colors.keys():
        value.append(r'\e[' + str(colors[x]) + 'm')
    else:
        value.append(r'\e[37m')
    value.append(r'\e[0m')

print(':'.join(value))
