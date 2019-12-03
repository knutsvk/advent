#pragma once
#include <vector>

enum Opcode
{
    Add = 1,
    Multiply = 2,
    Halt = 99
};

int intcode(std::vector<int> &program);

