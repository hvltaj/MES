from classes import Node, Element
from collections import OrderedDict
import operator
import numpy as np


class FileParser(object):

    def __init__(self, filename):
        self.filename = filename
        self.nodes = {}
        self.elements = OrderedDict()

    def parse_file(self):
        with open(self.filename, 'r') as f:
            number_of_nodes = int(f.readline().split(" ")[0])
            for item in range(number_of_nodes):
                line = f.readline().split(" ")
                node = Node(
                    int(line[0]),
                    float(line[1])
                )
                self.nodes[node.number] = node

            number_of_elements = int(f.readline().split(" ")[0])
            for item in range(number_of_elements):
                line = f.readline().split(" ")
                element = Element(
                    int(line[0]),
                    self.nodes[int(line[1])],
                    self.nodes[int(line[2])],
                    float(line[3]),
                    float(line[4])
                )
                self.elements[element.number] = element

            number_of_bc = int(f.readline().split(" ")[0])

            for item in range(number_of_bc):
                line = f.readline().split(" ")
                self.nodes[int(line[0])].BC = int(line[1])
                self.nodes[int(line[0])].BC_value = float(line[2])
                if len(line) > 3:
                    self.nodes[int(line[0])].BC_value2 = float(line[3])

            for element in data.elements.values():
                element.calculate_p_local()
                element.calculate_h_local()

            self.elements = sorted(
                self.elements.values(),
                key=operator.attrgetter('start')
            )


def fill_h_global(sorted_elements_list):
    number_of_elements = len(sorted_elements_list)
    H_global = [[0 for a in range(number_of_elements + 1)] for a in
                range(number_of_elements + 1)]

    for number in range(number_of_elements):
        H_local = sorted_elements_list[number].H_local
        H_global[number][number] += H_local[0][0]
        H_global[number][number+1] += H_local[0][1]
        H_global[number+1][number] += H_local[1][0]
        H_global[number+1][number+1] += H_local[1][1]

    return H_global


def fill_p_global(sorted_elements_list):
    number_of_elements = len(sorted_elements_list)
    P_global = [0 for a in range(number_of_elements + 1)]

    for number in range(number_of_elements):
        P_local = sorted_elements_list[number].P_local

        P_global[number] += P_local[0]
        P_global[number+1] += P_local[1]

    return P_global


def fill_matrix(H_global, P_global):
    number_of_elements = len(P_global)
    matrix = [[0 for a in range(number_of_elements)] for a in
                range(number_of_elements)]

    for row in range(number_of_elements):
        for column in range(number_of_elements):
            matrix[row][column] = H_global[row][column] + P_global[column]

    return matrix


data = FileParser("../tests/input_file.txt")
data.parse_file()

H_global = np.array(fill_h_global(data.elements))
P_global = np.array([item * -1 for item in fill_p_global(data.elements)])

result = np.linalg.solve(H_global, P_global)
print(H_global)
print(P_global)
print(result)





