def scan(filename):
    with open(filename) as file:
        return sorted([seat_id(boarding_pass) for boarding_pass in file.read().splitlines()])


def seat_id(boarding_pass):
    return int(boarding_pass.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2)


if __name__ == "__main__":
    seats = scan("input5")
    print(f"task 1: {max(seats)}")
    for i in range(len(seats)):
        if seats[i] != seats[i+1] - 1:
            print(f"task 2: {seats[i+1] - 1}")
            break
