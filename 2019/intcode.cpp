#include <iostream>
#include <string>

#include "intcode.hpp"

using namespace std;

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
}

llint Intcode::read(llint address) {
    if (program.size() < address + 1) {
        program.resize(address + 1, 0);
    }
    return program[address];
}

llint Intcode::getAddress(llint parameter_mode, llint input) {
    switch(parameter_mode) { 

        case ParameterMode::Position:
            return input;

        case ParameterMode::Relative:
            return relative_base + input;

        default:
            cout << "Error: unknown parameter mode for address:" << parameter_mode << endl;
            return 1;
    }
}

llint Intcode::getParameter(llint parameter_mode, llint input) {
    if (parameter_mode == ParameterMode::Immediate)
        return input;
    return read(getAddress(parameter_mode, input));
}

void Intcode::run(llint &inout) {
    while (read(pos) != Opcode::Halt) {
        string opcode = to_string(read(pos));

        while (opcode.size() < 5) {
            opcode.insert(0, "0");
        }

        switch (stoll(opcode.substr(3))) {
            llint x, y, address;

            case Opcode::Add:
                x = getParameter(stoll(opcode.substr(2,1)), read(pos + 1));
                y = getParameter(stoll(opcode.substr(1,1)), read(pos + 2));
                address = getAddress(stoll(opcode.substr(0,1)), read(pos + 3));
                insert(address, x + y);
                pos += 4;
                break;

            case Opcode::Multiply:
                x = getParameter(stoll(opcode.substr(2,1)), read(pos + 1));
                y = getParameter(stoll(opcode.substr(1,1)), read(pos + 2));
                address = getAddress(stoll(opcode.substr(0,1)), read(pos + 3));
                insert(address, x * y);
                pos += 4;
                break;

            case Opcode::Input:
                if (status == Status::WaitingForInput) {
                    address = getAddress(stoll(opcode.substr(2,1)), read(pos + 1));
                    insert(address, inout);
                    pos += 2;
                    status = Status::ReadyToGo;
                } else {
                    status = Status::WaitingForInput;
                    return;
                }
                break;

            case Opcode::Output: 
                address = getParameter(stoll(opcode.substr(2,1)), read(pos + 1));
                pos += 2;
                inout = address;
                return;

            case Opcode::JumpIfTrue:
                x = getParameter(stoll(opcode.substr(2,1)), read(pos + 1));
                y = getParameter(stoll(opcode.substr(1,1)), read(pos + 2));
                pos = x ? y : pos + 3;
                break;

            case Opcode::JumpIfFalse:
                x = getParameter(stoll(opcode.substr(2,1)), read(pos + 1));
                y = getParameter(stoll(opcode.substr(1,1)), read(pos + 2));
                pos = x ? pos + 3 : y;
                break;

            case Opcode::LessThan:
                x = getParameter(stoll(opcode.substr(2,1)), read(pos + 1));
                y = getParameter(stoll(opcode.substr(1,1)), read(pos + 2));
                address = getAddress(stoll(opcode.substr(0,1)), read(pos + 3));
                insert(address, x < y ? 1 : 0);
                pos += 4;
                break;

            case Opcode::Equals:
                x = getParameter(stoll(opcode.substr(2,1)), read(pos + 1));
                y = getParameter(stoll(opcode.substr(1,1)), read(pos + 2));
                address = getAddress(stoll(opcode.substr(0,1)), read(pos + 3));
                insert(address, x == y ? 1 : 0);
                pos += 4;
                break;

            case Opcode::AddToRelativeBase:
                x = getParameter(stoll(opcode.substr(2,1)), read(pos + 1));
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
}
