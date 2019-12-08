#include <iostream>
#include "intcode.hpp"
#include "read_input.hpp"
using namespace std;

void task1(vector<int> input_data){
    vector<int> settings = {2, 0};
    int best = 0;
    int output_0, output_1, output_2, output_3, output_4;
    for (int i = 0; i < 5; i++) {
        vector<int> settings = {i, 0};
        output_0 = intcode(input_data, settings, false);
        for(int j = 0; j < 5; j++) {
            if (j == i) continue;
            settings = {j, output_0};
            output_1 = intcode(input_data, settings, false);
            for(int k = 0; k < 5; k++) {
            if (k == i or k == j) continue;
                settings = {k, output_1};
                output_2 = intcode(input_data, settings, false);
                for(int l = 0; l < 5; l++) {
                    if (l == i or l == j or l == k) continue;
                    settings = {l, output_2};
                    output_3 = intcode(input_data, settings, false);
                    for(int m = 0; m < 5; m++) {
                        if (m == i or m == j or m == k or m == l) continue;
                        settings = {m, output_3};
                        output_4 = intcode(input_data, settings, false);
                        if (output_4 > best) {
                            best = output_4;
                            cout << "New best from " 
                                << i << " " << j << " " << k << " " << l << " " << m << ": " 
                                << best << endl; 
                        }
                    }
                }
            }
        }
    }
}

int main(int argc, char *argv[]) {
    vector<int> input_data = comma_separated("input7");
    task1(input_data);
    // task2(input_data);
}
