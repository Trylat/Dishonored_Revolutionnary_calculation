nodes_list = [    
    {"name": "Node 1", "health": 10, "equipment": 0, "morale": 0, "supplies": 0, "training": 0},    
    {"name": "Node 2", "health": 0, "equipment": 50, "morale": 0, "supplies": 0, "training": 0},    
    {"name": "Node 3", "health": 0, "equipment": 0, "morale": 20, "supplies": 0, "training": 0},    
    {"name": "Node 4", "health": 0, "equipment": 0, "morale": 0, "supplies": 40, "training": 0},    
    {"name": "Node 5", "health": 0, "equipment": 0, "morale": 0, "supplies": 0, "training": 50},
    {"name": "Node 6", "health": 0, "equipment": 0, "morale": 0, "supplies": 0, "training": 30}
    ]

flows_list = [
    {'name': 'flow1', 'nodes': ["Node 1", "Node 3", "Node 6", "Node 4", "Node 2"]},
    {'name': 'flow2', 'nodes': ["Node 1", "Node 4", "Node 3", "Node 2", "Node 6"]},
    {'name': 'flow3', 'nodes': ["Node 5", "Node 4", "Node 2", "Node 3", "Node 1"]},
    {'name': 'flow4', 'nodes': ["Node 6", "Node 4", "Node 2", "Node 3", "Node 1"]}
]

negative_combinations = [
                        ("health", "supplies"), 
                        ("morale", "equipment"), 
                        ("training", "health"), 
                        ("supplies", "morale"), 
                        ("equipment", "training")
                        ]

positive_combinations = [
                        ("health", "morale"), 
                        ("morale", "training"), 
                        ("training", "supplies"), 
                        ("supplies", "equipment"), 
                        ("equipment", "health")
                        ]

pillar_list = [
               "health",
               "morale",
               "training",
               "supplies",
               "equipment",
              ]

