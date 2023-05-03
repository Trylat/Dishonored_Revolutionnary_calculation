from app.nodes import ResistanceNodes
from app.score import RevolutionScore
from app.data_manager import RevolutionData
from gui.gui import Interface
from app.constants import *
from app.utils import *

class main():
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
    main_loop = main()