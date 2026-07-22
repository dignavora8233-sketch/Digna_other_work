students = []

print("Welcome to the Student Data Organizer!!")

print("Select an option:")

while True:
    print("\n1.Add Student")
    print("2.Display All Students")
    print("3.Upsate student Information")
    print("4.Delate Student")
    print("5.Display Subject Offered")
    print("6.Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student = {}
        student["id"] = input("Student ID: ")
        student["name"] = input("Name: ")
        student["age"] = input("Age: ")
        student["grade"] = input("Grade: ")
        student["dob"] = input("DOB (YYYY-MM-DD): ")
        student["subjects"] = input("Subjects: ").split(",")
    
        students.append(student)
        print("\nStudent added successfully!!")

    elif choice == "2":
        print("\n---Display All Students---")
        if len(students) == 0:
            print("NO students found!!")
        else:
            for student in students:
                print(f"ID:{student['id']} | Name:{student['name']} | Age:{student['age']} | Grade:{student['grade']} | subjects:{student['subjects']}")
        
    

     

    
