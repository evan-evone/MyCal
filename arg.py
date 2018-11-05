#!/usr/bin/env python

from sys import argv

argv = argv[1:]

while 'month' in argv: argv.remove('month')
while 'year' in argv: argv.remove('year')
while '-c' in argv: argv.remove('-c')

colors = [
    'black', 'red', 'green', 'yellow',
    'blue', 'magenta', 'cyan', 'white',
    'brigh_black', 'bright_red', 'bright_green', 'bright_yellow',
    'bright_blue', 'bright_magenta', 'bright_cyan', 'bright_white'
]

for color in colors:
    while color in argv:
        argv.remove(color)

print(' '.join(argv))
