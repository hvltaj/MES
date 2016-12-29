class Node(object):

    def __init__(self, number, position, BC=0):
        self.number = number
        self.position = position
        self.BC = BC


class Element(object):

    def __init__(self, number, node1, node2, S, K):
        self.number = number
        self.node1 = node1
        self.node2 = node2
        self.S = S
        self.K = K