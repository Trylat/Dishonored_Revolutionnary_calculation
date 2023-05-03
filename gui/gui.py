import os
import json
from tkinter import filedialog
from tkinter import Tk
from app.data_manager import RevolutionData
from app.nodes import ResistanceNodes
from app.flow import ResistanceFlow
from app.score import RevolutionScore

class Interface:
    
    def __init__(self, data_manager: RevolutionData):
        self.exit = False
        self.rev_data = data_manager
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_menu(self):
        self.clear_screen()
        print("Bienvenue dans l'application de gestion de Noeuds et de Flows")
        print("----------------------------------------------------------\n")
        print("1. Gestion de Noeuds")
        print("2. Gestion de Flows")
        print("3. Sauvegarder")
        print("4. Charger")
        print("5. Quitter")

    def print_node_menu(self):
        self.clear_screen()
        print("Node Management Menu")
        print("1. Add New Node")
        print("2. Remove Node")
        print("3. Modify Node")
        print("4. View Node")
        print("5. Back to Main Menu")

    def print_flow_menu(self):
        print("Flow Management Menu")
        print("1. Add Flow")
        print("2. Remove Flow")
        print("3. Modify Flow")
        print("4. View Flows")
        print("5. Exit")

    
    def get_choice(self):
        choice = input("Entrez votre choix : ")
        return choice
    
    def manage_node(self):
        while True:
            self.print_node_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                while True:
                    node_name = input("Enter node name: ")
                    if not self.check_node_name(node_name, self.rev_data.nodes):
                        break
                    else:
                        print("This node already exist!!!")
                node_stats = self.get_stat_value()
                new_node = ResistanceNodes(node_name, **node_stats)
                self.rev_data.add_node(new_node)
                print("Node added successfully!")
            elif choice == "2":
                self.clear_screen()
                print("Select a node to Delete: ")
                self.print_node_list(self.rev_data.nodes, True)
                index = self.get_valid_node_index(self.rev_data.nodes, True)
                if index < len(self.rev_data.nodes):
                    node_name = self.rev_data.nodes[index]
                    print(f"node_NAME {node_name}")
                    self.rev_data.remove_node_from_flows(node_name)
                elif index == len(self.rev_data.nodes):
                    pass
            elif choice == "3":
                self.clear_screen()
                print("Select a node to Modify: ")
                self.print_node_list(self.rev_data.nodes, True)
                index = self.get_valid_node_index(self.rev_data.nodes, True)
                if index < len(self.rev_data.nodes):
                    stat = self.get_stat_value()
                    self.rev_data.modify_node(index, **stat)
                elif index == len(self.rev_data.nodes):
                    pass
            elif choice == "4":
                self.clear_screen()
                print("This is the list of Nodes in the map and the stats values of each ones of them:")
                self.print_node_list(self.rev_data.nodes, True)
                self.get_valid_node_index(self.rev_data.nodes, True)
            elif choice == "5":
                break
            else:
                print("Invalid choice, please try again.")

    def check_node_name(self, node_name, node_list):
        for node in node_list:
            if node.name == node_name:
                return True
        return False
    
    def print_node_list(self, node_list, exit = False):
        print("Node List:")
        i = 0
        for i, node in enumerate(node_list):
            print(f"{i}. {node.name} - {node.get_non_null_stats()} - {node.stats[node.get_non_null_stats()[0]]}")
        if exit:    
            print(f"{len(node_list)}. Exit")

    def print_flow_list(self, flow_list, exit = False, score = False):
        print("Flow List:")
        i=0
        for i, flow in enumerate(flow_list):
            node_list = flow.nodes
            if score:
                # Create temporary elements for the display
                print("-------------------------------------------------------------------------------------------")
                fakeflow = ResistanceFlow(flow.name, node_list)
                fakescore = RevolutionScore()
                fakeflow.get_stats_sum()
                fakescore.calculate_flow_score(fakeflow)
                node_list = fakeflow.nodes
                print(f"{i}. {fakeflow.name} score:[{fakescore.score}]:"+" ".join(str(f"|{x.name} - {x.get_non_null_stats()} - {x.stats[x.get_non_null_stats()[0]]}|") for x in node_list))
                print("-------------------------------------------------------------------------------------------")
            else:
                print(f"{i}. {flow.name}:"+" ".join(str(f"|{x.name} - {x.get_non_null_stats()} - {x.stats[x.get_non_null_stats()[0]]}|") for x in node_list))
        if exit:    
            print(f"{len(flow_list)}. Exit")

        

    def get_valid_node_index(self, node_list, exit = False):
        """
        Get a valid node index from user input.
        """
        if exit:
            valid_indexes = [str(i) for i in range(len(node_list)+1)]
        else:
            valid_indexes = [str(i) for i in range(len(node_list))]
        while True:
            user_input = input("Enter the index of the node: ")
            if user_input in valid_indexes:
                return int(user_input)
            else:
                print("Invalid input. Please enter a valid index.")



    def get_stat_value(self):
        print("Select a stat:")
        print("1. Health")
        print("2. Equipment")
        print("3. Morale")
        print("4. Supplies")
        print("5. Training")
        
        # Prompt user to select a stat
        stat_choice = input("Enter stat number (1-5): ")
        while stat_choice not in ['1', '2', '3', '4', '5']:
            stat_choice = input("Invalid input. Enter stat number (1-5): ")
        stat_choice = int(stat_choice)
        
        # Prompt user to enter a value for the selected stat
        value = input("Enter value for selected stat: ")
        while not value.isdigit():
            value = input("Invalid input. Enter a numerical value: ")
        value = int(value)
        
        # Create a dictionary with all stats set to 0
        stats = {"health": 0, "equipment": 0, "morale": 0, "supplies": 0, "training": 0}
        # Set the value of the selected stat
        if stat_choice == 1:
            stats["health"] = value
        elif stat_choice == 2:
            stats["equipment"] = value
        elif stat_choice == 3:
            stats["morale"] = value
        elif stat_choice == 4:
            stats["supplies"] = value
        elif stat_choice == 5:
            stats["training"] = value
        
        return stats
    
    def manage_flow(self):
        """Add, remove, or modify a flow."""
        while True:
            self.clear_screen()
            self.print_flow_menu()
            choice = input("Enter your choice: ")

            if choice == "1": # Add a flow
                while True:
                    flow_name = input("Enter flow name: ")
                    if not self.check_node_name(flow_name, self.rev_data.flows):
                        break
                    else:
                        print("This flow already exist!!!")
                node_list = []
                while True:
                    self.clear_screen()
                    print("Current Node list in flow:\n")
                    print(f"{flow_name}")
                    print(" ".join(str(f"|{x.name} - {x.get_non_null_stats()} - {x.stats[x.get_non_null_stats()[0]]}|") for x in node_list))
                    print("Select a node to add to Flow:")
                    self.print_node_list(self.rev_data.nodes, True)
                    index = self.get_valid_node_index(self.rev_data.nodes, True)
                    if index < len(self.rev_data.nodes):
                        node = self.rev_data.nodes[index]
                        if node not in node_list:
                            node_list.append(node)
                        else:
                            input("This Node is already in the list!!!")

                    if index == len(self.rev_data.nodes) or node not in node_list:
                        print(f"{flow_name}")
                        print(" ".join(str(f"{x.name} - {x.get_non_null_stats()} - {x.stats[x.get_non_null_stats()[0]]}\n") for x in node_list))
                        answer = input("Did you add all Nodes to this Flow? yes(y)/no(n)")
                        if answer == "yes" or answer == "y":
                            break
                    
                if len(node_list) > 1:
                    new_flow = ResistanceFlow(flow_name, node_list)
                    self.rev_data.add_flow(new_flow)
                else:
                    input("This Flow do not have enought nodes (minimum 2 nodes)")

            elif choice == "2": # Remouve a Flow
                while True:
                    self.clear_screen()
                    self.print_flow_list(self.rev_data.flows, True)
                    index = self.get_valid_node_index(self.rev_data.flows, True)
                    # Manage exit and the deletion of selected flows
                    if index < len(self.rev_data.flows):
                        flow = self.rev_data.flows[index]
                        self.rev_data.remove_flow(flow.name)
                    elif index == len(self.rev_data.flows):
                        break

            elif choice == "3": # Modify a flow
                """Modify an existing flow by adding, removing, or moving nodes."""
                while True:
                    self.clear_screen()
                    self.print_flow_list(self.rev_data.flows, True)
                    index = self.get_valid_node_index(self.rev_data.flows, True)
                    if index < len(self.rev_data.flows):
                        flow = self.rev_data.flows[index]
                        while True:
                            self.clear_screen()
                            print(f"Current node list in flow {flow.name}:")
                            for i, node in enumerate(flow.nodes):
                                print(f"{i}. {node.name} - {node.get_non_null_stats()} - {node.stats[node.get_non_null_stats()[0]]}")
                            print("Select an action:\n"
                                "1. Add a node to the flow\n"
                                "2. Remove a node from the flow\n"
                                "3. Move a node within the flow\n"
                                "4. Return to previous menu")
                            choice = input("Enter your choice: ")
                            if choice == "1": # Add a node to the flow
                                while True:
                                    self.clear_screen()
                                    print("Current node list in flow:\n")
                                    print(f"{flow.name}")
                                    self.print_node_list(flow.nodes, True)
                                    print("Select a node to add to the flow:")
                                    self.print_node_list(self.rev_data.nodes, True)
                                    index = self.get_valid_node_index(self.rev_data.nodes, True)
                                    if index < len(self.rev_data.nodes):
                                        node_name_list = [] # Extract all node name in the flow sins they are not the same object than those in the node list
                                        for node in flow.nodes:
                                            node_name_list.append(node.name)
                                        node = self.rev_data.nodes[index]
                                        if node.name not in node_name_list:
                                            flow.add_node(node)
                                            break
                                        else:
                                            input("This node is already in the flow!!! Press enter to continue...")
                                    elif index == len(self.rev_data.nodes):
                                        break
                            elif choice == "2": # Remove a node from the flow
                                while True:
                                    self.clear_screen()
                                    print(f"Current node list in flow {flow.name}:")
                                    self.print_node_list(flow.nodes, True)
                                    print("Select a node to remove from the flow:")
                                    index = self.get_valid_node_index(flow.nodes, True)
                                    if index < len(flow.nodes):
                                        flow.nodes.pop(index)
                                    elif index == len(flow.nodes):
                                        break
                            elif choice == "3": # Move a node within the flow
                                while True:
                                    self.clear_screen()
                                    print(f"Current node list in flow {flow.name}:")
                                    self.print_node_list(flow.nodes, True)
                                    print("Select a node to move within the flow:")
                                    index1 = self.get_valid_node_index(flow.nodes, True)
                                    if index1 < len(flow.nodes):
                                        print(f"Select a position to move {flow.nodes[index1].name} to:")
                                        index2 = self.get_valid_node_index(flow.nodes, True)
                                        if index2 < len(flow.nodes):
                                            node = flow.nodes.pop(index1)
                                            flow.nodes.insert(index2, node)
                                            break
                                        elif index2 == len(flow.nodes):
                                            break
                                    elif index1 == len(flow.nodes):
                                        break
                            elif choice == "4": # return to flow menu
                                break
                    elif index == len(self.rev_data.flows): # return to main menu
                        break
            elif choice == "4": # View Flow
                self.clear_screen()
                print("This is the list of Flow in the map and the score revolution score generated by them each turn:")
                self.print_flow_list(self.rev_data.flows, True, True)
                self.get_valid_node_index(self.rev_data.flows, True)
            elif choice == "5": # Return to main menu
                break
  
    def select_flow(self):
        print("Sélectionnez un flow :")
        flows = self.rev_data.flows
        for i, flow in enumerate(flows):
            print(f"{i+1}. {flow['name']}")
        while True:
            try:
                choix = int(input("Votre choix : "))
                if 1 <= choix <= len(flows):
                    return flows[choix-1]
                else:
                    print("Choix invalide. Veuillez réessayer.")
            except ValueError:
                print("Choix invalide. Veuillez réessayer.")

    def save(self):
        # Code pour sauvegarder
        self.clear_screen()
        responce = self.end_round_prompt()
        if responce:
            self.rev_data.end_turn("save")
        else:
            file_name = f"save_{self.rev_data.turn_number}.json"
            self.rev_data.save_data(file_name)
        input("Save success!!. Press Enter to continue...")
        
    
    def load(self):
        self.clear_screen()
        # Create Tkinter root window
        root = Tk()
        root.withdraw() # Hide the root window

        # Open file dialog
        file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])

        # Load the JSON file
        self.rev_data = RevolutionData.from_file(file_path)
    
    def end_round_prompt(self):
        """Prompt user to end current round or not."""
        while True:
            response = input("Do you want to end the current round? (y/n): ").lower()
            if response == "y":
                return True
            elif response == "n":
                return False
            else:
                print("Invalid response. Please enter 'y' or 'n'.")

    def exit_application(self):
        self.save() # Save before closing the application
        self.exit = True
    
    def run(self):
        while not self.exit:
            self.print_menu()
            choice = self.get_choice()
            if choice == "1":
                self.manage_node()
            elif choice == "2":
                self.manage_flow()
            elif choice == "3":
                self.save()
            elif choice == "4":
                self.load()
            elif choice == "5":
                self.exit_application()
            else:
                print("Choix invalide. Veuillez entrer un choix valide.")
                input("Appuyez sur une touche pour continuer...")
