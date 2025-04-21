import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt

# Set the appearance and color theme (optional)
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("School Management System")
        self.geometry("800x600")
        
        # Container to hold all pages
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        # Dictionary of frames (pages)
        self.frames = {}
        for F in (LoginPage, RegisterPage, MainMenuPage, ManageStudentsPage, StudentFeesPage, ManageTeachersPage, GraphsPage):
            frame = F(parent=self.container, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(LoginPage)
    
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

# ------------------ LOGIN PAGE ------------------
class LoginPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.label = ctk.CTkLabel(self, text="Login", font=("Arial", 24))
        self.label.pack(pady=20)
        
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Username")
        self.username_entry.pack(pady=10)
        
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=10)
        
        self.login_button = ctk.CTkButton(self, text="Login", command=self.login)
        self.login_button.pack(pady=10)
        
        self.register_button = ctk.CTkButton(self, text="Register", 
                                             command=lambda: controller.show_frame(RegisterPage))
        self.register_button.pack(pady=10)
        
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        try:
            df = pd.read_csv("Data.csv")
        except Exception:
            messagebox.showerror("Error", "Data.csv not found!")
            return
        
        # Validate credentials from Data.csv
        matching_creds = (len(df[(df.username == username) & (df.password == password)]) > 0)
        if matching_creds:
            self.controller.show_frame(MainMenuPage)
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password.")

# ------------------ REGISTER PAGE ------------------
class RegisterPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.label = ctk.CTkLabel(self, text="Register New User", font=("Arial", 24))
        self.label.pack(pady=20)
        
        self.username_entry = ctk.CTkEntry(self, placeholder_text="New Username")
        self.username_entry.pack(pady=10)
        
        self.password_entry = ctk.CTkEntry(self, placeholder_text="New Password", show="*")
        self.password_entry.pack(pady=10)
        
        self.register_button = ctk.CTkButton(self, text="Register", command=self.register)
        self.register_button.pack(pady=10)
        
        self.back_button = ctk.CTkButton(self, text="Back to Login",
                                         command=lambda: controller.show_frame(LoginPage))
        self.back_button.pack(pady=10)
        
    def register(self):
        new_user = self.username_entry.get()
        new_pass = self.password_entry.get()
        try:
            df = pd.read_csv("Data.csv")
        except Exception:
            df = pd.DataFrame(columns=["username", "password"])
        df = df.append({"username": new_user, "password": new_pass}, ignore_index=True)
        df.to_csv("Data.csv", index=False)
        messagebox.showinfo("Success", "User registered successfully!")
        self.controller.show_frame(LoginPage)

# ------------------ MAIN MENU PAGE ------------------
class MainMenuPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.label = ctk.CTkLabel(self, text="School Management System", font=("Arial", 24))
        self.label.pack(pady=20)
        
        self.btn_register = ctk.CTkButton(self, text="Register/Login", 
                                          command=lambda: controller.show_frame(RegisterPage))
        self.btn_register.pack(pady=5)
        
        self.btn_students = ctk.CTkButton(self, text="Manage Students", 
                                          command=lambda: controller.show_frame(ManageStudentsPage))
        self.btn_students.pack(pady=5)
        
        self.btn_fees = ctk.CTkButton(self, text="Student Fees", 
                                      command=lambda: controller.show_frame(StudentFeesPage))
        self.btn_fees.pack(pady=5)
        
        self.btn_teachers = ctk.CTkButton(self, text="Manage Teachers", 
                                          command=lambda: controller.show_frame(ManageTeachersPage))
        self.btn_teachers.pack(pady=5)
        
        self.btn_notices = ctk.CTkButton(self, text="Notices", command=self.show_notices)
        self.btn_notices.pack(pady=5)
        
        self.btn_graphs = ctk.CTkButton(self, text="Graphs", 
                                        command=lambda: controller.show_frame(GraphsPage))
        self.btn_graphs.pack(pady=5)
        
        self.btn_logout = ctk.CTkButton(self, text="Logout", 
                                        command=lambda: controller.show_frame(LoginPage))
        self.btn_logout.pack(pady=5)
        
        self.btn_exit = ctk.CTkButton(self, text="Logout & Exit", command=self.quit)
        self.btn_exit.pack(pady=5)
        
    def show_notices(self):
        try:
            df = pd.read_csv("Notice Board.csv")
            notices = df.to_string(index=False)
        except Exception:
            notices = "No notices found."
        # Create a window with a scrollable text widget
        win = ctk.CTkToplevel(self)
        win.title("Notices")
        frame = ctk.CTkFrame(win)
        frame.pack(fill="both", expand=True, padx=10, pady=10)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")
        text_box = tk.Text(frame, width=80, height=20, yscrollcommand=scrollbar.set)
        text_box.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=text_box.yview)
        text_box.insert("1.0", notices)
        text_box.config(state="disabled")

