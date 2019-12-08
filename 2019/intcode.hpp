#pragma once
#include <vector>

enum Opcode {
    Add = 1,
    Multiply = 2,
    Input = 3, 
    Output = 4,
    JumpIfTrue = 5,
    JumpIfFalse = 6, 
    LessThan = 7, 
    Equals = 8,
    Halt = 99
};

enum ParameterMode {
    Position = 0,
    Immediate = 1
};

int decipherParameterMode(int parameter_mode, int pos, const std::vector<int> &program);
int intcode(std::vector<int> &program, std::vector<int> inputs = std::vector<int>(2, -1), bool verbose=true);

