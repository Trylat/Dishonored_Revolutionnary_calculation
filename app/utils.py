from app.constants import *
from app.nodes import ResistanceNodes
from app.flow import ResistanceFlow
import json

def multinode():
    nodes = []
    for node_data in nodes_list:
        node = None
        node = ResistanceNodes(**node_data)
        if node:
            nodes.append(node)
    return nodes


def multiflow(nodes_list):
        flows = []
        for flow_dict in flows_list:
            flow_name = flow_dict['name']
            node_names = flow_dict['nodes']
            nodes = []

            for node_name in node_names:
                node = next((n for n in nodes_list if n.name == node_name), None)
                if node:
                    nodes.append(node)
                else:
                    print(f"Error: node {node_name} does not exist")

            if len(nodes) == len(node_names):
                flow = ResistanceFlow(flow_name, nodes)
                flows.append(flow)
            else:
                print("Error not the same number of node than what was suppose to be in flow")

        return flows


def write_to_json(flows:list, file_path: str):
    flow_state_list = []
    for flow in flows:
        flow_state = {
            "name"  : flow.name,
            "nodes" : [node.stats for node in flow.nodes],
        }
        flow_state_list.append(flow_state)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(flow_state_list, f, indent=4, sort_keys=True, ensure_ascii=False)


def read_from_json(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if not data:
        print(f"File {file_path} is empty.")
    return data
