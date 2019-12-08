#include <iostream>
#include "intcode.hpp"
#include "read_input.hpp"
using namespace std;

vector<vector<int>> getPossiblePhaseSettings(int lo, int hi) {
    vector<vector<int>> possibilities;
    for (int i = lo; i < hi; i++) {
        for (int j = lo; j < hi; j++) {
            if (j == i) continue;
            for(int k = lo; k < hi; k++) {
                if (k == i or k == j) continue;
                for(int l = lo; l < hi; l++) {
                    if (l == i or l == j or l == k) continue;
                    for(int m = lo; m < hi; m++) {
                        if (m == i or m == j or m == k or m == l) continue;
                        vector<int> phase_settings = {i, j, k, l, m};
                        possibilities.push_back(phase_settings);
                    }
                }
            }
        }
    }
    return possibilities;
}

int amplifier(vector<int> input_data, int phase_setting, int input_value) {
    Intcode intcode(input_data);
    int dummy = 0;
    intcode.run(dummy);
    intcode.run(phase_setting);
    intcode.run(input_value);
    return input_value;
}

int amplificationCircuit(vector<int> input_data, vector<int> phase_settings) {
    int input = 0;
    for(int i = 0; i < 5; i++) {
        input = amplifier(input_data, phase_settings[i], input);
    }
    return input;
}

int task1(vector<int> input_data){
    int lo = 0; 
    int hi = 5;
    vector<vector<int>> possible_phase_settings = getPossiblePhaseSettings(lo, hi);
    int best = 0;
    int current;
    for (auto phase_settings : possible_phase_settings) {
        current = amplificationCircuit(input_data, phase_settings);
        if (current > best) best = current;
    }
    return best;
}

int feedbackLoop(vector<int> input_data, vector<int> phase_settings) {
    int input = 0;
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

int task2(vector<int> input_data){
    int lo = 5; 
    int hi = 10;
    vector<vector<int>> possible_phase_settings = getPossiblePhaseSettings(lo, hi);
    int best = 0;
    int current;
    for (auto phase_settings : possible_phase_settings) {
        current = feedbackLoop(input_data, phase_settings);
        if (current > best) best = current;
    }
    return best;
}

int main(int argc, char *argv[]) {
    vector<int> input_data = comma_separated("input7");
    cout << "Task 1: " << task1(input_data) << endl;
    cout << "Task 2: " << task2(input_data) << endl;
}
