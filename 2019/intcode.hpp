#pragma once
#include <vector>

typedef long long int llint;

enum Opcode {
    Add = 1,
    Multiply = 2,
    Input = 3, 
    Output = 4,
    JumpIfTrue = 5,
    JumpIfFalse = 6, 
    LessThan = 7, 
    Equals = 8,
    AddToRelativeBase = 9,
    Halt = 99
};

enum ParameterMode {
    Position = 0,
    Immediate = 1,
    Relative = 2
};

enum Status {
    Finished = 0,
    ReadyToGo = 1,
    WaitingForInput = 2,
    Error = 3
};

class Intcode {
    private:
        std::vector<llint> program;
        llint status;
        llint relative_base;
        llint pos;
    public:
        Intcode(const std::vector<llint> &_program);
        llint operator [](llint i) const {return program[i];}
        llint &operator [](llint i) {return program[i];}
        llint getStatus() {return status;}
        llint decipherParameterMode(llint parameter_mode, llint pos);
        void insert(llint address, llint value);
        void run(llint &inout);
};
