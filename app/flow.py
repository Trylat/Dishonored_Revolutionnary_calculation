from app.nodes import ResistanceNodes
from app.constants import *

class ResistanceFlow:
    def __init__(self, name, nodes = None):
        self.name = name
        if nodes:
            self.nodes = nodes
        else:
            self.nodes = []

    def add_node(self, node:ResistanceNodes):
        if node not in self.nodes:
            self.nodes.append(node)
        else:
            print("This node is already in this flow !!")

    def remove_node(self, node:ResistanceNodes):
        if node in self.nodes:
            self.nodes.remove(node)
        else:
            print("This node is not in this flow !!")

    def insert_node(self, index, node:ResistanceNodes):
        if node not in self.nodes:
            self.nodes.insert(index, node)
        else:
            print("This node is already in the flow")

    def display_nodes(self):
        for node in self.nodes:
            print(node.name)

    def get_stats_sum(self):
        stats_sum = {"health": 0, "equipment": 0, "morale": 0, "supplies": 0, "training": 0}
        total_sum = 0  # initial total_sum
        for i, node in enumerate(self.nodes):
            # Sum up each stat for all nodes
            stats_sum["health"] += node.stats["health"]
            stats_sum["equipment"] += node.stats["equipment"]
            stats_sum["morale"] += node.stats["morale"]
            stats_sum["supplies"] += node.stats["supplies"]
            stats_sum["training"] += node.stats["training"]
            
            # If this is not the first node
            if i > 0:
                prev_node = self.nodes[i-1]
                prev_stat_name = prev_node.get_non_null_stats()[0]
                node_stat_name = node.get_non_null_stats()[0]
                
                # Check if this is a negative combination of stats
                if (prev_stat_name, node_stat_name) in negative_combinations:
                    print(f"{prev_stat_name} followed by {node_stat_name} is a negative combination")
                    # Subtract half of the previous stat value from the current stat value
                    stats_sum[node_stat_name] -= int(prev_node.stats[prev_stat_name]/2)
                    
                # Check if this is a positive combination of stats
                elif (prev_stat_name, node_stat_name) in positive_combinations:
                    print(f"{prev_stat_name} followed by {node_stat_name} is a positive combination")
                    # Add half of the previous stat value to the current stat value
                    stats_sum[node_stat_name] += int(prev_node.stats[prev_stat_name]/2)
            
            # Check if all stats are non-zero
            if all(stats_sum.values()):
                # If so, add the sum of all stats to the total sum
                total_sum += sum(stats_sum.values())
        
        # Return the stats sum and the total sum
        return stats_sum, total_sum


