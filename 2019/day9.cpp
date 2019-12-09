#include <iostream>
#include "intcode.hpp"
#include "read_input.hpp"
using namespace std;

int main(int argc, char *argv[]) {
    vector<llint> input_data = comma_separated("input9");
    Intcode intcode(input_data);
    llint inout = 0;
    while (intcode.getStatus() != Status::Finished) {
        intcode.run(inout);
        switch (intcode.getStatus()) {
            case Status::Finished:
                break;
            case Status::ReadyToGo:
                cout << inout << endl;
                break;
            case Status::WaitingForInput:
                cout << "Input: ";
                cin >> inout;
                break;
            default:
                return 1;
        }
    }
    return 0;
}
