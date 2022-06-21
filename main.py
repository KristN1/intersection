import sys
import time

from classes.intersection import Intersection

acceptedArgs = ["-speed", "-light", "-car"]
speed = 100
lightInterval = 8
carSpawnInterval = [0, 5]

if len(sys.argv) > 1:
    if sys.argv[1] == "--h" or sys.argv[1] == "--help":
        print("-speed=<int> -light=<int> -car=<int,int>\nspeed = speed of the simulation\nlight = time between lights change\ncar = spawn interval of cars (min, max)\nAll times are in seconds")
        sys.exit(0)

def ArgToDict():
    args = {}
    for arg in sys.argv:
        if "=" in arg:
            key, value = arg.split("=")
            args[key] = value
    return args

args = ArgToDict()

for arg in args:
    print(arg)
    if arg in acceptedArgs:
        if arg == "-speed":
            speed = int(args[arg])

        elif arg == "-light":
            lightInterval = int(args[arg])

        elif arg == "-car":
            carSpawnInterval = args[arg].split(",")
            carSpawnInterval = [int(i) for i in carSpawnInterval]

intersection = Intersection(speed, lightInterval, carSpawnInterval)
intersection.start()

i = 0

while True:
    if intersection.status() == True:
        time.sleep(intersection.lightInterval / speed)

    else:
        print(f"Survived {i} cycles")
        sys.exit(0)

    i += 1