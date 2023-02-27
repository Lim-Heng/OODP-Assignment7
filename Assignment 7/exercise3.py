#function to display the menu
def display_menu():
    print("a. Add a new student")
    print("b. Search a student by id")
    print("c. Update a student by id")
    print("d. Delete a student by id")
    print("e. Display all student")
    print("f. Exit program")

class Student:
    def __init__(self):
        with open("Student.txt","r") as file1:
            data = file1.read().rstrip("\n")

        self.StudentList = {}
        list1 = data.split("\n")
        for item in list1:
            self.StudentID, self.StudentName, self.Gender, self.DOB, self.PhoneNo, self.Address, self.Year, self.Generation, self.Degree = item.split(", ")
            self.StudentList[self.StudentID] = {"StudentName":self.StudentName, "Gender":self.Gender, "DOB":self.DOB, "PhoneNo":self.PhoneNo, "Address":self.Address, "Year":self.Year, "Generation":self.Generation, "Degree":self.Degree}

    #function to update the new data to the file
    def update_data(self):
        with open("Student.txt","w") as file1:
            for key in self.StudentList:
                file1.write(key + ", " + self.StudentList[key]["StudentName"] + ", " + self.StudentList[key]["Gender"] + ", " + self.StudentList[key]["DOB"] + ", " + self.StudentList[key]["PhoneNo"] + ", " + self.StudentList[key]["Address"] + self.StudentList[key]["Year"] + ", " + self.StudentList[key]["Generation"] + ", " + self.StudentList[key]["Degree"] + "\n")

    #function to add a new student
    def add_student(self):
        self.StudentID = input("Student ID: ")
        self.StudentName = input("Student Name: ")
        self.Gender = input("Gender: ")
        self.DOB = input("Date of birth: ")
        self.PhoneNo = input("Phone number: ")
        self.Address = input("Address: ")
        self.Year = input("Year: ")
        self.Generation = input("Generation: ")
        self.Degree = input("Degree: ")
        self.StudentList[self.StudentID] = {"StudentName":self.StudentName, "Gender":self.Gender, "DOB":self.DOB, "PhoneNo":self.PhoneNo, "Address":self.Address, "Year":self.Year, "Generation":self.Generation, "Degree":self.Generation}

        self.update_data()

    #function to search for a specific student
    def search_student(self, id):
        if(id not in self.StudentList.keys()):
            print("Search not found")
        else:
            for key in self.StudentList:
                if id == key:
                    print(key + " " + self.StudentList[key]["StudentName"] + " " + self.StudentList[key]["Gender"] + " " + self.StudentList[key]["DOB"] + " " + self.StudentList[key]["PhoneNo"] + " " + self.StudentList[key]["Address"] + " " + self.StudentList[key]["Year"] + " " + self.StudentList[key]["Generation"] + " " + self.StudentList[key]["Degree"])
                    break

    #functiont to update information about a student
    def update_a_student(self, id):
        if(id not in self.StudentList.keys()):
            print("ID(to update) not found")
        else:
            self.StudentName = input("Student Name: ")
            self.DOB = input("Date of birth: ")
            self.PhoneNo = input("Phone number: ")
            self.Address = input("Address: ")
            self.Year = input("Year: ")
            self.Generation = input("Generation: ")
            self.Degree = input("Degree: ")
            self.StudentList[id] = {"StudentName":self.StudentName, "Gender":self.Gender, "DOB":self.DOB, "PhoneNo":self.PhoneNo, "Address":self.Address, "Year":self.Year, "Generation":self.Generation, "Degree":self.Generation}

            self.update_data()

    #function to delete a specific student
    def delete_a_student(self, id):
        if(id not in self.StudentList.keys()):
            print("ID(to delete) not found")
        else:
            for key in self.StudentList:
                if id == key:
                    del self.StudentList[id]
                    break

            self.update_data()

    #function to display all the students
    def display_all_student(self):
        for key in self.StudentList:
            print(key + " " + self.StudentList[key]["StudentName"] + " " + self.StudentList[key]["Gender"] + " " + self.StudentList[key]["DOB"] + " " + self.StudentList[key]["PhoneNo"] + " " + self.StudentList[key]["Address"] + " " + self.StudentList[key]["Year"] + " " + self.StudentList[key]["Generation"] + " " + self.StudentList[key]["Degree"])

studentList1 = Student()
while(1):
    #display menu and get user's input
    print("")
    display_menu()
    print("")
    menu = input("Select menu: ").lower()
    print("")

    #decision based on user's input
    if(menu == "a"):
        studentList1.add_student()
    elif(menu == "b"):
        id = input("ID(to search): ")
        studentList1.search_student(id)
    elif(menu == "c"):
        id = input("ID(to update): ")
        studentList1.update_a_student(id)
    elif(menu == "d"):
        id = input("ID(to delete): ")
        studentList1.delete_a_student(id)
    elif(menu == "e"):
        studentList1.display_all_student()
    elif(menu == "f"):
        break
    else:
        print("Please enter a letter between a and f")