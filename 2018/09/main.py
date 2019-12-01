if __name__ == "__main__":
    num_players = 405
    last_marble = 7170000
    ans = "%d players; last marble is worth %d points: " % (num_players, last_marble)

    scores = [0] * num_players
    marbles = [0]
    current_pos = 0
    current_player = '-'
    step = 0
    while step < last_marble:
        if step % 10000 == 0:
            print(step)
#        print("%d [%s]\t" % (step, current_player), end="")
#        for i, marble in enumerate(marbles):
#            if i == current_pos:
#                print("(%d)" % marble, end="")
#            else:
#                print(" %d " % marble, end="")

        current_player = step % num_players
        step += 1

        if step % 23 == 0:
            current_pos -= 7
            if current_pos < 0:
                current_pos += len(marbles)
            scores[current_player] += step
            scores[current_player] += marbles[current_pos]
            del marbles[current_pos]

        else:
            if current_pos == len(marbles) - 1:
                current_pos = 1
            else:
                current_pos += 2
            marbles.insert(current_pos, step)
    ans += "high scores is %d" % max(scores)
    print(ans)
