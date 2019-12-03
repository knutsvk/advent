#include <cstdlib>
#include <iostream>

#include "intcode.hpp"

using namespace std;

int intcode(vector<int> &program)
{
    int pos = 0;
    while (program[pos] != Opcode::Halt)
    {
        int opcode = program[pos];
        int x = program[pos + 1];
        int y = program[pos + 2];
        int destination = program[pos + 3];
        switch (opcode)
        {
            case Opcode::Add: 
                program[destination] = program[x] + program[y];
                break;
            case Opcode::Multiply:
                program[destination] = program[x] * program[y];
                break;
            default:
                cout << "Error: unknown opcode" << endl;
                return 1;
        }
        pos += 4;
    }
    return 0;
}
