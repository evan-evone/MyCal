#!/usr/bin/env bash

location="$1"

if [ "$location" == "" ]; then
  location='/usr/local/bin'
fi

if [ -f "$location/mycal" ]; then
  rm $location/mycal
fi

ln -s $(pwd)/mycal.sh $location/mycal
