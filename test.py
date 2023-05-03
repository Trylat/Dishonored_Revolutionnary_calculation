from app.nodes import ResistanceNodes
from app.score import RevolutionScore
from app.data_manager import RevolutionData
from gui.gui import Interface
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
        self.test_sequence()

    def test_sequence(self):
        for flow in self.flows:
            print(flow.name)
            for node in flow.nodes:
                print(f"    {node.name, node.get_non_null_stats()[0]}")

        # Apply modifier to node based on node order and node stats
        for flow in self.flows:
            print("===============================")
            print(flow.name)
            print("---------Initial:")
            flow.display_nodes()
            print("---------Apply modifier:")
            flow.get_stats_sum()
            print("---------Updated:")
            flow.display_nodes()

class testScore:
    def __init__(self):
        self.nodes = multinode()
        self.flows = multiflow(self.nodes)
        self.score = RevolutionScore()
        self.test_sequence()
    
    def test_sequence(self):
        print("++++++++++SCORE CALCULATION+++++++++++")
        for flow in self.flows:
            print("=====================================")
            flow.get_stats_sum()
            print("=====================================")
            self.score.calculate_flow_score(flow)
            print(f"Score = {self.score.score}")
            
class testSave:
    def __init__(self):
        # Create RevolutionData instance
        self.rev_data = RevolutionData()
        # Creade World data
        self.nodes = multinode()
        self.flows = multiflow(self.nodes)
        self.score = RevolutionScore()

        self.test_sequence()

    def test_sequence(self):
        for flow in self.flows:
            flow.get_stats_sum()
            self.score.calculate_flow_score(flow)
        
        # Add Revolution score
        self.rev_data.current_score = self.score

        # Add nodes
        for node in self.nodes:
            self.rev_data.add_node(node)

        # Add flows
        for flow in self.flows:
            self.rev_data.add_flow(flow)

        # Save data to file
        self.rev_data.save_data("revolution_data.json")

        # Load data from json
        print("TEST LOAD DATA===============")
        rev_data_2 = RevolutionData.from_file("revolution_data.json")
        print("EXTRACTED DATA========================")
        print(f"Score: {rev_data_2.current_score.score}")
        print(f"Turn Number: {rev_data_2.turn_number}")
        print(f"Flows:")
        for flow in rev_data_2.flows:
            flow.display_nodes()
        print(f"Nodes:")
        for node in rev_data_2.nodes:
            stat_name = node.get_non_null_stats()[0]
            print(node.name, stat_name, node.stats[stat_name])

        # Next_Turn No change
        rev_data_2.end_turn("save")
        # modify node
        new_node = ResistanceNodes("Node 8", health=80)
        rev_data_2.add_node(new_node)
        rev_data_2.end_turn("save")
        # Modify flow
        rev_data_2.flows[1].insert_node(2,rev_data_2.nodes[-1])
        rev_data_2.end_turn("save")
        # Load modify data2
        print("extract new data")

        print("EXTRACTED DATA========================")
        file_name = f"save_{rev_data_2.turn_number}.json"
        rev_data_3 = RevolutionData.from_file(file_name)
        print(f"Score: {rev_data_3.current_score.score}")
        print(f"Turn Number: {rev_data_3.turn_number}")
        print(f"Flows:")
        for flow in rev_data_3.flows:
            flow.display_nodes()
        print(f"Nodes:")
        for node in rev_data_3.nodes:
            stat_name = node.get_non_null_stats()[0]
            print(node.name, stat_name, node.stats[stat_name])

class testGui:
    def __init__(self):
        # Create RevolutionData instance
        self.rev_data = RevolutionData()
        # Creade World data
        self.nodes = multinode()
        self.flows = multiflow(self.nodes)
        self.score = RevolutionScore()

        # Add Revolution score
        self.rev_data.current_score = self.score
        # Add nodes
        for node in self.nodes:
            self.rev_data.add_node(node)
        # Add flows
        for flow in self.flows:
            self.rev_data.add_flow(flow)

        # Create GUI
        self.gui = Interface(self.rev_data)
        self.gui.run()


        

if __name__ == '__main__':
    #NodeTest = testNode()
    #FlowTest = testFlow()
    #ScoreTest = testScore()
    #SaveTest = testSave()
    DisplayTest = testGui()