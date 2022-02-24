class Contributor:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

    def __str__(self):
        return str({self.name: self.skills})

    # TODO: can work function
    @staticmethod
    def from_file(reader):
        name, num_skills = reader.readline().split(" ")
        skills = {}
        for i in range(int(num_skills)):
            skill, level = reader.readline().split(" ")
            skills[skill] = int(level)

        return Contributor(name, skills)
