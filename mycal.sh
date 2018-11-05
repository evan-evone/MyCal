#!/usr/bin/env bash

if [ -f './mycal.sh' ] && [ -f './color.py' ] && [ -f './arg.py' ]; then
  wd="."
else
  wd="$(ls -lhAG $(which mycal) | awk '{print $NF}')"
  wd="${wd%/*}/"
fi

args="$@"
color=$($wd/color.py '$@')
other_args=$($wd/arg.py "$@")

if [[ " ${args[@]} " =~ " month " ]]; then
  gcal -s 1 -H $color -q US_AK $(date "+%m %Y") "$other_args"
elif [[ " ${args[@]} " =~ " year " ]]; then
  gcal -s 1 -H $color -q US_AK $(date "+%Y") "$other_args"
else
  gcal -s 1 -H $color -q US_AK "$other_args"
fi
