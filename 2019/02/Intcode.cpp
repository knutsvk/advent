int add(int x, int y) {
    return x + y;
}

int multiply(int x, int y) {
    return x * y;
}

void runIntcode(int& data) {
    int pos = 0;
    while (data[pos] != 99) {
        int instruction = data[pos];
        int x = data[pos+1];
        int y = data[pos+2];
        int destination = data[pos+3];
        if (instruction == 1) {
            data[destination] = add(x, y);
        } else if (instruction == 1) {
            data[destination] = add(x, y);
        }
        pos += 4;
    }
}

void main() {
    // read data

}
