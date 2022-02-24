# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from Contributor import Contributor
from Project import Project
from Solution import Solution

solution_names = {
    "a":"a_an_example.in.txt",
    "b":"b_better_start_small.in.txt",
    "c":"c_collaboration.in.txt",
    "d":"d_dense_schedule.in.txt",
    "e":"e_exceptional_skills.in.txt",
    "f":"f_find_great_mentors.in.txt",
}

if __name__ == '__main__':
    solution_id = "f"
    solution = Solution(solution_names[solution_id])

    # for contributor in solution.contributors:
    #     print(contributor)

    for project in solution.projects.values():
        print(project)

    # A
    # solution.projects["WebServer"].assignments = ["Bob", "Anna"]
    # solution.projects["Logging"].assignments = ["Anna"]
    # solution.projects["WebChat"].assignments = ["Maria", "Bob"]

    # B
    # solution.projects["SlidesNextv2"].assignments = ["JenZ", "PhilippH"]

    # C
    # solution.projects["AssistantMaxv9"].assignments = ["ThomasQ"]

    # D ["{'s592': 3}", "{'s394': 2}"]
    solution.projects["p1225"].assignments = ["c698", "c350"]


    with open("solutions/%s"%solution_id, "w") as file:
        file.write(str(solution))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
