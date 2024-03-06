import json
import datetime
import checker


def read_project_file():
    try:
        with open("projects.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_projects(projects):
    with open("projects.json", "w") as file:
        json.dump(projects, file, indent=4)


def create_project(user_id):
    projects = read_project_file()
    title = checker.checkString("Enter project title: ")
    details = input("Enter project details: ")
    target = checker.checkInt("Enter total target amount: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    try:
        start_time = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end_time = datetime.datetime.strptime(end_date, "%Y-%m-%d")

        if start_time < end_time:
            project = {
                "Title": title,
                "Details": details,
                "Total target": target,
                "Start time": start_time.isoformat(),
                "End time": end_time.isoformat(),
                "User": user_id  
            }
            projects.append(project)
            save_projects(projects)
            print("Project created successfully.")
        else:
            print("End time should be after start time.")
    except ValueError:
        print("Invalid date format (YYYY-MM-DD).")


def view_all_projects():
    projects = read_project_file()
    if projects:
        print("All Projects:")
        for index, project in enumerate(projects, start=1):
            print(f"Project {index}:")
            for key, value in project.items():
                print(f"{key}: {value}")
            print()
    else:
        print("No projects available.")


def edit_project(user_id):
    projects = read_project_file()
    for project in projects:
        if project["User"] == user_id:
            print(f"Editing project: {project}")
            new_details = input("Enter new details: ")
            project["Details"] = new_details
            save_projects(projects)
            print("Project updated successfully.")
            return

    print("No projects found .")


def delete_project(user_id):
    projects = read_project_file()
    for project in projects:
        if project["User"] == user_id:
            print(f"Deleting project: {project}")
            projects.remove(project)
            save_projects(projects)
            print("Project deleted successfully.")
            return

    print("No projects found .")


def search_by_date():
    projects = read_project_file()
    Sdate = input("Enter start date (YYYY-MM-DD): ")
    Edate = input("Enter end date (YYYY-MM-DD): ")

    try:
        start_date = datetime.datetime.strptime(Sdate, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(Edate, "%Y-%m-%d")

        Fprojects = []

        for project in projects:
            projectSTime = datetime.datetime.fromisoformat(project["Start time"])
            if start_date <= projectSTime <= end_date:
                Fprojects.append(project)

        if Fprojects:
            print("Projects found:")
            for project in Fprojects:
                print(project)
        else:
            print("No projects found.")
    except ValueError:
        print("Invalid date format")
