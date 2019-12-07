#include <iostream>
#include "intcode.hpp"
#include "read_input.hpp"
using namespace std;

int task1(vector<int> program) {
    intcode(program);
    return 0;
}

int main(int argc, char *argv[]) {
    vector<int> input_data = comma_separated("input5");
    intcode(input_data);
}
