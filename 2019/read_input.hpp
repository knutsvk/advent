#include <cstdlib>
#include <fstream>
#include <sstream>

using namespace std;

vector<int> comma_separated(string filename) {
    vector<int> data;
    ifstream infile (filename);
    string line;
    while (getline(infile, line)) {
        stringstream linestream(line);
        string value;
        while (getline(linestream, value, ',')) {
            data.push_back(stoi(value));
        }
    }
    return data;
}
