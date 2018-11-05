# MyCal - Easily Customizable CLI Calendar

`MyCal` is a calendar command that is designed to be easy to learn and easily customizable
based on the `gcal`, GNU calendar, command. This command uses certain defaults of mine,
namely starting the week on Monday and using the U.S./Alaska holiday calendar, and has
default color settings based on my preferences, but color can be easily customized using
the `-c` flag (see below).

### Requirements

- [GCal](https://www.gnu.org/software/gcal/)
- [Python](https://anaconda.org)

### Installation

1. Navigate to the directory in which the files are contained.
2. Type the command `./install.sh`
    - Installs to `/usr/local/bin`
    - Optional: Specify and install path as the first argument to `install.sh`
3. You're done! Celebrate! (Or maybe just use the command as necessary.)

### Options

- `-c` -- color
    - Set a custom color scheme using **lowercase** color names (red, blue, green, etc.),
      in the specific order of day highlight color, year highlight color.
    - Accepts: `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`, and
      `bright_*`, where `*` is any of the previous colors. In short, any acceptable ANSI
      color names.
- `month`, `year`
    - Display current month or current year (as opposed to entering a number).
- Any other acceptable `gcal` options will be automatically passed to the `gcal`.
