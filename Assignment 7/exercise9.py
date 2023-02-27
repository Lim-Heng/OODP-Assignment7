class Login:
    #the init function to get all the data about account, teacher and student as a dictionary
    def __init__(self):
        with open("Account.txt","r") as file1:
            data = file1.read().rstrip("\n")
        self.AccountList = {}
        list1 = data.split("\n")
        for item in list1:
            self.AccountID, self.UserName, self.Password, self.PhoneNo, self.Role, self.UserID = item.split(", ")
            self.AccountList[self.AccountID] = {"UserName":self.UserName, "PassWord":self.Password, "PhoneNo":self.PhoneNo, "Role":self.Role, "UserID":self.UserID}

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


    def login_verification(self):
        login = False

        while(1):
            userName = input("UserName: ")
            passWord = input("Password: ")

            for key in self.AccountList:
                if(userName == self.AccountList[key]["UserName"] and passWord == self.AccountList[key]["PassWord"] and self.AccountList[key]["Role"] == "Teacher"):
                    print("Hi, " + self.AccountList[key]["Role"] + ": " + self.TeacherList[self.AccountList[key]["UserID"]]["TeacherName"])
                    login = True
                    break

                elif(userName == self.AccountList[key]["UserName"] and passWord == self.AccountList[key]["PassWord"] and self.AccountList[key]["Role"] == "Student"):
                    print("Hi, " + self.AccountList[key]["Role"] + ": " + self.StudentList[self.AccountList[key]["UserID"]]["StudentName"])
                    login = True
                    break

            if(login == False):
                print("Wrong username or password\n")
            else:
                break

login1 = Login()
login1.login_verification()