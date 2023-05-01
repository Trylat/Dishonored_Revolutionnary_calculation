from app.nodes import ResistanceNodes
from app.constants import *

class testNode:
    def __init__(self):
        self.node1 = ResistanceNodes('Node A', health=50)
        self.nodes = []
        self.multinode()
        self.test_sequence()

    def multinode(self):
        self.nodes = []
        for node_data in nodes_list:
            node = ResistanceNodes(**node_data)
            self.nodes.append(node)

    def test_sequence(self):
        print(self.node1.name, self.node1.get_stats())
        for node in self.nodes:
            print(node.name, node.get_stats())
        

if __name__ == '__main__':
    NodeTest = testNode()