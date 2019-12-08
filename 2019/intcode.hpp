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

enum Status {
    Finished = 0,
    ReadyToGo = 1,
    WaitingForInput = 2,
    Error = 3
};

int decipherParameterMode(int parameter_mode, int pos, const std::vector<int> &program);

class Intcode {
    private:
        std::vector<int> program;
        int pos;
        int status;
    public:
        Intcode(const std::vector<int> &_program);
        void run(int &inout);
        int getStatus() {return status;}
        int operator [](int i) const {return program[i];}
        int &operator [](int i) {return program[i];}
};
