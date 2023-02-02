import sys
import os
import csv
from time import *
from datetime import datetime

currentPath = str(os.path.dirname(os.path.abspath(__file__)))
fileName = sys.argv[1]

# Open the original CSV file and create a reader object
with open(fileName) as csvfile:
    reader = csv.reader(csvfile)
    
    counter = 0
    # Open the new CSV file and create a writer object
    with open(str(currentPath)+"/SensorData.csv", "w") as new_csvfile:
        writer = csv.writer(new_csvfile)
        
        # Iterate over the rows of the original CSV file
        for row in reader:
            # Get the last column of the row (in normal date format)
            if(counter ==0):
                


                print(row[3:6])
                print(row[:3])
                #timestamp [ns],w_RS_S_x [rad s^-1],w_RS_S_y [rad s^-1],w_RS_S_z [rad s^-1],a_RS_S_x [m s^-2],a_RS_S_y [m s^-2],a_RS_S_z [m s^-2]
                writer.writerow(["#timestamp [ns]"]+ ["w_RS_S_x [rad s^-1]"] + ["w_RS_S_y [rad s^-1]"] + ["w_RS_S_z [rad s^-1]"] + ["a_RS_S_x [m s^-2]"] + ["a_RS_S_y [m s^-2]"] + ["a_RS_S_z [m s^-2]"])

                counter+=1
            else:
                date = row[-1]
                

                #2022-12-12 15:09:43:346
                formatTime = "%Y-%m-%d %H:%M:%S:%f"
                timestruct = int(str(datetime.strptime(date,formatTime).timestamp()).replace('.', ''))
                
                if(len(str(timestruct)) <13):
                    zeroString = str(("0"* (13- len(str(timestruct)))))
                    timestruct = str(timestruct) + zeroString
                print(timestruct)


                # Write the first three columns and the timestamp to the new CSV file
                writer.writerow([timestruct] + row[3:6] +  row[:3] )

