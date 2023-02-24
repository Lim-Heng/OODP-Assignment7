def display_menu():
    print("a. Enroll a student into a department")
    print("b. Remove a student from a department")
    print("c. Display all students at a department")
    print("d. Exit program")

class StudentDetail:
    def __init__(self):
        with open("Department.txt","r") as file1:
            data = file1.read().rstrip("\n")
        self.DepartmentList = {}
        list1 = data.split("\n")
        for item in list1:
            self.DepartmentID, self.DepartmentName, self.HeadName, self.OfficeNo, self.FacultyID = item.split(", ")
            self.DepartmentList[self.DepartmentID] = {"DepartmentName":self.DepartmentName, "HeadName":self.HeadName, "OfficeNo":self.OfficeNo, "FacultyID":self.FacultyID}

        with open("Student.txt","r") as file1:
            data = file1.read().rstrip("\n")
        self.StudentList = {}
        list1 = data.split("\n")
        for item in list1:
            self.StudentID, self.StudentName, self.Gender, self.DOB, self.PhoneNo, self.Address, self.Year, self.Generation, self.Degree = item.split(", ")
            self.StudentList[self.StudentID] = {"StudentName":self.StudentName, "Gender":self.Gender, "DOB":self.DOB, "PhoneNo":self.PhoneNo, "Address":self.Address, "Year":self.Year, "Generation":self.Generation, "Degree":self.Degree}

    def enroll_student_to_dept(self):
        StuID = input("Student ID: ")
        if(StuID not in self.StudentList.keys()):
            print("The student ID doesn't exist")
        else:
            DeptID = input("Department ID: ")
            if(DeptID not in self.DepartmentList.keys()):
                print("The Department ID doesn't exist")
            else:
                with open("StudentDetail.txt","a") as file1:
                    file1.write(DeptID + ", " + StuID + "\n")

    def get_studentDetialList_as_dict(self):
        with open("StudentDetail.txt","r") as file1:
            data = file1.read().rstrip("\n")
        self.StudentDetailList = {}
        self.DeptIDList = []
        self.StuIDList = []
        list1 = data.split("\n")
        idex = 0
        for item in list1:
            DeptID, StuID = item.split(", ")
            self.StudentDetailList[idex] = {"DeptID":DeptID, "StuID":StuID}
            idex = idex + 1

    def remove_a_student_from_department(self):
        self.get_studentDetialList_as_dict()
        StuID = input("Student ID(to remove): ")
        if(StuID not in self.StuIDList):
            print("The student ID doesn't exist")
        else:
            DeptID = input("Department ID(of the student): ")
            if(DeptID not in self.DeptIDList):
                print("The department ID doesn't exist")
            else:
                for key in self.StudentDetailList:
                    if(DeptID == self.StudentDetailList[key]["DeptID"] and StuID == self.StudentDetailList[key]["StuID"]):
                        del self.StudentDetailList[key]
                        break

    def display_all_students_at_a_department(self, dept_id):
        self.get_studentDetialList_as_dict()

        for key in self.StudentDetailList:
            if(dept_id == self.StudentDetailList[key]["DeptID"]):
                print(self.StudentList[self.StudentDetailList[key]["StuID"]]["StudentName"])

studentDetailList1 = StudentDetail()
while(1):
    print("")
    display_menu()
    menu = input("Select menu: ")
    print("")

    if(menu == "a"):
        studentDetailList1.enroll_student_to_dept()
    elif(menu == "b"):
        studentDetailList1.remove_a_student_from_department()
    elif(menu == "c"):
        dept_id = input("Department ID(to diplay students): ")
        studentDetailList1.display_all_students_at_a_department(dept_id)
    elif(menu == "d"):
        break
    else:
        print("Please enter a letter between a and c")