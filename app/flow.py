from app.nodes import ResistanceNodes
from app.constants import *

class ResistanceFlow:
    def __init__(self, name, nodes = None):
        self.name = name
        if nodes:
            self.nodes = [node.clone() for node in nodes]
        else:
            self.nodes = []

    def add_node(self, node:ResistanceNodes):
        if node not in self.nodes:
            self.nodes.append(node.clone())
        else:
            print("This node is already in this flow !!")

    def remove_node(self, node:ResistanceNodes):
        if node in self.nodes:
            self.nodes.remove(node)
        else:
            print("This node is not in this flow !!")

    def insert_node(self, index, node:ResistanceNodes):
        if node not in self.nodes:
            self.nodes.insert(index, node.clone())
        else:
            print("This node is already in the flow")

    def display_nodes(self):
        print(self.name)
        for node in self.nodes:
            stat_name = node.get_non_null_stats()[0]
            print(node.name, stat_name, node.stats[stat_name])
    
    def get_stats_sum(self):
        #total_sum = 0  # initial total_sum
        for i, node in enumerate(self.nodes):
            temp_stats = {"health": 0, "equipment": 0, "morale": 0, "supplies": 0, "training": 0}
            # Sum up each stat for all nodes
            temp_stats["health"] = node.stats["health"]
            temp_stats["equipment"] = node.stats["equipment"]
            temp_stats["morale"] = node.stats["morale"]
            temp_stats["supplies"] = node.stats["supplies"]
            temp_stats["training"] = node.stats["training"]

            node_stat_name = node.get_non_null_stats()[0]
            # If this is not the first node
            if i > 0:
                prev_node = self.nodes[i-1]
                prev_stat_name = prev_node.get_non_null_stats()[0]
                
                # Check if this is a negative combination of stats
                if (prev_stat_name, node_stat_name) in negative_combinations:
                    print(f"{prev_stat_name} followed by {node_stat_name} is a negative combination")
                    print(f"Remouve {int(prev_node.stats[prev_stat_name]/2)} to {temp_stats[node_stat_name]}")
                    # Subtract half of the previous stat value from the current stat value
                    temp_stats[node_stat_name] -= int(prev_node.stats[prev_stat_name]/2)
                    
                # Check if this is a positive combination of stats
                elif (prev_stat_name, node_stat_name) in positive_combinations:
                    print(f"{prev_stat_name} followed by {node_stat_name} is a positive combination")
                    print(f"Add {int(prev_node.stats[prev_stat_name]/2)} to {temp_stats[node_stat_name]}")
                    # Add half of the previous stat value to the current stat value
                    temp_stats[node_stat_name] += int(prev_node.stats[prev_stat_name]/2)

            # Set the new node value
            node.stats[node_stat_name] = temp_stats[node_stat_name]
            #print(node.name, node_stat_name, node.stats[node_stat_name])
        
    


