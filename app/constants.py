nodes_list = [    
    {"name": "Clinique de Janne",
     "health": 3, 
     "equipment": 0,
     "morale": 0, 
     "supplies": 0, 
     "training": 0
     },    
    {"name": "La Taverne de la Raclure noire",
      "health": 0,
      "equipment": 3,
      "morale": 0,
      "supplies": 0,
      "training": 0
      },    
    {"name": "Porte du principal quartier",
      "health": 0, 
      "equipment": 0, 
      "morale": 0, 
      "supplies": 3, 
      "training": 0
      },    
    {"name": "L'imprimerie Clandestine",
      "health": 0, 
      "equipment": 0, 
      "morale": 3, 
      "supplies": 0, 
      "training": 0
      },    
    {"name": "Terrain d'entrainement", 
     "health": 0, 
     "equipment": 0, 
     "morale": 0, 
     "supplies": 0, 
     "training": 3
     },
    ]

flows_list = []

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

