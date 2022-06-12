#This program tracks my sleep patterns. Columns order is Quality, Position, Light Level, Audio Level, Heatpack

import csv

#DEFINE VARIABLES
quality = input("How did you sleep? (Scale of 1-5): ")
position = input("What position did you fall asleep in? (Back, Side, Stomach, Unsure): ")
lightLevel = input("How much light was in the room? (Scale of 1-5): ")
audioLevel = input("What were you listening to? (Livesteam/Video, Ambient Music, Natural Sounds, Nothing): ")
heatpack = input("Where was your heatpack? (Chest, Eyes, Pillow, Stomach): ")

#DEFINE DATATOAPPEND
dataToAppend = [
        [quality, position, lightLevel, audioLevel, heatpack]
]

#APPEND SAID DATA
with open('aelis-log.csv','a', newline='') as file:
    myFile = csv.writer(file)
    myFile.writerows(dataToAppend)

    file.close()

    print("Thank you for the information.")