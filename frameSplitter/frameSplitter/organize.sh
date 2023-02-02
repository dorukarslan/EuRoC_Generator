#!/bin/sh
cd frameSplitter/frameSplitter

rm -rf resized_results*
rm -rf results*


cd ./final_results


echo "" > ./timestamp.txt
for f in *png; do
#  newName=$(echo ${f:14})
#  mv -- "$f" "${newName}"
 # part=$(echo ${f:0:13})
  echo $f >> timestamp.txt

done

cd ../../..

