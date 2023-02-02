import os
import sys
import cv2
import math
from PIL import Image
import csv

CURRENT_DIR = str(os.path.dirname(os.path.abspath(__file__)))
VIDEO_NAME = ""
FIRST_TIMESTAMP = 0
LAST_TIMESTAMP = 0


def checkArguments():
    global VIDEO_NAME
    global FIRST_TIMESTAMP
    global LAST_TIMESTAMP
    
    if len(sys.argv) != 4:
        print("Please launch the script as following:")
        print("python3 dataset_creator.py <<video name>> <<first timestamp>> <<last timestamp>>")
        sys.exit()

    try:
        VIDEO_NAME = sys.argv[1]
        FIRST_TIMESTAMP = int(sys.argv[2])
        LAST_TIMESTAMP = int(sys.argv[3])
    except:
        print("Timestamps must be numbers!")

    if not os.path.exists(CURRENT_DIR+r"/results"):
        os.mkdir(CURRENT_DIR+r"/results")
    if not os.path.exists(CURRENT_DIR+r"/resized_results"):
        os.mkdir(CURRENT_DIR+r"/resized_results")
    if not os.path.exists(CURRENT_DIR+r"/final_results"):
        os.mkdir(CURRENT_DIR+r"/final_results")

    print("Directories created.")


def splitFrames():
    vidcap = cv2.VideoCapture(VIDEO_NAME)
    success,image = vidcap.read()
    count = 0

    while success:
        cv2.imwrite("./frameSplitter/frameSplitter/results/%d.png" % count, image)     
        success, image = vidcap.read()
        count += 1

    print("Video splitted into frames! Results are stored in \"results\" folder.")

    for i in range(count):
        image = Image.open("./frameSplitter/frameSplitter/results/"+str(i)+".png")
        new_image = image.resize((752,480))
        new_image.save("./frameSplitter/frameSplitter/resized_results/" + str(i) + ".png")

    print("Images are resized into 752x480! Results are stored in \"resized_results\" folder.")

    increaseRate = math.floor((LAST_TIMESTAMP - FIRST_TIMESTAMP) / count)

    for i in range(count):
        image = cv2.imread("./frameSplitter/frameSplitter/resized_results/" + str(i) + ".png")
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("./frameSplitter/frameSplitter/final_results/" + str(i*increaseRate + FIRST_TIMESTAMP) + ".png", gray)

    print("Images are grayscaled and renamed! Results are stored in \"resized_results\" folder.")

    with open("./frameSplitter/frameSplitter/data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["#timestamp [ns]", "filename"])
        for i in range(count):
            writer.writerow([str(i*increaseRate + FIRST_TIMESTAMP), str(i*increaseRate + FIRST_TIMESTAMP)+".png"])

    print("Timestamps are corresponding file names are stored in \"data.csv\" file.")






checkArguments()
splitFrames()
os.system("./frameSplitter/frameSplitter/organize.sh")




