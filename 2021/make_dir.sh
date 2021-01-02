#!/bin/bash
# make python file for 2021 all days!
for month in {1..12}; do
  for date in {1..31}; do
    FOLDER=$month/$date
    if [ ! -e $FOLDER ]; then
      mkdir -p $FOLDER
    fi
    for file in a b c d e f
    do
    if [[ ! -f ./$FOLDER/$file.py ]]; then
      cp ../a.py ./$FOLDER/$file.py
    fi
    done
  done
done