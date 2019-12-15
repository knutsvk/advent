#pragma once
#include <vector>

typedef long long int llint;

enum Direction {
    Up = 0,
    Right = 1, 
    Down = 2,
    Left = 3;
};

class Robot {

    private:
        llint x, llint y;
        std::vector<std::vector<bool> > panels;

    public:
        void rotateClockwise();
        void rotateCounterClockwise();
        void step();
        void paintPanel(llint instruction);
        llint readPanel();

