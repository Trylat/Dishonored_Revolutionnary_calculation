class ResistanceNodes:
    def __init__(self, name, **stats):
        self.name = name
        self.stats = {stat: 0 for stat in ['health', 'equipment', 'morale', 'supplies', 'training']}
        self.set_stats(**stats)

    def set_stats(self, **stats):
        for stat, value in stats.items():
            if stat in self.stats:
                self.stats[stat] = value

    def get_stats(self):
        return self.stats