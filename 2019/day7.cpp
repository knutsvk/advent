#include <iostream>
#include "intcode.hpp"
#include "read_input.hpp"
using namespace std;

vector<vector<llint>> getPossiblePhaseSettings(llint lo, llint hi) {
    vector<vector<llint>> possibilities;
    for (llint i = lo; i < hi; i++) {
        for (llint j = lo; j < hi; j++) {
            if (j == i) continue;
            for(llint k = lo; k < hi; k++) {
                if (k == i or k == j) continue;
                for(llint l = lo; l < hi; l++) {
                    if (l == i or l == j or l == k) continue;
                    for(llint m = lo; m < hi; m++) {
                        if (m == i or m == j or m == k or m == l) continue;
                        vector<llint> phase_settings = {i, j, k, l, m};
                        possibilities.push_back(phase_settings);
                    }
                }
            }
        }
    }
    return possibilities;
}

llint amplifier(vector<llint> input_data, llint phase_setting, llint input_value) {
    Intcode intcode(input_data);
    llint dummy = 0;
    intcode.run(dummy);
    intcode.run(phase_setting);
    intcode.run(input_value);
    return input_value;
}

llint amplificationCircuit(vector<llint> input_data, vector<llint> phase_settings) {
    llint input = 0;
    for(int i = 0; i < 5; i++) {
        input = amplifier(input_data, phase_settings[i], input);
    }
    return input;
}

llint task1(vector<llint> input_data){
    llint lo = 0; 
    llint hi = 5;
    vector<vector<llint>> possible_phase_settings = getPossiblePhaseSettings(lo, hi);
    llint best = 0;
    llint current;
    for (auto phase_settings : possible_phase_settings) {
        current = amplificationCircuit(input_data, phase_settings);
        if (current > best) best = current;
    }
    return best;
}

llint feedbackLoop(vector<llint> input_data, vector<llint> phase_settings) {
    llint input = 0;
    vector<Intcode> amplifiers;
    for (int i = 0; i < 5; i++) {
        amplifiers.push_back(Intcode(input_data));
        amplifiers[i].run(input);
        amplifiers[i].run(phase_settings[i]);
    }
    while (amplifiers[4].getStatus() != Status::Finished) {
        for(int i = 0; i < 5; i++) {
            amplifiers[i].run(input);
        }
    }
    return input;
}

llint task2(vector<llint> input_data){
    llint lo = 5; 
    llint hi = 10;
    vector<vector<llint>> possible_phase_settings = getPossiblePhaseSettings(lo, hi);
    llint best = 0;
    llint current;
    for (auto phase_settings : possible_phase_settings) {
        current = feedbackLoop(input_data, phase_settings);
        if (current > best) best = current;
    }
    return best;
}

int main(int argc, char *argv[]) {
    vector<llint> input_data = comma_separated("input7");
    cout << "Task 1: " << task1(input_data) << endl;
    cout << "Task 2: " << task2(input_data) << endl;
}
