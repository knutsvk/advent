from enum import Enum


class Direction(Enum):
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = "W"


class Boat(object):
    def __init__(self, direction: Direction):
        self.x: int = 0
        self.y: int = 0
        self.direction: Direction = direction

    def move(self, direction: Direction, number: int) -> None:
        if direction == Direction.NORTH:
            self.y += number
        elif direction == Direction.EAST:
            self.x += number
        elif direction == Direction.SOUTH:
            self.y -= number
        elif direction == Direction.WEST:
            self.x -= number
        else:
            raise RuntimeError(f"tried to move in undefined direction {direction}")

    def forward(self, number: int) -> None:
        self.move(self.direction, number)

    def turn_right(self) -> None:
        if self.direction == Direction.NORTH:
            self.direction = Direction.EAST
        elif self.direction == Direction.EAST:
            self.direction = Direction.SOUTH
        elif self.direction == Direction.SOUTH:
            self.direction = Direction.WEST
        elif self.direction == Direction.WEST:
            self.direction = Direction.NORTH

    def turn_left(self) -> None:
        if self.direction == Direction.EAST:
            self.direction = Direction.NORTH
        elif self.direction == Direction.NORTH:
            self.direction = Direction.WEST
        elif self.direction == Direction.WEST:
            self.direction = Direction.SOUTH
        elif self.direction == Direction.SOUTH:
            self.direction = Direction.EAST

    def manhattan_distance(self) -> float:
        return abs(self.x) + abs(self.y)

    def follow_instruction(self, instruction: str) -> None:
        action = instruction[0]
        num = int(instruction[1:])
        if action in ["N", "S", "E", "W"]:
            self.move(Direction(action), num)
        elif action == "F":
            self.forward(num)
        elif action == "L":
            for count in range(num // 90):
                self.turn_left()
        elif action == "R":
            for count in range(num // 90):
                self.turn_right()
        else:
            raise RuntimeError(f"unknown action {action}")


if __name__ == "__main__":
    with open("input12") as file:
        instructions = file.read().splitlines()
    boat = Boat(Direction.EAST)
    for i, instruction in enumerate(instructions):
        boat.follow_instruction(instruction)
    print(abs(boat.x) + abs(boat.y))
