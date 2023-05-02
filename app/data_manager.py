from app.score import RevolutionScore
from app.utils import *
import json
import os

class RevolutionData:
    def __init__(self):
        self.flows = []
        self.nodes = []
        self.current_score = RevolutionScore()
        self.turn_number = 0

    def add_flow(self, flow):
        self.flows.append(flow)

    def add_node(self, node):
        self.nodes.append(node)

    def save_data(self, file_name):
        data = {
            "current_score": self.current_score.score,
            "turn_number" : self.turn_number,
            "flows": [],
            "nodes": []
        }

        for flow in self.flows:
            flow_data = {
                "name": flow.name,
                "nodes": []
            }

            for node in flow.nodes:
                # Find the corresponding node in the top-level node list
                for top_node in self.nodes:
                    if top_node.name == node.name:
                        node_data = {
                            "name": node.name,
                            "stats": top_node.stats
                        }
                        flow_data["nodes"].append(node_data)
                        break

            data["flows"].append(flow_data)

        for node in self.nodes:
            node_data = {
                "name": node.name,
                "stats": node.stats
            }
            data["nodes"].append(node_data)

        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, sort_keys=True, ensure_ascii=False)

    @classmethod
    def from_file(cls, file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)

        revolution_data = cls()
        revolution_data.current_score.score = data["current_score"]
        revolution_data.turn_number = data["turn_number"]

        for flow_data in data["flows"]:
            flow = ResistanceFlow(flow_data["name"])

            for node_data in flow_data["nodes"]:
                node = ResistanceNodes(node_data["name"], **node_data["stats"])
                flow.add_node(node)

            revolution_data.add_flow(flow)
        
        for node_data in data["nodes"]:
            node_name = node_data["name"]
            node_stats = node_data["stats"]
            node = ResistanceNodes(node_name, **node_stats)
            revolution_data.add_node(node)

        return revolution_data
    
    def end_turn(self, file_name_prefix):
        self.turn_number += 1
        file_name = f"{file_name_prefix}_{self.turn_number}.json"
        previous_file_name = f"{file_name_prefix}_{self.turn_number-1}.json"
        
        if os.path.isfile(previous_file_name):
            previous_data = self.from_file(previous_file_name)
            previous_score = previous_data.current_score
            # Re-Calculate the flow score
            for flow in self.flows:
                flow.get_stats_sum()
                self.current_score.calculate_flow_score(flow)
            # Add previous score from save to the new score
            self.current_score.score + previous_score.score

        self.save_data(file_name)
