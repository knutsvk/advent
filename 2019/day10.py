from copy import deepcopy
from matplotlib import pyplot as plt
from math import *
import numpy as np


class Asteroid(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.visible_asteroids = 0
        self.blasted = False


def read_asteroid_map(filename):
    asteroids = []
    with open(filename) as file:
        for row, line in enumerate(file): 
            for col, symbol in enumerate(list(line[:-1])):
                if symbol == '#':
                    asteroids.append(Asteroid(col, row))
    return asteroids


def distance(a1: Asteroid, a2: Asteroid):
    return sqrt((a1.x - a2.x)**2 + (a1.y - a2.y)**2)


def is_between(start, point, stop):
    return isclose(distance(start, point) + distance(point, stop), distance(start, stop))


def count_visible_asteroids(asteroids, station):
    possible_sightings = [asteroid for asteroid in asteroids if not asteroid.pos == station.pos]
    visible_asteroids = []

    for asteroid in possible_sightings:
        other_asteroids = [other for other in possible_sightings if not other == asteroid]
        blocked = False
        for other in other_asteroids:
            if is_between(asteroid, other, station):
                blocked = True
                break
        if not blocked:
            visible_asteroids.append(asteroid)

    station.visible_asteroids = len(visible_asteroids)


def get_angle(a1: Asteroid, a2: Asteroid):
    dx = a2.x - a1.x
    dy = a1.y - a2.y
    angle = - atan2(dy, dx) + pi / 2
    if angle < 0: 
        return angle + 2 * pi
    return angle


if __name__ == "__main__":
    asteroids = read_asteroid_map("input10")

    station = Asteroid(0, 0)
    for candidate in asteroids:
        count_visible_asteroids(asteroids, candidate)
        if candidate.visible_asteroids > station.visible_asteroids: 
            station = candidate
    
    print(f"Task 1: {station.visible_asteroids} {station.pos}")

    remaining_asteroids = [asteroid for asteroid in asteroids if not asteroid == station]    
    remaining_asteroids.sort(key=lambda x: (get_angle(station, x), distance(station, x)))

    count = 0
    while count < len(remaining_asteroids):
        previous_angle = -1 
        for asteroid in remaining_asteroids:
            angle = get_angle(station, asteroid)
            if asteroid.blasted or angle == previous_angle:
                continue
            else: 
                asteroid.blasted = True
                previous_angle = angle
                count += 1
                if count == 200: 
                    print(f"Task 2: {asteroid.x * 100 + asteroid.y}")
                    break



