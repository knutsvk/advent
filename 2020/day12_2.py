from dataclasses import dataclass
from enum import Enum


class Direction(Enum):
    NORTH = 'N'
    EAST = 'E'
    SOUTH = 'S'
    WEST = 'W'


@dataclass
class Position:
    x: float
    y: float


class Boat(object):
    def __init__(self, direction: Direction):
        self.position: Position = Position(0, 0)
        self.direction: Direction = direction
        self.waypoint: Position = Position(10, 1)

    def move_waypoint(self, direction: Direction, number: int) -> None:
        if direction == Direction.NORTH:
            self.waypoint.y += number
        elif direction == Direction.EAST:
            self.waypoint.x += number
        elif direction == Direction.SOUTH:
            self.waypoint.y -= number
        elif direction == Direction.WEST:
            self.waypoint.x -= number
        else:
            raise RuntimeError(f"tried to move waypoint in undefined direction {direction}")

    def forward(self, number: int) -> None:
        self.position.x += number * self.waypoint.x
        self.position.y += number * self.waypoint.y

    def rotate_waypoint(self, orientation, degrees: int) -> None:
        if degrees == 180:
            self.waypoint.x = -self.waypoint.x
            self.waypoint.y = -self.waypoint.y
        elif degrees == 90 and orientation == "L" or degrees == 270 and orientation == "R":
            tmp = self.waypoint.x
            self.waypoint.x = -self.waypoint.y
            self.waypoint.y = tmp
        elif degrees == 90 and orientation == "R" or degrees == 270 and orientation == "L":
            tmp = self.waypoint.x
            self.waypoint.x = self.waypoint.y
            self.waypoint.y = -tmp
        else:
            raise RuntimeError(f"tried to rotate waypoint with undefined command {orientation}{degrees}")

    def manhattan_distance(self) -> float:
        return abs(self.position.x) + abs(self.position.y)

    def follow_instruction(self, instruction: str) -> None:
        action = instruction[0]
        num = int(instruction[1:])
        if action in ['N', 'S', 'E', 'W']:
            self.move_waypoint(Direction(action), num)
        elif action == "F":
            self.forward(num)
        elif action in ["L", "R"]:
            self.rotate_waypoint(action, num)
        else:
            raise RuntimeError(f"unknown action {action}")


if __name__ == "__main__":
    with open("input12") as file:
        instructions = file.read().splitlines()
    boat = Boat(Direction.EAST)
    for i, instruction in enumerate(instructions):
        boat.follow_instruction(instruction)
    print(abs(boat.position.x) + abs(boat.position.y))
