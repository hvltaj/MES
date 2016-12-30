class Node(object):

    def __init__(self, number, position, bc=0, bc_value=0, bc_value2=0):
        self.number = number
        self.position = position
        self.BC = bc
        self.BC_value = bc_value
        self.BC_value2 = bc_value2


class Element(object):

    def __init__(self, number, node1, node2, s, k):
        self.number = number
        self.node1 = node1
        self.node2 = node2
        self.S = s
        self.K = k
        self.H_local = [[0, 0], [0, 0]]
        self.P_local = [0, 0]
        self.start = self.node1.position

        self.length = (self.node2.position - self.node1.position)
        self.C = 1.0 * self.S * self.K / self.length

    def calculate_h_local(self):
        self.H_local[0][0] = self.C
        self.H_local[0][1] = self.C * -1
        self.H_local[1][0] = self.C * -1
        self.H_local[1][1] = self.C + self.node2.BC_value

    def calculate_p_local(self):
        self.P_local[0] = self.node1.BC_value
        self.P_local[1] = self.node2.BC_value2
