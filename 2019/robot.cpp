#include "robot.hpp"

using namespace std;

Robot::Robot() {
    x = 0;
    y = 0;
}

void Robot::rotateClockwise {
    switch(direction) {

        case Direction::Up:
            direction = Direction::Right;
            break;

        case Direction::Right:
            direction = Direction::Down;
            break;

        case Direction::Down:
            direction = Direction::Left;
            break;

        case Direction::Left:
            direction = Direction::Up;
            break;
    }
}

void Robot::rotateCounterClockwise {
    switch(direction) {

        case Direction::Up:
            direction = Direction::Left;
            break;

        case Direction::Left:
            direction = Direction::Down;
            break;

        case Direction::Down:
            direction = Direction::Right;
            break;

        case Direction::Right:
            direction = Direction::Up;
            break;
    }
}

void Robot::step() {
    switch(direction) {

        case Direction::Up: 
            y++;
            break;

        case Direction::Right: 
            x++;
            break;

        case Direction::Down: 
            y--;
            break;

        case Direction::Left: 
            x--;
            break;
    }
}
