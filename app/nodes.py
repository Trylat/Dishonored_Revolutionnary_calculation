class ResistanceNodes:
    def __init__(self, name, **stats):
        self.name = name
        print(f"Node {self.name} created!!")
        self.stats = {stat: 0 for stat in ['health', 'equipment', 'morale', 'supplies', 'training']}
        self.set_stats(**stats)
        stats_values = self.get_non_null_stats()
        if stats_values[0] == None:
            self.__del__(self)
    
    def __del__(self):
        print(f"Node {self.name} destroyed!!")

    def set_stats(self, **stats):
        for stat, value in stats.items():
            if stat in self.stats:
                self.stats[stat] = value

    def get_stats(self):
        return self.stats
    
    def get_non_null_stats(self):
        non_null_stats = []
        for stat, value in self.stats.items():
            if value != 0:
                non_null_stats.append(stat)
        if len(non_null_stats) == 0:
            non_null_stats.append(None)
        return non_null_stats