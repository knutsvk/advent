def scan(filename):
    with open(filename) as file:
        return file.read().splitlines()


def get_row(boarding_pass):
    return int(boarding_pass[:7].replace('F', '0').replace('B', '1'), 2)


def get_col(boarding_pass):
    return int(boarding_pass[7:].replace('L', '0').replace('R', '1'), 2)


def seat_id(row, col):
    return row * 8 + col


def task1():
    boarding_passes = scan("input5")
    seat_ids = [seat_id(get_row(bp), get_col(bp)) for bp in boarding_passes]
    print(max(seat_ids))


def task2():
    boarding_passes = scan("input5")
    unique_rows = set([get_row(bp) for bp in boarding_passes])
    rows = {row: [] for row in unique_rows }
    for bp in boarding_passes:
        rows[get_row(bp)].append(get_col(bp))
    row, occupied_seats = next(
        (k, v) for (k, v) in rows.items() if len(v) < 8 and k != min(unique_rows) and k != max(unique_rows)
    )
    col = next(i for i in range(8) if i not in occupied_seats)
    print(seat_id(row, col))


if __name__ == "__main__":
    task1()
    task2()
