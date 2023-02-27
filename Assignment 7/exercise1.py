#function to display the menu
def display_menu():
    print("a. Add a new faculty")
    print("b. Search a faculty by id")
    print("c. Update a faculty by id")
    print("d. Delete a faculty by id")
    print("e. Display all faculties")
    print("f. Exit program")

class Faculty:
    #the init function to read all the data about faculty from the file into a dictionary
    def __init__(self):
        with open("Faculty.txt","r") as file1:
            data = file1.read().rstrip("\n")

        self.FacultyList = {}
        list1 = data.split("\n")
        for item in list1:
            self.FacultyID, self.FacultyName, self.DeanName, self.OfficeNo = item.split(", ")
            self.FacultyList[self.FacultyID] = {"FacultyName":self.FacultyName, "DeanName":self.DeanName, "OfficeNo":self.OfficeNo}

    #function to update the new data to the file
    def update_data(self):
        with open("Faculty.txt","w") as file1:
            for key in self.FacultyList:
                file1.write(key + ", " + self.FacultyList[key]["FacultyName"] + ", " + self.FacultyList[key]["DeanName"] + ", " + self.FacultyList[key]["OfficeNo"] + "\n")

    #function to add a new faculty
    def add_faculty(self):
        self.FacultyID = input("Faculty ID: ")
        while(self.FacultyID in self.FacultyList.keys()):
            print("The ID is already existed")
        self.FacultyID = input("Faculty ID: ")
        self.FacultyName = input("Faculty Name: ")
        self.DeanName = input("Dean Name: ")
        self.OfficeNo = input("Office No: ")
        self.FacultyList[self.FacultyID] = {"FacultyName":self.FacultyName, "DeanName":self.DeanName, "OfficeNo":self.OfficeNo}

        self.update_data()

    #function to search for a specific faculty by id   
    def search_a_faculty(self, id):
        if(id not in self.FacultyList.keys()):
            print("Search not found")
        else:
            for key in self.FacultyList:
                if id == key:
                    print(key + " " + self.FacultyList[key]["FacultyName"] + " " + self.FacultyList[key]["DeanName"] + " " + self.FacultyList[key]["OfficeNo"])
                    break
    
    #function to update infomation about a faculty by id
    def update_a_faculty(self, id):
        if(id not in self.FacultyList.keys()):
            print("ID(to update) not found")
        else:
            self.FacultyID = input("Faculty ID: ")
            self.FacultyName = input("Faculty Name: ")
            self.DeanName = input("Dean Name: ")
            self.OfficeNo = input("Office No: ")
            self.FacultyList[id] = {"FacultyName":self.FacultyName, "DeanName":self.DeanName, "OfficeNo":self.OfficeNo}

            self.update_data()

    #function to delete a faculty by id
    def delete_a_faculty(self, id):
        if(id not in self.FacultyList.keys()):
            print("ID(to delete) not found")
        else:
            for key in self.FacultyList:
                if id == key:
                    del self.FacultyList[id]
                    break

            self.update_data()

    #function to display all the faculties
    def display_all_faculties(self):
        for key in self.FacultyList:
            print(key + " " + self.FacultyList[key]["FacultyName"] + " " + self.FacultyList[key]["DeanName"] + " " + self.FacultyList[key]["OfficeNo"])

facultyList1 = Faculty()
while(1):
    #display the menu and get the user's input
    print("")
    display_menu()
    menu = input("Select menu: ").lower()
    print("")

    #decision based on the user's input
    if(menu == "a"):
        facultyList1.add_faculty()
    elif(menu == "b"):
        id = input("ID(to search): ")
        facultyList1.search_a_faculty(id)
    elif(menu == "c"):
        id = input("ID(to update): ")
        facultyList1.update_a_faculty(id)
    elif(menu == "d"):
        id = input("ID(to delete): ")
        facultyList1.delete_a_faculty(id)
    elif(menu == "e"):
        facultyList1.display_all_faculties()
    elif(menu == "f"):
        break
    else:
        print("Please enter a letter between a and f")    