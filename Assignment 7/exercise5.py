#function to display the menu
def display_menu():
    print("a. Add a new course")
    print("b. Search a course by id")
    print("c. Update a course by id")
    print("d. Delete a course by id")
    print("e. Display all courses")
    print("f. Exit program")

class Course:
    #the init function to get all the data about course as a dictionary
    def __init__(self):
        with open("Course.txt","r") as file1:
            data = file1.read().rstrip("'\n")

        self.CourseList = {}
        list1 = data.split("\n")
        for item in list1:
            self.CourseID, self.CourseName, self.Credit, self.Type, self.DeptID = item.split(", ")
            self.CourseList[self.CourseID] = {"CourseName":self.CourseName, "Credit":self.Credit, "Type":self.Type, "DeptID":self.DeptID}

    #function to update the new data to the file
    def update_data(self):
        with open("Course.txt","w") as file1:
            for key in self.CourseList:
                file1.write(key + ", " + self.CourseList[key]["CourseName"] + ", " + self.CourseList[key]["Credit"] + ", " + self.CourseList[key]["Type"] + ", " + self.CourseList[key]["DeptID"] + "\n")
    
    def add_course(self):
        self.CourseID = input("CourseID: ")
        while(self.CourseID in self.CourseList.keys()):
            print("The ID is already existed")
            self.CourseList = input("Faculty ID: ")
        self.CourseName = input("CourseName: ")
        self.Credit = input("Credit: ")
        self.Type = input("Type: ")
        self.DeptID = input("Department ID: ")
        self.CourseList[self.CourseID] = {"CourseName":self.CourseName, "Credit":self.Credit, "Type":self.Type, "DeptID":self.DeptID}

        self.update_data()

    def search_course(self, id):
        if(id not in self.CourseList.keys()):
            print("Search not found")
        else:
            for key in self.CourseList:
                if id == key:
                    print(key + " " + self.CourseList[key]["CourseName"] + " " + self.CourseList[key]["Credit"] + " " + self.CourseList[key]["Type"] + " " + self.CourseList[key]["DeptID"])
                    break

    def update_a_course(self, id):
        if(id not in self.CourseList.keys()):
            print("ID(to update) not found")
        else:
            self.CourseName = input("CourseName: ")
            self.Credit = input("Credit: ")
            self.Type = input("Type: ")
            self.DeptID = input("Department ID: ")
            self.CourseList[id] = {"CourseName":self.CourseName, "Credit":self.Credit, "Type":self.Type, "DeptID":self.DeptID}

            self.update_data()

    def delete_a_course(self, id):
        if(id not in self.CourseList.keys()):
            print("ID(to delete) not found")
        else:
            for key in self.CourseList:
                if id == key:
                    del self.CourseList[id]
                    break

            self.update_data()

    def display_all_course(self):
        for key in self.CourseList:
            print(key + " " + self.CourseList[key]["CourseName"] + " " + self.CourseList[key]["Credit"] + " " + self.CourseList[key]["Type"] + " " + self.CourseList[key]["DeptID"])

courseList1 = Course()
while(1):
    print("")
    display_menu()
    print("")
    menu = input("Select menu: ").lower()
    print("")

    if(menu == "a"):
        courseList1.add_course()
    elif(menu == "b"):
        id = input("ID(to search): ")
        courseList1.search_course(id)
    elif(menu == "c"):
        id = input("ID(to update): ")
        courseList1.update_a_course(id)
    elif(menu == "d"):
        id = input("ID(to delete): ")
        courseList1.delete_a_course(id)
    elif(menu == "e"):
        courseList1.display_all_course()
    elif(menu == "f"):
        break
    else:
        print("Please enter a letter between a and f")