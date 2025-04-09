class Student:
    def __init__(self, r, n, m):
        self.rn = r
        self.name = n
        self.marks = m

    def __str__(self):
        return f"RN={self.rn}, NAME={self.name}, MARKS={self.marks}"

s1 = Student(1, "abcd", 10)
s2 = Student(2, "defg", 20)
s3 = Student(3, "ghij", 30)

students_list = [s1, s2, s3]

def show_students():
    if not students_list:
        print("\nNO STUDENTS TO SHOW...\n")
    else:
        for stu_obj in students_list:
            print(stu_obj)

def add_student():
    r = int(input("Enter Roll Number: "))
    for stu_obj in students_list:
        if r == stu_obj.rn:
            print("\nSTUDENT ALREADY EXISTS WITH THIS ROLL NUMBER!\n")
            return
    n = input("Enter Name: ")
    m = int(input("Enter Marks: "))
    s = Student(r, n, m)
    students_list.append(s)
    print("\nSTUDENT ADDED SUCCESSFULLY!\n")

def delete_student():
    r = int(input("Enter Roll No To Delete: "))
    for stu_obj in students_list:
        if r == stu_obj.rn:
            students_list.remove(stu_obj)
            print("\nSTUDENT DELETED SUCCESSFULLY!\n")
            return
    print("\nSTUDENT NOT FOUND...\n")

def update_student():
    r = int(input("Enter Roll No To Update: "))
    for stu_obj in students_list:
        if r == stu_obj.rn:
            stu_obj.name = input("Enter Updated Name: ")
            stu_obj.marks = int(input("Enter Updated Marks: "))
            print("\nSTUDENT UPDATED SUCCESSFULLY!\n")
            return
    print("\nSTUDENT NOT FOUND...\n")

# Menu Loop
while True:
    ch = int(input("\n\nEnter Choice:\n1. Add Student\n2. Delete Student\n3. Show Students\n4. Update Student\n5. Exit\n"))
    if ch == 1:
        add_student()
    elif ch == 2:
        delete_student()
    elif ch == 3:
        show_students()
    elif ch == 4:
        update_student()
    elif ch == 5:
        print("\nEXITING...")
        break
    else:
        print("\nINVALID CHOICE...")