from Contributor import Contributor
from Project import Project


class Solution:
    def __init__(self, input_file_name):
        input = open("input_data/"+input_file_name, "r")
        num_contributors, num_projects = map(int, input.readline().split(" "))

        self.contributors = []
        self.projects = []

        while num_contributors > 0:
            self.contributors.append(Contributor.from_file(input))
            num_contributors -= 1

        while num_projects > 0:
            project = Project.from_file(input)
            self.projects[project.name] = project
            num_projects -= 1

    def __str__(self):
        count = 0
        result = ""
        for project in self.projects:
            if(len(project.assignments) > 0): # skip jobs with no assigments
                count += 1
                result += project.name + "\n"
                result += " ".join(project.assignments) + "\n"
        return str(count) + "\n" + result