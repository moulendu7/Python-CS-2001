iiit_ranchi = {
    "Director": {
        "name": "Prof. Rajiv Ranjan",
        "Dean": {
            "Academic": {
                "name": "Prof. S. K. Singh",
                "Departments": {
                    "Computer Science": {
                        "Head": "Dr. A. Kumar",
                        "Assistant Professors": ["Dr. Ishan Singh", "Dr. Priya Sharma"]
                    },
                    "Electronics": {
                        "Head": "Dr. R. Gupta",
                        "Assistant Professors": ["Dr. Ankit Verma", "Dr. Sneha Roy"]
                    },
                    "Mathematics": {
                        "Head": "Dr. M. Das",
                        "Assistant Professors": ["Dr. Neha Jain", "Dr. Saurabh Sinha"]
                    }
                }
            },
            "Research": {
                "name": "Prof. P. Mishra",
                "Departments": {
                    "AI & Data Science": {
                        "Head": "Dr. T. Singh",
                        "Assistant Professors": ["Dr. Ritu Agarwal", "Dr. Vivek Kumar"]
                    }
                }
            }
        }
    }
}
def find_assistant_professor(structure, prof_name):
    for key, value in structure.items():
        if isinstance(value, dict):
            result = find_assistant_professor(value, prof_name)
            if result:
                return result
        elif key == "Assistant Professors":
            if prof_name in value:
                return structure.get("Head", "Unknown Department")
    if "Departments" in structure:
        for dept, dept_info in structure["Departments"].items():
            if "Assistant Professors" in dept_info and prof_name in dept_info["Assistant Professors"]:
                return dept
            result = find_assistant_professor(dept_info, prof_name)
            if result:
                return dept
    return None
prof_name = input("Enter the name of the Assistant Professor: ")
department = find_assistant_professor(iiit_ranchi, prof_name)
if department:
    print(f"{prof_name} belongs to the '{department}' department.")
else:
    print(f"Assistant Professor '{prof_name}' was not found .")