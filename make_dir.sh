#!/bin/bash
MIN_NUM=1
MAX_NUM=200
GAP=1
for i in `seq -w $MIN_NUM $GAP $MAX_NUM`
do
# if no files in directory,
 # if [ -z "$(ls $i)" ]; then
    # echo $i
# if the directory does not exist
# make new directory
if [ ! -e $i ]; then
  mkdir $i
fi
for file in a b c d e f
do
if [[ ! -f ./$i/$file.py ]]; then
  # ls -l ./$i/$file.py
  cp ../a.py ./$i/$file.py
fi
done
 # fi
done
cp ./make_dir.sh ../make_dir.sh
echo "[Finished] making directory from $MIN_NUM to $MAX_NUM."
echo "[Finished] making a - f.py under the directories if they don't exist."
echo "[Finished] copying this file to ../make_dir.sh the same as this."
