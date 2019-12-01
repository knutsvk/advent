import numpy as np

if __name__ == "__main__":
    data = np.loadtxt("input", dtype=int)
    # Task 1
    print(sum(data))

    # Task 2
    foundit = False
    freq = [0]
    loop = 0
    while(not foundit):
        print("loop %d" % loop)
        for i, x in enumerate(data):
            new_freq = freq[loop*len(data) + i] + x
            if new_freq in freq:
                print(new_freq)
                foundit = True
                break
            else: 
                freq.append(new_freq)
        loop += 1
