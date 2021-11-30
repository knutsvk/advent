PREAMBLE_LENGTH = 25


with open("input9") as file:
    data = [int(x) for x in file.read().splitlines()]


def find_invalid_number():
    for i in range(len(data)):
        preamble = data[i : i + PREAMBLE_LENGTH]
        preamble_sums = [x + y for x in preamble for y in preamble]
        if data[i + PREAMBLE_LENGTH] not in preamble_sums:
            return data[i + PREAMBLE_LENGTH]


def find_contiguous_range(target):
    for i in range(len(data)):
        for j in range(i, len(data)):
            if sum(data[i:j]) > target:
                break
            if sum(data[i:j]) == target:
                return data[i:j]


if __name__ == "__main__":
    invalid_number = find_invalid_number()
    print(invalid_number)
    contiguous_range = find_contiguous_range(invalid_number)
    print(min(contiguous_range) + max(contiguous_range))
