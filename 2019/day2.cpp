#include <iostream>
#include "intcode.hpp"
#include "read_input.hpp"
using namespace std;

llint task1(vector<llint> program) {
    program[1] = 12;
    program[2] = 2;
    Intcode intcode(program);
    llint dummy = 0;
    while (intcode.getStatus() != Status::Finished) {
        intcode.run(dummy);
    }
    return intcode[0];
}

llint task2(const vector<llint>& initial_state, llint target_output) {
    for (llint noun = 0; noun < 100; noun++) {
        for (llint verb = 0; verb < 100; verb++) {
            vector<llint> memory = initial_state;
            memory[1] = noun;
            memory[2] = verb;
            Intcode intcode(memory);
            llint dummy = 0;
            while (intcode.getStatus() != Status::Finished) {
                intcode.run(dummy);
            }
            if (intcode[0] == target_output) return 100 * noun + verb;
        }
    }
    return 1;
}

int main(int argc, char *argv[]) {
    vector<llint> input_data = comma_separated("input2");
    cout << task1(input_data) << endl;
    cout << task2(input_data, 19690720) << endl;
}
