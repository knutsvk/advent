import numpy as np

class Node(object):
    def __init__(self, data):
        self.children = []
        self.metadata = []
        i = 2
        for c in range(data[0]):
            self.children.append(Node(data[i:]))
            i += self.children[c].datalength()
        for j in range(data[1]):
            self.metadata.append(data[i + j])
        if data[0] == 0:
            self.value = sum(self.metadata)
        else:
            self.value = 0
            for entry in self.metadata:
                if entry <= len(self.children):
                    self.value += self.children[entry-1].value


    def __str__(self):
        string = str(self.metadata)
        for child in self.children:
            string += child.__str__()
        return string

    
    def datalength(self):
        length = 2 + len(self.metadata)
        for child in self.children:
            length += child.datalength()
        return length

    
    def sum_metadata(self):
        ans = 0
        ans = sum(self.metadata)
        for child in self.children:
            ans += child.sum_metadata()
        return ans
        

if __name__ == "__main__":
    data = np.loadtxt("input", dtype=int)
    tree = Node(data)
    print(tree.sum_metadata())
    print(tree.value)
