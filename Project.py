from SkillRequirement import SkillRequirement


class Project:
    def __init__(self, name, days, score, best_before, roles):
        self.name = name
        self.days = days
        self.score = score
        self.best_before = best_before
        self.roles = roles
        self.assignments = []

    def __str__(self):
        result = self.name + "\n"
        result += str(list(map(str,self.roles)))

        return result

    @staticmethod
    def from_file(reader):
        name, days, score, best_before, num_contributors = reader.readline().split(" ")
        roles = []
        for i in range(int(num_contributors)):
            skill, min_level = reader.readline().split(" ")
            roles.append(SkillRequirement(skill, int(min_level)))

        return Project(name, int(days), int(score), int(best_before), roles)


