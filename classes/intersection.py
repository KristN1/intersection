import time
import random
import threading

from classes.car import Car

class Intersection():
    def __init__(self, speed: int, lightInterval: int, carSpawnInterval: list):
        self.speed = speed
        self.lightInterval = lightInterval / self.speed
        self.carSpawnInterval = carSpawnInterval
        self.roads = [[],[],[],[]]
        self.currentLight = random.randint(0, 3)

    def start(self):
        self._carGenerator()
        self._lightLoop()

        threading.Timer(3 / self.speed, self._carLoop).start()

    def status(self, criticalOnly=False):
        def _checkStatus():
            for index, road in enumerate(self.roads):
                if len(road) > 20:
                    print(f"Road {index + 1} is full")
                    return False
                    
            return True

        if criticalOnly:
            return _checkStatus()

        else:
            print(f"Current light: {self.currentLight + 1}")
            print(f"Road 1: {len(self.roads[0])}")
            print(f"Road 2: {len(self.roads[1])}")
            print(f"Road 3: {len(self.roads[2])}")
            print(f"Road 4: {len(self.roads[3])}")

            return _checkStatus()


    def _carGenerator(self):
        car = Car()
        self.roads[car.origin].append(car)

        threading.Timer(random.randint(self.carSpawnInterval[0], self.carSpawnInterval[1]) / self.speed, self._carGenerator).start()

    def _lightLoop(self):
        self.currentLight = (self.currentLight + 1) % 4

        threading.Timer(self.lightInterval / self.speed, self._lightLoop).start()

    def _carLoop(self):
        while True:
            try:
                self.roads[self.currentLight].pop(0)
            except IndexError:
                pass

            time.sleep(3/self.speed)

