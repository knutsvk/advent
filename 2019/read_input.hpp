#include <cstdlib>
#include <fstream>
#include <sstream>

using namespace std;

vector<llint> comma_separated(const string& filename) {
    vector<llint> data;
    ifstream infile (filename);
    string line;
    while (getline(infile, line)) {
        stringstream linestream(line);
        string value;
        while (getline(linestream, value, ',')) {
            data.push_back(stoll(value));
        }
    }
    return data;
}
