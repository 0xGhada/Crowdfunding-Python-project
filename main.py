import checker
import auth
import project

def main():
    print("Welcome to the Crowd-Funding application")
    user_id = None  
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Create Project")
        print("4. View All Projects")
        print("5. Edit Project")
        print("6. Delete Project")
        print("7. Search Projects by Date")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            auth.Registeration()
        elif choice == "2":
            user_id = auth.login()
        elif choice == "3":
            if user_id:
                project.create_project(user_id)
            else:
                print("Please log in first.")
        elif choice == "4":
            project.view_all_projects()
        elif choice == "5":
            if user_id:
                project.edit_project(user_id)
            else:
                print("Please log in first.")
        elif choice == "6":
            if user_id:
                project.delete_project(user_id)
            else:
                print("Please log in first.")
        elif choice == "7":
            project.search_by_date()
        elif choice == "8":
            exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
