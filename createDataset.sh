#!/bin/sh


mkdir euroc && cd "$_"
cp  ../timestampOrganizer/timestampdata.txt ./timestamp.txt


mkdir mav0 && cd "$_"

cp  ../../yamlFiles/body.yaml ./body.yaml


mkdir cam0 cam1 imu0
# For cam0
cd cam0
cp  ../../../yamlFiles/cam0_sensor.yaml ./sensor.yaml
cp ../../../timestampOrganizer/finalData.csv ./data.csv
cp -R ../../../frameSplitter/frameSplitter/final_results/. ./data
cd ..

#For cam 1
cd cam1
cp  ../../../yamlFiles/cam1_sensor.yaml ./sensor.yaml
cp ../../../timestampOrganizer/finalData.csv ./data.csv
cp -R ../../../frameSplitter/frameSplitter/final_results/. ./data
cd ..

#For imu0
cd imu0
cp  ../../../yamlFiles/imu.yaml ./sensor.yaml
cp ../../../timestampOrganizer/AndroSensor.csv ./data.csv




