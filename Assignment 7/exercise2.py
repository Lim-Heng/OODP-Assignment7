#function to display the menu
def display_menu():
    print("a. Add a new department")
    print("b. Search a department by id")
    print("c. Update a department by id")
    print("d. Delete a department by id")
    print("e. Search department by faculty id")
    print("f. Display all departments")
    print("g. Exit program")

class Department:
    #the init function to read all the data about department into a file
    def __init__(self):
        with open("Department.txt","r") as file1:
            data = file1.read().rstrip("\n")

        self.DepartmentList = {}
        list1 = data.split("\n")
        for item in list1:
            self.DepartmentID, self.DepartmentName, self.HeadName, self.OfficeNo, self.FacultyID = item.split(", ")
            self.DepartmentList[self.DepartmentID] = {"DepartmentName":self.DepartmentName, "HeadName":self.HeadName, "OfficeNo":self.OfficeNo, "FacultyID":self.FacultyID}

    #function to update the new data to the file
    def update_data(self):
        with open("Department.txt","w") as file1:
            for key in self.DepartmentList:
                file1.write(key + ", " + self.DepartmentList[key]["DepartmentName"] + ", " + self.DepartmentList[key]["HeadName"] + ", " + self.DepartmentList[key]["OfficeNo"] + ", " + self.DepartmentList[key]["FacultyID"] + "\n")

    #function to add department
    def add_department(self):
        self.DepartmentID = input("Department ID: ")
        while(self.FacultyID in self.DepartmentList.keys()):
            print("The ID is already existed")
            self.DepartmentList = input("Faculty ID: ")
        self.DepartmentName = input("Department Name: ")
        self.HeadName = input("Head Name: ")
        self.OfficeNo = input("Office No: ")
        self.FacultyID = input("Faculty ID: ")
        self.DepartmentList[self.DepartmentID] = {"DepartmentName":self.DepartmentName, "HeadName":self.HeadName, "OfficeNo":self.OfficeNo, "FacultyID":self.FacultyID}

        self.update_data()

    #function to search for a specific department by id
    def search_a_department(self, id):
        if(id not in self.DepartmentList.keys()):
            print("Search not found")
        else:
            for key in self.DepartmentList:
                if id == key:
                    print(key + " " + self.DepartmentList[key]["DepartmentName"] + " " + self.DepartmentList[key]["HeadName"] + " " + self.DepartmentList[key]["OfficeNo"] + " " + self.DepartmentList[key]["FacultyID"])
                    break

    #function to update information about a department by id
    def update_a_department(self, id):
        if(id not in self.DepartmentList.keys()):
            print("ID(to update) not found")
        else:
            self.DepartmentName = input("Department Name: ")
            self.HeadName = input("Head Name: ")
            self.OfficeNo = input("Office No: ")
            self.FacultyID = input("Faculty ID: ")
            self.DepartmentList[id] = {"DepartmentName":self.DepartmentName, "HeadName":self.HeadName, "OfficeNo":self.OfficeNo, "FacultyID":self.FacultyID}

            self.update_data()
            print("The department has been updated")

    #function to delete a department by id
    def delete_a_department(self, id):

        if(id not in self.DepartmentList.keys()):
            print("ID(to delete) not found")
        else:
            for key in self.DepartmentList:
                if id == key:
                    del self.DepartmentList[id]
                    break

            self.update_data()
            print("The department has been deleted")

    #function to display all the departments
    def display_all_department(self):
        for key in self.DepartmentList:
            print(key + " " + self.DepartmentList[key]["DepartmentName"] + " " + self.DepartmentList[key]["HeadName"] + " " + self.DepartmentList[key]["OfficeNo"] + " " + self.DepartmentList[key]["FacultyID"])

    #function to display all the departments that belongs a faculty
    def display_departments_by_a_faculty(self, fac_id):
        existedFacID = []
        for key in self.DepartmentList:
            existedFacID.append(self.DepartmentID[key]["FacultyID"])

        if(fac_id not in existedFacID):
            print("The Faculty ID doesn't exist")
        else:
            for key in self.DepartmentList:
                if(self.DepartmentList[key]["FacultyID"] == fac_id):
                    print(key + " " + self.DepartmentList[key]["DepartmentName"] + " " + self.DepartmentList[key]["HeadName"] + " " + self.DepartmentList[key]["OfficeNo"] + " " + self.DepartmentList[key]["FacultyID"])

departmentList1 = Department()
while(1):
    #display the menu and get the user's input
    print("")
    display_menu()
    menu = input("Select menu: ").lower()
    print("")

    #decision based on the user's input
    if(menu == "a"):
        departmentList1.add_department()
    elif(menu == "b"):
        id = input("ID(to search): ")
        departmentList1.search_a_department(id)
    elif(menu == "c"):
        id = input("ID(to update): ")
        departmentList1.update_a_department(id)
    elif(menu == "d"):
        id = input("ID(to delete): ")
        departmentList1.delete_a_department(id)
    elif(menu == "e"):
        fac_id = input("Faculty ID(to search): ")
        departmentList1.display_departments_by_a_faculty(fac_id)
    elif(menu == "f"):
        departmentList1.display_all_department()
    elif(menu == "g"):
        break
    else:
        print("Please  enter a letter between a and g")