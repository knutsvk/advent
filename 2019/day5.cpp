#include <iostream>
#include "intcode.hpp"
#include "read_input.hpp"
using namespace std;

int day5(const vector<int> &input_data, int system_id) {
    Intcode intcode(input_data);
    int inout = 0;
    while (intcode.getStatus() != Status::Finished) {
        intcode.run(inout);
        switch (intcode.getStatus()) {
            case Status::Finished:
                break;
            case Status::ReadyToGo:
                cout << inout << endl;
                break;
            case Status::WaitingForInput:
                inout = system_id;
                break;
            default:
                return 1;
        }
    }
    return 0;
}

int main(int argc, char *argv[]) {
    vector<int> input_data = comma_separated("input5");
    cout << "Task 1: " << endl;
    day5(input_data, 1);
    cout << endl;
    cout << "Task 2: " << endl;
    day5(input_data, 5);
    cout << endl;
}
