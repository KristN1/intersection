import sys
import time

from classes.intersection import Intersection

speed = 500
lightInterval = 8
carSpawnInterval = [0, 5]

intersection = Intersection(speed, lightInterval, carSpawnInterval)
intersection.start()

i = 0

while True:
    if intersection.status() == True:
        time.sleep(intersection.lightInterval / speed)

    else:
        print(f"Survived {i // 4} cycles")
        sys.exit(0)

    i += 1