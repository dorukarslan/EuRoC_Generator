# EuRoC_Generator
Allows users to generate EuRoC MAV dataset


This script is used to generate a EuRoC MAV dataset using a video recording and sensor data obtained from the AndroSensor application.

## Requirements

Python 3  
opencv_python==4.7.0.68  
pandas==1.5.2  
Pillow==9.4.0  


## Inputs

The script takes two arguments:

The file path of the video recording
The file path of the sensor data obtained from the AndroSensor application
Output

The script generates a dataset that can be used for EuRoC MAV research.

## Usage

To run the script, use the following command:

python
Copy code
python3 main.py 'video_file_path' 'Androsensor_file_path'
Replace 'video_file_path' with the file path of your video recording and 'Androsensor_file_path' with the file path of the sensor data obtained from the AndroSensor application.

## Steps

The script performs the following steps:

1. Converts the AndroSensor data into a CSV file in appropriate format
2. Extracts timestamps from the sensor data file
3. Splits the video recording into frames based on the extracted timestamps
4. Organizes the timestamp data
5. Creates the EuRoC MAV dataset using a shell script

## Note

The script assumes that the required dependencies (AndroSensorConverter, frameSplitter, and timestampOrganizer) are located in the 'androsnsor', 'frameSplitter/frameSplitter', and 'timestampOrganizer' directories, respectively.
The script uses a shell script named 'createDataset.sh' to create the final dataset. The shell script must be located in the same directory as the main script.

I also want to thank Doğukan Terzi for his help and contribution.



