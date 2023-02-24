def display_menu():
    print("a. Add a new teacher")
    print("b. Search a teacher by id")
    print("c. Update a teacher by id")
    print("d. Delete a teacher by id")
    print("e. Display all teachers")
    print("f. Exit program")

class Teacher:
    def __init__(self):
        with open("Teacher.txt","r") as file1:
            data = file1.read().rstrip("\n")

        self.TeacherList = {}
        list1 = data.split("\n")
        for item in list1:
            self.TeacherID, self.TeacherName, self.Gender, self.DOB, self.PhoneNo, self.Address = item.split(", ")
            self.TeacherList[self.TeacherID] = {"TeacherName":self.TeacherName, "Gender":self.Gender, "DOB":self.DOB, "PhoneNo":self.PhoneNo, "Address":self.Address}
    
    def update_data(self):
        with open("Teacher.txt","w") as file1:
            for key in self.TeacherList:
                file1.write(key + ", " + self.TeacherList[key]["TeacherName"] + ", " + self.TeacherList[key]["Gender"] + ", " + self.TeacherList[key]["DOB"] + ", " + self.TeacherList[key]["PhoneNo"] + ", " + self.TeacherList[key]["Address"] + "\n") 

    def add_teacher(self):
        self.TeacherID = input("Teacher ID: ")
        while(self.TeacherID in self.TeacherList.keys()):
            print("The ID is already existed")
        self.TeacherName = input("Teacher Name: ")
        self.Gender = input("Gender: ")
        self.DOB = input("DateOfBirth: ")
        self.PhoneNo = input("Phone Number: ")
        self.Address = input("Address: ")
        self.TeacherList[self.TeacherID] = {"TeacherName":self.TeacherName, "Gender":self.Gender, "DOB":self.DOB, "PhoneNo":self.PhoneNo, "Address":self.Address}

        self.update_data()

    def search_teacher(self, id):
        if(id not in self.TeacherList.keys()):
            print("Search not found")
        else:
            for key in self.TeacherList:
                if id == key:
                    print(key + " " + self.TeacherList[key]["TeacherName"] + " " + self.TeacherList[key]["Gender"] + " " + self.TeacherList[key]["DOB"] + " " + self.TeacherList[key]["PhoneNo"] + " " + self.TeacherList[key]["Address"])
                    break

    def update_a_teacher(self, id):
        if(id not in self.TeacherList.keys()):
            print("ID(to update) not found")
        else:
            self.TeacherName = input("Teacher Name: ")
            self.Gender = input("Gender: ")
            self.DOB = input("DateOfBirth: ")
            self.PhoneNo = input("Phone Number: ")
            self.Address = input("Address: ")
            self.TeacherList[id] = {"TeacherName":self.TeacherName, "Gender":self.Gender, "DOB":self.DOB, "PhoneNo":self.PhoneNo, "Address":self.Address}

            self.update_data()

    def delete_a_teacher(self, id):
        if(id not in self.TeacherList.keys()):
            print("ID(to delete) not found")
        else:
            for key in self.TeacherList:
                if id == key:
                    del self.TeacherList[id]
                    break

            self.update_data()

    def display_all_teacher(self):
        for key in self.TeacherList:
            print(key + " " + self.TeacherList[key]["TeacherName"]  + " " + self.TeacherList[key]["Gender"] + " " + self.TeacherList[key]["DOB"] + " " + self.TeacherList[key]["PhoneNo"] + " " + self.TeacherList[key]["Address"])

teacherList1 = Teacher()
while(1):
    print("")
    display_menu()
    menu = input("Select menu: ").lower()
    print("")

    if(menu == "a"):
        teacherList1.add_teacher()
    elif(menu == "b"):
        id = input("ID(to search): ")
        teacherList1.search_teacher(id)
    elif(menu == "c"):
        id = input("ID(to update): ")
        teacherList1.update_a_teacher(id)
    elif(menu == "d"):
        id = input("ID(to delete): ")
        teacherList1.delete_a_teacher(id)
    elif(menu == "e"):
        teacherList1.display_all_teacher()
    elif(menu == "f"):
        break
    else:
        print("Please enter a letter between a and f")