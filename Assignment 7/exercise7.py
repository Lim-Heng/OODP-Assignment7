#function to display the menu
def display_menu():
    print("a. Assign a course to a teacher")
    print("b. Remove a course from a teacher")
    print("c. Display all course taught by a teacher")
    print("d. Exit program")

class TeacherCourse:
    #function to get the data about course and teacher as a dictionary
    def __init__(self):
        with open("Course.txt","r") as file1:
            data = file1.read().rstrip("'\n")
        self.CourseList = {}
        list1 = data.split("\n")
        for item in list1:
            self.CourseID, self.CourseName, self.Credit, self.Type, self.DeptID = item.split(", ")
            self.CourseList[self.CourseID] = {"CourseName":self.CourseName, "Credit":self.Credit, "Type":self.Type, "DeptID":self.DeptID}

        with open("Teacher.txt","r") as file1:
            data = file1.read().rstrip("\n")
        self.TeacherList = {}
        list1 = data.split("\n")
        for item in list1:
            self.TeacherID, self.TeacherName, self.Gender, self.DOB, self.PhoneNo, self.Address = item.split(", ")
            self.TeacherList[self.TeacherID] = {"TeacherName":self.TeacherName, "Gender":self.Gender, "DOB":self.DOB, "PhoneNo":self.PhoneNo, "Address":self.Address}

    #function to assign a course to a teacher
    def assign_course_to_teacher(self):
        CourseID = input("Course ID: ")
        if(CourseID not in self.CourseList.keys()):
            print("The course ID doesn't exist")
        else:
            TeacherID = input("Teacher ID: ")
            if(TeacherID not in self.TeacherList.keys()):
                print("The teacher ID doesn't exist")
            else:
                with open("TeacherCourse.txt","a") as file1:
                    file1.write(TeacherID + ", " + CourseID + "\n")
                print("The course has been assigned to the teacher")

    #function to get the teacherCourseList as dictionary
    def get_teacherCourseList_as_dict(self):
        with open("TeacherCourse.txt","r") as file1:
            data = file1.read().rstrip("\n")
        self.TeacherCourseList = {}
        list1 = data.split("\n")
        idex = 0
        for item in list1:
            TeacherID, CourseID = item.split(", ")
            self.TeacherCourseList[str(idex)] = {"Teacher_id":TeacherID, "Course_id":CourseID}
            idex = idex + 1

    #function to update the new data to the file
    def update_data(self):
        with open("TeacherCourse.txt", "w") as file1:
            for key in self.TeacherCourseList:
                file1.write(self.TeacherCourseList[key]["Teacher_id"] + ", " + self.TeacherCourseList[key]["Course_id"] + "\n")

    #function to get all the existed teacher ID from the TeacherCourseList
    def get_existedTeacherID(self):
        self.existedTeacherID = []
        for key in self.TeacherCourseList:
            self.existedTeacherID.append(self.TeacherCourseList[key]["Teacher_id"])

    #function to get all the existed course ID from the TeacherCourseList
    def get_existedCourseID(self):
        self.existedCourseID = []
        for key in self.TeacherCourseList:
            self.existedCourseID.append(self.TeacherCourseList[key]["Course_id"])

    #function to remove a course from a teacher
    def remove_a_course_from_a_teacher(self):
        self.get_teacherCourseList_as_dict()
        self.get_existedTeacherID()
        self.get_existedCourseID()

        CourseID = input("Course ID(to remove): ")
        if(CourseID not in self.existedCourseID):
            print("The course ID doesn't exist")
        else:
            TeacherID = input("Teacher ID(of the course): ")
            if(TeacherID not in self.existedTeacherID):
                print("The teacher ID doesn't exist")
            else:
                found = False
                for key in self.TeacherCourseList:
                    if(TeacherID == self.TeacherCourseList[key]["Teacher_id"] and CourseID == self.TeacherCourseList[key]["Course_id"]):
                        del self.TeacherCourseList[key]
                        found = True
                        self.update_data()
                        print("The course has been removed from the teacher")
                        break
                if not(found):
                    print("There is no equivalent course id and teacher id combination ")

    #function to display all the courses taught by a teacher
    def display_all_courses_taught_by_a_teacher(self, teacher_id):
        self.get_teacherCourseList_as_dict()
        self.get_existedTeacherID()

        if(teacher_id not in self.existedTeacherID):
            print("The teacher ID doesn't exist")
        else:
            print("---------------------------------------")
            print("Teacher ID          Course Name")
            print("---------------------------------------")
            for key in self.TeacherCourseList:
                if(teacher_id == self.TeacherCourseList[key]["Teacher_id"]):
                    print(teacher_id + "                    " + self.CourseList[self.TeacherCourseList[key]["Course_id"]]["CourseName"])
            print("---------------------------------------")
                    
teacherCourseList1 = TeacherCourse()
while(1):
    #function to display the menu and get user's input
    print("")
    display_menu()
    menu = input("Select menu: ")
    print("")

    #decision based on user's input
    if(menu == "a"):
        teacherCourseList1.assign_course_to_teacher()
    elif(menu == "b"):
        teacherCourseList1.remove_a_course_from_a_teacher()
    elif(menu == "c"):
        teacher_id = input("Teacher ID(to display courses): ")
        teacherCourseList1.display_all_courses_taught_by_a_teacher(teacher_id)
    elif(menu == "d"):
        break
    else:
        print("Please enter a letter between a and d")