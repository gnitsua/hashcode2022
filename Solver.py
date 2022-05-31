from collections import defaultdict


class Solver:
    def __init__(self, contributors, projects):
        self.contributors = contributors
        self.projects = projects

    def solve(self):
        # combined_projects = []
        # already_combined = set()
        # for project in self.projects:
        #     for project_to_combine in self.projects:
        #         if(project.name != project_to_combine.name and project_to_combine.name not in already_combined):
        #             for pro

        # Doesn't seem to matter for B
        # self.projects.sort(key=lambda project: project.best_before)
        self.projects.sort(key=lambda project: project.days)

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