# ------------------ MANAGE STUDENTS PAGE ------------------
class ManageStudentsPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.label = ctk.CTkLabel(self, text="Manage Students", font=("Arial", 24))
        self.label.pack(pady=20)
        
        self.btn_add = ctk.CTkButton(self, text="Add New Student", command=self.add_student_form)
        self.btn_add.pack(pady=5)
        
        self.btn_display = ctk.CTkButton(self, text="Display Student Info", command=self.display_students)
        self.btn_display.pack(pady=5)
        
        self.btn_back = ctk.CTkButton(self, text="Back", 
                                      command=lambda: controller.show_frame(MainMenuPage))
        self.btn_back.pack(pady=5)
    
    def add_student_form(self):
        add_win = ctk.CTkToplevel(self)
        add_win.title("Add New Student")
        
        fields = ["Roll Number", "Name", "Age", "Grade", "Phone Number", 
                  "English", "Physics", "Chemistry", "Maths", "IP", "Fees"]
        entries = {}
        for i, field in enumerate(fields):
            l = ctk.CTkLabel(add_win, text=field)
            l.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            e = ctk.CTkEntry(add_win)
            e.grid(row=i, column=1, padx=10, pady=5)
            entries[field] = e
        
        def save_student():
            rollnumber = entries["Roll Number"].get()
            name = entries["Name"].get()
            age = entries["Age"].get()
            grade = entries["Grade"].get()
            phone_no = entries["Phone Number"].get()
            english = entries["English"].get()
            physics = entries["Physics"].get()
            chemistry = entries["Chemistry"].get()
            maths = entries["Maths"].get()
            ip = entries["IP"].get()
            fees = entries["Fees"].get()
            
            # Save student info
            try:
                df_students = pd.read_csv("students.csv")
            except Exception:
                df_students = pd.DataFrame(columns=["rollnumber", "name", "age", "grade", "phone_no"])
            df_students.loc[len(df_students)] = [rollnumber, name, age, grade, phone_no]
            df_students.to_csv("students.csv", index=False)
            
            # Save student marks
            try:
                df_marks = pd.read_csv("studentmark.csv")
            except Exception:
                df_marks = pd.DataFrame(columns=["rollnumber", "english", "physics", "chemistry", "maths", "ip"])
            df_marks.loc[len(df_marks)] = [rollnumber, english, physics, chemistry, maths, ip]
            df_marks.to_csv("studentmark.csv", index=False)
            
            # Save fee details
            try:
                df_fees = pd.read_csv("fees.csv")
            except Exception:
                df_fees = pd.DataFrame(columns=["rollnumber", "fees"])
            df_fees.loc[len(df_fees)] = [rollnumber, fees]
            df_fees.to_csv("fees.csv", index=False)
            
            messagebox.showinfo("Success", "Student information saved successfully!")
            add_win.destroy()
        
        btn_save = ctk.CTkButton(add_win, text="Save", command=save_student)
        btn_save.grid(row=len(fields), column=0, columnspan=2, pady=10)
    
    def display_students(self):
        try:
            df = pd.read_csv("students.csv")
            info = df.to_string(index=False)
        except Exception:
            info = "No student information available."
        display_win = ctk.CTkToplevel(self)
        display_win.title("Student Information")
        
        # Create a frame with a vertical scrollbar for the text widget
        frame = ctk.CTkFrame(display_win)
        frame.pack(fill="both", expand=True, padx=10, pady=10)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")
        text_box = tk.Text(frame, width=80, height=20, yscrollcommand=scrollbar.set)
        text_box.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=text_box.yview)
        
        text_box.insert("1.0", info)
        text_box.config(state="disabled")

