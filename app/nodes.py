class ResistanceNodes:
    def __init__(self, name, **stats):
        self.name = name
        self.stats = {stat: 0 for stat in ['health', 'equipment', 'morale', 'supplies', 'training']}
        self.set_stats(**stats)

    def set_stats(self, **stats):
        for stat, value in stats.items():
            if stat in self.stats:
                self.stats[stat] = value

    def set_stats_2(self, stat_name, value):
        for stat in self.stats:
            if stat_name in self.stats:
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
    
    def clone(self):
        return ResistanceNodes(self.name, **self.stats)
