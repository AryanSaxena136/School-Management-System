import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
'''
username = ['aryan', 'admin']
passward = ['aryan123', 'admin1234']
'''
def login():
    while True:
        userData = pd.read_csv('Data.csv')
        df = pd.DataFrame(userData)
        username = df['username']
        password = df['password']
        user = input('Enter username:')
        passw = input('Enter Password:')
        matching_creds = (len(df[(df.username == user) & (df.password == passw)]) > 0)
        if matching_creds:
            main_loop()
        else:
            print('Your username or password is incorrect')
def show_menu():
    print("\n--- School Management System ---")
    print("\n1. Register/Login")
    print("2. Manage Students")
    print("3. Students Fees")
    print("4. Manage Teachers")
    print('5. Notices')
    print('6. Graphs')
    print("7. Logout")
    print("8. Logout & Exit")   
def register_login():
    new_user = input('Enter New username  :')
    new_pass = input('Enter new password  :')
    df = pd.read_csv("Data.csv")
    df = pd.DataFrame(df)
    df.loc[new_user] = [new_user,new_pass]
    df.to_csv('Data.csv',index = False)
    print("New UserID & Password saved successfully!")
    print('-------------------------------------------------------------------------')

def manage_students():
    while True:
        print('\t1. Add New Student')
        print('\t2. Display Student info')
        print('\t3. Back')
        ch1=int(input('enter your choice(1-3)  :'))
        if ch1 == 1:
            rollnumber = int(input("Enter Roll Number  :"))
            name = input("Enter Student Name  :")
            age = input("Enter Student Age  :")
            grade = input("Enter Student Grade  :")
            phone_no = input("Enter a Phone Number  :")
            english = input("Enter Student's marks in English  :")
            physics = input("Enter Student's marks in Physics  :")
            cemistry = input("Enter Student's marks in Chemistry  :")
            maths = input("Enter Student's marks in Maths  :")
            ip = input("Enter Student's marks in IP  :")
            fees = input("Enter student's annual fee Amount  :")
            df1 = pd.read_csv("students.csv")
            df1 = pd.DataFrame(df1)
            df1.loc[rollnumber] = [rollnumber,name, age, grade, phone_no]
            df1.to_csv('students.csv',index=False)
            df2 = pd.read_csv("studentmark.csv")
            df2.loc[rollnumber] = [rollnumber,english,physics,cemistry,maths,ip]
            df2.to_csv("studentmark.csv",index=False)
            df3 = pd.read_csv("fees.csv")
            df3.loc[rollnumber]=[rollnumber,fees]
            df3.to_csv("fees.csv",index=False)
            print("Student information saved successfully!")
            print('-------------------------------------------------------------------------')
        elif ch1 == 2:
            ch1_is_2()
        elif ch1 == 3:
            main_loop()
        else:
            print("Invalid  choice. Please Try Again")
def ch1_is_2():
    while True:
        print('\t\t1. To Display Student Information')
        print('\t\t2. Test Report')
        print('\t\t3. Timetable')
        print('\t\t4. Homework')
        print('\t\t5. Back')
        ch2=int(input("Enter your choice(1-5):"))
        if ch2 == 1:
            stdinfo = pd.read_csv("students.csv")
            print(stdinfo)
            print('-------------------------------------------------------------------------')
        elif ch2==2:
            df = pd.read_csv("studentmark.csv")
            print(df)               
        elif ch2 == 3:
            df3 = pd.read_csv("Time Table.csv")
            print(df3)
            print('-------------------------------------------------------------------------')
        elif ch2 == 4:
            df4 = pd.read_csv("homework.csv")
            print(df4)
            print('-------------------------------------------------------------------------')
        elif ch2 == 5:
            manage_students()
            print('-------------------------------------------------------------------------')
        else:
            print("--Invalid choice. Please Try Again--")