# ------------------ STUDENT FEES PAGE ------------------
class StudentFeesPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.label = ctk.CTkLabel(self, text="Student Fees", font=("Arial", 24))
        self.label.pack(pady=20)
        
        self.btn_display = ctk.CTkButton(self, text="Display Fees", command=self.display_fees)
        self.btn_display.pack(pady=5)
        
        self.btn_back = ctk.CTkButton(self, text="Back", 
                                      command=lambda: controller.show_frame(MainMenuPage))
        self.btn_back.pack(pady=5)
    
    def display_fees(self):
        try:
            df = pd.read_csv("fees.csv")
            fees_info = df.to_string(index=False)
        except Exception:
            fees_info = "No fee information available."
        fees_win = ctk.CTkToplevel(self)
        fees_win.title("Fees Information")
        
        frame = ctk.CTkFrame(fees_win)
        frame.pack(fill="both", expand=True, padx=10, pady=10)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")
        text_box = tk.Text(frame, width=80, height=20, yscrollcommand=scrollbar.set)
        text_box.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=text_box.yview)
        
        text_box.insert("1.0", fees_info)
        text_box.config(state="disabled")

# ------------------ MANAGE TEACHERS PAGE ------------------
class ManageTeachersPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.label = ctk.CTkLabel(self, text="Manage Teachers", font=("Arial", 24))
        self.label.pack(pady=20)
        
        self.btn_add = ctk.CTkButton(self, text="Add New Teacher", command=self.add_teacher_form)
        self.btn_add.pack(pady=5)
        
        self.btn_display = ctk.CTkButton(self, text="Display Teacher Info", command=self.display_teachers)
        self.btn_display.pack(pady=5)
        
        self.btn_homework = ctk.CTkButton(self, text="Add Homework", command=self.add_homework_form)
        self.btn_homework.pack(pady=5)
        
        self.btn_notice = ctk.CTkButton(self, text="Add Notice", command=self.add_notice_form)
        self.btn_notice.pack(pady=5)
        
        self.btn_timetable = ctk.CTkButton(self, text="Teacher Timetable", command=self.show_teacher_timetable)
        self.btn_timetable.pack(pady=5)
        
        self.btn_back = ctk.CTkButton(self, text="Back", 
                                      command=lambda: controller.show_frame(MainMenuPage))
        self.btn_back.pack(pady=5)
    
    def add_teacher_form(self):
        add_win = ctk.CTkToplevel(self)
        add_win.title("Add New Teacher")
        fields = ["Teacher ID", "Name", "Subject", "Salary"]
        entries = {}
        for i, field in enumerate(fields):
            l = ctk.CTkLabel(add_win, text=field)
            l.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            e = ctk.CTkEntry(add_win)
            e.grid(row=i, column=1, padx=10, pady=5)
            entries[field] = e
        
        def save_teacher():
            teacher_id = entries["Teacher ID"].get()
            name = entries["Name"].get()
            subject = entries["Subject"].get()
            salary = entries["Salary"].get()
            try:
                df_teachers = pd.read_csv("teachers.csv")
            except Exception:
                df_teachers = pd.DataFrame(columns=["teacher_id", "name", "subject", "salary"])
            df_teachers.loc[len(df_teachers)] = [teacher_id, name, subject, salary]
            df_teachers.to_csv("teachers.csv", index=False)
            messagebox.showinfo("Success", "Teacher information saved successfully!")
            add_win.destroy()
        
        btn_save = ctk.CTkButton(add_win, text="Save", command=save_teacher)
        btn_save.grid(row=len(fields), column=0, columnspan=2, pady=10)
    
    def display_teachers(self):
        try:
            df = pd.read_csv("teachers.csv")
            info = df.to_string(index=False)
        except Exception:
            info = "No teacher information available."
        display_win = ctk.CTkToplevel(self)
        display_win.title("Teacher Information")
        frame = ctk.CTkFrame(display_win)
        frame.pack(fill="both", expand=True, padx=10, pady=10)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")
        text_box = tk.Text(frame, width=80, height=20, yscrollcommand=scrollbar.set)
        text_box.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=text_box.yview)
        text_box.insert("1.0", info)
        text_box.config(state="disabled")
    
    def add_homework_form(self):
        add_win = ctk.CTkToplevel(self)
        add_win.title("Add Homework")
        fields = ["Subject Code", "Subject Name", "Homework", "Due Date (yyyy-mm-dd)"]
        entries = {}
        for i, field in enumerate(fields):
            l = ctk.CTkLabel(add_win, text=field)
            l.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            e = ctk.CTkEntry(add_win)
            e.grid(row=i, column=1, padx=10, pady=5)
            entries[field] = e
        
        def save_homework():
            subject_code = entries["Subject Code"].get()
            subject = entries["Subject Name"].get()
            homework = entries["Homework"].get()
            due_date = entries["Due Date (yyyy-mm-dd)"].get()
            try:
                df_homework = pd.read_csv("homework.csv")
            except Exception:
                df_homework = pd.DataFrame(columns=["subject_code", "subject", "homework", "due_date"])
            df_homework.loc[len(df_homework)] = [subject_code, subject, homework, due_date]
            df_homework.to_csv("homework.csv", index=False)
            messagebox.showinfo("Success", "Homework saved successfully!")
            add_win.destroy()
        
        btn_save = ctk.CTkButton(add_win, text="Save", command=save_homework)
        btn_save.grid(row=len(fields), column=0, columnspan=2, pady=10)
    
    def add_notice_form(self):
        add_win = ctk.CTkToplevel(self)
        add_win.title("Add Notice")
        fields = ["Grade/Class", "Notice"]
        entries = {}
        for i, field in enumerate(fields):
            l = ctk.CTkLabel(add_win, text=field)
            l.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            e = ctk.CTkEntry(add_win)
            e.grid(row=i, column=1, padx=10, pady=5)
            entries[field] = e
        
        def save_notice():
            grade = entries["Grade/Class"].get()
            notice = entries["Notice"].get()
            try:
                df_notice = pd.read_csv("Notice Board.csv")
            except Exception:
                df_notice = pd.DataFrame(columns=["grade", "notice"])
            df_notice.loc[len(df_notice)] = [grade, notice]
            df_notice.to_csv("Notice Board.csv", index=False)
            messagebox.showinfo("Success", "Notice saved successfully!")
            add_win.destroy()
        
        btn_save = ctk.CTkButton(add_win, text="Save", command=save_notice)
        btn_save.grid(row=len(fields), column=0, columnspan=2, pady=10)
    
    def show_teacher_timetable(self):
        try:
            df = pd.read_csv("teacher_timetable.csv")
            info = df.to_string(index=False)
        except Exception:
            info = "No timetable information available."
        timetable_win = ctk.CTkToplevel(self)
        timetable_win.title("Teacher Timetable")
        frame = ctk.CTkFrame(timetable_win)
        frame.pack(fill="both", expand=True, padx=10, pady=10)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")
        text_box = tk.Text(frame, width=80, height=20, yscrollcommand=scrollbar.set)
        text_box.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=text_box.yview)
        text_box.insert("1.0", info)
        text_box.config(state="disabled")

