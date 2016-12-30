from classes import Node, Element
from collections import OrderedDict
import operator


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
                    int(line[1])
                )
                self.nodes[node.number] = node

            number_of_elements = int(f.readline().split(" ")[0])
            for item in range(number_of_elements):
                line = f.readline().split(" ")
                element = Element(
                    int(line[0]),
                    self.nodes[int(line[1])],
                    self.nodes[int(line[2])],
                    int(line[3]),
                    int(line[4])
                )
                self.elements[element.number] = element

            number_of_bc = int(f.readline().split(" ")[0])

            for item in range(number_of_bc):
                line = f.readline().split(" ")
                self.nodes[int(line[0])].BC = int(line[1])
                self.nodes[int(line[0])].BC_value = int(line[2])
                if len(line) > 3:
                    self.nodes[int(line[0])].BC_value2 = int(line[3])


data = FileParser("../tests/input_file.txt")
data.parse_file()

for element in data.elements.values():
    element.calculate_p_local()
    element.calculate_h_local()

list_of_sorted_elements = sorted(data.elements.values(), key=operator.attrgetter('start'))
print( [c.H_local for c in list_of_sorted_elements])

