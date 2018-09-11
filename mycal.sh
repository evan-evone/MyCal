#!/usr/bin/env bash

if [ "$1"=="month" ]; then
  gcal -H '\e[34m:\e[0m:\e[32m:\e[0m' -q US_AK $(date "+%m %Y")
elif [ "$1"=="year" ]; then
  gcal -H '\e[34m:\e[0m:\e[32m:\e[0m' -q US_AK $(date "+%Y")
else
  gcal
fi
