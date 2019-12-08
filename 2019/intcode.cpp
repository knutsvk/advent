#include <cstdlib>
#include <iostream>
#include <string>

#include "intcode.hpp"

using namespace std;

int decipherParameterMode(int parameter_mode, int pos, const vector<int> &program) {
    switch(parameter_mode) { 
        case ParameterMode::Position:
            return program[program[pos]];
        case ParameterMode::Immediate: 
            return program[pos];
        default:
            cout << "Error: unknown parameter mode" << endl;
            return 1;
    }
}

Intcode::Intcode(const vector<int> &_program) {
    program = _program;
    pos = 0;
    completed = false;
}

int Intcode::run() {
    while (program[pos] != Opcode::Halt) {
        string opcode = to_string(program[pos]);
        while (opcode.size() < 5) {
            opcode.insert(0, "0");
        }
        switch (stoi(opcode.substr(3))) {
            int x, y, address;
            case Opcode::Add: 
                x = decipherParameterMode(stoi(opcode.substr(2,1)), pos + 1, program);
                y = decipherParameterMode(stoi(opcode.substr(1,1)), pos + 2, program);
                address = program[pos + 3];
                program[address] = x + y;
                pos += 4;
                break;
            case Opcode::Multiply:
                x = decipherParameterMode(stoi(opcode.substr(2,1)), pos + 1, program);
                y = decipherParameterMode(stoi(opcode.substr(1,1)), pos + 2, program);
                address = program[pos + 3];
                program[address] = x * y;
                pos += 4;
                break;
            case Opcode::Input: 
                address = program[pos + 1];
                cout << "Enter input: ";
                cin >> program[address];
                pos += 2;
                break;
            case Opcode::Output: 
                address = decipherParameterMode(stoi(opcode.substr(2,1)), pos + 1, program);
                pos += 2;
                return address;
            case Opcode::JumpIfTrue:
                x = decipherParameterMode(stoi(opcode.substr(2,1)), pos + 1, program);
                y = decipherParameterMode(stoi(opcode.substr(1,1)), pos + 2, program);
                pos = x ? y : pos + 3;
                break;
            case Opcode::JumpIfFalse:
                x = decipherParameterMode(stoi(opcode.substr(2,1)), pos + 1, program);
                y = decipherParameterMode(stoi(opcode.substr(1,1)), pos + 2, program);
                pos = x ? pos + 3 : y;
                break;
            case Opcode::LessThan:
                x = decipherParameterMode(stoi(opcode.substr(2,1)), pos + 1, program);
                y = decipherParameterMode(stoi(opcode.substr(1,1)), pos + 2, program);
                address = program[pos + 3];
                program[address] = (x < y) ? 1 : 0;
                pos += 4;
                break;
            case Opcode::Equals:
                x = decipherParameterMode(stoi(opcode.substr(2,1)), pos + 1, program);
                y = decipherParameterMode(stoi(opcode.substr(1,1)), pos + 2, program);
                address = program[pos + 3];
                program[address] = (x == y) ? 1 : 0;
                pos += 4;
                break;
            default:
                cout << "Error: unknown opcode: " << stoi(opcode.substr(3)) << endl;
                return 1;
        }
    }
    completed = true;
    return 0;
}
