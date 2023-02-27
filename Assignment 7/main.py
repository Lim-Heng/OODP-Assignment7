import runpy

while(1):
    print("")
    print("1. Manage Faculties")
    print("2. Manage Departments")
    print("3. Manage Students")
    print("4. Enroll Students into Departments")
    print("5. Manage Course")
    print("6. Manage teacher")
    print("7. Assign Course to Teacher")
    print("8. Create teacher and student account")
    print("9. Login")
    print("10. Exit")
    menu = input("Select menu: ").lower()
    print("")

    if(menu == "1"):
        runpy.run_path("Assignment 7/exercise1.py")
    elif(menu == "2"):
        runpy.run_path("Assignment 7/exercise2.py")
    elif(menu == "3"):
        runpy.run_path("Assignment 7/exercise3.py")
    elif(menu == "4"):
        runpy.run_path("Assignment 7/exercise4.py")
    elif(menu == "5"):
        runpy.run_path("Assignment 7/exercise5.py")
    elif(menu == "6"):
        runpy.run_path("Assignment 7/exercise6.py")
    elif(menu == "7"):
        runpy.run_path("Assignment 7/exercise7.py")
    elif(menu == "8"):
        runpy.run_path("Assignment 7/exercise8.py")
    elif(menu == "9"):
        runpy.run_path("Assignment 7/exercise9.py")
    elif(menu == "10"):
        break
    else:
        print("Please enter a number between 1 and 9")