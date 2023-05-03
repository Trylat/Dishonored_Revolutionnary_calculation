from app.flow import *

class RevolutionScore:
    def __init__(self):
        self.score = 0  # Initialize the score value to 0
        self.prev_score = 0  # Initialize the previous score value to 0
    
    def calculate_flow_score(self, flow:ResistanceFlow):
        print(f"{flow.name}")
        start_node = flow.nodes[0]  
        current_score = start_node.stats[start_node.get_non_null_stats()[0]]  # Get the initial score from the first node
        print(f"Initial Score = {current_score}")
        checklist = {}
        for node in flow.nodes:  # If all nodes have non-null stats and the final score is positive
            checklist[node.get_non_null_stats()[0]] = node.stats[node.get_non_null_stats()[0]]

        check_keys = list(checklist.keys()) # This compare that all pillar exist sins if they are all pillars in Check_keys, theys are not null.
        pillar_number = len(pillar_list)
        
        if len(check_keys) == pillar_number:
            for i in range(len(flow.nodes) - 1):  # Loop through all nodes in the flow
                print(f"i = {i}")
                current_node = flow.nodes[i]
                next_node = flow.nodes[i + 1]
                current_node_score = current_node.stats[current_node.get_non_null_stats()[0]]  # Get the score for the current node
                next_node_score = next_node.stats[next_node.get_non_null_stats()[0]]  # Get the score for the next node

                if next_node_score < current_node_score:  # If the score for the next node is lower than the current node
                    diff = int((current_node_score - next_node_score)/2)
                    print(f"{next_node_score} < {current_node_score}: Remouve {diff} to {current_score}")
                    current_score -=  diff  # Subtract half of the difference from the current score

                elif next_node_score > current_node_score:  # If the score for the next node is higher than the current node
                    diff = int((next_node_score - current_node_score)/2)
                    print(f"{next_node_score} > {current_node_score}: Add {diff} to {current_score}")
                    current_score += diff  # Add half of the difference to the current score

                else:  # If the scores are equal
                    print("No difference")
                    current_score = current_score

                print(f"Add {current_score} to total Score {self.score}")
                self.score += current_score # Add the final score to the overall score
                print(f"Score Total = {self.score}")

            return self.score
        else:
            print("Not all pillar are in this flow. No score apply")

    
    def manual_score_update(self, value):
        self.score = value
