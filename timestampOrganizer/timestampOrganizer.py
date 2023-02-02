import csv
import math
import os
# Open the files in read-only mode

with open('./timestampOrganizer/data.csv', 'r') as frame_file, open('./timestampOrganizer/AndroSensor.csv', 'r') as sensor_file ,open('./timestampOrganizer/finalData.csv', 'w' , newline="") as final, open('./timestampOrganizer/timestampdata.txt', 'w') as timestampfile :
    # Create CSV reader objects for each file
    frame_reader = csv.reader(frame_file)
    sensor_reader = csv.reader(sensor_file)


    Finalwriter = csv.writer(final)
    Finalwriter.writerow(["#timestamp [ns]", "filename"])
    
    
    # Skip the header row in both files
    next(frame_reader)
    next(sensor_reader)

    # Iterate through each row in the frameData.csv file
    for frame_row in frame_reader:
        # Get the timestamp value from the "#timestamp [ns]" column
        frame_timestamp = frame_row[0]
        # Initialize a variable to store the closest sensor data
        closest_sensor_data = None

        # Initialize a variable to store the difference between the current
        # frame timestamp and the closest sensor timestamp
        min_diff = float('inf')

        # Iterate through each row in the sensorData.csv file
        greatCount = 5
        for sensor_row in sensor_reader:

        
            # Get the timestamp value from the "#timestamp [ns]" column
            sensor_timestamp = sensor_row[0]
            if sensor_timestamp > frame_timestamp:
                min_diff = diff
                closest_sensor_data = sensor_row[0]
                break
            # Calculate the difference between the current frame timestamp
            # and the current sensor timestamp
            diff = abs(int(frame_timestamp) - int(sensor_timestamp))
            # If the difference is smaller than the minimum difference,
            # update the minimum difference and the closest sensor data
            if diff < min_diff:
                min_diff = diff
                closest_sensor_data = sensor_row[0]


        # Once we have found the closest sensor data for the current frame,
        # we can use it to do something, such as print it to the screen
        newImageName = str(closest_sensor_data) + ".png"
        imagePath =        "./frameSplitter/frameSplitter/final_results/" + str(frame_row[0]) + ".png"
        updatedImagePath = "./frameSplitter/frameSplitter/final_results/" + newImageName

        os.rename(imagePath , updatedImagePath)
        timestampfile.write(closest_sensor_data + "\n")
        Finalwriter.writerow([closest_sensor_data, newImageName])
      #  print(frame_row[0], "is closest to " , closest_sensor_data)