def manage_teachers():
    teachers_df=pd.read_csv('teachers.csv')
    while True:
        print('\t1. Add New Teacher')
        print("\t2. Display data of all Teachers.")
        print("\t3. Add Homework for your Students.")
        print('\t4. ADD Notices')
        print('\t5. Teacher Time Table')
        print('\t6. Back')
        ar3=int(input("Enter your choice(1-7)  :"))
        if ar3 == 1:
            teacher_id = input("Enter Teacher ID  :")
            name = input("Enter Teacher Name  :")
            subject = input("Enter Teacher Subject  :")
            salary = int(input("Enter Teacher's Salary  :"))
            df8 = pd.read_csv("teachers.csv")
            df8.loc[teacher_id] = [teacher_id,name,subject,salary]
            df8.to_csv("teachers.csv",index=False)
            print("Teacher information saved successfully!")
            print('-------------------------------------------------------------------------')
        if ar3 == 2:
            while True:
                print('\t\t1. Teacher Information')
                print('\t\t2. Student Teacher Subject Graph')
                print('\t\t3. Back')
                ch4 = int(input("Enter your choice(1-3)  :"))
                if ch4 == 1:
                    print("\n--- Teacher Information ---")
                    print(teachers_df)
                    print('-------------------------------------------------------------------------')
                elif ch4 == 2:
                    teachers_df = pd.read_csv('teachers.csv')
                    print("\n--- Teacher Information ---")
                    print(teachers_df)
                    teacher_names = teachers_df['name']
                    subject = teachers_df['subject']
                    plt.scatter(teacher_names, subject, marker='o', color='b', label='Teachers')
                    plt.title("Teacher Subjects")
                    plt.xlabel("Teacher Names")
                    plt.ylabel("Subjects")
                    plt.xticks(rotation=45)
                    plt.grid(True)
                    plt.show()
                    print('-------------------------------------------------------------------------')
                elif ch4 == 3:
                    manage_teachers()
                else:
                    print("Invalid choice. Please Try Again")
        elif ar3 == 3:
            Subject_code = input("Enter the subject code  :")
            Subject = input("Whatis the name of the subject  :")
            homework = input("type the homework  :")
            due_date =input("Due Date ti submit the Homework(yyyy-mm-dd)  :")
            df9 = pd.read_csv("homework.csv")
            df9.loc[Subject_code] = [Subject_code,Subject,homework,due_date]
            df9.to_csv("homework.csv",index = False)
            print("Homework saved successfully!")
            print('-------------------------------------------------------------------------')
        elif ar3 == 4:
            Class = input("this notice is for grade?  :")
            Notice = input("Type the Notice  :")
            df10 = pd.read_csv("Notice Board.csv")
            df10.loc[Class] = [Class,Notice]
            df10.to_csv("Notice Board.csv",index = False)
            print("notice saved successfully!")
            print('-------------------------------------------------------------------------')
        elif ar3 == 5:
            df2 = pd.read_csv("teacher_timetable.csv")
            print(df2)
            print('-------------------------------------------------------------------------')
        elif ar3 == 6:
            main_loop()
        else:
            print("Invalid choice. Please Try Again")
def line_graph():
    while True:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>LINE GRAPHS OF MARKS OF STUDENTS IN SUBJECTS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print('\t\t1.Physics ')
        print('\t\t2.Chemistry')
        print('\t\t3.Maths')
        print('\t\t4.English')
        print('\t\t5.IP')
        print('\t\t6.Back')
        io = pd.read_csv("studentmark.csv")
        line=int(input('Enter your choice(1-6)  :'))
        
        if line == 1:
            io = pd.read_csv("studentmark.csv")
            io['physics'].plot(kind = 'line', color = 'fuchsia', legend = False)
            plt.title("physics")
            plt.ylabel('Marks in Physics')
            plt.xlabel('Roll No.')
            plt.show()
            print('-------------------------------------------------------------------------')
        elif line == 2:
            io['chemistry'].plot(kind = 'line',color = 'cyan',legend = False)
            plt.title("chemistry")
            plt.ylabel('Marks in Chemistry')
            plt.xlabel('Roll No.')
            plt.show()
            print('-------------------------------------------------------------------------')
        elif line == 3:
            io['maths'].plot(kind = 'line', color = 'green', legend = False)
            plt.title("maths")
            plt.ylabel('Marks in Maths')
            plt.xlabel('Roll No.')
            plt.show()
            print('-------------------------------------------------------------------------')
        elif line == 4:
            io['english'].plot(kind = 'line', color = 'yellow', legend = False)
            plt.title("english")
            plt.ylabel('Marks in English')
            plt.xlabel('Roll No.')
            plt.show()
            print('-------------------------------------------------------------------------')
        elif line == 5:
            io['ip'].plot(kind = 'line', color = 'pink', legend = False)
            plt.title("ip")
            plt.ylabel('Marks in IP')
            plt.xlabel('Roll No.')
            plt.show()
            print('-------------------------------------------------------------------------')
        elif line == 6:
            print('-------------------------------------------------------------------------')
            graphs()
        else:
            print('Please Try again')
