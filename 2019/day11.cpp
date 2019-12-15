int main(int argc, char *argv[]) {
    vector<llint> input_data = comma_separated("input11");
    Intcode intcode(input_data);
    Robot robot();
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
