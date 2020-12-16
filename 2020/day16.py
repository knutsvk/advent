def get_input(filename):
    with open(filename) as file:
        data = file.read()
        rule_input, tickets = data.split('your ticket:')
        my_ticket_input, nearby_ticket_input = tickets.split('nearby tickets:')
    rules = {
        rule.split(":")[0]: [
            {"start": int(interval.split("-")[0]), "end": int(interval.split("-")[1])}
            for interval in rule.split(":")[1].split(" or ")
        ]
        for rule in rule_input.split("\n")[:-2]
    }
    my_ticket = [int(x) for x in next(rule for rule in my_ticket_input.split("\n") if len(rule) > 2).split(',')]
    nearby_tickets = [[int(x) for x in ticket.split(",")] for ticket in nearby_ticket_input.split("\n")[1:]]
    return rules, my_ticket, nearby_tickets


def is_potentially_valid(value, rules):
    for intervals in rules.values():
        if satisfies_rule(value, intervals):
            return True
    return False


def satisfies_rule(value, intervals):
    for interval in intervals:
        if interval["start"] <= value <= interval["end"]:
            return True
    return False


if __name__ == "__main__":
    rules, my_ticket, nearby_tickets = get_input("input16")

    print(sum([value for ticket in nearby_tickets for value in ticket if not is_potentially_valid(value, rules)]))

    nearby_tickets = [ticket for ticket in nearby_tickets if all([is_potentially_valid(value, rules) for value in ticket])]
    identified_rules = {}
    while rules:
        for i in range(len(my_ticket)):
            potential_rules = []
            for field, intervals in rules.items():
                if all([satisfies_rule(ticket[i], intervals) for ticket in nearby_tickets]):
                    potential_rules.append(field)
            if len(potential_rules) == 1:
                identified_rules[i+1] = potential_rules[0]
                del rules[potential_rules[0]]

    relevant_identified_keys = [key for key, val in identified_rules.items() if val[:9] == "departure"]
    answer = 1
    for value in relevant_identified_keys:
        answer *= my_ticket[value-1]
    print(answer)