# ------------------ GRAPHS PAGE ------------------
class GraphsPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.label = ctk.CTkLabel(self, text="Graphs", font=("Arial", 24))
        self.label.pack(pady=20)
        
        self.subject_var = tk.StringVar(value="Select Subject")
        self.dropdown = ctk.CTkOptionMenu(self, variable=self.subject_var, 
                                          values=["physics", "chemistry", "maths", "english", "ip"])
        self.dropdown.pack(pady=10)
        
        self.btn_line = ctk.CTkButton(self, text="Line Graph", command=lambda: self.show_graph("line"))
        self.btn_line.pack(pady=5)
        
        self.btn_bar = ctk.CTkButton(self, text="Bar Graph", command=lambda: self.show_graph("bar"))
        self.btn_bar.pack(pady=5)
        
        self.btn_back = ctk.CTkButton(self, text="Back", 
                                      command=lambda: controller.show_frame(MainMenuPage))
        self.btn_back.pack(pady=5)
    
    def show_graph(self, graph_type):
        subject = self.subject_var.get()
        if subject == "Select Subject":
            messagebox.showerror("Error", "Please select a subject.")
            return
        try:
            df = pd.read_csv("studentmark.csv")
        except Exception:
            messagebox.showerror("Error", "studentmark.csv not found.")
            return
        
        if graph_type == "line":
            df[subject].plot(kind="line", marker='o', color="blue")
        else:
            df[subject].plot(kind="bar", color="green")
        plt.title(f"{subject.capitalize()} Marks")
        plt.xlabel("Roll Number")
        plt.ylabel("Marks")
        plt.grid(True)
        plt.show()

# ------------------ MAIN ------------------
if __name__ == "__main__":
    app = App()
    app.mainloop()
