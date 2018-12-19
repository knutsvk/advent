#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;


int main(int argc, char* argv[])
{
    int num_players = 405;
    int last_marble = 7170000;
    if(argc == 3)
    {
        num_players = atoi(argv[1]);
        last_marble = atoi(argv[2]);
    }
    cout << "Playing with " << num_players << " players until marble " << last_marble << " has been played." << endl;

    unsigned long long int scores[num_players] = {0ull};
    vector<int> marbles = {0};
    int current_pos = 0;
    int current_player = 0;
    int step = 0;
    while(step < last_marble)
    {
        if(step % 10000 == 0)
            cout << step << endl; 
        current_player = step % num_players;
        step++;
        if(step % 23 == 0)
        {
            current_pos -= 7;
            if(current_pos < 0)
                current_pos += marbles.size();
            scores[current_player] += step;
            scores[current_player] += marbles[current_pos];
            marbles.erase(marbles.begin() + current_pos);
        }
        else
        {
            if(current_pos == marbles.size() - 1)
                current_pos = 1;
            else
                current_pos += 2;
            marbles.insert(marbles.begin() + current_pos, step);
        }
    }
    cout << *max_element(scores, scores + num_players) << endl; 
}

// 18446462602351721784
