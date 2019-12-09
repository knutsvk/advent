#include <cstdlib>
#include <iostream>
#include <string>

#include "intcode.hpp"

using namespace std;

llint Intcode::decipherParameterMode(llint parameter_mode, llint input) {
    switch(parameter_mode) { 
        case ParameterMode::Position:
            return program[input];
        case ParameterMode::Immediate: 
            return input;
        case ParameterMode::Relative: 
            return program[relative_base + input];
        default:
            cout << "Error: unknown parameter mode " << parameter_mode << endl;
            return 1;
    }
}

Intcode::Intcode(const vector<llint> &_program) {
    program = _program;
    status = Status::ReadyToGo;
    relative_base = 0;
    pos = 0;
}

void Intcode::insert(llint address, llint value) {
    if (program.size() < address + 1) {
        program.resize(address + 1, 0);
    }
    program[address] = value;
    return;
}

void Intcode::run(llint &inout) {
    while (program[pos] != Opcode::Halt) {
        string opcode = to_string(program[pos]);
        while (opcode.size() < 5) {
            opcode.insert(0, "0");
        }
        switch (stoll(opcode.substr(3))) {
            llint x, y, address;
            case Opcode::Add: 
                x = decipherParameterMode(stoll(opcode.substr(2,1)), program[pos + 1]);
                y = decipherParameterMode(stoll(opcode.substr(1,1)), program[pos + 2]);
                address = program[pos + 3];
                insert(address, x + y);
                pos += 4;
                break;
            case Opcode::Multiply:
                x = decipherParameterMode(stoll(opcode.substr(2,1)), program[pos + 1]);
                y = decipherParameterMode(stoll(opcode.substr(1,1)), program[pos + 2]);
                address = program[pos + 3];
                insert(address, x * y);
                pos += 4;
                break;
            case Opcode::Input: 
                if (status == Status::WaitingForInput) {
                    address = program[pos + 1];
                    insert(address, inout);
                    pos += 2;
                    status = Status::ReadyToGo;
                } else {
                    status = Status::WaitingForInput;
                    return;
                }
                break;
            case Opcode::Output: 
                address = decipherParameterMode(stoll(opcode.substr(2,1)), program[pos + 1]);
                pos += 2;
                inout = address;
                return;
            case Opcode::JumpIfTrue:
                x = decipherParameterMode(stoll(opcode.substr(2,1)), program[pos + 1]);
                y = decipherParameterMode(stoll(opcode.substr(1,1)), program[pos + 2]);
                pos = x ? y : pos + 3;
                break;
            case Opcode::JumpIfFalse:
                x = decipherParameterMode(stoll(opcode.substr(2,1)), program[pos + 1]);
                y = decipherParameterMode(stoll(opcode.substr(1,1)), program[pos + 2]);
                pos = x ? pos + 3 : y;
                break;
            case Opcode::LessThan:
                x = decipherParameterMode(stoll(opcode.substr(2,1)), program[pos + 1]);
                y = decipherParameterMode(stoll(opcode.substr(1,1)), program[pos + 2]);
                address = program[pos + 3];
                insert(address, x < y ? 1 : 0);
                pos += 4;
                break;
            case Opcode::Equals:
                x = decipherParameterMode(stoll(opcode.substr(2,1)), program[pos + 1]);
                y = decipherParameterMode(stoll(opcode.substr(1,1)), program[pos + 2]);
                address = program[pos + 3];
                insert(address, x == y ? 1 : 0);
                pos += 4;
                break;
            case Opcode::AddToRelativeBase:
                x = decipherParameterMode(stoll(opcode.substr(2,1)), program[pos + 1]);
                relative_base += x;
                pos += 2;
                break;
            default:
                cout << "Error: unknown opcode: " << stoll(opcode.substr(3)) << endl;
                status = Status::Error;
                return;
        }
    }
    status = Status::Finished;
    return;
}
