import os
import sys
import shutil
import csv
import pandas as pd

    
    



if len(sys.argv) != 3:
  print("Wrong argument format, use the pattern below to run the script.")
  print("python3 main.py 'video_file_path' 'Androsensor_file_path'")
  sys.exit()

videFilePath = sys.argv[1]
sensorDataPath = sys.argv[2]



sensorScriptCommand = 'python3 ./androsnsor/AndroSensorConverter.py ' +  sensorDataPath
os.system(sensorScriptCommand)


print("Finished processing sensor file.")

firstTimestamp = ""
lastTimestamp = ""
with open('./androsnsor/SensorData.csv', 'r', encoding='utf-8') as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    # Get the column names from the first row
    headers = next(reader)
    # Find the index of the timestamp column
    timestamp_index = headers.index("#timestamp [ns]")
    # Initialize a list to store the timestamp values
    timestamps = []
    # Iterate over the rows of the CSV file
    for row in reader:
            
            timestamps.append(row[timestamp_index])

        # Append the timestamp value to the list
        
    # Print the first and last timestamps
    firstTimestamp = timestamps[0]
    lastTimestamp = timestamps[-1]

print("Timestamps from SensorData file obtained as follows:  First Timestamp: " + str(firstTimestamp) + "  Last Timestamp: " + str(lastTimestamp))





frameSplitCommmand = 'python3  ./frameSplitter/frameSplitter/frameSplitter.py ' +  videFilePath + ' ' + firstTimestamp + ' ' + lastTimestamp
os.system(frameSplitCommmand)




shutil.move('./androsnsor/SensorData.csv', './timestampOrganizer/AndroSensor.csv')
shutil.move('frameSplitter/frameSplitter/data.csv', 'timestampOrganizer/data.csv')




timestamporganizerCommand = 'python3 ./timestampOrganizer/timestampOrganizer.py'
os.system(timestamporganizerCommand)




createDatasetCommand = "sh ./createDataset.sh"
os.system(createDatasetCommand)


