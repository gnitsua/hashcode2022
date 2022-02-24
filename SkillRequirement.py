class SkillRequirement:
    def __init__(self, name, min_level):
        self.name = name
        self.min_level = min_level

    def __str__(self):
        return str({self.name:self.min_level})