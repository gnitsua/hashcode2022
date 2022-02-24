from collections import defaultdict


class Solver:
    def __init__(self, contributors, projects):
        self.contributors = contributors
        self.projects = projects

    def solve(self):
        # skills = defaultdict(defaultdict(list))
        # # for contributor in self.contributors:
        # #     for skill,level in contributor.skills.items():
        # #         skills["%s-%s"%(skill,level)].append(contributor.name)

        for project in self.projects:
            temp_assignments = []
            busy_contributors = set()
            for role in project.roles:
                for contributor in self.contributors:
                    if(contributor.can_work(role) and contributor.name not in busy_contributors):
                        temp_assignments.append(contributor.name)
                        busy_contributors.add(contributor.name)
                        break
                if(len(project.roles) == len(temp_assignments)): # make sure we found someone for every role
                    project.assignments = temp_assignments
            print(project.assignments)
