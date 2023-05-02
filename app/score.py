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

        for i in range(len(flow.nodes) - 1):  # Loop through all nodes in the flow
            current_node = flow.nodes[i]
            next_node = flow.nodes[i + 1]
            current_node_score = current_node.stats[current_node.get_non_null_stats()[0]]  # Get the score for the current node
            next_node_score = next_node.stats[next_node.get_non_null_stats()[0]]  # Get the score for the next node

            if next_node_score < current_node_score:  # If the score for the next node is lower than the current node
                diff = int((current_node_score - next_node_score)/2)
                print(f"{next_node_score} < {current_node_score}: Remouve {diff}")
                current_score -=  diff  # Subtract half of the difference from the current score

            elif next_node_score > current_node_score:  # If the score for the next node is higher than the current node
                diff = int((next_node_score - current_node_score)/2)
                print(f"{next_node_score} > {current_node_score}: Add {diff}")
                current_score += diff  # Add half of the difference to the current score

            else:  # If the scores are equal
                print("No difference")
                current_score = current_score
            print(f"Current Score = {current_score}")
                
        if all(node.get_non_null_stats() for node in flow.nodes) and current_score > 0:  # If all nodes have non-null stats and the final score is positive
            self.score += current_score  # Add the final score to the overall score
            return self.score

    
    def manual_score_update(self, value):
        self.score = value
    
    def add_to_prev_score(self):
        self.score += self.prev_score  # Add the current score to the previous score
        self.prev_score = 0  # Reset the previous score to 0 after adding it to the current score
