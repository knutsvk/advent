import sys


if __name__ == "__main__":
    inputdata = "047801"
    if len(sys.argv) > 1:
        inputdata = sys.argv[1]

    print("Doing the heavy lifting...")
    positions = [0,1]
    recipes = "37"
    while(inputdata not in recipes[-7:]):
        recipes += str(sum([int(recipes[pos]) for pos in positions]))
        positions = [(pos + int(recipes[pos]) + 1) % len(recipes) for pos in positions]

    print("Task 1: %s" % recipes[int(inputdata):int(inputdata)+10])
    print("Task 2: %d" % recipes.find(inputdata))
