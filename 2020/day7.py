with open("input7") as file:
    data = file.read().splitlines()


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


def contains_shiny_gold(bag_type):
    if bag_type == "shiny gold":
        return True
    for rule in bag_rules[bag_type]:
        if contains_shiny_gold(rule[0]):
            return True
    return False


def count_bags(bag_type):
    total = 1
    for rule in bag_rules[bag_type]:
        total += rule[1] * count_bags(rule[0])
    return total


if __name__ == "__main__":
    print(len([key for key in bag_rules.keys() if contains_shiny_gold(key)]) - 1)
    print(count_bags("shiny gold") - 1)
