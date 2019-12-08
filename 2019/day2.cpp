#include <iostream>
#include "intcode.hpp"
#include "read_input.hpp"
using namespace std;

int task1(vector<int> program) {
    program[1] = 12;
    program[2] = 2;
    Intcode intcode(program);
    int dummy = 0;
    while (intcode.getStatus() != Status::Finished) {
        intcode.run(dummy);
    }
    return intcode[0];
}

int task2(vector<int> initial_state, int target_output) {
    for (int noun = 0; noun < 100; noun++) {
        for (int verb = 0; verb < 100; verb++) {
            vector<int> memory = initial_state;
            memory[1] = noun;
            memory[2] = verb;
            Intcode intcode(memory);
            int dummy = 0;
            while (intcode.getStatus() != Status::Finished) {
                intcode.run(dummy);
            }
            if (intcode[0] == target_output) return 100 * noun + verb;
        }
    }
    return 1;
}

int main(int argc, char *argv[]) {
    vector<int> input_data = comma_separated("input2");
    cout << task1(input_data) << endl;
    cout << task2(input_data, 19690720) << endl;
}
