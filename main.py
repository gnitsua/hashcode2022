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
    solution_id = "b"
    solution = Solution(solution_names[solution_id])

    # for contributor in solution.contributors:
    #     print(contributor)

    # for project in solution.projects:
    #     print(project)


    with open("solutions/%s"%solution_id, "w") as file:
        file.write(str(solution))
