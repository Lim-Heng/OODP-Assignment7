def display_menu():
    print("a. Create a teacher account")
    print("b. Create a student account")
    print("c. Exit program")

class Create_Account:
    def __init__(self):
        with open("Teacher.txt","r") as file1:
            data = file1.read().rstrip("\n")
        self.TeacherList = {}
        list1 = data.split("\n")
        for item in list1:
            self.TeacherID, self.TeacherName, self.Gender, self.DOB, self.PhoneNo, self.Address = item.split(", ")
            self.TeacherList[self.TeacherID] = {"TeacherName":self.TeacherName, "Gender":self.Gender, "DOB":self.DOB, "PhoneNo":self.PhoneNo, "Address":self.Address}

        with open("Student.txt","r") as file1:
            data = file1.read().rstrip("\n")
        self.StudentList = {}
        list1 = data.split("\n")
        for item in list1:
            self.StudentID, self.StudentName, self.Gender, self.DOB, self.PhoneNo, self.Address, self.Year, self.Generation, self.Degree = item.split(", ")
            self.StudentList[self.StudentID] = {"StudentName":self.StudentName, "Gender":self.Gender, "DOB":self.DOB, "PhoneNo":self.PhoneNo, "Address":self.Address, "Year":self.Year, "Generation":self.Generation, "Degree":self.Degree}

    def get_accounts_as_dict(self):
        with open("Account.txt","r") as file1:
            data = file1.read().rstrip("\n")
        self.AccountList = {}
        list1 = data.split("\n")
        for item in list1:
            self.AccountID, self.UserName, self.Password, self.PhoneNo, self.Role, self.UserID = item.split("\n")
            self.AccountList[self.AccountID] = {"UserName":self.UserName, "Password":self.Password, "PhoneNo":self.PhoneNo, "Role":self.Role, "UserID":self.UserID}

    def create_a_teacher_account(self):
        self.get_accounts_as_dict()

        self.AccountID = input("Account ID: ")
        while(self.AccountID in self.AccountList.keys()):
            print("The account ID is already existed")
            self.AccountID = input("Account ID: ")
        self.UserName = input("Username: ")
        self.Password = input("Password: ")
        self.Role = "Teacher"
        self.UserID = input("User ID: ")

        if(self.UserID not in self.TeacherList.keys()):
            print("The teacher ID doesn't exist")
        else:
            self.PhoneNo = self.TeacherList[self.UserID]["PhoneNo"]
            with open("Account.txt","a") as file1:
                file1.write(self.AccountID + ", " + self.UserName + ", " + self.Password + ", " + self.PhoneNo + ", " + self.Role + ", " + self.UserID + "\n")

    def create_a_student_account(self):
        self.AccountID = input("Account ID: ")
        self.UserName = input("Username: ")
        self.Password = input("Password: ")
        self.Role = "Student"
        self.UserID = input("User ID: ")

        if(self.UserID not in self.StudentList.keys()):
            print("The student ID doesn't exist")
        else:
            self.PhoneNo = self.StudentList[self.UserID]["PhoneNo"]
            with open("Account.txt", "a") as file1:
                file1.write(self.AccountID + ", " + self.UserName + ", " + self.Password + ", " + self.PhoneNo + ", " + self.Role + ", " + self.UserID + "\n")

accountList1 = Create_Account()
while(1):
    print("")
    display_menu()
    menu = input("Select menu: ")
    print("")

    if(menu == "a"):
        accountList1.create_a_teacher_account()
    elif(menu == "b"):
        accountList1.create_a_student_account()
    elif(menu == "c"):
        break
    else:
        print("Please enter a letter between a and c")