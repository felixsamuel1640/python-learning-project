import time

def fetching_record():
    print("fetching student's record..")
    time.sleep(5)

def students_grade():
    st_grades = {
            "Sandy": "A",
            "Spongebob": "B",
            "Patrick": "C",
            "Squidwards": "D"
        }
    option = """
    1. Check a student's grade
    2. Add a new student
    3. View all students record
    4. Exit
    """

    is_running = True

    while is_running:
        print("\nStudent's Grade Lookup Database📚")
        print(option)

        choice = input("choose an option(1-4): ")

        if choice == "1":
            student_name = input("Enter student's name: ").title()
            if student_name in st_grades:
                print(f"{student_name}'s grade is 
{st_grades[student_name]}")
            else:
                print(f"{student_name}'s name NOT found")
        elif choice == "2":
            new_name = input("Enter new name: ").capitalize()
            new_grade = input("Enter new grade: ").upper()

            st_grades[new_name] = new_grade
            print("Adding student...")
            time.sleep(4)
            print(f"New student:{new_name}, Grade:{new_grade} added 
succesfully to the database✅")

        elif choice == "3":
            fetching_record()
            for key, value in st_grades.items():
                print(f"{key}: {value}")

        elif choice == "4":
            print("Closing student's database..")
            time.sleep(5)
            print("Exited succesfully..")
            is_running = False

        else:
            print("Oops..option not recognized")



students_grade()