def bar_graph():
    while True:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>BAR GRAPHS OF MARKS OF STUDENTS  IN SUBJECTS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print('\t\t1.Physics ')
        print('\t\t2.Chemistry')
        print('\t\t3.Maths')
        print('\t\t4.English')
        print('\t\t5.IP')
        print('\t\t6.Back')
        io = pd.read_csv("studentmark.csv")
        bar = int(input("Enter your Choice(1-6)  :"))
        if bar == 1:
            io['physics'].plot(kind = 'bar', color = 'fuchsia', legend = False)
            plt.title("physics")
            plt.ylabel('Marks in Physics')
            plt.xlabel('Roll No.')
            plt.show()
            print('-------------------------------------------------------------------------')
        elif bar == 2:
            io['chemistry'].plot(kind = 'bar', color = 'cyan', legend = False)
            plt.title("chemistry")
            plt.ylabel('Marks in Chemistry')
            plt.xlabel('Roll No.')
            plt.show()
            print('-------------------------------------------------------------------------')
        elif bar == 3:
            io['maths'].plot(kind = 'bar', color = 'green', legend = False)
            plt.title("maths")
            plt.ylabel('Marks in Maths')
            plt.xlabel('Roll No.')
            plt.show()
            print('-------------------------------------------------------------------------')
        elif bar == 4:
            io['english'].plot(kind = 'bar', color = 'yellow', legend = False)
            plt.title("english")
            plt.ylabel('Marks in English')
            plt.xlabel('Roll No.')
            plt.show()
            print('-------------------------------------------------------------------------')
        elif bar == 5:
            io['ip'].plot(kind = 'bar', color = 'pink', legend = False)
            plt.title("ip")
            plt.ylabel('Marks in IP')
            plt.xlabel('Roll No.')
            plt.show()
            print('-------------------------------------------------------------------------')
        elif bar == 6:
            print('-------------------------------------------------------------------------')
            graphs()
        else:
            print('Please Try again')
def graphs():
    while True:
        print("\t1.Line Graphs")
        print("\t2.Bar Graphs")
        print("\t3.Back")
        graph = int(input("Enter Your choce(1-3) :"))
        if graph == 1:
            line_graph()
        elif graph == 2:
            bar_graph()
        elif graph == 3:
            main_loop()
        else:
            print('Please Try again')
# Main program loop
def main_loop():
    while True:
        show_menu()
        ar = int(input("\nEnter your choice(1-8): "))
        if ar == 1:
            register_login()
        elif ar == 2:
            print("\n--- Student Management ---")
            manage_students()
        elif ar == 3:
            print("\n--- Fee ---")
            fees_df =pd.read_csv('fees.csv')
            print(fees_df)
        elif ar == 4:
            print("\n--- Teachers Management ---")
            manage_teachers()
        elif ar == 5:
            print("\n--- Notice Board ---")
            df2 = pd.read_csv("Notice Board.csv")
            print(df2)
            print('-------------------------------------------------------------------------')
        elif ar == 6:
            graphs()
        elif ar == 7:
            print("\nLogging out...")       
            login()
        elif ar == 8:
            print("\nLogging out...")        
            exit()
        else:
            print("Invalid choice. Please try again.")
login()
