from app.nodes import ResistanceNodes
from app.constants import *
from app.utils import *

class testNode:
    def __init__(self):
        self.node1 = ResistanceNodes('Node A', health=50)
        self.nodes = multinode()
        self.test_sequence()

    def test_sequence(self):
        print(self.node1.name, self.node1.get_stats())
        for node in self.nodes:
            print(node.name, node.get_non_null_stats()[0])

class testFlow:
    def __init__(self):
        self.nodes = multinode()
        self.flows = multiflow(self.nodes)

        for flow in self.flows:
            print(flow.name)
            for node in flow.nodes:
                print(node.name, node.get_non_null_stats()[0])

        for flow in self.flows:
            print(flow.get_stats_sum())

if __name__ == '__main__':
    NodeTest = testNode()
    FlowTest = testFlow()