with open("input7") as file:
    data = file.read().splitlines()


def task1():
    loop_again = True
    old_bags = []
    bags_found = []
    bags_to_find = ["shiny gold"]
    while loop_again:
        loop_again = False
        for bag_to_find in bags_to_find:
            for rule in data:
                containing_bag = rule.split("bags")[0][:-1]
                contained_bags = [description.lstrip().rstrip()[2:].replace("bag", "").rstrip() for description in
                                  "".join(rule.split("bags")[1:]).replace("contain", "").replace("bag.", "").replace(
                                      " .", "").split(",")]
                if bag_to_find in contained_bags and containing_bag not in bags_found + old_bags:
                    loop_again = True
                    bags_found.append(containing_bag)
            old_bags.append(bag_to_find)
        bags_to_find = bags_found
        bags_found = []
    print(len(set(old_bags)) - 1)


bag_rules = {}
for rule in data:
    key = rule.split("bags")[0][:-1]
    bag_rules[key] = []
    for desc in "".join(rule.split("bags")[1:]).replace("contain", "").replace("bag.", "").replace(" .", "").split(","):
        simple_description = desc.lstrip().rstrip().replace("bag", "").rstrip()
        if simple_description != "no other":
            num_bags = int(simple_description[0])
            bag_type = simple_description[2:]
            bag_rules[key].append((bag_type, num_bags))


def count_bags(bag_type):
    total = 1
    for rule in bag_rules[bag_type]:
        total += rule[1] * count_bags(rule[0])
    return total


def task2():
    print(count_bags("shiny gold") - 1)


if __name__ == "__main__":
    task1()
    task2()
