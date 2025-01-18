import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkinter import filedialog, messagebox
from functools import partial
import mysql.connector
from datetime import datetime
from mysql.connector import Error
from tkinter import messagebox
import time


# Database connection
def connect_to_db():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="studentmanagement_system"  # Use the same database name here
        )
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

# Initialize database connection
db = connect_to_db()
if db is None:
    raise SystemExit("Unable to connect to the database.")

cursor = db.cursor()

def create_tables():
    try:
        # Create users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                role ENUM('student', 'faculty', 'hod', 'principal' , 'accountant' , 'admin') NOT NULL
            )
        """)
        
        # Create students table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                student_id INT NOT NULL,
                student_name VARCHAR(255) NOT NULL,
                admission_date VARCHAR(255) NOT NULL,
                department VARCHAR(255) NOT NULL,
                semester VARCHAR(255) NOT NULL,
                admission_number INT NOT NULL,
                roll_no INT NOT NULL,
                gender VARCHAR(255) NOT NULL,
                dob VARCHAR(255) NOT NULL,
                blood_group VARCHAR(255) NOT NULL,
                father_name VARCHAR(255) NOT NULL,
                father_occupation VARCHAR(255) NOT NULL,
                mother_name VARCHAR(255) NOT NULL,
                mother_occupation VARCHAR(255) NOT NULL,
                address VARCHAR(255) NOT NULL,
                city VARCHAR(255) NOT NULL,
                country VARCHAR(255) NOT NULL,
                religion VARCHAR(255) NOT NULL,
                caste VARCHAR(255) NOT NULL,
                pin_code INT NOT NULL,
                state VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                phone BIGINT NOT NULL,
                parent_phone BIGINT NOT NULL,
                guardian_name VARCHAR(255) NOT NULL,
                guardian_relationship VARCHAR(255) NOT NULL,
                guardian_phone BIGINT NOT NULL,
                guardian_address VARCHAR(255) NOT NULL,
                photo_path LONGBLOB,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )
        """)
        
        # Create faculty table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS faculty (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                faculty_id INT NOT NULL,
                faculty_name VARCHAR(255) NOT NULL,
                department VARCHAR(255) NOT NULL,
                faculty_gender VARCHAR(255) NOT NULL,
                faculty_dob VARCHAR(255) NOT NULL,
                faculty_blood_group VARCHAR(255) NOT NULL,
                faculty_marital_status VARCHAR(255) NOT NULL,
                faculty_job_position VARCHAR(255) NOT NULL,
                faculty_address VARCHAR(255) NOT NULL,
                faculty_city VARCHAR(255) NOT NULL,
                faculty_country VARCHAR(255) NOT NULL,
                faculty_pin_code INT NOT NULL,
                faculty_state VARCHAR(255) NOT NULL,
                faculty_email VARCHAR(255) NOT NULL,
                faculty_phone BIGINT NOT NULL,
                faculty_guardian_name VARCHAR(255) NOT NULL,
                faculty_guardian_relationship VARCHAR(255) NOT NULL,
                faculty_guardian_phone BIGINT NOT NULL,
                faculty_guardian_address VARCHAR(255) NOT NULL,
                photo_path LONGBLOB,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )
        """)
        
        # Create hod table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS hod (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                faculty_id INT NOT NULL,
                faculty_name VARCHAR(255) NOT NULL,
                department VARCHAR(255) NOT NULL,
                faculty_gender VARCHAR(255) NOT NULL,
                faculty_dob VARCHAR(255) NOT NULL,
                faculty_blood_group VARCHAR(255) NOT NULL,
                faculty_marital_status VARCHAR(255) NOT NULL,
                faculty_job_position VARCHAR(255) NOT NULL,
                faculty_address VARCHAR(255) NOT NULL,
                faculty_city VARCHAR(255) NOT NULL,
                faculty_country VARCHAR(255) NOT NULL,
                faculty_pin_code INT NOT NULL,
                faculty_state VARCHAR(255) NOT NULL,
                faculty_email VARCHAR(255) NOT NULL,
                faculty_phone BIGINT NOT NULL,
                faculty_guardian_name VARCHAR(255) NOT NULL,
                faculty_guardian_relationship VARCHAR(255) NOT NULL,
                faculty_guardian_phone BIGINT NOT NULL,
                faculty_guardian_address VARCHAR(255) NOT NULL,
                photo_path LONGBLOB,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )
        """)
        # Create accountant table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS accountant (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                faculty_id INT NOT NULL,
                faculty_name VARCHAR(255) NOT NULL,
                department VARCHAR(255) NOT NULL,
                faculty_gender VARCHAR(255) NOT NULL,
                faculty_dob VARCHAR(255) NOT NULL,
                faculty_blood_group VARCHAR(255) NOT NULL,
                faculty_marital_status VARCHAR(255) NOT NULL,
                faculty_job_position VARCHAR(255) NOT NULL,
                faculty_address VARCHAR(255) NOT NULL,
                faculty_city VARCHAR(255) NOT NULL,
                faculty_country VARCHAR(255) NOT NULL,
                faculty_pin_code INT NOT NULL,
                faculty_state VARCHAR(255) NOT NULL,
                faculty_email VARCHAR(255) NOT NULL,
                faculty_phone BIGINT NOT NULL,
                faculty_guardian_name VARCHAR(255) NOT NULL,
                faculty_guardian_relationship VARCHAR(255) NOT NULL,
                faculty_guardian_phone BIGINT NOT NULL,
                faculty_guardian_address VARCHAR(255) NOT NULL,
                photo_path LONGBLOB,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )
        """)

        # Create accountant table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS admin (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                faculty_id INT NOT NULL,
                faculty_name VARCHAR(255) NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )
        """)
        # Create accountant table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS principa (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                faculty_id INT NOT NULL,
                faculty_name VARCHAR(255) NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )
        """)
        # Create chat_messages table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chat_messages (
                id INT AUTO_INCREMENT PRIMARY KEY,
                sender_user_id INT NOT NULL,
                receiver_user_id INT NOT NULL,
                department VARCHAR(100),
                message TEXT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                is_read BOOLEAN DEFAULT FALSE,
                FOREIGN KEY (sender_user_id) REFERENCES users(id) ON DELETE CASCADE,
                FOREIGN KEY (receiver_user_id) REFERENCES users(id) ON DELETE CASCADE
            )
        """)
        # Create chat_messages table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS groupp_chat_messages (
                id INT AUTO_INCREMENT PRIMARY KEY,
                sender_user_id INT NOT NULL,
                receiver_user_id INT NULL,
                department VARCHAR(100),
                message TEXT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                is_read BOOLEAN DEFAULT FALSE,
                FOREIGN KEY (sender_user_id) REFERENCES users(id) ON DELETE CASCADE,
                FOREIGN KEY (receiver_user_id) REFERENCES users(id) ON DELETE CASCADE
            )
        """)
        # Ensure the table is created correctly
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS adminda_notifications (
                id INT AUTO_INCREMENT PRIMARY KEY,
                message TEXT NOT NULL,
                sender VARCHAR(255) NOT NULL,
                recipient VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                is_read BOOLEAN DEFAULT FALSE
            );

        """)
        # Ensure the table is created correctly
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS principal_notifications (
                id INT AUTO_INCREMENT PRIMARY KEY,
                message TEXT NOT NULL,
                sender VARCHAR(255) NOT NULL,
                recipient VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                is_read BOOLEAN DEFAULT FALSE
            );

        """)
        # Ensure the table is created correctly
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS accountant_notifications (
                id INT AUTO_INCREMENT PRIMARY KEY,
                message TEXT NOT NULL,
                sender VARCHAR(255) NOT NULL,
                recipient VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                is_read BOOLEAN DEFAULT FALSE
            );

        """)
        # Ensure the table is created correctly
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS hod_notifications (
                id INT AUTO_INCREMENT PRIMARY KEY,
                message TEXT NOT NULL,
                sender VARCHAR(255) NOT NULL,
                recipient VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                is_read BOOLEAN DEFAULT FALSE
            );

        """)
        # Ensure the table is created correctly
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS faculty_notifications (
                id INT AUTO_INCREMENT PRIMARY KEY,
                message TEXT NOT NULL,
                sender VARCHAR(255) NOT NULL,
                recipient VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                is_read BOOLEAN DEFAULT FALSE
            );

        """)

                # Create indexes for chat_messages table
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_sender_user_id ON chat_messages(sender_user_id);")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_receiver_user_id ON chat_messages(receiver_user_id);")
        
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_sender_user_id ON staff_chat_messages(sender_user_id);")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_receiver_user_id ON staff_chat_messages(receiver_user_id);")  
        
        db.commit()
    except Error as e:
        print(f"Error creating tables: {e}")

create_tables()

current_user = None

class PlaceholderEntry(ttk.Frame):
    def __init__(self, master=None, placeholder="PLACEHOLDER", show='', *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.entry = ttk.Entry(self, font=("Helvetica", 11), show=show)
        self.entry.pack(fill="x", padx=5, pady=5)
        self.entry.bind("<FocusIn>", self._clear_placeholder)
        self.entry.bind("<FocusOut>", self._add_placeholder)
        self.entry.bind("<KeyRelease>", self._check_placeholder)

        self.label = tk.Label(self.entry, text=self.placeholder, font=("Helvetica", 11), foreground="grey", background="white")
        self.label.place(x=5, y=1)
        self._add_placeholder()

    def _clear_placeholder(self, e=None):
        if not self.entry.get():
            self.label.place_forget()

    def _add_placeholder(self, e=None):
        if not self.entry.get():
            self.label.place(x=5, y=1)

    def _check_placeholder(self, e=None):
        if self.entry.get():
            self.label.place_forget()
        else:
            self.label.place(x=5, y=1)

    def get(self):
        return self.entry.get()

    def set(self, value):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)

    def destroy(self):
        # Avoid printing or additional logic here if not needed
        if self.entry.winfo_exists():
            self.entry.destroy()
        if self.label.winfo_exists():
            self.label.destroy()
        super().destroy()

def switch_window(current_window, new_window_func):
    if current_window and current_window.winfo_exists():
        current_window.destroy()
    new_window_func()

# Login Window
def login_window():
    def attempt_login():
        global current_user
        username = username_entry.get()
        password = password_entry.get()

        # Check for principal hardcoded credentials first
        if username == "pri" and password == "123":
            messagebox.showinfo("Login Successful", "Welcome, Principal!")
            login_login_window.destroy()
            principal_dashboard_window()  # Open the principal's dashboard
            return

        # Check for principal hardcoded credentials first
        if username == "ad" and password == "123":
            messagebox.showinfo("Login Successful", "Welcome, admin!")
            login_login_window.destroy()
            admin_dashboard_window(username)  # Open the principal's dashboard
            return

        cursor.execute("SELECT id, role FROM users WHERE username=%s AND password=%s", (username, password))
        result = cursor.fetchone()

        if result:
            user_id, role = result

            # Check for None or empty role
            if role is None:
                messagebox.showerror("Error", "Role is not assigned. Please contact support.")
                return

            # Remove any leading or trailing spaces from the role
            role = role.strip()

            # Debugging: print the cleaned role
            print(f"Cleaned role: '{role}'")

            if not role:
                messagebox.showerror("Error", "Role not found. Please contact support.")
                return

            # Define the table_name based on the role
            if role == "faculty":
                table_name = "faculty"
            elif role == "hod":
                table_name = "hod"
            elif role == "accountant":
                table_name = "accountant"
            elif role == "student":
                table_name = "students"
            elif role == "admin":
                table_name = "admin"
            elif role == "principal":
                table_name = "principal"
            else:
                # If an unexpected role is found, raise an error
                raise ValueError(f"Unexpected role: '{role}'")
            
            if role == "principal":
                principal_dashboard_window(username,"principal")
            elif role == "admin":
                admin_dashboard_window(username)

            cursor.execute(f"SELECT department FROM {table_name} WHERE user_id=%s", (user_id,))
            department = cursor.fetchone()[0]
            login_login_window.destroy()  


            if role == "student":
                student_dashboard_window(username,department,role)
            elif role == "faculty":
                faculty_dashboard_window(username,department,role)
            elif role == "accountant":
                accountant_dashboard_window(username,department)
            elif role == "hod":
                hod_dashboard_window(username,department,role)
        else:
            messagebox.showerror("Error", "Invalid username or password")

    window.withdraw()  # Hide the main window
    login_login_window = tk.Toplevel(background="#ccccb3")
    login_login_window.title("Login")
    login_login_window.geometry("350x600")

    # Add content to the new window
    login_label = ttk.Label(login_login_window, text="Student Login Page",background="#ccccb3")
    login_label.pack(pady=10)
    
    username_label = ttk.Label(login_login_window, text="User_Name",background="#ccccb3")
    username_label.place(x=18, y=65)
    
    username_entry = PlaceholderEntry(login_login_window, placeholder="Enter user name")
    username_entry.place(x=16, y=85, width=320)
  
    password_label = ttk.Label(login_login_window, text="Password",background="#ccccb3")
    password_label.place(x=18, y=130)
    
    password_entry = PlaceholderEntry(login_login_window, placeholder="Enter Password", show="*")
    password_entry.place(x=16, y=150, width=320)

    def open_register_window():
        switch_window(login_login_window, role_selection_window)
    # Function to change the button color when hovered over
    def on_enter_submit(e):
        submit_button['bg'] = '#add8e6'  # Light blue on hover

    # Function to change the button color back when not hovered
    def on_leave_submit(e):
        submit_button['bg'] = '#4d4d33'  # Dark blue

    # Function to change the button color when hovered over for New User
    def on_enter_new_user(e):
        new_user_button['bg'] = '#add8e6'  # Light blue on hover

    # Function to change the button color back when not hovered for New User
    def on_leave_new_user(e):
        new_user_button['bg'] = '#4d4d33'  # Dark blue

    # Create a standard button with specific styles for Submit button
    button_width = 15  # Set a fixed width for both buttons
    button_height = 2  # Set a fixed height for both buttons

    submit_button = tk.Button(
        login_login_window,
        text="Submit",
        command=attempt_login,
        bg="#4d4d33",  # Dark blue background
        fg="white",    # White font color
        font=("Arial", 12),  # Font size
        relief="raised",
        width=button_width,   # Set fixed width
        height=button_height, # Set fixed height
    )

    # Bind hover events for the Submit button
    submit_button.bind("<Enter>", on_enter_submit)
    submit_button.bind("<Leave>", on_leave_submit)

    # Place the Submit button
    submit_button.place(x=20, y=220)

    # Create a standard button with specific styles for New User button
    new_user_button = tk.Button(
        login_login_window,
        text="New User?",
        command=open_register_window,
        bg="#4d4d33",  # Dark blue background
        fg="white",    # White font color
        font=("Arial", 12),  # Font size
        relief="raised",
        width=button_width,   # Set fixed width
        height=button_height, # Set fixed height
    )

    # Bind hover events for the New User button
    new_user_button.bind("<Enter>", on_enter_new_user)
    new_user_button.bind("<Leave>", on_leave_new_user)

    # Place the New User button
    new_user_button.place(x=185, y=220)

    login_login_window.mainloop()

# Role Selection Window
def role_selection_window():     

    selection_window = tk.Toplevel(background="#ffb3ff")
    selection_window.title("New Account")
    selection_window.geometry("350x500")

    # Function to change button color on hover
    def on_enter(e):
        e.widget['bg'] = '#DA70D6'  # Light violet on hover

    # Function to change button color back
    def on_leave(e):
        e.widget['bg'] = '#9400D3'  # Dark violet back

    # Button configuration
    button_config = {
        'bg': "#9400D3",  # Dark violet color
        'fg': "white",    # White font color
        'font': ("Arial", 12),  # Font size
        'padx': 20,       # Horizontal padding
        'pady': 10,       # Vertical padding
        'width': 15       # Fixed width for buttons
    }

    # Create buttons with the specified colors and configuration
    admin_button = tk.Button(selection_window, text="Admin", command=lambda: switch_window(selection_window, register_window(selection_window, "admin")), **button_config)
    admin_button.place(x=100, y=50)
    admin_button.bind("<Enter>", on_enter)
    admin_button.bind("<Leave>", on_leave)

    # Increased the Y coordinate for spacing
    principal_button = tk.Button(selection_window, text="Principal", command=lambda: switch_window(selection_window, register_window(selection_window, 'principal')), **button_config)
    principal_button.place(x=100, y=110)  # Increased y to 110 for spacing
    principal_button.bind("<Enter>", on_enter)
    principal_button.bind("<Leave>", on_leave)

    hod_button = tk.Button(selection_window, text="HOD", command=lambda: switch_window(selection_window, register_window(selection_window, 'hod')), **button_config)
    hod_button.place(x=100, y=170)  # Increased y to 170 for spacing
    hod_button.bind("<Enter>", on_enter)
    hod_button.bind("<Leave>", on_leave)

    faculty_button = tk.Button(selection_window, text="Faculty", command=lambda: switch_window(selection_window, register_window(selection_window, 'faculty')), **button_config)
    faculty_button.place(x=100, y=230)  # Increased y to 230 for spacing
    faculty_button.bind("<Enter>", on_enter)
    faculty_button.bind("<Leave>", on_leave)

    accountant_button = tk.Button(selection_window, text="Accountant", command=lambda: switch_window(selection_window, register_window(selection_window, 'accountant')), **button_config)
    accountant_button.place(x=100, y=290)  # Increased y to 290 for spacing
    accountant_button.bind("<Enter>", on_enter)
    accountant_button.bind("<Leave>", on_leave)

    student_button = tk.Button(selection_window, text="Student", command=lambda: switch_window(selection_window, register_window(selection_window, 'student')), **button_config)
    student_button.place(x=100, y=350)  # Increased y to 350 for spacing
    student_button.bind("<Enter>", on_enter)
    student_button.bind("<Leave>", on_leave)

    back_button = tk.Button(selection_window, text="Go Back", command=lambda: switch_window(selection_window, login_window), **button_config)
    back_button.place(x=100, y=410)  # Increased y to 410 for spacing
    back_button.bind("<Enter>", on_enter)
    back_button.bind("<Leave>", on_leave)

    selection_window.mainloop()

# Registration Window
def register_window(parent, role):
    parent.destroy()

    def select_photo():
        global photo_path
        filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if filepath:
            img = Image.open(filepath)
            img.thumbnail((100, 100))
            photo_img = ImageTk.PhotoImage(img)
            photo_label.config(image=photo_img)
            photo_label.image = photo_img
            select_photo.photo_path = filepath

    def clear_photo():
        # Clear the photo from the label and reset the photo path
        photo_label.config(image="")
        photo_label.image = None
        select_photo.photo_path = None

    def complete_registration():
        if role == "student":
            student_id = student_id_entry.get()
            student_name = student_name_entry.get()
            admission_date = admission_date_entry.get()
            department = department_var.get()  if role in ["student", "faculty","hod","accountant"] else None
            semester = semester_var.get()
            admission_number = admission_number_entry.get()
            roll_no = roll_no_entry.get()
            gender = gender_var.get()
            dob = dob_var.get()
            blood_group = blood_var.get()
            father_name = father_name_entry.get()
            father_occupation = father_occupation_entry.get()
            mother_name = mother_name_entry.get()
            mother_occupation = mother_occupation_entry.get()
            address = address_entry.get("1.0", tk.END).strip()  # for multiline text
            city = city_entry.get()
            country = country_var.get()
            religion = religion_entry.get()
            caste = caste_entry.get()
            pin_code = pin_code_entry.get()
            state = state_var.get()
            email = email_entry.get()
            phone = phone_entry.get()
            parent_phone = parent_phone_entry.get()
            guardian_name = guardian_entry.get()
            guardian_relationship = relationship_entry.get()
            guardian_phone = guardian_phone_entry.get()
            guardian_address = guardian_address_entry.get("1.0", "end-1c") 
            photo_path = None if not hasattr(select_photo, 'photo_path') else select_photo.photo_path
    
            cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", ("temp_user", "temp_pass", role))
            db.commit()
            user_id = cursor.lastrowid
            
            if (not student_id or not student_name or not admission_date or not department or not semester or not admission_number or not roll_no or not 
                    gender or not dob or not blood_group or not father_name or not father_occupation or not mother_name or not mother_occupation or not 
                    address or not city or not country or not religion or not caste or not pin_code or not state or not email or not phone or not parent_phone 
                    or not guardian_name or not guardian_relationship or not guardian_phone or not guardian_address or not photo_path):
                messagebox.showerror("Error", "Please fill all fields")
                return
            
            # Corrected SQL query and passing of values
            cursor.execute("""
                    INSERT INTO students (
                    user_id,student_id, student_name, admission_date, department, semester, admission_number, roll_no, 
                    gender, dob, blood_group, father_name, father_occupation, mother_name, mother_occupation, 
                    address, city, country, religion, caste, pin_code, state, email, phone, parent_phone, 
                    guardian_name, guardian_relationship, guardian_phone, guardian_address, photo_path
                ) 
                VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (user_id,student_id, student_name, admission_date, department, semester, admission_number, roll_no, 
                gender, dob, blood_group, father_name, father_occupation, mother_name, mother_occupation, 
                address, city, country, religion, caste, pin_code, state, email, phone, parent_phone, 
                guardian_name, guardian_relationship, guardian_phone, guardian_address, photo_path)
        )
        elif role == "admin":
            faculty_id = faculty_id_entry.get()
            faculty_name =faculty_name_entry.get()
            cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", ("temp_user", "temp_pass", role))
            db.commit()
            user_id = cursor.lastrowid

            if (not faculty_id or not faculty_name ):
                # Insert details into MySQL
                messagebox.showerror("Error", "Please fill all fields")
                return
            cursor.execute( """INSERT INTO admin (
                    user_id,faculty_id, faculty_name
                ) 
                VALUES (%s, %s, %s)
                """, 
                (user_id,faculty_id, faculty_name)
            )
        elif role == "principal":
            faculty_id = faculty_id_entry.get()
            faculty_name =faculty_name_entry.get()
            cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", ("temp_user", "temp_pass", role))
            db.commit()
            user_id = cursor.lastrowid

            if (not faculty_id or not faculty_name ):
                # Insert details into MySQL
                messagebox.showerror("Error", "Please fill all fields")
                return
            cursor.execute( """INSERT INTO principa (
                    user_id,faculty_id, faculty_name
                ) 
                VALUES (%s, %s, %s)
                """, 
                (user_id,faculty_id, faculty_name)
            )
        elif role == "faculty":
            faculty_id = faculty_id_entry.get()
            faculty_name =faculty_name_entry.get()
            faculty_gender =faculty_gender_var.get()
            department = department_var.get()  if role in ["student", "faculty","hod","accountant"] else None
            faculty_dob =faculty_dob_var.get()
            faculty_blood_group =faculty_blood_var.get()
            faculty_marital_status =faculty_marital_var.get()
            faculty_job_position =faculty_job_position_entry.get()
            faculty_address =faculty_address_entry.get("1.0", tk.END).strip()  # for multiline text
            faculty_city =faculty_city_entry.get()
            faculty_country =faculty_country_var.get()
            faculty_pin_code =faculty_pin_code_entry.get()
            faculty_state =faculty_state_var.get()
            faculty_email =faculty_email_entry.get()
            faculty_phone =faculty_phone_entry.get()
            faculty_guardian_name =faculty_guardian_entry.get()
            faculty_guardian_relationship =faculty_guardian_relationship_entry.get()
            faculty_guardian_phone =faculty_guardian_phone_entry.get()
            faculty_guardian_address =faculty_guardian_address_entry.get("1.0", "end-1c")
            photo_path = None if not hasattr(select_photo, 'photo_path') else select_photo.photo_path
 
            cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", ("temp_user", "temp_pass", role))
            db.commit()
            user_id = cursor.lastrowid

            if (not faculty_id or not faculty_name or not  department or not  faculty_gender or not  faculty_dob or not faculty_blood_group or not faculty_marital_status or not 
                faculty_job_position or not  faculty_address or not  faculty_city or not faculty_country or not  faculty_pin_code or not faculty_state or not faculty_email or not faculty_phone or not 
                faculty_guardian_name or not faculty_guardian_relationship or not faculty_guardian_phone or not faculty_guardian_address or not  photo_path):
                # Insert details into MySQL
                messagebox.showerror("Error", "Please fill all fields")
                return
            cursor.execute( """INSERT INTO faculty (
                    user_id,faculty_id, faculty_name, department, faculty_gender, faculty_dob, faculty_blood_group,
                    faculty_marital_status, faculty_job_position, faculty_address, faculty_city, faculty_country, faculty_pin_code,
                    faculty_state, faculty_email, faculty_phone, faculty_guardian_name, faculty_guardian_relationship,
                    faculty_guardian_phone, faculty_guardian_address, photo_path
                ) 
                VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, 
                (user_id,faculty_id, faculty_name, department, faculty_gender, faculty_dob, faculty_blood_group,
                faculty_marital_status, faculty_job_position, faculty_address, faculty_city, faculty_country, faculty_pin_code,
                faculty_state, faculty_email, faculty_phone, faculty_guardian_name, faculty_guardian_relationship,
                faculty_guardian_phone, faculty_guardian_address, photo_path)
            )
        elif role == "accountant":
            faculty_id = faculty_id_entry.get()
            faculty_name =faculty_name_entry.get()
            faculty_gender =faculty_gender_var.get()
            department = department_var.get()  if role in ["student", "faculty","hod","accountant"] else None
            faculty_dob =faculty_dob_var.get()
            faculty_blood_group =faculty_blood_var.get()
            faculty_marital_status =faculty_marital_var.get()
            faculty_job_position =faculty_job_position_entry.get()
            faculty_address =faculty_address_entry.get("1.0", tk.END).strip()  # for multiline text
            faculty_city =faculty_city_entry.get()
            faculty_country =faculty_country_var.get()
            faculty_pin_code =faculty_pin_code_entry.get()
            faculty_state =faculty_state_var.get()
            faculty_email =faculty_email_entry.get()
            faculty_phone =faculty_phone_entry.get()
            faculty_guardian_name =faculty_guardian_entry.get()
            faculty_guardian_relationship =faculty_guardian_relationship_entry.get()
            faculty_guardian_phone =faculty_guardian_phone_entry.get()
            faculty_guardian_address =faculty_guardian_address_entry.get("1.0", "end-1c")
            photo_path = None if not hasattr(select_photo, 'photo_path') else select_photo.photo_path

            cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", ("temp_user", "temp_pass", role))
            db.commit()
            user_id = cursor.lastrowid

            if (not faculty_id or not faculty_name or not  department or not  faculty_gender or not  faculty_dob or not faculty_blood_group or not faculty_marital_status or not 
                faculty_job_position or not  faculty_address or not  faculty_city or not faculty_country or not  faculty_pin_code or not faculty_state or not faculty_email or not faculty_phone or not 
                faculty_guardian_name or not faculty_guardian_relationship or not faculty_guardian_phone or not faculty_guardian_address or not  photo_path):
                # Insert details into MySQL
                messagebox.showerror("Error", "Please fill all fields")
                return
                # SQL query for inserting accountant data
            
            cursor.execute( """INSERT INTO accountant (
                                user_id,faculty_id, faculty_name, department, faculty_gender, faculty_dob, faculty_blood_group,
                faculty_marital_status, faculty_job_position, faculty_address, faculty_city, faculty_country, faculty_pin_code,
                faculty_state, faculty_email, faculty_phone, faculty_guardian_name, faculty_guardian_relationship,
                faculty_guardian_phone, faculty_guardian_address, photo_path
            ) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s)
            """, 
            (user_id,faculty_id, faculty_name, department, faculty_gender, faculty_dob, faculty_blood_group,
            faculty_marital_status, faculty_job_position, faculty_address, faculty_city, faculty_country, faculty_pin_code,
            faculty_state, faculty_email, faculty_phone, faculty_guardian_name, faculty_guardian_relationship,
            faculty_guardian_phone, faculty_guardian_address, photo_path)
            )
        elif role == "hod":
            faculty_id = faculty_id_entry.get()
            faculty_name =faculty_name_entry.get()
            faculty_gender =faculty_gender_var.get()
            department = department_var.get()  if role in ["student", "faculty","hod","accountant"] else None
            faculty_dob =faculty_dob_var.get()
            faculty_blood_group =faculty_blood_var.get()
            faculty_marital_status =faculty_marital_var.get()
            faculty_job_position =faculty_job_position_entry.get()
            faculty_address =faculty_address_entry.get("1.0", tk.END).strip()  # for multiline text
            faculty_city =faculty_city_entry.get()
            faculty_country =faculty_country_var.get()
            faculty_pin_code =faculty_pin_code_entry.get()
            faculty_state =faculty_state_var.get()
            faculty_email =faculty_email_entry.get()
            faculty_phone =faculty_phone_entry.get()
            faculty_guardian_name =faculty_guardian_entry.get()
            faculty_guardian_relationship =faculty_guardian_relationship_entry.get()
            faculty_guardian_phone =faculty_guardian_phone_entry.get()
            faculty_guardian_address =faculty_guardian_address_entry.get("1.0", "end-1c")
            photo_path = None if not hasattr(select_photo, 'photo_path') else select_photo.photo_path

            cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", ("temp_user", "temp_pass", role))
            db.commit()
            user_id = cursor.lastrowid

            if (not faculty_id or not faculty_name or not  department or not  faculty_gender or not  faculty_dob or not faculty_blood_group or not faculty_marital_status or not 
                faculty_job_position or not  faculty_address or not  faculty_city or not faculty_country or not  faculty_pin_code or not faculty_state or not faculty_email or not faculty_phone or not 
                faculty_guardian_name or not faculty_guardian_relationship or not faculty_guardian_phone or not faculty_guardian_address or not  photo_path):
                # Insert details into MySQL
                messagebox.showerror("Error", "Please fill all fields")
                return
            cursor.execute( """INSERT INTO hod (
                            user_id,faculty_id, faculty_name, department, faculty_gender, faculty_dob, faculty_blood_group,
            faculty_marital_status, faculty_job_position, faculty_address, faculty_city, faculty_country, faculty_pin_code,
            faculty_state, faculty_email, faculty_phone, faculty_guardian_name, faculty_guardian_relationship,
            faculty_guardian_phone, faculty_guardian_address, photo_path
            ) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s ,%s, %s, %s, %s, %s, %s, %s,%s, %s, %s)
            """, 
            (user_id,faculty_id, faculty_name, department, faculty_gender, faculty_dob, faculty_blood_group,
            faculty_marital_status, faculty_job_position, faculty_address, faculty_city, faculty_country, faculty_pin_code,
            faculty_state, faculty_email, faculty_phone, faculty_guardian_name, faculty_guardian_relationship,
            faculty_guardian_phone, faculty_guardian_address, photo_path)
)

        db.commit()
        messagebox.showinfo("Success", "Registration successful")
        set_username_password(user_id)

    def set_username_password(user_id):
        def update_user_credentials():
            username = username_entry.get()
            password = password_entry.get()
            confirm_password = confirm_password_entry.get()

            if password != confirm_password:
                messagebox.showerror("Error", "Passwords do not match")
                return
            # Check if username already exists
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            if cursor.fetchone() is not None:
                messagebox.showerror("Error", "Username already exists")
                return
            cursor.execute("UPDATE users SET username=%s, password=%s WHERE id=%s", (username, password, user_id))
            db.commit()
            messagebox.showinfo("Success", f"Registration completed for {role.capitalize()}!")
            login_button_window.destroy()
            login_window()

        # Create a new top-level window
        login_button_window = tk.Toplevel()
        login_button_window.title("New Account")
        login_button_window.geometry("320x400")

        login_label = ttk.Label(login_button_window, text="Enter your login details")
        login_label.pack(pady=10)
        
        username_label = ttk.Label(login_button_window, text="User Name")
        username_label.place(x=18, y=65)
        
        username_entry = PlaceholderEntry(login_button_window, placeholder="User Name")
        username_entry.place(x=16, y=85, width=280)
    
        password_label = ttk.Label(login_button_window, text="Password")
        password_label.place(x=18, y=130)
        
        password_entry = PlaceholderEntry(login_button_window, placeholder="Password", show="*")
        password_entry.place(x=16, y=150, width=280)

        confirm_password_label = ttk.Label(login_button_window, text="confirm_password")
        confirm_password_label.place(x=18, y=195)
        
        confirm_password_entry = PlaceholderEntry(login_button_window, placeholder="confirm_password", show="*")
        confirm_password_entry.place(x=16, y=215, width=280)

        login_button = ttk.Button(login_button_window, text="Login", command=update_user_credentials)
        login_button.place(x=80, y=270)

        window.mainloop()

    if role == "student":

        student_window = tk.Toplevel(background="#008000")
        student_window.title("Student Registration")
        student_window.geometry("1380x768")

        # Canvas for drawing
        canvas = tk.Canvas(student_window, bg="#008000")
        canvas.place(relwidth=1, relheight=1)

        # Draw square lines for visual separation
        canvas.create_rectangle(1200, 325, 25, 600, width=2, outline="#FFD700")  # Square 1
        canvas.create_rectangle(1200, 300, 25, 30, width=2, outline="#FFD700")   # Square 2
        canvas.create_rectangle(1200, 625, 25, 685, width=2, outline="#FFD700")  # Square 3
        canvas.create_rectangle(1225, 360, 1350, 30, width=2, outline="#FFD700")  # Square 4
        

        # Add content to the new window
        login_label = ttk.Label(student_window, text="Students New Registration",background="#008000",foreground="white", font=("Helvetica", 16))
        login_label.place(x=55, y=15)

            # Student ID Number
        student_id_label = ttk.Label(student_window, text="Student Id No",background="#008000",foreground="white", font=("arial", 14))
        student_id_label.place(x=30, y=55)    

        student_id_entry = PlaceholderEntry(student_window, placeholder="Student Id Number")
        student_id_entry.place(x=210, y=50, width=210)

        student_name_label = ttk.Label(student_window, text="Name",background="#008000",foreground="white", font=("arial", 14))
        student_name_label.place(x=30, y=105)

        student_name_entry = PlaceholderEntry(student_window, placeholder="Enter Your Name")
        student_name_entry.place(x=210, y=100, width=210)

        admission_date_label = ttk.Label(student_window, text="Date Of Admission",background="#008000",foreground="white", font=("arial", 14))
        admission_date_label.place(x=30, y=155)

        admission_date_entry = PlaceholderEntry(student_window, placeholder="Enter Your Admission date")
        admission_date_entry.place(x=210, y=150, width=210)
       
        department_label = ttk.Label(student_window, text="Department",background="#008000",foreground="white", font=("arial", 14))
        department_label.place(x=30, y=205) 

        department_var = tk.StringVar()
        department_combobox = ttk.Combobox(student_window, textvariable=department_var, font=("Helvetica", 12), state='readonly')
        department_combobox['values'] = ["B.E Civil Engineering","B.E Computer Science Engineering","B.E Electrical and Electronics Engineering","B.E Electronics and Communication Engineering","B.Tech Information Technology","B.E Mechanical Engineering",
    "B.Tech Artificial Intelligence and Data Science","B.Tech Computer Science and Business Systems","Marine Engineering","Aerospace Engineering","Master of Business Administration (MBA)","Master of Computer Application (MCA)",
    "M.E Power Electronics and Drives","M.E Communication systems","M.E Computer Science Engineering","M.E Engineering Design"]
        department_combobox.place(x=210, y=205, width=210 ,height=30)   

        #year
        semester_label = ttk.Label(student_window, text="Semester",background="#008000",foreground="white", font=("arial", 16))
        semester_label.place(x=30, y=250) 

        semester_var = tk.StringVar()
        semester_combobox = ttk.Combobox(student_window, textvariable=semester_var, font=("Helvetica", 12), state='readonly')
        semester_combobox['values'] = ["1st Semester","2nd Semester","3ed Semester","4th Semester","5th Semester","6th Semester","7th Semester","8th Semester"]
        semester_combobox.place(x=210, y=250, width=210 ,height=30) 

        admission_number_label = ttk.Label(student_window, text="Admission No",background="#008000",foreground="white", font=("arial", 14))
        admission_number_label.place(x=450, y=55)

        admission_number_entry = PlaceholderEntry(student_window, placeholder="Enter Your Admission No")
        admission_number_entry.place(x=650, y=50, width=210)

        roll_no_label = ttk.Label(student_window, text="Roll No",background="#008000",foreground="white", font=("arial", 14))
        roll_no_label.place(x=450, y=105)

        roll_no_entry = PlaceholderEntry(student_window, placeholder="Enter Your Roll No")
        roll_no_entry.place(x=650, y=100, width=210)

        #GENDER ENTRY
        gender_label = ttk.Label(student_window, text="Gender ",background="#008000",foreground="white", font=("arial", 14))
        gender_label.place(x=450, y=155) 

        gender_var = tk.StringVar()
        gender_combobox = ttk.Combobox(student_window, textvariable=gender_var, font=("Helvetica", 12), state='readonly')
        gender_combobox['values'] = ["Male","Female","Transgender"]
        gender_combobox.place(x=650, y=155, width=210 ,height=30)  

            #GENDER ENTRY
        dob_label = ttk.Label(student_window, text="DOB ",background="#008000",foreground="white", font=("arial", 14))
        dob_label.place(x=450, y=205)  

        # Combobox for day, month, and year - Replaced with DateEntry
        dob_var = tk.StringVar()
        dob_entry = DateEntry(student_window, textvariable=dob_var, font=("Helvetica", 11), date_pattern='dd/MM/yyyy')
        dob_entry.place(x=650, y=205, width=210 ,height=30)

            #BLOOD GROUP
        blood_label = ttk.Label(student_window, text="Blood Group ",background="#008000",foreground="white", font=("arial", 14))
        blood_label.place(x=450, y=250) 

        blood_var = tk.StringVar()
        blood_combobox = ttk.Combobox(student_window, textvariable=blood_var, font=("Helvetica", 12), state='readonly')
        blood_combobox['values'] = ["A RhD positive (A+)","A RhD negative (A-)","B RhD positive (B+)","B RhD negative (B-)","O RhD positive (O+)","O RhD negative (O-)","AB RhD positive (AB+)","AB RhD negative (AB-)"]
        blood_combobox.place(x=650, y=250, width=210 ,height=30)

            #family information
            
        family_label = ttk.Label(student_window, text="Family Information",background="#008000",foreground="white", font=("arial", 14))
        family_label.place(x=55, y=308) 

        father_label = ttk.Label(student_window, text="Father's Name ",background="#008000",foreground="white", font=("arial", 14))
        father_label.place(x=30, y=355)  

        father_name_entry = PlaceholderEntry(student_window, placeholder="Enter Father's Name")
        father_name_entry.place(x=210, y=355, width=210) 

        father_occupation_label = ttk.Label(student_window, text="Fatther's occupation",background="#008000",foreground="white", font=("arial", 14))
        father_occupation_label.place(x=30, y=410) 

        father_occupation_entry = PlaceholderEntry(student_window, placeholder="Father Occupation")
        father_occupation_entry.place(x=210, y=405, width=210)  

        mother_name_label = ttk.Label(student_window, text="Mother's Name",background="#008000",foreground="white", font=("arial", 14))
        mother_name_label.place(x=450, y=355) 

        mother_name_entry = PlaceholderEntry(student_window, placeholder="Enter Mother's Name")
        mother_name_entry.place(x=650, y=355, width=210)

        mother_occupation_label = ttk.Label(student_window, text="Mother Occupation",background="#008000",foreground="white", font=("arial", 14))
        mother_occupation_label.place(x=450, y=410)  

        mother_occupation_entry = PlaceholderEntry(student_window, placeholder="Mother Occupation")
        mother_occupation_entry.place(x=650, y=405, width=210) 

        #     #ADDRESS
        address_label = ttk.Label(student_window, text="Address ",background="#008000",foreground="white", font=("arial", 14))
        address_label.place(x=30, y=455)
        
        address_entry = tk.Text(student_window, width=39, height=3, font=("Helvetica", 14))
        address_entry.place(x=210, y=455)     

        city_label = ttk.Label(student_window, text="City ",background="#008000",foreground="white", font=("arial", 14))
        city_label.place(x=660, y=458)    
        
        city_entry = PlaceholderEntry(student_window, placeholder="Enter Your City")
        city_entry.place(x=740, y=455, width=215)

        country_label = ttk.Label(student_window, text="Country ",background="#008000",foreground="white", font=("arial", 14))
        country_label.place(x=660, y=505)    
        
        #country 
        country_var = tk.StringVar()
        country_combobox = ttk.Combobox(student_window, textvariable=country_var, font=("Helvetica", 12), state='readonly')
        country_combobox['values'] = ["USA", "Canada", "Mexico", "Germany", "France", "Italy", "Spain", "UK", "India", "China", "Japan"]
        country_combobox.place(x=740, y=505,width=210 ,height=30)
    
        religion_label = ttk.Label(student_window, text="Religion",background="#008000",foreground="white", font=("arial", 14))  
        religion_label.place(x=960, y=458)    
        
        religion_entry = PlaceholderEntry(student_window, placeholder="Enter Your Religion")
        religion_entry.place(x=1040, y=455, width=150)

        caste_label = ttk.Label(student_window, text="Caste",background="#008000",foreground="white", font=("arial", 14))  
        caste_label.place(x=960, y=505)    
        
        caste_entry = PlaceholderEntry(student_window, placeholder="Enter Your Caste")
        caste_entry.place(x=1040, y=505, width=150)

        #pin code
        pin_label = ttk.Label(student_window, text="Pin Code",background="#008000",foreground="white", font=("arial", 14))
        pin_label.place(x=30, y=555) 

        pin_code_entry = PlaceholderEntry(student_window, placeholder="Postal/Zip Code")
        pin_code_entry.place(x=210, y=545, width=210)

        state_label = ttk.Label(student_window, text="State ",background="#008000",foreground="white", font=("arial", 14))
        state_label.place(x=450, y=550)  

            #state
        state_var = tk.StringVar()
        state_combobox = ttk.Combobox(student_window, textvariable=state_var, font=("Helvetica", 12), state='readonly')
        state_combobox['values'] = ["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Maharashtra",
    "Madhya Pradesh","Manipur","Meghalaya", "Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Tripura","Telangana","Uttar Pradesh",
    "Uttarakhand","West Bengal","Andaman & Nicobar (UT)","Chandigarh (UT)","Dadra & Nagar Haveli (UT)","Daman & Diu (UT)","Jammu & Kashmir(UT)","Lakshadweep (UT)","Ladakh (UT)","Puducherry (UT)"]
        state_combobox.place(x=545, y=550, width=210 ,height=30)

        # # EMAIL
        email_label = ttk.Label(student_window, text="Email ",background="#008000",foreground="white", font=("arial", 14))
        email_label.place(x=890, y=360)  

        email_entry = PlaceholderEntry(student_window, placeholder="Enter Your Email")
        email_entry.place(x=975, y=355, width=210)  

        #     #PHONE NUMBER
        phone_label = ttk.Label(student_window, text="Phone No ",background="#008000",foreground="white", font=("arial", 14))
        phone_label.place(x=890, y=405)  

        phone_entry = PlaceholderEntry(student_window, placeholder="Enter Your Phone Number")
        phone_entry.place(x=975, y=405, width=210)    

        parent_phone_label = ttk.Label(student_window, text="Phone No ",background="#008000",foreground="white", font=("arial", 14))
        parent_phone_label.place(x=790, y=555)  

        parent_phone_entry = PlaceholderEntry(student_window, placeholder="Enter Phone Number")
        parent_phone_entry.place(x=900, y=550, width=250)

        infgardian_label = ttk.Label(student_window, text="Guardian Information ",background="#008000",foreground="white", font=("arial", 14))
        infgardian_label.place(x=55, y=610)      
        
        guardian_label = ttk.Label(student_window, text="Name ",background="#008000",foreground="white", font=("arial", 14))
        guardian_label.place(x=30, y=640) 

        guardian_entry = PlaceholderEntry(student_window, placeholder="Guardian Name")
        guardian_entry.place(x=85, y=635, width=150)

        relationship_label = ttk.Label(student_window, text="Relationship",background="#008000",foreground="white", font=("arial", 14))
        relationship_label.place(x=240, y=640)  

        relationship_entry = PlaceholderEntry(student_window, placeholder="Relationship")
        relationship_entry.place(x=360, y=635, width=150)    

        #     #PHONE NUMBER
        guardian_phone_label = ttk.Label(student_window, text="Emergency contact No ",background="#008000",foreground="white", font=("arial", 14))
        guardian_phone_label.place(x=520, y=640)  

        guardian_phone_entry = PlaceholderEntry(student_window, placeholder="Enter Your Phone Number")
        guardian_phone_entry.place(x=680, y=635, width=170)  

        #     #ADDRESS
        guardian_address_label = ttk.Label(student_window, text=" Address ",background="#008000",foreground="white", font=("arial", 14))
        guardian_address_label.place(x=850, y=640)
        
        guardian_address_entry = tk.Text(student_window, width=25, height=2, font=("Helvetica", 12))
        guardian_address_entry.place(x=950, y=635) 

        def clear_all():
            student_id_entry.delete(0, tk.END)
            student_name_entry.delete(0, tk.END)
            admission_date_entry.delete(0, tk.END)
            department_var.set('')
            semester_var.set('')
            admission_number_entry.delete(0, tk.END)
            roll_no_entry.delete(0, tk.END)
            gender_var.set('')
            dob_var.set('')
            blood_var.set('')
            father_name_entry.delete(0, tk.END)
            father_occupation_entry.delete(0, tk.END)
            mother_name_entry.delete(0, tk.END)
            mother_occupation_entry.delete(0, tk.END)
            address_entry.delete('1.0', tk.END)
            city_entry.delete(0, tk.END)
            country_var.set('')
            religion_entry.delete(0, tk.END)
            caste_entry.delete(0, tk.END)
            pin_code_entry.delete(0, tk.END)
            state_var.set('')
            email_entry.delete(0, tk.END)
            phone_entry.delete(0, tk.END)
            parent_phone_entry.delete(0, tk.END)
            guardian_entry.delete(0, tk.END)
            relationship_entry.delete(0, tk.END)
            guardian_phone_entry.delete(0, tk.END)
            guardian_address_entry.delete('1.0', tk.END)
            photo_label.config(image='')

                # Placeholder for photo
        photo_label = tk.Label(student_window, text="Upload Your Photo",background="#008000",foreground="white", font=("arial", 12))
        photo_label.place(x=900, y=100)

        def on_enter(e):
            e.widget['bg'] = '#DA70D6'  # Light violet on hover

        def on_leave(e):
            e.widget['bg'] = '#FFD700'  # Dark violet back

        # Button configuration
        button_config = {
            'bg': "#FFD700",  # Dark violet color
            'fg': "white",    # White font color
            'font': ("Arial", 12),  # Font size
            'padx': 20,       # Horizontal padding
            'pady': 10,       # Vertical padding
            'width': 7       # Fixed width for buttons
        }
        # Button positions
        button_x = 1055  # Common x position for left buttons
        button_spacing = 60  # Space between buttons

        # Browse Photo button
        browse_button = tk.Button(student_window, text="Browse Photo", command=select_photo, **button_config)
        browse_button.place(x=button_x, y=100)
        browse_button.bind("<Enter>", on_enter)
        browse_button.bind("<Leave>", on_leave)

        # Clear Photo button
        clear_button = tk.Button(student_window, text="Clear Photo", command=clear_photo, **button_config)
        clear_button.place(x=button_x, y=100 + button_spacing)  # Adjust y for spacing
        clear_button.bind("<Enter>", on_enter)
        clear_button.bind("<Leave>", on_leave)

        # Delete Data button
        delete_button = tk.Button(student_window, text="Delete Data", command=clear_all, **button_config)
        delete_button.place(x=1233, y=100)  # Keep this x position consistent
        delete_button.bind("<Enter>", on_enter)
        delete_button.bind("<Leave>", on_leave)

        # Register button
        register_button = tk.Button(student_window, text="Register", command=complete_registration, **button_config)
        register_button.place(x=1233, y=100 + button_spacing)  # Consistent y position
        register_button.bind("<Enter>", on_enter)
        register_button.bind("<Leave>", on_leave)

        # Go Back button
        back_button = tk.Button(student_window, text="Go Back", command=lambda: switch_window(student_window, role_selection_window), **button_config)
        back_button.place(x=1233, y=100 + 2 * button_spacing)  # Consistent y position
        back_button.bind("<Enter>", on_enter)
        back_button.bind("<Leave>", on_leave)


        window.mainloop()

    elif role == "admin":
        
        faculty_window = tk.Toplevel(background="#6666ff")
        faculty_window.title("Admin Registration")
        faculty_window.geometry("400x500")

        faculty_id_label = ttk.Label(faculty_window, text="admin New Registration",background="#6666ff", font=("Helvetica", 16))
        faculty_id_label.place(x=55, y=15)

        faculty_id_label = ttk.Label(faculty_window, text="admin Id No",background="#6666ff", font=("arial", 14))
        faculty_id_label.place(x=30, y=90)    

        faculty_id_entry = PlaceholderEntry(faculty_window, placeholder="admin Id Number")
        faculty_id_entry.place(x=150, y=85, width=210)

        faculty_name_label = ttk.Label(faculty_window, text="Name",background="#6666ff", font=("arial", 14))
        faculty_name_label.place(x=30, y=150)

        faculty_name_entry = PlaceholderEntry(faculty_window, placeholder="Enter Your Name")
        faculty_name_entry.place(x=150, y=145, width=210)
        # Function to change button color on hover
        def on_enter(e):
            e.widget['bg'] = '#DA70D6'  # Light violet on hover

        # Function to change button color back
        def on_leave(e):
            e.widget['bg'] = '#0000cc'  # Dark violet back

        # Button configuration
        button_config = {
            'bg': "#0000cc",  # Dark violet color
            'fg': "white",    # White font color
            'font': ("Arial", 12),  # Font size
            'padx': 20,       # Horizontal padding
            'pady': 10,       # Vertical padding
            'width': 8       # Fixed width for buttons
        }

        # Create Register button
        registerbutton = tk.Button(faculty_window, text="Register", command=complete_registration, **button_config)
        registerbutton.place(x=30, y=230)  # X position is 75, Y position is 230
        registerbutton.bind("<Enter>", on_enter)
        registerbutton.bind("<Leave>", on_leave)

        # Create Go Back button
        backbutton = tk.Button(faculty_window, text="Go Back", command=lambda: switch_window(faculty_window, role_selection_window), **button_config)
        backbutton.place(x=235, y=230)  # Same X position, Y position is 280 for spacing
        backbutton.bind("<Enter>", on_enter)
        backbutton.bind("<Leave>", on_leave)
        window.mainloop()

    elif role == "principal":
        
        faculty_window = tk.Toplevel(background="#6666ff")
        faculty_window.title("Principal Registration")
        faculty_window.geometry("400x500")

        faculty_id_label = ttk.Label(faculty_window, text="Principal New Registration",background="#6666ff", font=("Helvetica", 16))
        faculty_id_label.place(x=55, y=15)

        faculty_id_label = ttk.Label(faculty_window, text="Principal Id No",background="#6666ff", font=("arial", 14))
        faculty_id_label.place(x=30, y=90)    

        faculty_id_entry = PlaceholderEntry(faculty_window, placeholder="Principal Id Number")
        faculty_id_entry.place(x=160, y=85, width=210)

        faculty_name_label = ttk.Label(faculty_window, text="Name",background="#6666ff", font=("arial", 14))
        faculty_name_label.place(x=30, y=150)

        faculty_name_entry = PlaceholderEntry(faculty_window, placeholder="Enter Your Name")
        faculty_name_entry.place(x=160, y=145, width=210)
        # Function to change button color on hover
        def on_enter(e):
            e.widget['bg'] = '#DA70D6'  # Light violet on hover

        # Function to change button color back
        def on_leave(e):
            e.widget['bg'] = '#0000cc'  # Dark violet back

        # Button configuration
        button_config = {
            'bg': "#0000cc",  # Dark violet color
            'fg': "white",    # White font color
            'font': ("Arial", 12),  # Font size
            'padx': 20,       # Horizontal padding
            'pady': 10,       # Vertical padding
            'width': 8       # Fixed width for buttons
        }

        # Create Register button
        registerbutton = tk.Button(faculty_window, text="Register", command=complete_registration, **button_config)
        registerbutton.place(x=30, y=230)  # X position is 75, Y position is 230
        registerbutton.bind("<Enter>", on_enter)
        registerbutton.bind("<Leave>", on_leave)

        # Create Go Back button
        backbutton = tk.Button(faculty_window, text="Go Back", command=lambda: switch_window(faculty_window, role_selection_window), **button_config)
        backbutton.place(x=245, y=230)  # Same X position, Y position is 280 for spacing
        backbutton.bind("<Enter>", on_enter)
        backbutton.bind("<Leave>", on_leave)

        window.mainloop()

    elif role == "faculty":
        # Create the faculty registration window
        faculty_window = tk.Toplevel(background="#800033")
        faculty_window.title("Faculty Registration")
        faculty_window.geometry("1380x768")

        # Canvas for drawing
        canvas = tk.Canvas(faculty_window, bg="#800033")
        canvas.place(relwidth=1, relheight=1)

        # Draw square lines for visual separation
        canvas.create_rectangle(1200, 325, 25, 600, width=2, outline="#FFD700")  # Square 1
        canvas.create_rectangle(1200, 300, 25, 30, width=2, outline="#FFD700")   # Square 2
        canvas.create_rectangle(1200, 625, 25, 685, width=2, outline="#FFD700")  # Square 3
        canvas.create_rectangle(1225, 360, 1350, 30, width=2, outline="#FFD700")  # Square 4

        faculty_id_label = ttk.Label(faculty_window, text="Faculty New Registration",background="#800033",foreground="white", font=("Helvetica", 16))
        faculty_id_label.place(x=55, y=15)

        faculty_id_label = ttk.Label(faculty_window, text="Faculty Id No",background="#800033",foreground="white", font=("arial", 14))
        faculty_id_label.place(x=30, y=60)    

        faculty_id_entry = PlaceholderEntry(faculty_window, placeholder="Faculty Id Number")
        faculty_id_entry.place(x=210, y=55, width=210)

        faculty_name_label = ttk.Label(faculty_window, text="Name",background="#800033",foreground="white", font=("arial", 14))
        faculty_name_label.place(x=30, y=120)

        faculty_name_entry = PlaceholderEntry(faculty_window, placeholder="Enter Your Name")
        faculty_name_entry.place(x=210, y=115, width=210)

        department_label = ttk.Label(faculty_window, text="Department",background="#800033",foreground="white", font=("arial", 14))
        department_label.place(x=30, y=205) 

        department_var = tk.StringVar()
        department_combobox = ttk.Combobox(faculty_window, textvariable=department_var, font=("Helvetica", 12), state='readonly')
        department_combobox['values'] = ["B.E Civil Engineering","B.E Computer Science Engineering","B.E Electrical and Electronics Engineering","B.E Electronics and Communication Engineering","B.Tech Information Technology","B.E Mechanical Engineering",
    "B.Tech Artificial Intelligence and Data Science","B.Tech Computer Science and Business Systems","Marine Engineering","Aerospace Engineering","Master of Business Administration (MBA)","Master of Computer Application (MCA)",
    "M.E Power Electronics and Drives","M.E Communication systems","M.E Computer Science Engineering","M.E Engineering Design"]
        department_combobox.place(x=210, y=205, width=210 ,height=30)   

        # GENDER ENTRY
        faculty_gender_label = ttk.Label(faculty_window, text="Gender ",background="#800033",foreground="white", font=("arial", 14))
        faculty_gender_label.place(x=450, y=60) 

        faculty_gender_var = tk.StringVar()  # Correct variable name
        faculty_gender_combobox = ttk.Combobox(faculty_window, textvariable=faculty_gender_var, font=("Helvetica", 12), state='readonly')
        faculty_gender_combobox['values'] = ["Male", "Female", "Transgender"]
        faculty_gender_combobox.place(x=590, y=60, width=210 ,height=30)

        # DOB ENTRY
        faculty_dob_label = ttk.Label(faculty_window, text="DOB ",background="#800033",foreground="white", font=("arial", 14))
        faculty_dob_label.place(x=450, y=120)  

        # DateEntry with the correct variable
        faculty_dob_var = tk.StringVar()  # Correct variable name
        faculty_dob_entry = DateEntry(faculty_window, textvariable=faculty_dob_var, font=("Helvetica", 11), date_pattern='dd/MM/yyyy')
        faculty_dob_entry.place(x=590, y=120, width=210 ,height=30)

        # BLOOD GROUP
        faculty_blood_label = ttk.Label(faculty_window, text="Blood Group ",background="#800033",foreground="white", font=("arial", 14))
        faculty_blood_label.place(x=450, y=180) 

        faculty_blood_var = tk.StringVar()  # Correct variable name
        faculty_blood_combobox = ttk.Combobox(faculty_window, textvariable=faculty_blood_var, font=("Helvetica", 12), state='readonly')
        faculty_blood_combobox['values'] = ["A RhD positive (A+)", "A RhD negative (A-)", "B RhD positive (B+)", "B RhD negative (B-)",
                                            "O RhD positive (O+)", "O RhD negative (O-)", "AB RhD positive (AB+)", "AB RhD negative (AB-)"]
        faculty_blood_combobox.place(x=590, y=180, width=210 ,height=30)

        faculty_marital_label = ttk.Label(faculty_window, text="Marital Status ",background="#800033",foreground="white", font=("arial", 14))
        faculty_marital_label.place(x=30, y=240) 

        faculty_marital_var = tk.StringVar()
        faculty_marital_combobox = ttk.Combobox(faculty_window, textvariable=faculty_marital_var, font=("Helvetica", 12), state='readonly')
        faculty_marital_combobox['values'] = ["Single","Married"]
        faculty_marital_combobox.place(x=210, y=240, width=210 ,height=30)

            #family information
        faculty_family_label = ttk.Label(faculty_window, text="Personal Details",background="#800033",foreground="white", font=("arial", 14))
        faculty_family_label.place(x=55, y=308) 


        faculty_job_position_label = ttk.Label(faculty_window, text="Post / Position",background="#800033",foreground="white", font=("arial", 14))
        faculty_job_position_label.place(x=450, y=240)  

        faculty_job_position_entry = PlaceholderEntry(faculty_window, placeholder="Enter Your Job Position")
        faculty_job_position_entry.place(x=590, y=235, width=210) 

        #     #ADDRESS
        faculty_address_label = ttk.Label(faculty_window, text="Address ",background="#800033",foreground="white", font=("arial", 14))
        faculty_address_label.place(x=30, y=430)
        
        faculty_address_entry = tk.Text(faculty_window, width=39, height=3, font=("Helvetica", 14))
        faculty_address_entry.place(x=215, y=430)     

        faculty_city_label = ttk.Label(faculty_window, text="City ",background="#800033",foreground="white", font=("arial", 14))
        faculty_city_label.place(x=660, y=465)    
        
        faculty_city_entry = PlaceholderEntry(faculty_window, placeholder="Enter Your City")
        faculty_city_entry.place(x=740, y=465, width=215)

        # COUNTRY
        faculty_country_label = ttk.Label(faculty_window, text="Country ",background="#800033",foreground="white", font=("arial", 14))
        faculty_country_label.place(x=660, y=425) 

        # Correct variable name
        faculty_country_var = tk.StringVar()
        faculty_country_combobox = ttk.Combobox(faculty_window, textvariable=faculty_country_var, font=("Helvetica", 12), state='readonly')
        faculty_country_combobox['values'] = ["USA", "Canada", "Mexico", "Germany", "France", "Italy", "Spain", "UK", "India", "China", "Japan"]
        faculty_country_combobox.place(x=740, y=425, width=210 ,height=30)
            #pin code
        faculty_pin_label = ttk.Label(faculty_window, text="Pin Code",background="#800033",foreground="white", font=("arial", 14))
        faculty_pin_label.place(x=30, y=540) 

        faculty_pin_code_entry = PlaceholderEntry(faculty_window, placeholder="Postal/Zip Code")
        faculty_pin_code_entry.place(x=210, y=535, width=210)

        # STATE
        faculty_state_label = ttk.Label(faculty_window, text="State ",background="#800033",foreground="white", font=("arial", 14))
        faculty_state_label.place(x=450, y=540)  

        # Correct variable name
        faculty_state_var = tk.StringVar()
        faculty_state_combobox = ttk.Combobox(faculty_window, textvariable=faculty_state_var, font=("Helvetica", 12), state='readonly')
        faculty_state_combobox['values'] = [
            "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Delhi", "Goa", "Gujarat", "Haryana", 
            "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Maharashtra", "Madhya Pradesh", "Manipur", "Meghalaya", 
            "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Tripura", "Telangana", 
            "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman & Nicobar (UT)", "Chandigarh (UT)", "Dadra & Nagar Haveli (UT)", 
            "Daman & Diu (UT)", "Jammu & Kashmir(UT)", "Lakshadweep (UT)", "Ladakh (UT)", "Puducherry (UT)"
        ]
        faculty_state_combobox.place(x=545, y=540, width=210 ,height=30)
            # # EMAIL
        faculty_email_label = ttk.Label(faculty_window, text="Email ",background="#800033",foreground="white", font=("arial", 14))
        faculty_email_label.place(x=30, y=365)  

        faculty_email_entry = PlaceholderEntry(faculty_window, placeholder="Enter Your Email")
        faculty_email_entry.place(x=215, y=360, width=210)    

        faculty_phone_label = ttk.Label(faculty_window, text="Phone No ",background="#800033",foreground="white", font=("arial", 14))
        faculty_phone_label.place(x=450, y=365)  

        faculty_phone_entry = PlaceholderEntry(faculty_window, placeholder="Enter Phone Number")
        faculty_phone_entry.place(x=560, y=360, width=250)

        faculty_infgardian_label = ttk.Label(faculty_window, text="Guardian Information ",background="#800033",foreground="white", font=("arial", 14))
        faculty_infgardian_label.place(x=55, y=610)      
        
        faculty_guardian_label = ttk.Label(faculty_window, text="Name ",background="#800033",foreground="white", font=("arial", 14))
        faculty_guardian_label.place(x=30, y=640) 

        faculty_guardian_entry = PlaceholderEntry(faculty_window, placeholder="Guardian Name")
        faculty_guardian_entry.place(x=85, y=635, width=150)

        faculty_guardian_relationship_label = ttk.Label(faculty_window, text="Relationship",background="#800033",foreground="white", font=("arial", 14))
        faculty_guardian_relationship_label.place(x=240, y=640)  

        faculty_guardian_relationship_entry = PlaceholderEntry(faculty_window, placeholder="Relationship")
        faculty_guardian_relationship_entry.place(x=360, y=635, width=150)   

            #     #PHONE NUMBER
        faculty_guardian_phone_label = ttk.Label(faculty_window, text="Phone No ",background="#800033",foreground="white", font=("arial", 14))
        faculty_guardian_phone_label.place(x=520, y=640)  

        faculty_guardian_phone_entry = PlaceholderEntry(faculty_window, placeholder="Enter Your Phone Number")
        faculty_guardian_phone_entry.place(x=610, y=635, width=170)  

        #     #ADDRESS
        faculty_garaddress_label = ttk.Label(faculty_window, text="Address ",background="#800033",foreground="white", font=("arial", 14))
        faculty_garaddress_label.place(x=800, y=640)
        
        faculty_guardian_address_entry = tk.Text(faculty_window, width=25, height=2, font=("Helvetica", 12))
        faculty_guardian_address_entry.place(x=900, y=635) 

        def clear_all():
            # Clear Entry fields
            faculty_id_entry.clear()  # Use the clear method
            faculty_name_entry.clear()  # Use the clear method
            department_var.set('')  # Use set() if it's a StringVar
            faculty_gender_var.set('')  # Use set() if it's a StringVar
            faculty_dob_var.set('')  # Use set() if it's a StringVar
            faculty_blood_var.set('')  # Use set() if it's a StringVar
            faculty_marital_var.set('')  # Use set() if it's a StringVar
            faculty_job_position_entry.clear()  # Use the clear method
            faculty_address_entry.delete(1.0, tk.END)  # Clear Text widget (1.0 is the start index)
            faculty_city_entry.clear()  # Use the clear method
            faculty_country_var.set('')  # Use set() if it's a StringVar
            faculty_pin_code_entry.clear()  # Use the clear method
            faculty_state_var.set('')  # Use set() if it's a StringVar
            faculty_email_entry.clear()  # Use the clear method
            faculty_phone_entry.clear()  # Use the clear method
            faculty_guardian_entry.clear()  # Use the clear method
            faculty_guardian_relationship_entry.clear()  # Use the clear method
            faculty_guardian_phone_entry.clear()  # Use the clear method
            faculty_guardian_address_entry.delete(1.0, tk.END)  # Clear Text widget

            # Reset the photo label
            photo_label.config(image='')  # Reset the image, if applicable
            photo_label.image = None  # Also clear the reference to the image


                # Placeholder for photo
        photo_label = tk.Label(faculty_window, text="Upload Your Photo",background="#800033",foreground="white", font=("arial", 12))
        photo_label.place(x=900, y=100)

        def on_enter(e):
            e.widget['bg'] = '#DA70D6'  # Light violet on hover

        def on_leave(e):
            e.widget['bg'] = '#FFD700'  # Dark violet back

        # Button configuration
        button_config = {
            'bg': "#FFD700",  # Dark violet color
            'fg': "white",    # White font color
            'font': ("Arial", 12),  # Font size
            'padx': 20,       # Horizontal padding
            'pady': 10,       # Vertical padding
            'width': 7       # Fixed width for buttons
        }
        # Button positions
        button_x = 1055  # Common x position for left buttons
        button_spacing = 60  # Space between buttons

        # Browse Photo button
        browse_button = tk.Button(faculty_window, text="Browse Photo", command=select_photo, **button_config)
        browse_button.place(x=button_x, y=100)
        browse_button.bind("<Enter>", on_enter)
        browse_button.bind("<Leave>", on_leave)

        # Clear Photo button
        clear_button = tk.Button(faculty_window, text="Clear Photo", command=clear_photo, **button_config)
        clear_button.place(x=button_x, y=100 + button_spacing)  # Adjust y for spacing
        clear_button.bind("<Enter>", on_enter)
        clear_button.bind("<Leave>", on_leave)

        # Delete Data button
        delete_button = tk.Button(faculty_window, text="Delete Data", command=clear_all, **button_config)
        delete_button.place(x=1233, y=100)  # Keep this x position consistent
        delete_button.bind("<Enter>", on_enter)
        delete_button.bind("<Leave>", on_leave)

        # Register button
        register_button = tk.Button(faculty_window, text="Register", command=complete_registration, **button_config)
        register_button.place(x=1233, y=100 + button_spacing)  # Consistent y position
        register_button.bind("<Enter>", on_enter)
        register_button.bind("<Leave>", on_leave)

        # Go Back button
        back_button = tk.Button(faculty_window, text="Go Back", command=lambda: switch_window(faculty_window, role_selection_window), **button_config)
        back_button.place(x=1233, y=100 + 2 * button_spacing)  # Consistent y position
        back_button.bind("<Enter>", on_enter)
        back_button.bind("<Leave>", on_leave)

        window.mainloop()

    elif role == "hod":
        
        # Create the faculty registration window
        faculty_window = tk.Toplevel(background="#4d0000")
        faculty_window.title("HOD Registration")
        faculty_window.geometry("1380x768")

        # Canvas for drawing
        canvas = tk.Canvas(faculty_window, bg="#4d0000")
        canvas.place(relwidth=1, relheight=1)

        # Draw square lines for visual separation
        canvas.create_rectangle(1200, 325, 25, 600, width=2, outline="#FFD700")  # Square 1
        canvas.create_rectangle(1200, 300, 25, 30, width=2, outline="#FFD700")   # Square 2
        canvas.create_rectangle(1200, 625, 25, 685, width=2, outline="#FFD700")  # Square 3
        canvas.create_rectangle(1225, 360, 1350, 30, width=2, outline="#FFD700")  # Square 4 


        faculty_id_label = ttk.Label(faculty_window, text="Faculty New Registration" ,background="#4d0000",foreground="white", font=("Helvetica", 16))
        faculty_id_label.place(x=55, y=15)

        faculty_id_label = ttk.Label(faculty_window, text="Faculty Id No" ,background="#4d0000",foreground="white", font=("arial", 14))
        faculty_id_label.place(x=30, y=60)    

        faculty_id_entry = PlaceholderEntry(faculty_window, placeholder="Faculty Id Number")
        faculty_id_entry.place(x=210, y=55, width=210)

        faculty_name_label = ttk.Label(faculty_window, text="Name" ,background="#4d0000",foreground="white", font=("arial", 14))
        faculty_name_label.place(x=30, y=120)

        faculty_name_entry = PlaceholderEntry(faculty_window, placeholder="Enter Your Name")
        faculty_name_entry.place(x=210, y=115, width=210)

        department_label = ttk.Label(faculty_window, text="Department" ,background="#4d0000",foreground="white", font=("arial", 14))
        department_label.place(x=30, y=205) 

        department_var = tk.StringVar()
        department_combobox = ttk.Combobox(faculty_window, textvariable=department_var, font=("Helvetica", 12), state='readonly')
        department_combobox['values'] = ["B.E Civil Engineering","B.E Computer Science Engineering","B.E Electrical and Electronics Engineering","B.E Electronics and Communication Engineering","B.Tech Information Technology","B.E Mechanical Engineering",
    "B.Tech Artificial Intelligence and Data Science","B.Tech Computer Science and Business Systems","Marine Engineering","Aerospace Engineering","Master of Business Administration (MBA)","Master of Computer Application (MCA)",
    "M.E Power Electronics and Drives","M.E Communication systems","M.E Computer Science Engineering","M.E Engineering Design"]
        department_combobox.place(x=210, y=205, width=210,height=30)   

        # GENDER ENTRY
        faculty_gender_label = ttk.Label(faculty_window, text="Gender " ,background="#4d0000",foreground="white", font=("arial", 14))
        faculty_gender_label.place(x=450, y=60) 

        faculty_gender_var = tk.StringVar()  # Correct variable name
        faculty_gender_combobox = ttk.Combobox(faculty_window, textvariable=faculty_gender_var, font=("Helvetica", 12), state='readonly')
        faculty_gender_combobox['values'] = ["Male", "Female", "Transgender"]
        faculty_gender_combobox.place(x=590, y=60, width=210, height=30)

        # DOB ENTRY
        faculty_dob_label = ttk.Label(faculty_window, text="DOB " ,background="#4d0000",foreground="white", font=("arial", 14))
        faculty_dob_label.place(x=450, y=120)  

        # DateEntry with the correct variable
        faculty_dob_var = tk.StringVar()  # Correct variable name
        faculty_dob_entry = DateEntry(faculty_window, textvariable=faculty_dob_var, font=("Helvetica", 11), date_pattern='dd/MM/yyyy')
        faculty_dob_entry.place(x=590, y=120, width=210, height=30)

        # BLOOD GROUP
        faculty_blood_label = ttk.Label(faculty_window, text="Blood Group " ,background="#4d0000",foreground="white", font=("arial", 14))
        faculty_blood_label.place(x=450, y=180) 

        faculty_blood_var = tk.StringVar()  # Correct variable name
        faculty_blood_combobox = ttk.Combobox(faculty_window, textvariable=faculty_blood_var, font=("Helvetica", 12), state='readonly')
        faculty_blood_combobox['values'] = ["A RhD positive (A+)", "A RhD negative (A-)", "B RhD positive (B+)", "B RhD negative (B-)",
                                            "O RhD positive (O+)", "O RhD negative (O-)", "AB RhD positive (AB+)", "AB RhD negative (AB-)"]
        faculty_blood_combobox.place(x=590, y=180, width=210, height=30)

        faculty_marital_label = ttk.Label(faculty_window, text="Marital Status " ,background="#4d0000",foreground="white", font=("arial", 14))
        faculty_marital_label.place(x=30, y=240) 

        faculty_marital_var = tk.StringVar()
        faculty_marital_combobox = ttk.Combobox(faculty_window, textvariable=faculty_marital_var, font=("Helvetica", 12), state='readonly')
        faculty_marital_combobox['values'] = ["Single","Married"]
        faculty_marital_combobox.place(x=210, y=240, width=210,height=30)

            #family information
        faculty_family_label = ttk.Label(faculty_window, text="Personal Details" ,background="#4d0000",foreground="white", font=("arial", 14))
        faculty_family_label.place(x=55, y=308) 


        faculty_job_position_label = ttk.Label(faculty_window, text="Post / Position" ,background="#4d0000",foreground="white", font=("arial", 14))
        faculty_job_position_label.place(x=450, y=240)  

        faculty_job_position_entry = PlaceholderEntry(faculty_window, placeholder="Enter Your Job Position")
        faculty_job_position_entry.place(x=590, y=235, width=210) 

        #     #ADDRESS
        faculty_address_label = ttk.Label(faculty_window, text="Address " ,background="#4d0000",foreground="white", font=("arial", 14))
        faculty_address_label.place(x=30, y=430)
        
        faculty_address_entry = tk.Text(faculty_window, width=39, height=3, font=("Helvetica", 14))
        faculty_address_entry.place(x=215, y=430)     

        faculty_city_label = ttk.Label(faculty_window, text="City " ,background="#4d0000",foreground="white", font=("arial", 14))
        faculty_city_label.place(x=660, y=465)    
        
        faculty_city_entry = PlaceholderEntry(faculty_window, placeholder="Enter Your City")
        faculty_city_entry.place(x=740, y=465, width=215)

        # COUNTRY
        faculty_country_label = ttk.Label(faculty_window, text="Country " ,background="#4d0000",foreground="white", font=("arial", 14))
        faculty_country_label.place(x=660, y=425) 

        # Correct variable name
        faculty_country_var = tk.StringVar()
        faculty_country_combobox = ttk.Combobox(faculty_window, textvariable=faculty_country_var, font=("Helvetica", 12), state='readonly')
        faculty_country_combobox['values'] = ["USA", "Canada", "Mexico", "Germany", "France", "Italy", "Spain", "UK", "India", "China", "Japan"]
        faculty_country_combobox.place(x=740, y=425, width=210,height=30)
            #pin code
        faculty_pin_label = ttk.Label(faculty_window, text="Pin Code" ,background="#4d0000",foreground="white", font=("arial", 14))
        faculty_pin_label.place(x=30, y=540) 

        faculty_pin_code_entry = PlaceholderEntry(faculty_window, placeholder="Postal/Zip Code")
        faculty_pin_code_entry.place(x=210, y=535, width=210)

        # STATE
        faculty_state_label = ttk.Label(faculty_window, text="State " ,background="#4d0000",foreground="white", font=("arial", 14))
        faculty_state_label.place(x=450, y=540)  

        # Correct variable name
        faculty_state_var = tk.StringVar()
        faculty_state_combobox = ttk.Combobox(faculty_window, textvariable=faculty_state_var, font=("Helvetica", 12), state='readonly')
        faculty_state_combobox['values'] = [
            "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Delhi", "Goa", "Gujarat", "Haryana", 
            "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Maharashtra", "Madhya Pradesh", "Manipur", "Meghalaya", 
            "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Tripura", "Telangana", 
            "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman & Nicobar (UT)", "Chandigarh (UT)", "Dadra & Nagar Haveli (UT)", 
            "Daman & Diu (UT)", "Jammu & Kashmir(UT)", "Lakshadweep (UT)", "Ladakh (UT)", "Puducherry (UT)"
        ]
        faculty_state_combobox.place(x=545, y=540, width=210, height=30)
            # # EMAIL
        faculty_email_label = ttk.Label(faculty_window, text="Email " ,background="#4d0000",foreground="white", font=("arial", 14))
        faculty_email_label.place(x=30, y=365)  

        faculty_email_entry = PlaceholderEntry(faculty_window, placeholder="Enter Your Email")
        faculty_email_entry.place(x=215, y=360, width=210)    

        faculty_phone_label = ttk.Label(faculty_window, text="Phone No " ,background="#4d0000",foreground="white", font=("arial", 14))
        faculty_phone_label.place(x=450, y=365)  

        faculty_phone_entry = PlaceholderEntry(faculty_window, placeholder="Enter Phone Number")
        faculty_phone_entry.place(x=560, y=360, width=250)

        faculty_infgardian_label = ttk.Label(faculty_window, text="Guardian Information " ,background="#4d0000",foreground="white", font=("arial", 14))
        faculty_infgardian_label.place(x=55, y=610)      
        
        faculty_guardian_label = ttk.Label(faculty_window, text="Name " ,background="#4d0000",foreground="white", font=("arial", 14))
        faculty_guardian_label.place(x=30, y=640) 

        faculty_guardian_entry = PlaceholderEntry(faculty_window, placeholder="Guardian Name")
        faculty_guardian_entry.place(x=85, y=635, width=150)

        faculty_guardian_relationship_label = ttk.Label(faculty_window, text="Relationship" ,background="#4d0000",foreground="white", font=("arial", 14))
        faculty_guardian_relationship_label.place(x=240, y=640)  

        faculty_guardian_relationship_entry = PlaceholderEntry(faculty_window, placeholder="Relationship")
        faculty_guardian_relationship_entry.place(x=360, y=635, width=150)   

            #     #PHONE NUMBER
        faculty_guardian_phone_label = ttk.Label(faculty_window, text="Phone No " ,background="#4d0000",foreground="white", font=("arial", 14))
        faculty_guardian_phone_label.place(x=520, y=640)  

        faculty_guardian_phone_entry = PlaceholderEntry(faculty_window, placeholder="Enter Your Phone Number")
        faculty_guardian_phone_entry.place(x=610, y=635, width=170)  

        #     #ADDRESS
        faculty_garaddress_label = ttk.Label(faculty_window, text="Address " ,background="#4d0000",foreground="white", font=("arial", 14))
        faculty_garaddress_label.place(x=800, y=640)
        
        faculty_guardian_address_entry = tk.Text(faculty_window, width=25, height=2, font=("Helvetica", 12))
        faculty_guardian_address_entry.place(x=900, y=635) 

        def clear_all():

            faculty_id_entry.delete(0, tk.END),
            faculty_name_entry.delete(0, tk.END),
            department_var.delete(0, tk.END),
            faculty_gender_var.delete(0, tk.END),
            faculty_dob_var.delete(0, tk.END),
            faculty_blood_var.delete(0, tk.END),
            faculty_marital_var.delete(0, tk.END),
            faculty_job_position_entry.delete(0, tk.END),
            faculty_address_entry.Text.delete(0, tk.END),
            faculty_city_entry.delete(0, tk.END),
            faculty_country_var.delete(0, tk.END),
            faculty_pin_code_entry.delete(0, tk.END),
            faculty_state_var.delete(0, tk.END),
            faculty_email_entry.delete(0, tk.END),
            faculty_phone_entry.delete(0, tk.END),
            faculty_guardian_entry.delete(0, tk.END),
            faculty_guardian_relationship_entry.delete(0, tk.END),
            faculty_guardian_phone_entry.delete(0, tk.END),
            faculty_guardian_address_entry.Text.delete(0, tk.END),
            photo_label.config(image='')

                # Placeholder for photo
        photo_label = tk.Label(faculty_window, text="Upload Your Photo" ,background="#4d0000",foreground="white", font=("arial", 12))
        photo_label.place(x=900, y=100)

        def on_enter(e):
            e.widget['bg'] = '#DA70D6'  # Light violet on hover

        def on_leave(e):
            e.widget['bg'] = '#FFD700'  # Dark violet back

        # Button configuration
        button_config = {
            'bg': "#FFD700",  # Dark violet color
            'fg': "white",    # White font color
            'font': ("Arial", 12),  # Font size
            'padx': 20,       # Horizontal padding
            'pady': 10,       # Vertical padding
            'width': 7       # Fixed width for buttons
        }
        # Button positions
        button_x = 1055  # Common x position for left buttons
        button_spacing = 60  # Space between buttons

        # Browse Photo button
        browse_button = tk.Button(faculty_window, text="Browse Photo", command=select_photo, **button_config)
        browse_button.place(x=button_x, y=100)
        browse_button.bind("<Enter>", on_enter)
        browse_button.bind("<Leave>", on_leave)

        # Clear Photo button
        clear_button = tk.Button(faculty_window, text="Clear Photo", command=clear_photo, **button_config)
        clear_button.place(x=button_x, y=100 + button_spacing)  # Adjust y for spacing
        clear_button.bind("<Enter>", on_enter)
        clear_button.bind("<Leave>", on_leave)

        # Delete Data button
        delete_button = tk.Button(faculty_window, text="Delete Data", command=clear_all, **button_config)
        delete_button.place(x=1233, y=100)  # Keep this x position consistent
        delete_button.bind("<Enter>", on_enter)
        delete_button.bind("<Leave>", on_leave)

        # Register button
        register_button = tk.Button(faculty_window, text="Register", command=complete_registration, **button_config)
        register_button.place(x=1233, y=100 + button_spacing)  # Consistent y position
        register_button.bind("<Enter>", on_enter)
        register_button.bind("<Leave>", on_leave)

        # Go Back button
        back_button = tk.Button(faculty_window, text="Go Back", command=lambda: switch_window(faculty_window, role_selection_window), **button_config)
        back_button.place(x=1233, y=100 + 2 * button_spacing)  # Consistent y position
        back_button.bind("<Enter>", on_enter)
        back_button.bind("<Leave>", on_leave)


        window.mainloop()

    elif role == "accountant":
        
        # Create the faculty registration window
        faculty_window = tk.Toplevel(background="#4d4d00")
        faculty_window.title("Accountant Registration")
        faculty_window.geometry("1380x768")

        # Canvas for drawing
        canvas = tk.Canvas(faculty_window, bg="#4d4d00")
        canvas.place(relwidth=1, relheight=1)

        # Draw square lines for visual separation
        canvas.create_rectangle(1200, 325, 25, 600, width=2, outline="#FFD700")  # Square 1
        canvas.create_rectangle(1200, 300, 25, 30, width=2, outline="#FFD700")   # Square 2
        canvas.create_rectangle(1200, 625, 25, 685, width=2, outline="#FFD700")  # Square 3
        canvas.create_rectangle(1225, 360, 1350, 30, width=2, outline="#FFD700")  # Square 4 


        faculty_id_label = ttk.Label(faculty_window, text="Faculty New Registration",background="#4d4d00",foreground="white", font=("Helvetica", 16))
        faculty_id_label.place(x=55, y=15)

        faculty_id_label = ttk.Label(faculty_window, text="Faculty Id No",background="#4d4d00",foreground="white", font=("arial", 14))
        faculty_id_label.place(x=30, y=60)    

        faculty_id_entry = PlaceholderEntry(faculty_window, placeholder="Faculty Id Number")
        faculty_id_entry.place(x=210, y=55, width=210)

        faculty_name_label = ttk.Label(faculty_window, text="Name",background="#4d4d00",foreground="white", font=("arial", 14))
        faculty_name_label.place(x=30, y=120)

        faculty_name_entry = PlaceholderEntry(faculty_window, placeholder="Enter Your Name")
        faculty_name_entry.place(x=210, y=115, width=210)

        department_label = ttk.Label(faculty_window, text="Department",background="#4d4d00",foreground="white", font=("arial", 14))
        department_label.place(x=30, y=205) 

        department_var = tk.StringVar()
        department_combobox = ttk.Combobox(faculty_window, textvariable=department_var, font=("Helvetica", 12), state='readonly')
        department_combobox['values'] = ["B.E Civil Engineering","B.E Computer Science Engineering","B.E Electrical and Electronics Engineering","B.E Electronics and Communication Engineering","B.Tech Information Technology","B.E Mechanical Engineering",
    "B.Tech Artificial Intelligence and Data Science","B.Tech Computer Science and Business Systems","Marine Engineering","Aerospace Engineering","Master of Business Administration (MBA)","Master of Computer Application (MCA)",
    "M.E Power Electronics and Drives","M.E Communication systems","M.E Computer Science Engineering","M.E Engineering Design"]
        department_combobox.place(x=210, y=205, width=210,height=30)   

        # GENDER ENTRY
        faculty_gender_label = ttk.Label(faculty_window, text="Gender ",background="#4d4d00",foreground="white", font=("arial", 14))
        faculty_gender_label.place(x=450, y=60) 

        faculty_gender_var = tk.StringVar()  # Correct variable name
        faculty_gender_combobox = ttk.Combobox(faculty_window, textvariable=faculty_gender_var, font=("Helvetica", 12), state='readonly')
        faculty_gender_combobox['values'] = ["Male", "Female", "Transgender"]
        faculty_gender_combobox.place(x=590, y=60, width=210, height=30)

        # DOB ENTRY
        faculty_dob_label = ttk.Label(faculty_window, text="DOB ",background="#4d4d00",foreground="white", font=("arial", 14))
        faculty_dob_label.place(x=450, y=120)  

        # DateEntry with the correct variable
        faculty_dob_var = tk.StringVar()  # Correct variable name
        faculty_dob_entry = DateEntry(faculty_window, textvariable=faculty_dob_var, font=("Helvetica", 11), date_pattern='dd/MM/yyyy')
        faculty_dob_entry.place(x=590, y=120, width=210, height=30)

        # BLOOD GROUP
        faculty_blood_label = ttk.Label(faculty_window, text="Blood Group ",background="#4d4d00",foreground="white", font=("arial", 14))
        faculty_blood_label.place(x=450, y=180) 

        faculty_blood_var = tk.StringVar()  # Correct variable name
        faculty_blood_combobox = ttk.Combobox(faculty_window, textvariable=faculty_blood_var, font=("Helvetica", 12), state='readonly')
        faculty_blood_combobox['values'] = ["A RhD positive (A+)", "A RhD negative (A-)", "B RhD positive (B+)", "B RhD negative (B-)",
                                            "O RhD positive (O+)", "O RhD negative (O-)", "AB RhD positive (AB+)", "AB RhD negative (AB-)"]
        faculty_blood_combobox.place(x=590, y=180, width=210, height=30)

        faculty_marital_label = ttk.Label(faculty_window, text="Marital Status ",background="#4d4d00",foreground="white", font=("arial", 14))
        faculty_marital_label.place(x=30, y=240) 

        faculty_marital_var = tk.StringVar()
        faculty_marital_combobox = ttk.Combobox(faculty_window, textvariable=faculty_marital_var, font=("Helvetica", 12), state='readonly')
        faculty_marital_combobox['values'] = ["Single","Married"]
        faculty_marital_combobox.place(x=210, y=240, width=210,height=30)

            #family information
        faculty_family_label = ttk.Label(faculty_window, text="Personal Details",background="#4d4d00",foreground="white", font=("arial", 14))
        faculty_family_label.place(x=55, y=308) 


        faculty_job_position_label = ttk.Label(faculty_window, text="Post / Position",background="#4d4d00",foreground="white", font=("arial", 14))
        faculty_job_position_label.place(x=450, y=240)  

        faculty_job_position_entry = PlaceholderEntry(faculty_window, placeholder="Enter Your Job Position")
        faculty_job_position_entry.place(x=590, y=235, width=210) 

        #     #ADDRESS
        faculty_address_label = ttk.Label(faculty_window, text="Address ",background="#4d4d00",foreground="white", font=("arial", 14))
        faculty_address_label.place(x=30, y=430)
        
        faculty_address_entry = tk.Text(faculty_window, width=39, height=3, font=("Helvetica", 14))
        faculty_address_entry.place(x=215, y=430)     

        faculty_city_label = ttk.Label(faculty_window, text="City ",background="#4d4d00",foreground="white", font=("arial", 14))
        faculty_city_label.place(x=660, y=465)    
        
        faculty_city_entry = PlaceholderEntry(faculty_window, placeholder="Enter Your City")
        faculty_city_entry.place(x=740, y=465, width=215)

        # COUNTRY
        faculty_country_label = ttk.Label(faculty_window, text="Country ",background="#4d4d00",foreground="white", font=("arial", 14))
        faculty_country_label.place(x=660, y=425) 

        # Correct variable name
        faculty_country_var = tk.StringVar()
        faculty_country_combobox = ttk.Combobox(faculty_window, textvariable=faculty_country_var, font=("Helvetica", 12), state='readonly')
        faculty_country_combobox['values'] = ["USA", "Canada", "Mexico", "Germany", "France", "Italy", "Spain", "UK", "India", "China", "Japan"]
        faculty_country_combobox.place(x=740, y=425, width=210 ,height=30)
            #pin code
        faculty_pin_label = ttk.Label(faculty_window, text="Pin Code",background="#4d4d00",foreground="white", font=("arial", 14))
        faculty_pin_label.place(x=30, y=540) 

        faculty_pin_code_entry = PlaceholderEntry(faculty_window, placeholder="Postal/Zip Code")
        faculty_pin_code_entry.place(x=210, y=535, width=210)

        # STATE
        faculty_state_label = ttk.Label(faculty_window, text="State ",background="#4d4d00",foreground="white", font=("arial", 14))
        faculty_state_label.place(x=450, y=540)  

        # Correct variable name
        faculty_state_var = tk.StringVar()
        faculty_state_combobox = ttk.Combobox(faculty_window, textvariable=faculty_state_var, font=("Helvetica", 12), state='readonly')
        faculty_state_combobox['values'] = [
            "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Delhi", "Goa", "Gujarat", "Haryana", 
            "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Maharashtra", "Madhya Pradesh", "Manipur", "Meghalaya", 
            "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Tripura", "Telangana", 
            "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman & Nicobar (UT)", "Chandigarh (UT)", "Dadra & Nagar Haveli (UT)", 
            "Daman & Diu (UT)", "Jammu & Kashmir(UT)", "Lakshadweep (UT)", "Ladakh (UT)", "Puducherry (UT)"
        ]
        faculty_state_combobox.place(x=545, y=540, width=210, height=30)
            # # EMAIL
        faculty_email_label = ttk.Label(faculty_window, text="Email ",background="#4d4d00",foreground="white", font=("arial", 14))
        faculty_email_label.place(x=30, y=365)  

        faculty_email_entry = PlaceholderEntry(faculty_window, placeholder="Enter Your Email")
        faculty_email_entry.place(x=215, y=360, width=210)    

        faculty_phone_label = ttk.Label(faculty_window, text="Phone No ",background="#4d4d00",foreground="white", font=("arial", 14))
        faculty_phone_label.place(x=450, y=365)  

        faculty_phone_entry = PlaceholderEntry(faculty_window, placeholder="Enter Phone Number")
        faculty_phone_entry.place(x=560, y=360, width=250)

        faculty_infgardian_label = ttk.Label(faculty_window, text="Guardian Information ",background="#4d4d00",foreground="white", font=("arial", 14))
        faculty_infgardian_label.place(x=55, y=610)      
        
        faculty_guardian_label = ttk.Label(faculty_window, text="Name ",background="#4d4d00",foreground="white", font=("arial", 14))
        faculty_guardian_label.place(x=30, y=640) 

        faculty_guardian_entry = PlaceholderEntry(faculty_window, placeholder="Guardian Name")
        faculty_guardian_entry.place(x=85, y=635, width=150)

        faculty_guardian_relationship_label = ttk.Label(faculty_window, text="Relationship",background="#4d4d00",foreground="white", font=("arial", 14))
        faculty_guardian_relationship_label.place(x=240, y=640)  

        faculty_guardian_relationship_entry = PlaceholderEntry(faculty_window, placeholder="Relationship")
        faculty_guardian_relationship_entry.place(x=360, y=635, width=150)   

            #     #PHONE NUMBER
        faculty_guardian_phone_label = ttk.Label(faculty_window, text="Phone No ",background="#4d4d00",foreground="white", font=("arial", 14))
        faculty_guardian_phone_label.place(x=520, y=640)  

        faculty_guardian_phone_entry = PlaceholderEntry(faculty_window, placeholder="Enter Your Phone Number")
        faculty_guardian_phone_entry.place(x=610, y=635, width=170)  

        #     #ADDRESS
        faculty_garaddress_label = ttk.Label(faculty_window, text="Address ",background="#4d4d00",foreground="white", font=("arial", 14))
        faculty_garaddress_label.place(x=800, y=640)
        
        faculty_guardian_address_entry = tk.Text(faculty_window, width=25, height=2, font=("Helvetica", 12))
        faculty_guardian_address_entry.place(x=900, y=635) 

        def clear_all():

            faculty_id_entry.delete(0, tk.END),
            faculty_name_entry.delete(0, tk.END),
            department_var.delete(0, tk.END),
            faculty_gender_var.delete(0, tk.END),
            faculty_dob_var.delete(0, tk.END),
            faculty_blood_var.delete(0, tk.END),
            faculty_marital_var.delete(0, tk.END),
            faculty_job_position_entry.delete(0, tk.END),
            faculty_address_entry.Text.delete(0, tk.END),
            faculty_city_entry.delete(0, tk.END),
            faculty_country_var.delete(0, tk.END),
            faculty_pin_code_entry.delete(0, tk.END),
            faculty_state_var.delete(0, tk.END),
            faculty_email_entry.delete(0, tk.END),
            faculty_phone_entry.delete(0, tk.END),
            faculty_guardian_entry.delete(0, tk.END),
            faculty_guardian_relationship_entry.delete(0, tk.END),
            faculty_guardian_phone_entry.delete(0, tk.END),
            faculty_guardian_address_entry.Text.delete(0, tk.END),
            photo_label.config(image='')

                # Placeholder for photo
        photo_label = tk.Label(faculty_window, text="Upload Your Photo",background="#4d4d00",foreground="white", font=("arial", 12))
        photo_label.place(x=900, y=100)
        def on_enter(e):
            e.widget['bg'] = '#DA70D6'  # Light violet on hover

        def on_leave(e):
            e.widget['bg'] = '#FFD700'  # Dark violet back

        # Button configuration
        button_config = {
            'bg': "#FFD700",  # Dark violet color
            'fg': "white",    # White font color
            'font': ("Arial", 12),  # Font size
            'padx': 20,       # Horizontal padding
            'pady': 10,       # Vertical padding
            'width': 7       # Fixed width for buttons
        }

        # Button positions
        button_x = 1055  # Common x position for left buttons
        button_spacing = 60  # Space between buttons

        # Create and place buttons
        browse_button = tk.Button(faculty_window, text="Browse Photo", command=select_photo, **button_config)
        browse_button.place(x=button_x, y=100)
        browse_button.bind("<Enter>", on_enter)
        browse_button.bind("<Leave>", on_leave)

        clear_button = tk.Button(faculty_window, text="Clear Photo", command=clear_photo, **button_config)
        clear_button.place(x=button_x, y=100 + button_spacing)
        clear_button.bind("<Enter>", on_enter)
        clear_button.bind("<Leave>", on_leave)

        delete_button = tk.Button(faculty_window, text="Delete Data", command=clear_all, **button_config)
        delete_button.place(x=1233, y=100)
        delete_button.bind("<Enter>", on_enter)
        delete_button.bind("<Leave>", on_leave)

        register_button = tk.Button(faculty_window, text="Register", command=complete_registration, **button_config)
        register_button.place(x=1233, y=100 + button_spacing)
        register_button.bind("<Enter>", on_enter)
        register_button.bind("<Leave>", on_leave)

        back_button = tk.Button(faculty_window, text="Go Back", command=lambda: switch_window(faculty_window, role_selection_window), **button_config)
        back_button.place(x=1233, y=100 + 2 * button_spacing)
        back_button.bind("<Enter>", on_enter)
        back_button.bind("<Leave>", on_leave)

        window.mainloop()

# Function to go back to the previous page (main window)
def go_back(main_window, username, department, role):
    # Clear all widgets in the main window
    for widget in main_window.winfo_children():
        widget.destroy()

    # Check the role of the user and open the appropriate dashboard
    if role == 'student':
        student_dashboard_window(username, department,role)  # Open student dashboard
    elif role == 'faculty':
        faculty_dashboard_window(username, department,role)  # Open faculty dashboard
    elif role == 'hod':
        hod_dashboard_window(username, department,role)  # Open faculty dashboard
    else:
        # Handle other roles or default case
        messagebox.showerror("Error", f"Unknown role: {role}")


# Function to close the application
def logout_close():
    """Closes the Tkinter application on logout."""
    if messagebox.askyesno("Confirm Logout", "Are you sure you want to log out?"):
        window.destroy()  # Destroys the entire window and exits the application


def open_chat_sidebar(username, department, main_window,role):
    # Clear the main window to make space for the new layout
    for widget in main_window.winfo_children():
        widget.destroy()
    
    # Create header frame for the Back button and any title or navigation
    header_frame = tk.Frame(main_window, bg='#141f1f', height=150)  # Height set to 150
    header_frame.pack(side="top", fill="x")
    header_frame.pack_propagate(False)  # Prevent resizing based on content

    entry_font = ('Helvetica', 10)  # You can adjust the font size as neede

    # Chat section in the header frame (center aligned at the bottom)
    recipient_entry = tk.Entry(header_frame, width=60, font=entry_font)  # Change width as needed
    recipient_entry.insert(0, "Enter recipient username")
    recipient_entry.place(relx=0.44, rely=0.5, anchor='center')  # Centered horizontally, 70% down the height

    # Search button aligned at the bottom center of the header frame
    search_button = tk.Button(header_frame, text="Search",bg="#663300", fg="white" ,command=lambda: search_recipient(recipient_entry.get().strip()), width=15)
    search_button.place(relx=0.45, rely=0.85, anchor='center')  # Centered horizontally, 85% down the height

    # Back button (Top-left corner in header)
    back_button = tk.Button(header_frame, text="Back", bg='#663300', fg='white', width=10, height=2, 
                            command=lambda: go_back(main_window, username, department,role))
    back_button.pack(side="left", padx=5, pady=5)

    # Title in the header
    title_label = tk.Label(header_frame, text="Chat Sidebar", font=("Arial", 16), bg="#141f1f", fg="white")
    title_label.pack(side="left", padx=20)

    # Increase the size of the sidebars by 50%
    sidebar_width = 200  # Assuming original width was 200, increased by 50%
    # Increase the size of the sidebars by 50%
    right_sidebar_width = 350  # Assuming original width was 200, increased by 50%

    # Create left sidebar for role buttons
    left_sidebar = tk.Frame(main_window, bg='#8a8a5c', width=sidebar_width)
    left_sidebar.pack(side="left", fill="y", padx=10, pady=10)
    left_sidebar.pack_propagate(False)  # Prevent resizing based on content

    # Create right sidebar for chat and notifications
    right_sidebar = tk.Frame(main_window, bg='#8a8a5c', width=right_sidebar_width)
    right_sidebar.pack(side="right", fill="y", padx=10, pady=10)
    right_sidebar.pack_propagate(False)  # Prevent resizing based on content

    # Create bottom sidebar for additional options (e.g., settings, extra buttons)
    bottom_sidebar = tk.Frame(main_window, bg='#141f1f', height=150)
    bottom_sidebar.pack(side="bottom", fill="x", padx=10, pady=10)
    bottom_sidebar.pack_propagate(False)  # Prevent resizing based on content

    # Center frame for chat content
    center_frame = tk.Frame(main_window, bg="#c3c3a2")
    center_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Function to handle button click and toggle colors
    def on_button_click(clicked_button, other_buttons):
        # Change clicked button color to #f59dbe and revert the others to #f2025e
        clicked_button.config(bg='#663300', fg='white')  # Set clicked button to the active color
        for button in other_buttons:
            button.config(bg='#2e2e1f', fg='white')  # Revert other buttons to the default color

    # Add role buttons to the left sidebar
    student_button = tk.Button(left_sidebar, text="Student",font="white", bg='#2e2e1f', fg='white', width=20, height=3,
                            command=lambda: [on_button_click(student_button, [faculty_button, hod_button]), display_students(right_sidebar, recipient_entry)])
    student_button.pack(pady=10)

    faculty_button = tk.Button(left_sidebar, text="Faculty",font="white", bg='#2e2e1f', fg='white', width=20, height=3,
                            command=lambda: [on_button_click(faculty_button, [student_button, hod_button]), display_faculty(right_sidebar)])
    faculty_button.pack(pady=10)

    hod_button = tk.Button(left_sidebar, text="HOD",font="white", bg='#2e2e1f', fg='white', width=20, height=3,
                        command=lambda: [on_button_click(hod_button, [student_button, faculty_button]), display_hod(right_sidebar)])
    hod_button.pack(pady=10)


    # Frame to display recipient button in center frame
    recipient_button_frame = tk.Frame(center_frame)
    recipient_button_frame.pack(pady=5)

    # Chat text area and entry box
    msg_text = tk.Text(center_frame, height=15, width=50, wrap="word", state="disabled")
    msg_text.pack(pady=5)
    msg_entry = tk.Entry(center_frame, width=50)
    msg_entry.pack(pady=5)

    send_button = tk.Button(center_frame ,background="#663300" , font="white",fg='white', text="Send", command=lambda: send_message(recipient_entry.get().strip(), msg_entry.get().strip()))
    send_button.pack(pady=5)

    # Step 1: Add the button in your chat section
    old_messages_button = tk.Button(center_frame, background="#663300", font="white" ,fg='white',text="Show Old Messages", command=lambda: fetch_messages(current_recipient_username))
    old_messages_button.pack(pady=5,padx=100)  # Adjust padding as needed

    # Notification label for unread messages (right sidebar)
    notification_label = tk.Label(right_sidebar, text="Unread Messages: 0", fg="red")
    notification_label.pack(pady=10)

    # logout_button = tk.Button(bottom_sidebar, text="Logout", width=15, height=2,command=logout_close)
    # logout_button.pack(side="right", padx=10)

    def display_students(right_sidebar, recipient_entry):
        # Clear existing content in the right sidebar
        for widget in right_sidebar.winfo_children():
            widget.destroy()

        # Create a frame for the Treeview
        excel_frame = tk.Frame(right_sidebar)
        excel_frame.pack(pady=10)

        # Create the Treeview widget
        columns = ("Username", "Student Name", "Department", "Semester")
        treeview = ttk.Treeview(excel_frame, columns=columns, show="headings", height=15)

        # Define the headings
        for col in columns:
            treeview.heading(col, text=col)
            treeview.column(col, anchor="center", width=100)  # Set column width

        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(excel_frame, orient="vertical", command=treeview.yview)
        treeview.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Pack the Treeview
        treeview.pack(side="left", fill="both")

        # Fetch and display students data
        students = fetch_students()  # Call fetch_students() to get updated data
        for student in students:
            # Insert each student into the Treeview
            treeview.insert("", "end", values=(student['username'], student['student_name'], student['department'], student['semester']))

        # Bind the Treeview selection event to update the recipient entry
        treeview.bind("<<TreeviewSelect>>", lambda event: on_student_select(event, treeview, recipient_entry))


    def on_student_select(event, treeview, recipient_entry):
        # Get selected row
        selected_item = treeview.selection()
        
        if selected_item:
            # Get the values of the selected row
            student_values = treeview.item(selected_item, "values")
            username = student_values[0]  # Assuming username is the first value in the row
            
            # Update the recipient_entry with the selected student's username
            recipient_entry.delete(0, tk.END)  # Clear the current entry content
            recipient_entry.insert(0, username)  # Insert the selected username


    def fetch_students():
        global db, cursor  # Use global variables for db and cursor

        if db is None or cursor is None:
            db = connect_to_db()  # Reconnect if necessary
            cursor = db.cursor()

        query = """
        SELECT u.username, s.student_name, s.department, s.semester 
        FROM users u 
        JOIN students s ON u.id = s.user_id
        WHERE u.role = 'student'
        """

        try:
            cursor.execute(query)
            results = cursor.fetchall()  # Fetch all results

            students = [{'username': row[0], 'student_name': row[1], 'department': row[2], 'semester': row[3]} for row in results]
        except mysql.connector.Error as e:
            print(f"Error fetching students: {e}")
            students = []
        finally:
            # Optionally close the cursor but keep the connection open
            # cursor.close()  # Uncomment if you want to close cursor

            return students
    def display_faculty(right_sidebar):
        # Clear existing content in the right sidebar
        for widget in right_sidebar.winfo_children():
            widget.destroy()

        # Create a frame for the Treeview
        excel_frame = tk.Frame(right_sidebar)
        excel_frame.pack(pady=10)

        # Create the Treeview widget
        columns = ("Username", "Faculty Name", "Department")
        treeview = ttk.Treeview(excel_frame, columns=columns, show="headings", height=15)

        # Define the headings
        for col in columns:
            treeview.heading(col, text=col)
            treeview.column(col, anchor="center", width=100)  # Set column width

        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(excel_frame, orient="vertical", command=treeview.yview)
        treeview.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Pack the Treeview
        treeview.pack(side="left", fill="both")

        # Fetch and display faculty data
        faculty_list = fetch_faculty()  # Fetch faculty data
        for faculty in faculty_list:
            # Insert each faculty into the Treeview
            treeview.insert("", "end", values=(faculty['username'], faculty['faculty_name'], faculty['department']))

        # Bind the Treeview selection event to update the recipient entry
        treeview.bind("<<TreeviewSelect>>", lambda event: on_faculty_select(event, treeview, recipient_entry))


    def on_faculty_select(event, treeview, recipient_entry):
        # Get selected row
        selected_item = treeview.selection()
        
        if selected_item:
            # Get the values of the selected row
            student_values = treeview.item(selected_item, "values")
            username = student_values[0]  # Assuming username is the first value in the row
            
            # Update the recipient_entry with the selected student's username
            recipient_entry.delete(0, tk.END)  # Clear the current entry content
            recipient_entry.insert(0, username)  # Insert the selected username

    def fetch_faculty():
        global db, cursor  # Use global variables for db and cursor

        if db is None or cursor is None:
            db = connect_to_db()  # Reconnect if necessary
            cursor = db.cursor()

        query = """
        SELECT u.username, s.faculty_name, s.department 
        FROM users u 
        JOIN faculty s ON u.id = s.user_id
        WHERE u.role = 'faculty'
        """

        try:
            cursor.execute(query)
            results = cursor.fetchall()  # Fetch all results

            faculty = [{'username': row[0], 'faculty_name': row[1], 'department': row[2]} for row in results]
        except mysql.connector.Error as e:
            print(f"Error fetching faculty: {e}")
            faculty = []
        finally:
            # Optionally close the cursor but keep the connection open
            # cursor.close()  # Uncomment if you want to close cursor

            return faculty

    def display_hod(right_sidebar):
        # Clear existing content in the right sidebar
        for widget in right_sidebar.winfo_children():
            widget.destroy()

        # Create a frame for the Treeview
        excel_frame = tk.Frame(right_sidebar)
        excel_frame.pack(pady=10)

        # Create the Treeview widget
        columns = ("Username", "HOD Name", "Department")
        treeview = ttk.Treeview(excel_frame, columns=columns, show="headings", height=15)

        # Define the headings
        for col in columns:
            treeview.heading(col, text=col)
            treeview.column(col, anchor="center", width=100)  # Set column width

        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(excel_frame, orient="vertical", command=treeview.yview)
        treeview.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Pack the Treeview
        treeview.pack(side="left", fill="both")

        # Fetch and display HOD data
        hod_list = fetch_hod()  # Call fetch_hod() to get updated data
        for hod in hod_list:
            # Insert each HOD into the Treeview
            treeview.insert("", "end", values=(hod['username'], hod['faculty_name'], hod['department']))
        # Bind the Treeview selection event to update the recipient entry
        treeview.bind("<<TreeviewSelect>>", lambda event: on_hod_select(event, treeview, recipient_entry))


    def on_hod_select(event, treeview, recipient_entry):
        # Get selected row
        selected_item = treeview.selection()
        
        if selected_item:
            # Get the values of the selected row
            student_values = treeview.item(selected_item, "values")
            username = student_values[0]  # Assuming username is the first value in the row
            
            # Update the recipient_entry with the selected student's username
            recipient_entry.delete(0, tk.END)  # Clear the current entry content
            recipient_entry.insert(0, username)  # Insert the selected username

    def fetch_hod():
        global db, cursor  # Use global variables for db and cursor

        if db is None or cursor is None:
            db = connect_to_db()  # Reconnect if necessary
            cursor = db.cursor()

        query = """
        SELECT u.username, s.faculty_name, s.department 
        FROM users u 
        JOIN hod s ON u.id = s.user_id
        WHERE u.role = 'hod'
        """

        try:
            cursor.execute(query)
            results = cursor.fetchall()  # Fetch all results

            hod = [{'username': row[0], 'faculty_name': row[1], 'department': row[2]} for row in results]
        except mysql.connector.Error as e:
            print(f"Error fetching HOD: {e}")
            hod = []
        finally:
            return hod

    def search_recipient(recipient_username):
        """Search for the recipient's username and display it as a clickable button."""
        for widget in recipient_button_frame.winfo_children():
            widget.destroy()  # Clear previous search results

        if not recipient_username:
            messagebox.showerror("Error", "Recipient name cannot be empty.")
            return

        try:
            # Search for recipient username in the database
            cursor.execute("SELECT username FROM users WHERE username = %s", (recipient_username,))
            result = cursor.fetchone()

            if result is None:
                messagebox.showerror("Error", "Recipient not found.")
            else:
                # Display recipient as a button if found
                recipient_button = tk.Button(header_frame, 
                                            text=f"Chat with {result[0]}", 
                                            command=lambda: open_chat_section(result[0]), 
                                            name='recipient_button', 
                                            bg='#663300',  # Set the background color to blue
                                            fg='white')  # Optional: Set the text color to white
                recipient_button.place(relx=0.55, rely=0.85, anchor='center')  # Adjust this to position to the right of the search button

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Search failed: {e}")

    def open_chat_section(recipient_username):
        """Open the chat section for the selected recipient and remove search widgets."""
        global current_recipient_username
        current_recipient_username = recipient_username  # Store the current recipient username

        # Remove search-related widgets
        try:
            recipient_entry.pack_forget()
            search_button.pack_forget()
            recipient_button_frame.pack_forget()
        except Exception as e:
            print(f"Error removing search widgets: {e}")

        # Display the chat section
        try:
            msg_text.pack(pady=10, padx=10, fill="both", expand=True)  # Display chat text widget
            msg_entry.pack(pady=5)  # Display message entry
            send_button.pack(pady=5)  # Display send button
            notification_label.pack(pady=5)  # Show unread messages label
            
            # Fetch messages between current user and recipient
            fetch_messages(recipient_username)
        except Exception as e:
            print(f"Error displaying chat section: {e}")


    def send_message(recipient_username, message):
        """Send a message to the selected recipient."""
        if not recipient_username or not message:
            messagebox.showerror("Error", "Recipient and message cannot be empty")
            return

        try:
            # Fetch sender and recipient user IDs
            cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
            sender_id = cursor.fetchone()[0]
            cursor.execute("SELECT id FROM users WHERE username = %s", (recipient_username,))
            recipient_id = cursor.fetchone()[0]

            # Insert message into the database
            cursor.execute("""
                INSERT INTO chat_messages (sender_user_id, receiver_user_id, message, timestamp, is_read)
                VALUES (%s, %s, %s, NOW(), FALSE)
                """, (sender_id, recipient_id, message))
            
            db.commit()  # Commit the message to the database

            msg_entry.delete(0, tk.END)  # Clear the message entry

            # Immediately fetch the updated messages to show the new message
            fetch_messages(recipient_username)
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Message sending failed: {e}")


    def fetch_messages(recipient_username):
        """Fetch messages between the current user and the selected recipient."""
        try:
            cursor.execute("""
                SELECT sender_user_id, message, timestamp 
                FROM chat_messages 
                WHERE (sender_user_id=(SELECT id FROM users WHERE username=%s) 
                    AND receiver_user_id=(SELECT id FROM users WHERE username=%s))
                OR (sender_user_id=(SELECT id FROM users WHERE username=%s) 
                    AND receiver_user_id=(SELECT id FROM users WHERE username=%s))
                ORDER BY timestamp ASC
                """, (username, recipient_username, recipient_username, username))
            messages = cursor.fetchall()

            msg_text.config(state="normal")
            msg_text.delete(1.0, tk.END)

            for msg in messages:
                msg_time = msg[2].strftime("%H:%M")
                message_with_time = f"{msg[1]}\n{msg_time}"

                # Determine if it's a sent or received message
                cursor.execute("SELECT id FROM users WHERE username=%s", (username,))
                user_id = cursor.fetchone()[0]

                if msg[0] == user_id:  # Sent messages
                    msg_text.insert(tk.END, f"You:\n{message_with_time}\n", 'sent')
                else:  # Received messages
                    msg_text.insert(tk.END, f"{recipient_username}:\n{message_with_time}\n", 'received')

            msg_text.tag_configure('sent', justify='right', foreground='white', background="#cc6600", font=14)
            msg_text.tag_configure('received', justify='left', foreground='black', font=14)
            msg_text.config(state="disabled")
            msg_text.yview_moveto(1)  # Scroll to the end

            # Check for unread messages and update notification
            cursor.execute("""
                SELECT COUNT(*) FROM chat_messages
                WHERE receiver_user_id=(SELECT id FROM users WHERE username=%s)
                AND sender_user_id=(SELECT id FROM users WHERE username=%s) 
                AND is_read=FALSE
                """, (username, recipient_username))
            unread_count = cursor.fetchone()[0]
            notification_label.config(text=f"Unread Messages: {unread_count}")

            # Mark messages as read
            cursor.execute("""
                UPDATE chat_messages SET is_read=TRUE
                WHERE receiver_user_id=(SELECT id FROM users WHERE username=%s)
                AND sender_user_id=(SELECT id FROM users WHERE username=%s)
                AND is_read=FALSE
                """, (username, recipient_username))
            db.commit()
        except mysql.connector.Error as e:
            print(f"Error fetching messages: {e}")


    # Global variable to track unread message status and button click state
    has_unread_messages = False
    button_clicked = False  # Variable to track button clicks

    def show_unread_messages():
        """Show unread messages in a new section."""
        global has_unread_messages, button_clicked  # Declare global to modify the global variables
        for widget in right_sidebar.winfo_children():
            widget.destroy()  # Clear previous content

        # Create a frame for the Treeview
        excel_frame = tk.Frame(right_sidebar)
        excel_frame.pack(pady=10)

        # Create the Treeview widget
        columns = ("Sender Username", "Unread Message Count", "Action")
        treeview = ttk.Treeview(excel_frame, columns=columns, show="headings", height=15)

        # Define the headings
        for col in columns:
            treeview.heading(col, text=col)
            treeview.column(col, anchor="center", width=150)  # Set column width

        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(excel_frame, orient="vertical", command=treeview.yview)
        treeview.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Pack the Treeview
        treeview.pack(side="left", fill="both")

        # Function to handle row selection
        def on_treeview_select(event):
            selected_item = treeview.selection()  # Get selected item
            if selected_item:  # If there's a selection
                item = treeview.item(selected_item)
                sender_username = item['values'][0]  # Get the sender's username
                recipient_entry.delete(0, tk.END)  # Clear current entry
                recipient_entry.insert(0, sender_username)  # Insert selected username
                
                # Reset the button color to default when a user is selected
                reset_unread_button_color()

        treeview.bind("<<TreeviewSelect>>", on_treeview_select)  # Bind selection event

        try:
            cursor.execute(""" 
                SELECT DISTINCT sender_user_id 
                FROM chat_messages 
                WHERE receiver_user_id=(SELECT id FROM users WHERE username=%s) 
                AND is_read=FALSE 
            """, (username,))
            senders = cursor.fetchall()

            if not senders:
                messagebox.showinfo("No Unread Messages", "You have no unread messages.")
                has_unread_messages = False  # No unread messages
                return

            has_unread_messages = True  # There are unread messages

            # Change button color only after the first click
            if not button_clicked:
                unread_button.config(bg='red', fg='white')  # Change button color
                button_clicked = True  # Set button click flag

            for sender_id in senders:
                cursor.execute("SELECT username FROM users WHERE id=%s", (sender_id[0],))
                sender_username = cursor.fetchone()[0]

                # Fetch the count of unread messages from this sender
                cursor.execute(""" 
                    SELECT COUNT(*) 
                    FROM chat_messages 
                    WHERE sender_user_id = %s AND receiver_user_id = (SELECT id FROM users WHERE username=%s) 
                    AND is_read = FALSE 
                """, (sender_id[0], username))
                unread_count = cursor.fetchone()[0]

                # Insert each sender into the Treeview with unread message count
                treeview.insert("", "end", values=(sender_username, unread_count, "Chat"),
                                tags=("chat",))

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Failed to fetch unread messages: {e}")

    # Reset the button color on logout or as per your application's logic
    def reset_unread_button_color():
        """Reset the unread button color when necessary."""
        global button_clicked
        unread_button.config(bg='#2e2e1f', fg='white')  # Reset to default color
        button_clicked = False  # Reset button click flag

    # Add the unread messages button
    unread_button = tk.Button(left_sidebar, text="Unread Messages", font="white", bg='#2e2e1f', width=20, height=3, command=show_unread_messages)
    unread_button.pack(pady=10)

    # Call the function to set the initial button color based on existing unread messages
    reset_unread_button_color()
    # Fetch initial messages
    fetch_messages(username)

def fetch_and_display_faculty_notifications(username, role):
    notifications_window = tk.Toplevel()
    notifications_window.title("Notifications")
    notifications_window.geometry("600x400")

    tk.Label(notifications_window, text=f"Notifications for {role} ({username})", font=('Arial', 20)).pack(pady=10)

    try:
        print(f"Fetching notifications for username: {username}, role: {role}")

        # Updated query to fetch notifications for specific username, role, or general 'all' notifications
        query = """
            SELECT id, message, created_at, is_read 
            FROM faculty_notifications 
            WHERE recipient IN (%s, %s, 'all') 
            ORDER BY created_at DESC
        """
        
        print(f"Executing query with parameters: ({username}, {role})")
        cursor.execute(query, (username, role))
        notifications = cursor.fetchall()
        
        print(f"Fetched notifications: {notifications}")


        if notifications:
            scrollable_frame = tk.Frame(notifications_window)
            scrollable_frame.pack(fill=tk.BOTH, expand=True)

            scrollbar = tk.Scrollbar(scrollable_frame)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            notifications_canvas = tk.Canvas(scrollable_frame, yscrollcommand=scrollbar.set, width=580)
            notifications_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            scrollbar.config(command=notifications_canvas.yview)

            notification_frame = tk.Frame(notifications_canvas)
            notifications_canvas.create_window((0, 0), window=notification_frame, anchor='nw', width=580)

            def update_scrollregion(event):
                notifications_canvas.configure(scrollregion=notifications_canvas.bbox("all"))

            notification_frame.bind("<Configure>", update_scrollregion)

            unread_notifications = []

            for index, (notif_id, message, created_at, is_read) in enumerate(notifications):
                notification_box = tk.Frame(notification_frame, bd=2, relief="groove", padx=10, pady=10, width=580)
                notification_box.grid(row=index, column=0, padx=10, pady=5, sticky='ew')

                bg_color = 'white' if is_read else 'lightcoral'
                notification_box.config(bg=bg_color)

                notification_frame.grid_columnconfigure(0, weight=1)

                message_label = tk.Label(notification_box, text=message, font=('Arial', 14), wraplength=500, justify="left", bg=bg_color)
                message_label.pack(anchor='w')

                date_label = tk.Label(notification_box, text=created_at.strftime("%Y-%m-%d %H:%M:%S"), font=('Arial', 12, 'italic'), anchor='e', bg=bg_color)
                date_label.pack(anchor='e')

                if not is_read:
                    unread_notifications.append(notif_id)

            if not notifications:
                print("No notifications found.")
                tk.Label(notifications_window, text="No notifications available.", font=('Arial', 14)).pack(pady=20)

            # Messages Read button
            def mark_all_as_read():
                for notif_id in unread_notifications:
                    cursor.execute("""UPDATE faculty_notifications SET is_read = TRUE WHERE id = %s""", (notif_id,))
                db.commit()
                print("All unread messages marked as read.")
                for widget in notification_frame.winfo_children():
                    widget.config(bg='white')  # Change color back to normal
                unread_notifications.clear()  # Clear the list after marking

            messages_read_button = tk.Button(notifications_window, text="Messages Read", command=mark_all_as_read)
            messages_read_button.pack(pady=10)

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        messagebox.showerror("Error", f"Failed to fetch notifications. Error: {str(err)}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
        messagebox.showerror("Error", f"An unexpected error occurred. Error: {str(e)}")

def student_dashboard_window(username, department,role):
    root = tk.Tk()
    root.title("Student Dashboard")
    root.geometry("1366x768")

    # Header Frame
    header = tk.Frame(root, height=120, bg='#1abc9c')
    header.pack(side="top", fill="x")

    # Sidebar Frame with adjusted width
    sidebar_width = 100
    sidebar = tk.Frame(root, width=sidebar_width, bg='#2c3e50')
    sidebar.pack(side="left", fill="y")

    # Main content area
    main_content = tk.Frame(root, bg='white')
    main_content.pack(side="right", expand=True, fill="both")

    # Fetch user details (name) from the database
    try:
        query = """
            SELECT s.student_name
            FROM students s
            JOIN users u ON s.user_id = u.id
            WHERE u.username = %s
        """
        cursor.execute(query, (username,))
        user_data = cursor.fetchone()

        if user_data:
            student_name = user_data[0]
        else:
            student_name = "Unknown"
            print(f"No user data found for username: {username}")
    except mysql.connector.Error as err:
        student_name = "Unknown"
        print(f"Database Error: {err}")

    # Display student details (name and department) in the header
    name_label = tk.Label(header, text=f"Name: {student_name}", font=('Arial', 16), bg='#1abc9c', fg='white')
    name_label.pack(anchor="w", padx=10, pady=10)

    dept_label = tk.Label(header, text=f"Department: {department}", font=('Arial', 16), bg='#1abc9c', fg='white')
    dept_label.pack(anchor="w", padx=10, pady=30)

    # Function to update chat button with unread message count
    def admin_update_notification_button():
        try:
            cursor.execute("""
                SELECT COUNT(*) FROM adminda_notifications 
                WHERE recipient IN (%s, 'student', 'all') AND is_read = FALSE
            """, (username,))
            unread_count = cursor.fetchone()[0]

            # Update button text and color based on unread notifications
            if unread_count > 0:
                button2.config(text=f"Admin Notifications ({unread_count})", bg="red", fg="white")
            else:
                button2.config(text="Admin Notifications", bg="#2c3e50", fg="white")

            # Check for unread notifications every 1 second
            button2.after(1000, admin_update_notification_button)  # Update every 1 second

        except mysql.connector.Error as err:
            print(f"Error: {err}")


    def principal_update_notification_button():
        try:
            cursor.execute("""
                SELECT COUNT(*) FROM principal_notifications 
                WHERE recipient IN (%s, 'student', 'all') AND is_read = FALSE
            """, (username,))
            unread_count = cursor.fetchone()[0]

            # Update button text and color based on unread notifications
            if unread_count > 0:
                button3.config(text=f"principal Notifications ({unread_count})", bg="red", fg="white")
            else:
                button3.config(text="principal Notifications", bg="#2c3e50", fg="white")

            # Check for unread notifications every 1 second
            button3.after(1000, principal_update_notification_button)  # Update every 1 second

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def accountant_update_notification_button():
        try:
            cursor.execute("""
                SELECT COUNT(*) FROM accountant_notifications 
                WHERE recipient IN (%s, 'student', 'all') AND is_read = FALSE
            """, (username,))
            unread_count = cursor.fetchone()[0]

            # Update button text and color based on unread notifications
            if unread_count > 0:
                button4.config(text=f"accountnat Notifications ({unread_count})", bg="red", fg="white")
            else:
                button4.config(text="accountant Notifications", bg="#2c3e50", fg="white")

            # Check for unread notifications every 1 second
            button4.after(1000, accountant_update_notification_button)  # Update every 1 second

        except mysql.connector.Error as err:
            print(f"Error: {err}")


    def hod_update_notification_button():
        try:
            cursor.execute("""
                SELECT COUNT(*) FROM hod_notifications 
                WHERE recipient IN (%s, 'student', 'all') AND is_read = FALSE
            """, (username,))
            unread_count = cursor.fetchone()[0]

            # Update button text and color based on unread notifications
            if unread_count > 0:
                button5.config(text=f"hod Notifications ({unread_count})", bg="red", fg="white")
            else:
                button5.config(text="hod Notifications", bg="#2c3e50", fg="white")

            # Check for unread notifications every 1 second
            button5.after(1000, hod_update_notification_button)  # Update every 1 second

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def faculty_update_notification_button():
        try:
            cursor.execute("""
                SELECT COUNT(*) FROM faculty_notifications 
                WHERE recipient IN (%s, 'student', 'all') AND is_read = FALSE
            """, (username,))
            unread_count = cursor.fetchone()[0]

            # Update button text and color based on unread notifications
            if unread_count > 0:
                button6.config(text=f"faculty Notifications ({unread_count})", bg="red", fg="white")
            else:
                button6.config(text="faculty Notifications", bg="#2c3e50", fg="white")

            # Check for unread notifications every 1 second
            button6.after(1000, faculty_update_notification_button)  # Update every 1 second

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    # Function to load content dynamically
    def load_content(page_name):
        for widget in main_content.winfo_children():
            widget.destroy()

        if page_name == "Chat":
            open_chat_sidebar(username, department, root)
        elif page_name == "Notifications":
            tk.Label(main_content, text="Notifications Section", font=('Arial', 24)).pack(pady=20)
        elif page_name == "Logout":
            root.destroy()
        elif page_name == "view":
            open_student_view_window()
        else:
            tk.Label(main_content, text=f"Welcome to {page_name}", font=('Arial', 24)).pack(pady=20)

    def on_enter(e):
        e.widget['background'] = '#ADD8E6'  # Light blue on hover

    def on_leave(e):
        e.widget['background'] = '#00008B'  # Dark blue when not hovered

    def open_student_view_window():
        # Clear the content of the main_content window
        for widget in main_content.winfo_children():
            widget.destroy()

        page7_frame = tk.Frame(main_content, bg='white')
        page7_frame.pack(expand=True, fill='both')

        # Page 7 header
        tk.Label(page7_frame, text="Student View", font=('Arial', 24)).pack(pady=20)

        # Login Button
        login_button = tk.Button(page7_frame, text="Login to View Details", font=('Arial', 16), width=20, height=2,
                                bg='darkblue', fg='white', activebackground='lightblue', command=open_login_window)
        login_button.pack(pady=20)

    def open_login_window():
        # Create a new window for login
        login_window = tk.Toplevel(root ,background="#1f1f2e")
        login_window.title("Student Login")
        login_window.geometry("300x400")

        tk.Label(login_window, text="Username",background="#1f1f2e",foreground="white").pack(pady=5)
        username_entry = tk.Entry(login_window)
        username_entry.pack(pady=5)

        tk.Label(login_window, text="Password",background="#1f1f2e",foreground="white").pack(pady=5)
        password_entry = tk.Entry(login_window, show="*")
        password_entry.pack(pady=5)

        # Button to verify login credentials
        tk.Button(login_window, text="Login", background="#9595b7",command=lambda: verify_login(username_entry.get(), password_entry.get(), login_window)).pack(pady=10)

    def verify_login(username, password, login_window):
        sql_query = "SELECT id FROM users WHERE username = %s AND password = %s"
        try:
            cursor.execute(sql_query, (username, password))
            result = cursor.fetchone()

            if result:
                user_id = result[0]
                login_window.destroy()  # Close login window on successful login
                view_student_details_by_user(user_id)  # Fetch and display student details for the logged-in user
            else:
                messagebox.showerror("Login Failed", "Invalid username or password.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error occurred: {err}")

    def view_student_details_by_user(user_id):
        # Clear the content of the main_content window
        for widget in main_content.winfo_children():
            widget.destroy()

        # Create a new frame for student details with specific size and padding
        details_frame = tk.Frame(main_content, bg='white', width=1100, height=400)  # Set desired width and height
        details_frame.pack(expand=False, padx=20, pady=20, ipadx=10, ipady=10)  # Add padding and internal padding

        # Ensure that the frame resizes according to its content (optional)
        details_frame.pack_propagate(False)

        # Back button to return to the previous page
        back_button = tk.Button(details_frame, text="Back",  bg='blue', fg='white' ,font=('Arial', 14), command=open_student_view_window)
        back_button.pack(pady=10, anchor='w')

        # Scrollbars
        tree_scroll_y = ttk.Scrollbar(details_frame, orient="vertical")
        tree_scroll_x = ttk.Scrollbar(details_frame, orient="horizontal")

        # SQL Query to fetch student details by user_id
        sql_query = """
            SELECT s.student_id, u.username, s.student_name, s.admission_date, s.department, s.semester, 
                s.admission_number, s.roll_no, s.gender, s.dob, s.blood_group, s.father_name, 
                s.father_occupation, s.mother_name, s.mother_occupation, s.address, s.city, s.country, 
                s.religion, s.caste, s.pin_code, s.state, s.email, s.phone, s.parent_phone, s.guardian_name, 
                s.guardian_relationship, s.guardian_phone, s.guardian_address, s.photo_path
            FROM students s
            JOIN users u ON s.user_id = u.id
            WHERE u.id = %s
        """

        try:
            cursor.execute(sql_query, (user_id,))
            student_detail = cursor.fetchone()  # Fetch the logged-in student's details

            if student_detail:
                columns = [
                    "Student ID", "Username", "Student Name", "Admission Date", "Department", 
                    "Semester", "Admission Number", "Roll No", "Gender", "DOB", "Blood Group", 
                    "Father's Name", "Father's Occupation", "Mother's Name", 
                    "Mother's Occupation", "Address", "City", "Country", "Religion", 
                    "Caste", "Pin Code", "State", "Email", "Phone", 
                    "Parent Phone", "Guardian Name", "Guardian Relationship", 
                    "Guardian Phone", "Guardian Address", "Photo Path"
                ]

                # Create Treeview widget with scrollbars
                tree = ttk.Treeview(details_frame, columns=columns, show="headings", 
                                    height=5,  # Reduced height for a smaller table
                                    yscrollcommand=tree_scroll_y.set, 
                                    xscrollcommand=tree_scroll_x.set)

                tree_scroll_y.config(command=tree.yview)
                tree_scroll_x.config(command=tree.xview)

                tree_scroll_y.pack(side="right", fill="y")
                tree_scroll_x.pack(side="bottom", fill="x")
                tree.pack(expand=True, fill='both')

                # Define column headings and smaller widths
                for col in columns:
                    tree.heading(col, text=col)
                    tree.column(col, width=120, anchor='center')  # Adjusted width for smaller columns

                # Insert student details into Treeview
                tree.insert("", "end", values=student_detail)

                # Update button to allow for editing student details
                update_button = tk.Button(details_frame, text="Update", bg='blue', fg='white', font=('Arial', 14), command=lambda: update_student(user_id, student_detail))
                update_button.pack(pady=10)  # Add some padding for visual separation

            else:
                tk.Label(details_frame, text="No student details found.", font=('Arial', 14), fg='red').pack(pady=10)

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to retrieve student details: {err}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def update_student(user_id, student_detail):
        # Create a new window for updating student details
        update_window = tk.Toplevel(main_content,background="#a3a375")
        update_window.title("Update Student Details")
        update_window.geometry("800x600")  # Adjust width to accommodate two columns

        # Labels and Entry fields for each detail
        labels = [
            "Student ID", "Username", "Student Name", "Admission Date", "Department", 
            "Semester", "Admission Number", "Roll No", "Gender", "DOB", "Blood Group", 
            "Father's Name", "Father's Occupation", "Mother's Name", 
            "Mother's Occupation", "Address", "City", "Country", "Religion", 
            "Caste", "Pin Code", "State", "Email", "Phone", 
            "Parent Phone", "Guardian Name", "Guardian Relationship", 
            "Guardian Phone", "Guardian Address", "Photo Path"
        ]

        entries = []

        for i, label in enumerate(labels):
            # Calculate the row and column for two-layer layout
            row = i // 2  # Row index
            col = i % 2   # Column index (0 or 1)
            
            tk.Label(update_window, text=label,background="#a3a375").grid(row=row, column=col * 2, padx=10, pady=5, sticky='e')
            entry = tk.Entry(update_window, width=40)  # Set width for entries
            entry.grid(row=row, column=col * 2 + 1, padx=10, pady=5)
            entry.insert(0, student_detail[i])  # Fill entry with current details
            entries.append(entry)

        def save_changes():
            # Collect updated details from the entry fields
            updated_details = [entry.get() for entry in entries]

            # Debugging: Check if we collected the correct number of details
            print(f"Updated details: {updated_details}")
            print(f"Number of updated details collected: {len(updated_details)}")  # Should be 30

            # Check if entries list has the expected number of values (30 in this case)
            if len(updated_details) != 30:
                messagebox.showerror("Error", f"Expected 30 fields but got {len(updated_details)}.")
                return  # Stop execution if the entry collection is wrong

            # Assuming student_detail holds the current student's details, including student_id
            student_id = student_detail[0]  # Ensure this is correct
            print(f"Student ID: {student_id}")

            # SQL query to update student details
            update_query = """
                UPDATE students SET
                    username = %s, student_name = %s, admission_date = %s, department = %s,
                    semester = %s, admission_number = %s, roll_no = %s, gender = %s,
                    dob = %s, blood_group = %s, father_name = %s, father_occupation = %s,
                    mother_name = %s, mother_occupation = %s, address = %s, city = %s,
                    country = %s, religion = %s, caste = %s, pin_code = %s,
                    state = %s, email = %s, phone = %s, parent_phone = %s,
                    guardian_name = %s, guardian_relationship = %s, guardian_phone = %s,
                    guardian_address = %s, photo_path = %s
                WHERE student_id = %s
            """

            # Combine updated details with student_id for the WHERE clause
            parameters = (*updated_details, student_id)

            # Debugging: Check the SQL query and number of parameters passed
            print(f"SQL Query: {update_query}")
            print(f"Parameters: {parameters}")
            print(f"Number of parameters passed: {len(parameters)}")  # Should be 31

            # Check if parameters length matches the number of placeholders (31 in this case)
            if len(parameters) != 31:
                messagebox.showerror("Error", f"Expected 31 parameters but got {len(parameters)}.")
                return  # Stop execution if parameters length is wrong

            try:
                # Ensure that `cursor` and `conn` are initialized before
                cursor.execute(update_query, parameters)
                commit_changes()  # Ensure commit_changes() commits the transaction correctly
                messagebox.showinfo("Success", "Student details updated successfully.")
                update_window.destroy()  # Close the update window after saving
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Failed to update student details: {err}")
            except Exception as e:
                messagebox.showerror("Error", f"An unexpected error occurred: {e}")


        # Function for saving changes
        save_button = tk.Button(update_window, text="Save Changes", command=save_changes, 
                                bg='blue', fg='white', font=("Helvetica", 12))
        save_button.grid(row=(len(labels)//2)+1, column=0, columnspan=2, pady=10)  # Moved to a separate row

        def commit_changes():
            try:
                # Use the same connection to commit changes
                cursor.execute("COMMIT")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while committing changes: {str(e)}")

        def delete_student(username):
            # Confirmation dialog
            if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this student?"):
                for attempt in range(3):  # Retry up to 3 times
                    try:
                        # Fetch the user's ID using the username
                        cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
                        user_id = cursor.fetchone()
                        
                        if user_id:
                            user_id = user_id[0]
                            # Delete the student from the students table
                            cursor.execute("DELETE FROM students WHERE user_id = %s", (user_id,))
                            # Delete the user from the users table
                            cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
                            commit_changes()  # Call the commit function
                            messagebox.showinfo("Success", "Student deleted successfully.")
                            login_window()  # Go back to the previous page after deletion
                            return  # Exit the function after successful deletion
                        else:
                            messagebox.showerror("Error", "User not found.")
                        break  # Exit the retry loop if the user is found
                    except Exception as e:
                        if "Lock wait timeout exceeded" in str(e):
                            if attempt < 2:  # Retry only if we haven't exhausted attempts
                                time.sleep(1)  # Wait before retrying
                            else:
                                messagebox.showerror("Error", f"An error occurred while deleting the student: {str(e)}")
                        else:
                            messagebox.showerror("Error", f"An error occurred while deleting the student: {str(e)}")
                            
        delete_button = tk.Button(update_window, text="Delete My Account", 
                                command=lambda: delete_student(username),  # Use lambda to pass the username
                                bg='blue', fg='white', font=("Helvetica", 12))
        delete_button.grid(row=(len(labels)//2)+1, column=3, columnspan=2, pady=10)  # Positioned right below the Save button


    # Sidebar buttons
    button1 = tk.Button(sidebar, width=12, text='  Chat  ', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button1.pack(fill='x')
    button1.config(command=lambda: open_chat_sidebar(username, department, root,role))  # Replace 'student_username' with actual username
    button1.bind("<Enter>", lambda event: button1.configure(bg='blue'))
    button1.bind("<Leave>", lambda event: button1.configure(bg='#2c3e50'))

    button2 = tk.Button(sidebar, text=' Admin Notifications  ', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button2.pack(fill='x')
    button2.config(command=lambda: fetch_and_display_notifications(username,"student"))  # Replace 'student_username' with actual username
    button2.bind("<Enter>", lambda event: button2.configure(bg='blue'))
    button2.bind("<Leave>", lambda event: button2.configure(bg='#2c3e50'))

    button3 = tk.Button(sidebar, text='principal notification', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button3.pack(fill='x')
    button3.config(command=lambda: fetch_and_display_principal_notifications(username,"student"))
    button3.bind("<Enter>", lambda event: button3.configure(bg='blue'))
    button3.bind("<Leave>", lambda event: button3.configure(bg='#2c3e50'))

    button4 = tk.Button(sidebar, text='accountant notification', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button4.pack(fill='x')
    button4.config(command=lambda: fetch_and_display_accountant_notifications(username,"student"))
    button4.bind("<Enter>", lambda event: button4.configure(bg='blue'))
    button4.bind("<Leave>", lambda event: button4.configure(bg='#2c3e50'))

    button5 = tk.Button(sidebar, text='hod notification', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button5.pack(fill='x')
    button5.config(command=lambda: fetch_and_display_hod_notifications(username,"student"))
    button5.bind("<Enter>", lambda event: button5.configure(bg='blue'))
    button5.bind("<Leave>", lambda event: button5.configure(bg='#2c3e50'))

    button6 = tk.Button(sidebar, text='faculty notification', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button6.pack(fill='x')
    button6.config(command=lambda: fetch_and_display_faculty_notifications(username,"student"))
    button6.bind("<Enter>", lambda event: button6.configure(bg='blue'))
    button6.bind("<Leave>", lambda event: button6.configure(bg='#2c3e50'))

    button7 = tk.Button(sidebar, text='view', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button7.pack(fill='x')
    button7.config(command=lambda: load_content('view'))
    button7.bind("<Enter>", lambda event: button7.configure(bg='blue'))
    button7.bind("<Leave>", lambda event: button7.configure(bg='#2c3e50'))

    button8 = tk.Button(sidebar, text='Back', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button8.pack(fill='x')
    button8.config(command=lambda: switch_window(root,login_window))
    button8.bind("<Enter>", lambda event: button8.configure(bg='blue'))
    button8.bind("<Leave>", lambda event: button8.configure(bg='#2c3e50'))

        # Initial call to set the notification button based on unread messages
    admin_update_notification_button()
    
    principal_update_notification_button()

    accountant_update_notification_button()

    hod_update_notification_button()

    faculty_update_notification_button()
    
    root.mainloop()

def faculty_dashboard_window(username, department,role):
    root = tk.Tk()
    root.title("Faculty Dashboard")
    root.geometry("1368x766")

    # Header Frame
    header = tk.Frame(root, height=120, bg='#00cccc')
    header.pack(side="top", fill="x")

    # Sidebar Frame with adjusted width
    sidebar_width = 100
    sidebar = tk.Frame(root, width=sidebar_width, bg='#2c3e50')
    sidebar.pack(side="left", fill="y")

    # Main content area
    main_content = tk.Frame(root, bg='white')
    main_content.pack(side="right", expand=True, fill="both")
    # Fetch user details (name) from the database
    try:
        query = """
            SELECT s.faculty_name
            FROM faculty s
            JOIN users u ON s.user_id = u.id
            WHERE u.username = %s
        """
        cursor.execute(query, (username,))
        user_data = cursor.fetchone()

        if user_data:
            faculty_name = user_data[0]
        else:
            faculty_name = "Unknown"
            print(f"No user data found for username: {username}")
    except mysql.connector.Error as err:
        faculty_name = "Unknown"
        print(f"Database Error: {err}")

    # Display student details (name and department) in the header
    name_label = tk.Label(header, text=f"Name: {faculty_name}", font=('Arial', 16), bg='#00cccc', fg='white')
    name_label.pack(anchor="w", padx=10, pady=10)

    dept_label = tk.Label(header, text=f"Department: {department}", font=('Arial', 16), bg='#00cccc', fg='white')
    dept_label.pack(anchor="w", padx=10, pady=30)

    def load_content(page_name):
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        if page_name == "Logout":
            root.destroy()
            # test()  # Uncomment if needed
        elif page_name == "User Details":
            create_page5_content()  # Load buttons for roles
        else:
            tk.Label(main_content, text=f"Welcome to {page_name}", font=('Arial', 24)).pack(pady=20)
    def update_chat_button():
        try:
            # Query to check how many unread messages the user has
            cursor.execute("""
            SELECT COUNT(*) FROM chat_messages
            WHERE receiver_user_id=(SELECT id FROM users WHERE username=%s) AND is_read=FALSE
            """, (username,))
            unread_count = cursor.fetchone()[0]

            # Debug print for checking unread count
            print(f"Unread count for {username}: {unread_count}")

            # If unread messages exist, update the button to show red color and count
            if unread_count > 0:
                button1.config(text=f"Chat ({unread_count})", bg="red", fg="white")
            else:
                button1.config(text="Chat", bg="#2c3e50", fg="white")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        # Call the function again after 2 seconds to keep checking for updates
        button1.after(2000, update_chat_button)


    def admin_update_notification_button():
        try:
            cursor.execute("""
                SELECT COUNT(*) FROM adminda_notifications 
                WHERE recipient IN (%s, 'faculty', 'all') AND is_read = FALSE
            """, (username,))
            unread_count = cursor.fetchone()[0]

            # Update button text and color based on unread notifications
            if unread_count > 0:
                button2.config(text=f"Admin Notifications ({unread_count})", bg="red", fg="white")
            else:
                button2.config(text="Admin Notifications", bg="#2c3e50", fg="white")

            # Check for unread notifications every 1 second
            button2.after(1000, admin_update_notification_button)  # Update every 1 second

        except mysql.connector.Error as err:
            print(f"Error: {err}")


    def principal_update_notification_button():
        try:
            cursor.execute("""
                SELECT COUNT(*) FROM principal_notifications 
                WHERE recipient IN (%s, 'faculty', 'all') AND is_read = FALSE
            """, (username,))
            unread_count = cursor.fetchone()[0]

            # Update button text and color based on unread notifications
            if unread_count > 0:
                button3.config(text=f"principal Notifications ({unread_count})", bg="red", fg="white")
            else:
                button3.config(text="principal Notifications", bg="#2c3e50", fg="white")

            # Check for unread notifications every 1 second
            button3.after(1000, principal_update_notification_button)  # Update every 1 second

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def accountant_update_notification_button():
        try:
            cursor.execute("""
                SELECT COUNT(*) FROM accountant_notifications 
                WHERE recipient IN (%s, 'faculty', 'all') AND is_read = FALSE
            """, (username,))
            unread_count = cursor.fetchone()[0]

            # Update button text and color based on unread notifications
            if unread_count > 0:
                button4.config(text=f"accountnat Notifications ({unread_count})", bg="red", fg="white")
            else:
                button4.config(text="accountant Notifications", bg="#2c3e50", fg="white")

            # Check for unread notifications every 1 second
            button4.after(1000, accountant_update_notification_button)  # Update every 1 second

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def hod_update_notification_button():
        try:
            cursor.execute("""
                SELECT COUNT(*) FROM hod_notifications 
                WHERE recipient IN (%s, 'faculty', 'all') AND is_read = FALSE
            """, (username,))
            unread_count = cursor.fetchone()[0]

            # Update button text and color based on unread notifications
            if unread_count > 0:
                button5.config(text=f"hod Notifications ({unread_count})", bg="red", fg="white")
            else:
                button5.config(text="hod Notifications", bg="#2c3e50", fg="white")

            # Check for unread notifications every 1 second
            button5.after(1000, hod_update_notification_button)  # Update every 1 second

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def open_faculty_notification_interface():
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="Enter Notification Message:", font=('Arial', 14), bg="white").pack(pady=20)
        notification_entry = tk.Text(main_content, height=5, width=50)
        notification_entry.pack(pady=10)

        tk.Label(main_content, text="Select Recipients:", font=('Arial', 14), bg="white").pack(pady=10)
        role_var = tk.StringVar(value="all")
        roles = ["all", "student", "hod"]

        selected_role_label = tk.Label(main_content, text="", font=('Arial', 14), bg="white")
        selected_role_label.pack(pady=10)

        def on_role_change(*args):
            selected_role = role_var.get()
            selected_role_label.config(text=f"Selected Role: {selected_role.capitalize()}")

        role_dropdown = tk.OptionMenu(main_content, role_var, *roles, command=on_role_change)
        role_dropdown.pack(pady=10)

        def send_notification():
            notification_message = notification_entry.get("1.0", "end").strip()
            selected_role = role_var.get()

            if not notification_message:
                messagebox.showerror("Error", "Notification message cannot be empty.")
                return

            try:
                recipients = []
                if selected_role == "all":
                    cursor.execute("SELECT username FROM users")
                else:
                    cursor.execute("SELECT username FROM users WHERE role = %s", (selected_role,))
                recipients = cursor.fetchall()

                # Admin user (if applicable)
                faculty_username = 'faculty'
                if selected_role == "all" or selected_role in ["student", "hod"]:
                    recipients = [(faculty_username,)] + recipients if (faculty_username,) not in recipients else recipients

                if recipients:
                    for recipient in recipients:
                        cursor.execute(
                            "INSERT INTO faculty_notifications (message, sender, recipient) VALUES (%s, %s, %s)",
                            (notification_message, faculty_username, recipient[0])
                        )
                    db.commit()
                    messagebox.showinfo("Success", f"Notification sent to all {selected_role.capitalize()}s.")
                else:
                    messagebox.showinfo("Info", f"No {selected_role.capitalize()}s found to send notifications.")

                notification_entry.delete("1.0", "end")

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Failed to send notification. Error: {str(err)}")

        tk.Button(main_content, text="Send Notification", command=send_notification, font=('Arial', 14),
                  bg='#1abc9c', fg='white').pack(pady=20)

    def group_chat_button(username):
        try:
            # Query to count unread messages for the current user in the group chat
            cursor.execute("""
                SELECT COUNT(*) FROM groupp_chat_messages 
                WHERE receiver_user_id IS NULL AND is_read = FALSE
            """)
            unread_count = cursor.fetchone()[0]

            # Update button text and color based on unread messages
            if unread_count > 0:
                button7.config(text=f"Group Chat ({unread_count})", bg="red", fg="white")
            else:
                button7.config(text="Group Chat", bg="#2c3e50", fg="white")

            # Check for unread messages every 1 second
            button7.after(1000, group_chat_button, username)  # Update every 1 second

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def on_group_chat_click(username, main_content):
        # Open the group chat sidebar
        open_group_chat_sidebar(username, main_content)

        # Reset the button color to its normal state after clicking
        button7.config(bg="#2c3e50", fg="white")

        # Optionally, mark all unread messages as read
        try:
            cursor.execute("""
                UPDATE groupp_chat_messages 
                SET is_read = TRUE 
                WHERE receiver_user_id IS NULL AND is_read = FALSE
            """)
            db.commit()
        except mysql.connector.Error as err:
            print(f"Error marking messages as read: {err}")

#################################################################################################################

    def create_page5_content():
        # Create a new content for Page 5
        page5_content = tk.Frame(main_content, bg='white')
        page5_content.pack(expand=True, fill="both")

        tk.Label(page5_content, text="View Details", font=('Arial', 24)).pack(pady=20)

        button_width = 20  # Set desired width
        button_height = 2  # Set desired height
        dark_green = '#006400'  # Dark green color
        light_green = '#90EE90'  # Light green color (for active background)

        student_button = tk.Button(page5_content, text='Students', font=('Arial', 14), bg=dark_green, fg='white',
                                width=button_width, height=button_height, activebackground=light_green, command=open_student_window)
        student_button.pack(pady=10, padx=20)

        my_button = tk.Button(page5_content, text='My Account', font=('Arial', 14), bg=dark_green, fg='white',
                                width=button_width, height=button_height, activebackground=light_green, command=open_faculty_view_window)
        my_button.pack(pady=10, padx=20)

    def open_faculty_view_window():
        # Clear the content of the main_content window
        for widget in main_content.winfo_children():
            widget.destroy()

        page7_frame = tk.Frame(main_content, bg='white')
        page7_frame.pack(expand=True, fill='both')

        # Page 7 header
        tk.Label(page7_frame, text="Faculty View", font=('Arial', 24)).pack(pady=20)

        # Login Button
        login_button = tk.Button(page7_frame, text="Login to View Details", font=('Arial', 16), width=20, height=2,
                                bg='darkblue', fg='white', activebackground='lightblue', command=open_faculty_login_window)
        login_button.pack(pady=20)

    def open_faculty_login_window():
        # Create a new window for login
        login_window = tk.Toplevel(root ,background="#1f1f2e")
        login_window.title("Faculty Login")
        login_window.geometry("300x400")

        tk.Label(login_window, text="Username",background="#1f1f2e",foreground="white").pack(pady=5)
        username_entry = tk.Entry(login_window)
        username_entry.pack(pady=5)

        tk.Label(login_window, text="Password",background="#1f1f2e",foreground="white").pack(pady=5)
        password_entry = tk.Entry(login_window, show="*")
        password_entry.pack(pady=5)

        # Button to verify login credentials
        tk.Button(login_window, text="Login", background="#9595b7",command=lambda: verify_login(username_entry.get(), password_entry.get(), login_window)).pack(pady=10)

    def verify_login(username, password, login_window):
        sql_query = "SELECT id FROM users WHERE username = %s AND password = %s"
        try:
            cursor.execute(sql_query, (username, password))
            result = cursor.fetchone()

            if result:
                user_id = result[0]
                login_window.destroy()  # Close login window on successful login
                view_faculty_details_by_user(user_id)  # Fetch and display student details for the logged-in user
            else:
                messagebox.showerror("Login Failed", "Invalid username or password.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error occurred: {err}")

    def view_faculty_details_by_user(user_id):
        # Clear the content of the main_content window
        for widget in main_content.winfo_children():
            widget.destroy()

        # Create a new frame for student details with specific size and padding
        details_frame = tk.Frame(main_content, bg='white', width=1100, height=400)  # Set desired width and height
        details_frame.pack(expand=False, padx=20, pady=20, ipadx=10, ipady=10)  # Add padding and internal padding

        # Ensure that the frame resizes according to its content (optional)
        details_frame.pack_propagate(False)

        # Back button to return to the previous page
        back_button = tk.Button(details_frame, text="Back",  bg='blue', fg='white' ,font=('Arial', 14), command=open_faculty_view_window)
        back_button.pack(pady=10, anchor='w')

        # Scrollbars
        tree_scroll_y = ttk.Scrollbar(details_frame, orient="vertical")
        tree_scroll_x = ttk.Scrollbar(details_frame, orient="horizontal")

        # SQL Query to fetch faculty details by user_id
        sql_query = """
            SELECT f.faculty_id, u.username, f.faculty_name, f.department, f.faculty_gender, f.faculty_dob, 
                f.faculty_blood_group, f.faculty_marital_status, f.faculty_job_position, f.faculty_address, 
                f.faculty_city, f.faculty_country, f.faculty_pin_code, f.faculty_state, f.faculty_email, 
                f.faculty_phone, f.faculty_guardian_name, f.faculty_guardian_relationship, 
                f.faculty_guardian_phone, f.faculty_guardian_address, f.photo_path
            FROM faculty f
            JOIN users u ON f.user_id = u.id
            WHERE u.id = %s
        """

        try:
            cursor.execute(sql_query, (user_id,))
            faculty_detail = cursor.fetchone()  # Fetch the logged-in faculty's details

            if faculty_detail:
                columns = [
                    "Faculty ID", "Username", "Faculty Name", "Department", "Gender", "DOB", "Blood Group", 
                    "Marital Status", "Job Position", "Address", "City", "Country", "Pin Code", "State", 
                    "Email", "Phone", "Guardian Name", "Guardian Relationship", "Guardian Phone", 
                    "Guardian Address", "Photo Path"
                ]

                # Create Treeview widget with scrollbars
                tree = ttk.Treeview(details_frame, columns=columns, show="headings", 
                                    height=5,  # Reduced height for a smaller table
                                    yscrollcommand=tree_scroll_y.set, 
                                    xscrollcommand=tree_scroll_x.set)

                tree_scroll_y.config(command=tree.yview)
                tree_scroll_x.config(command=tree.xview)

                tree_scroll_y.pack(side="right", fill="y")
                tree_scroll_x.pack(side="bottom", fill="x")
                tree.pack(expand=True, fill='both')

                # Define column headings and smaller widths
                for col in columns:
                    tree.heading(col, text=col)
                    tree.column(col, width=120, anchor='center')  # Adjusted width for smaller columns

                # Insert student details into Treeview
                tree.insert("", "end", values=faculty_detail)

                # Update button to allow for editing student details
                update_button = tk.Button(details_frame, text="Delete My Account", bg='blue', fg='white', font=('Arial', 14), command=lambda: delete_faculty(username ))
                update_button.pack(pady=10)  # Add some padding for visual separation

            else:
                tk.Label(details_frame, text="No faculty details found.", font=('Arial', 14), fg='red').pack(pady=10)

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to retrieve faculty details: {err}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

        def commit_changes():
            try:
                # Use the same connection to commit changes
                cursor.execute("COMMIT")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while committing changes: {str(e)}")

        def delete_faculty(username):
            # Confirmation dialog
            if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this Account?"):
                for attempt in range(3):  # Retry up to 3 times
                    try:
                        # Fetch the user's ID using the username
                        cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
                        user_id = cursor.fetchone()
                        
                        if user_id:
                            user_id = user_id[0]
                            # Delete the student from the students table
                            cursor.execute("DELETE FROM faculty WHERE user_id = %s", (user_id,))
                            # Delete the user from the users table
                            cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
                            commit_changes()  # Call the commit function
                            messagebox.showinfo("Success", "faculty deleted successfully.")
                            login_window()  # Go back to the previous page after deletion
                            return  # Exit the function after successful deletion
                        else:
                            messagebox.showerror("Error", "User not found.")
                        break  # Exit the retry loop if the user is found
                    except Exception as e:
                        if "Lock wait timeout exceeded" in str(e):
                            if attempt < 2:  # Retry only if we haven't exhausted attempts
                                time.sleep(1)  # Wait before retrying
                            else:
                                messagebox.showerror("Error", f"An error occurred while deleting the faculty: {str(e)}")
                        else:
                            messagebox.showerror("Error", f"An error occurred while deleting the faculty: {str(e)}")
                            
###############################################################################333
    def open_student_window():
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=back_to_page5,
                                bg='#8B008B', fg='white', width=25, height=3,
                                activebackground='#DDA0DD')  # Dark magenta background, light magenta on click
        back_button.pack(pady=10)

        view_button = tk.Button(main_content, text='View All Students', font=('Arial', 14), command=view_students,
                                bg='#8B008B', fg='white', width=25, height=3,
                                activebackground='#DDA0DD')  # Dark magenta background, light magenta on click
        view_button.pack(pady=10)

    def open_student_details(username):
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="Student Details", font=('Arial', 24)).pack(pady=20)

        # Create a frame for the Treeview and scrollbar with the specified size
        detail_frame = tk.Frame(main_content)
        detail_frame.pack(pady=10)

        # Set the size of the frame using the grid geometry manager
        detail_frame.grid_propagate(False)  # Prevent the frame from resizing to fit contents
        detail_frame.config(width=1100, height=500)

        # Create a Treeview widget for student details
        columns = ("Field", "Details")
        tree = ttk.Treeview(detail_frame, columns=columns, show="headings")
        tree.pack(side='left', fill='both', expand=True)

        # Configure the column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=250)  # Adjust width as needed

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(detail_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscroll=scrollbar.set)

        try:
            # Fetch student details for the given username
            cursor.execute("""
                SELECT s.student_id, s.student_name, u.username, u.role, 
                    s.admission_date, s.department, s.semester, 
                    s.admission_number, s.roll_no, s.gender, s.dob, 
                    s.blood_group, s.father_name, s.father_occupation, 
                    s.mother_name, s.mother_occupation, s.address, 
                    s.city, s.country, s.religion, s.caste, 
                    s.pin_code, s.state, s.email, s.phone, 
                    s.parent_phone, s.guardian_name, 
                    s.guardian_relationship, s.guardian_phone, 
                    s.guardian_address 
                FROM students s 
                JOIN users u ON s.user_id = u.id 
                WHERE u.username = %s
            """, (username,))
            student = cursor.fetchone()

            if not student:
                messagebox.showinfo("Info", "No student details found for this username.")
                return

            # Display student details in the Treeview
            field_labels = [
                "Student ID", "Student Name", "Username", "Role",
                "Admission Date", "Department", "Semester", 
                "Admission Number", "Roll No", "Gender", "DOB", 
                "Blood Group", "Father's Name", "Father's Occupation", 
                "Mother's Name", "Mother's Occupation", "Address", 
                "City", "Country", "Religion", "Caste", 
                "Pin Code", "State", "Email", "Phone", 
                "Parent Phone", "Guardian Name", 
                "Guardian Relationship", "Guardian Phone", 
                "Guardian Address"
            ]
            
            # Insert student details into the Treeview
            for label, value in zip(field_labels, student):
                tree.insert("", tk.END, values=(label, value))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        # Back button to return to the previous page
        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=view_students, bg='blue', fg='white')
        back_button.pack(side='left', padx=10, pady=10)

    def show_login_window():
        # Create a new window for login
        login_window = tk.Toplevel()
        login_window.title("Login")

        tk.Label(login_window, text="Enter Username:", font=('Arial', 14)).pack(pady=10)

        username_entry = tk.Entry(login_window, font=('Arial', 14))
        username_entry.pack(pady=10)

        def on_login():
            username = username_entry.get()
            if username:
                cursor.execute("SELECT role FROM users WHERE username = %s", (username,))
                role = cursor.fetchone()

                if role and role[0] == 'student':
                    open_student_details(username)
                    login_window.destroy()  # Close the login window
                else:
                    messagebox.showerror("Error", "Username does not belong to a student.")
            else:
                messagebox.showwarning("Warning", "Please enter a username.")

        login_button = tk.Button(login_window, text="Login", font=('Arial', 14), command=on_login)
        login_button.pack(pady=10)
    # Declare the tree variable globally
    
    tree = None
    def view_students():
        global tree  # Declare the tree variable as global

        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="All Student Details", font=('Arial', 24)).pack(pady=20)

        # Create a frame for the Treeview and scrollbar
        student_frame = tk.Frame(main_content)
        student_frame.pack(pady=10)

        # Create a Treeview widget for listing students
        columns = ("Student ID", "Student Name", "Username", "Role", "Department", "Semester")
        tree = ttk.Treeview(student_frame, columns=columns, show="headings")
        tree.pack(side='left', fill='both', expand=True)

        # Configure the column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=150)  # Adjust width as needed

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(student_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscroll=scrollbar.set)

        # Set a minimum size for the Treeview frame
        student_frame.configure(width=1100, height=400)

        # Create a frame for the department and semester selection
        selection_frame = tk.Frame(main_content)
        selection_frame.pack(pady=20)

        # Create a StringVar to hold the selected department
        department_var = tk.StringVar()
        
        # Create a StringVar to hold the selected semester
        semester_var = tk.StringVar()

        # Create a frame for department section (combobox and button)
        department_frame = tk.Frame(selection_frame)
        department_frame.pack(side='left', padx=20)

        # Create a Combobox for department selection
        department_var = ttk.Combobox(department_frame, textvariable=department_var, font=("Helvetica", 12), state='readonly')
        department_var['values'] = [
            "B.E Civil Engineering",
            "B.E Computer Science Engineering",
            "B.E Electrical and Electronics Engineering",
            "B.E Electronics and Communication Engineering",
            "B.Tech Information Technology",
            "B.E Mechanical Engineering",
            "B.Tech Artificial Intelligence and Data Science",
            "B.Tech Computer Science and Business Systems",
            "Marine Engineering",
            "Aerospace Engineering",
            "Master of Business Administration (MBA)",
            "Master of Computer Application (MCA)",
            "M.E Power Electronics and Drives",
            "M.E Communication systems",
            "M.E Computer Science Engineering",
            "M.E Engineering Design"
        ]
        department_var.pack(padx=10)

        # Create Confirm button for department selection below the department combobox
        confirm_department_button = tk.Button(department_frame, text='Confirm Department', font=("Helvetica", 12), 
                                            command=lambda: filter_students_by_department(department_var.get()), 
                                            bg='blue', fg='white')
        confirm_department_button.pack(pady=10)

        # Create a frame for semester section (combobox and button)
        semester_frame = tk.Frame(selection_frame)
        semester_frame.pack(side='left', padx=20)

        # Create a Combobox for semester selection
        semester_var = ttk.Combobox(semester_frame, textvariable=semester_var, font=("Helvetica", 12), state='readonly')
        semester_var['values'] = [
        "1st Semester","2nd Semester","3ed Semester","4th Semester",
        "5th Semester","6th Semester","7th Semester","8th Semester"
        ]
        semester_var.pack(padx=10)

        # Create Confirm button for semester selection below the semester combobox
        confirm_semester_button = tk.Button(semester_frame, text='Confirm Semester', font=("Helvetica", 12), 
                                            command=lambda: filter_students_by_semester(semester_var.get()), 
                                            bg='blue', fg='white')
        confirm_semester_button.pack(pady=10)

        # Create Back button to return to the previous page
        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=open_student_window, bg='blue', fg='white')
        back_button.pack(side='left', padx=10, pady=10)

        # Create View button to open login window
        view_button = tk.Button(main_content, text='View', font=('Arial', 14), command=show_login_window, bg='blue', fg='white')
        view_button.pack(side='left', padx=10, pady=10)

        # Fetch and display all students initially
        display_all_students()


    def display_all_students():
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        try:
            # Execute the query to fetch all students
            cursor.execute("""
                SELECT s.student_id, s.student_name, u.username, u.role, s.department, s.semester 
                FROM students s 
                JOIN users u ON s.user_id = u.id
            """)
            students = cursor.fetchall()

            # Insert all student details into the Treeview
            for student_id, student_name, username, role, department, semester in students:
                tree.insert("", tk.END, values=(student_id, student_name, username, role, department, semester))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while fetching student details: {str(e)}")

    def filter_students_by_department(selected_department):
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        # Check if a department is selected
        if not selected_department:
            messagebox.showwarning("Warning", "Please select a department.")
            return  # Exit the function if no department is selected

        try:
            conn = connect_to_db()  # Establish a connection to the database
            if conn is None:
                messagebox.showerror("Error", "Database connection failed.")
                return

            cursor = conn.cursor()

            # SQL query to fetch students from the selected department with role 'student'
            cursor.execute("""
                SELECT s.student_id, s.student_name, u.username, u.role, s.department, s.semester 
                FROM students s 
                JOIN users u ON s.user_id = u.id 
                WHERE s.department = %s AND u.role = 'student'
            """, (selected_department,))

            students = cursor.fetchall()

            if not students:
                messagebox.showinfo("Info", "No students found in the selected department.")
                return

            # Insert filtered student details into the Treeview
            for student_id, student_name, username, role, department, semester in students:
                tree.insert("", tk.END, values=(student_id, student_name, username, role, department, semester))

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {str(err)}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while fetching student details: {str(e)}")
        finally:
            cursor.close()  # Close the cursor
            conn.close()    # Close the database connection


    def filter_students_by_semester(selected_semester):
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        # Check if a department is selected
        if not selected_semester:
            messagebox.showwarning("Warning", "Please select a semester.")
            return  # Exit the function if no department is selected

        try:
            conn = connect_to_db()  # Establish a connection to the database
            if conn is None:
                messagebox.showerror("Error", "Database connection failed.")
                return

            cursor = conn.cursor()

            # SQL query to fetch students from the selected department with role 'student'
            cursor.execute("""
                SELECT s.student_id, s.student_name, u.username, u.role, s.department, s.semester 
                FROM students s 
                JOIN users u ON s.user_id = u.id 
                WHERE s.semester = %s AND u.role = 'student'
            """, (selected_semester,))

            students = cursor.fetchall()

            if not students:
                messagebox.showinfo("Info", "No students found in the selected Semester.")
                return

            # Insert filtered student details into the Treeview
            for student_id, student_name, username, role, department, semester in students:
                tree.insert("", tk.END, values=(student_id, student_name, username, role, department, semester))

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {str(err)}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while fetching student details: {str(e)}")
        finally:
            cursor.close()  # Close the cursor
            conn.close()    # Close the database connection

    def show_users_by_role(role):
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        back_button = tk.Button(main_content, text="Back", font=('Arial', 12), command=display_role_buttons)
        back_button.pack(pady=10, anchor='w')

        tk.Label(main_content, text=f"Users in Role: {role}", font=('Arial', 24)).pack(pady=20)

        tree = ttk.Treeview(main_content, columns=("ID", "Username", "Role", "Action"), show="headings", height=10)
        tree.heading("ID", text="ID")
        tree.heading("Username", text="Username")
        tree.heading("Role", text="Role")
        tree.heading("Action", text="Action")
        tree.column("ID", width=50, anchor='center')
        tree.column("Username", width=200, anchor='center')
        tree.column("Role", width=100, anchor='center')
        tree.column("Action", width=100, anchor='center')
        tree.pack(pady=20, fill="both", expand=True)

        scrollbar = ttk.Scrollbar(main_content, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        try:
            cursor.execute("SELECT id, username, role FROM users WHERE role = %s", (role,))
            users = cursor.fetchall()

            for user in users:
                tree.insert("", tk.END, values=user + ("View",))

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to retrieve user details: {err}")

        tree.bind("<ButtonRelease-1>", lambda event: handle_treeview_click(tree, event))

    def handle_treeview_click(tree, event):
        item = tree.selection()
        if item:
            user_data = tree.item(item, 'values')
            user_id = user_data[0]
            messagebox.showinfo("User Info", f"Viewing details for User ID: {user_id}")

    def back_to_page5():
        for widget in main_content.winfo_children():
            widget.destroy()
        create_page5_content()

    def display_role_buttons():
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        # Create buttons for each role
        roles = ["Student", "Faculty", "HOD", "Principal", "Accountant", "Admin"]
        tk.Label(main_content, text="Select a Role", font=('Arial', 24)).pack(pady=20)

        for role in roles:
            role_button = tk.Button(main_content, text=role, font=('Arial', 14), command=lambda r=role: show_users_by_role(r))
            role_button.pack(pady=5)

        back_button = tk.Button(main_content, text="Back", font=('Arial', 12), command=back_to_page5)
        back_button.pack(pady=10)


    # Sidebar buttons
    button1 = tk.Button(sidebar, width=12, text='  Chat  ', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button1.pack(fill='x')
    button1.config(command=lambda: open_chat_sidebar(username, department, root,role))
    button1.bind("<Enter>", lambda event: button1.configure(bg='blue'))
    button1.bind("<Leave>", lambda event: button1.configure(bg='#2c3e50'))

    button2 = tk.Button(sidebar, text='  Admin Notifications  ', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button2.pack(fill='x')
    button2.config(command=lambda: fetch_and_display_notifications(username,"faculty"))
    button2.bind("<Enter>", lambda event: button2.configure(bg='blue'))
    button2.bind("<Leave>", lambda event: button2.configure(bg='#2c3e50'))

    button3 = tk.Button(sidebar, text='principal notification', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button3.pack(fill='x')
    button3.config(command=lambda: fetch_and_display_principal_notifications(username,"faculty"))
    button3.bind("<Enter>", lambda event: button3.configure(bg='blue'))
    button3.bind("<Leave>", lambda event: button3.configure(bg='#2c3e50'))

    button4 = tk.Button(sidebar, text='accountant notifiaction', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button4.pack(fill='x')
    button4.config(command=lambda: fetch_and_display_accountant_notifications(username,"faculty"))
    button4.bind("<Enter>", lambda event: button4.configure(bg='blue'))
    button4.bind("<Leave>", lambda event: button4.configure(bg='#2c3e50'))

    button5 = tk.Button(sidebar, text='hod notification', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button5.pack(fill='x')
    button5.config(command=lambda: fetch_and_display_hod_notifications(username,"faculty"))
    button5.bind("<Enter>", lambda event: button5.configure(bg='blue'))
    button5.bind("<Leave>", lambda event: button5.configure(bg='#2c3e50'))

    button6 = tk.Button(sidebar, text='Send Notification', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button6.pack(fill='x')
    button6.config(command=lambda: open_faculty_notification_interface)
    button6.bind("<Enter>", lambda event: button6.configure(bg='blue'))
    button6.bind("<Leave>", lambda event: button6.configure(bg='#2c3e50'))

    button7 = tk.Button(sidebar, text='Group Chat', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button7.pack(fill='x')
    button7.config(command=lambda: on_group_chat_click(username,main_content))
    button7.bind("<Enter>", lambda event: button7.configure(bg='blue'))
    button7.bind("<Leave>", lambda event: button7.configure(bg='#2c3e50'))

    button8 = tk.Button(sidebar, text='User Details', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button8.pack(fill='x')
    button8.config(command=lambda: load_content("User Details"))
    button8.bind("<Enter>", lambda event: button8.configure(bg='blue'))
    button8.bind("<Leave>", lambda event: button8.configure(bg='#2c3e50'))

    button9 = tk.Button(sidebar, text='Back', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button9.pack(fill='x')
    button9.config(command=lambda: switch_window(root,login_window))
    button9.bind("<Enter>", lambda event: button8.configure(bg='blue'))
    button9.bind("<Leave>", lambda event: button8.configure(bg='#2c3e50'))


        # Initial call to set the notification button based on unread messages
    admin_update_notification_button()

    update_chat_button()

    principal_update_notification_button()

    accountant_update_notification_button()

    hod_update_notification_button()

    open_faculty_notification_interface()

    group_chat_button(username)

    root.mainloop()

def fetch_and_display_hod_notifications(username, role):
    notifications_window = tk.Toplevel()
    notifications_window.title("Notifications")
    notifications_window.geometry("600x400")

    tk.Label(notifications_window, text=f"Notifications for {role} ({username})", font=('Arial', 20)).pack(pady=10)

    try:
        print(f"Fetching notifications for username: {username}, role: {role}")

        # Updated query to fetch notifications for specific username, role, or general 'all' notifications
        query = """
            SELECT id, message, created_at, is_read 
            FROM hod_notifications 
            WHERE recipient IN (%s, %s, 'all') 
            ORDER BY created_at DESC
        """
        
        print(f"Executing query with parameters: ({username}, {role})")
        cursor.execute(query, (username, role))
        notifications = cursor.fetchall()
        
        print(f"Fetched notifications: {notifications}")


        if notifications:
            scrollable_frame = tk.Frame(notifications_window)
            scrollable_frame.pack(fill=tk.BOTH, expand=True)

            scrollbar = tk.Scrollbar(scrollable_frame)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            notifications_canvas = tk.Canvas(scrollable_frame, yscrollcommand=scrollbar.set, width=580)
            notifications_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            scrollbar.config(command=notifications_canvas.yview)

            notification_frame = tk.Frame(notifications_canvas)
            notifications_canvas.create_window((0, 0), window=notification_frame, anchor='nw', width=580)

            def update_scrollregion(event):
                notifications_canvas.configure(scrollregion=notifications_canvas.bbox("all"))

            notification_frame.bind("<Configure>", update_scrollregion)

            unread_notifications = []

            for index, (notif_id, message, created_at, is_read) in enumerate(notifications):
                notification_box = tk.Frame(notification_frame, bd=2, relief="groove", padx=10, pady=10, width=580)
                notification_box.grid(row=index, column=0, padx=10, pady=5, sticky='ew')

                bg_color = 'white' if is_read else 'lightcoral'
                notification_box.config(bg=bg_color)

                notification_frame.grid_columnconfigure(0, weight=1)

                message_label = tk.Label(notification_box, text=message, font=('Arial', 14), wraplength=500, justify="left", bg=bg_color)
                message_label.pack(anchor='w')

                date_label = tk.Label(notification_box, text=created_at.strftime("%Y-%m-%d %H:%M:%S"), font=('Arial', 12, 'italic'), anchor='e', bg=bg_color)
                date_label.pack(anchor='e')

                if not is_read:
                    unread_notifications.append(notif_id)

            if not notifications:
                print("No notifications found.")
                tk.Label(notifications_window, text="No notifications available.", font=('Arial', 14)).pack(pady=20)

            # Messages Read button
            def mark_all_as_read():
                for notif_id in unread_notifications:
                    cursor.execute("""UPDATE hod_notifications SET is_read = TRUE WHERE id = %s""", (notif_id,))
                db.commit()
                print("All unread messages marked as read.")
                for widget in notification_frame.winfo_children():
                    widget.config(bg='white')  # Change color back to normal
                unread_notifications.clear()  # Clear the list after marking

            messages_read_button = tk.Button(notifications_window, text="Messages Read", command=mark_all_as_read)
            messages_read_button.pack(pady=10)

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        messagebox.showerror("Error", f"Failed to fetch notifications. Error: {str(err)}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
        messagebox.showerror("Error", f"An unexpected error occurred. Error: {str(e)}")

# Dashboard Window (varies based on role)
def hod_dashboard_window(username,department,role):
    root = tk.Tk()
    root.title("HOD Dashboard")
    root.geometry("1366x768")

    # Header Frame
    header = tk.Frame(root, height=120, bg='#1abc9c')
    header.pack(side="top", fill="x")

    # Sidebar Frame with adjusted width
    sidebar_width = 100  # Adjust this value as needed
    sidebar = tk.Frame(root, width=sidebar_width, bg='#2c3e50')
    sidebar.pack(side="left", fill="y")

    # Main content area
    main_content = tk.Frame(root, bg='white')
    main_content.pack(side="right", expand=True, fill="both")

    def load_content(page_name):
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        if page_name == "Logout":
            root.destroy()
            test()  # Call the test function or any other function you have
        elif page_name == "User Details":
            create_page5_content()  # Load buttons for roles
        else:
            tk.Label(main_content, text=f"Welcome to {page_name}", font=('Arial', 24)).pack(pady=20)
    def update_chat_button():
        try:
            # Query to check how many unread messages the user has
            cursor.execute("""
            SELECT COUNT(*) FROM chat_messages
            WHERE receiver_user_id=(SELECT id FROM users WHERE username=%s) AND is_read=FALSE
            """, (username,))
            unread_count = cursor.fetchone()[0]

            # Debug print for checking unread count
            print(f"Unread count for {username}: {unread_count}")

            # If unread messages exist, update the button to show red color and count
            if unread_count > 0:
                button1.config(text=f"Chat ({unread_count})", bg="red", fg="white")
            else:
                button1.config(text="Chat", bg="#2c3e50", fg="white")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        # Call the function again after 2 seconds to keep checking for updates
        button1.after(2000, update_chat_button)

    def admin_update_notification_button():
        try:
            cursor.execute("""
                SELECT COUNT(*) FROM adminda_notifications 
                WHERE recipient IN (%s, 'hod', 'all') AND is_read = FALSE
            """, (username,))
            unread_count = cursor.fetchone()[0]

            # Update button text and color based on unread notifications
            if unread_count > 0:
                button2.config(text=f"Admin Notifications ({unread_count})", bg="red", fg="white")
            else:
                button2.config(text="Admin Notifications", bg="#2c3e50", fg="white")

            # Check for unread notifications every 1 second
            button2.after(1000, admin_update_notification_button)  # Update every 1 second

        except mysql.connector.Error as err:
            print(f"Error: {err}")


    def principal_update_notification_button():
        try:
            cursor.execute("""
                SELECT COUNT(*) FROM principal_notifications 
                WHERE recipient IN (%s, 'hod', 'all') AND is_read = FALSE
            """, (username,))
            unread_count = cursor.fetchone()[0]

            # Update button text and color based on unread notifications
            if unread_count > 0:
                button3.config(text=f"principal Notifications ({unread_count})", bg="red", fg="white")
            else:
                button3.config(text="principal Notifications", bg="#2c3e50", fg="white")

            # Check for unread notifications every 1 second
            button3.after(1000, principal_update_notification_button)  # Update every 1 second

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def accountant_update_notification_button():
        try:
            cursor.execute("""
                SELECT COUNT(*) FROM accountant_notifications 
                WHERE recipient IN (%s, 'hod', 'all') AND is_read = FALSE
            """, (username,))
            unread_count = cursor.fetchone()[0]

            # Update button text and color based on unread notifications
            if unread_count > 0:
                button4.config(text=f"Accountant Notifications ({unread_count})", bg="red", fg="white")
            else:
                button4.config(text="Accountant Notifications", bg="#2c3e50", fg="white")

            # Check for unread notifications every 1 second
            button4.after(1000, accountant_update_notification_button)  # Update every 1 second

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def open_hod_notification_interface():
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="Enter Notification Message:", font=('Arial', 14), bg="white").pack(pady=20)
        notification_entry = tk.Text(main_content, height=5, width=50)
        notification_entry.pack(pady=10)

        tk.Label(main_content, text="Select Recipients:", font=('Arial', 14), bg="white").pack(pady=10)
        role_var = tk.StringVar(value="all")
        roles = ["all", "student", "faculty"]

        selected_role_label = tk.Label(main_content, text="", font=('Arial', 14), bg="white")
        selected_role_label.pack(pady=10)

        def on_role_change(*args):
            selected_role = role_var.get()
            selected_role_label.config(text=f"Selected Role: {selected_role.capitalize()}")

        role_dropdown = tk.OptionMenu(main_content, role_var, *roles, command=on_role_change)
        role_dropdown.pack(pady=10)

        def send_notification():
            notification_message = notification_entry.get("1.0", "end").strip()
            selected_role = role_var.get()

            if not notification_message:
                messagebox.showerror("Error", "Notification message cannot be empty.")
                return

            try:
                recipients = []
                if selected_role == "all":
                    cursor.execute("SELECT username FROM users")
                else:
                    cursor.execute("SELECT username FROM users WHERE role = %s", (selected_role,))
                recipients = cursor.fetchall()

                # Admin user (if applicable)
                hod_username = 'hod'
                if selected_role == "all" or selected_role in ["student", "faculty", "hod"]:
                    recipients = [(hod_username,)] + recipients if (hod_username,) not in recipients else recipients

                if recipients:
                    for recipient in recipients:
                        cursor.execute(
                            "INSERT INTO hod_notifications (message, sender, recipient) VALUES (%s, %s, %s)",
                            (notification_message, hod_username, recipient[0])
                        )
                    db.commit()
                    messagebox.showinfo("Success", f"Notification sent to all {selected_role.capitalize()}s.")
                else:
                    messagebox.showinfo("Info", f"No {selected_role.capitalize()}s found to send notifications.")

                notification_entry.delete("1.0", "end")

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Failed to send notification. Error: {str(err)}")

        tk.Button(main_content, text="Send Notification", command=send_notification, font=('Arial', 14),
                  bg='#1abc9c', fg='white').pack(pady=20)

    def faculty_update_notification_button():
        try:
            cursor.execute("""
                SELECT COUNT(*) FROM faculty_notifications 
                WHERE recipient IN (%s, 'hod', 'all') AND is_read = FALSE
            """, (username,))
            unread_count = cursor.fetchone()[0]

            # Update button text and color based on unread notifications
            if unread_count > 0:
                button6.config(text=f"faculty Notifications ({unread_count})", bg="red", fg="white")
            else:
                button6.config(text="faculty Notifications", bg="#2c3e50", fg="white")

            # Check for unread notifications every 1 second
            button6.after(1000, faculty_update_notification_button)  # Update every 1 second

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def group_chat_button(username):
        try:
            # Query to count unread messages for the current user in the group chat
            cursor.execute("""
                SELECT COUNT(*) FROM groupp_chat_messages 
                WHERE receiver_user_id IS NULL AND is_read = FALSE
            """)
            unread_count = cursor.fetchone()[0]

            # Update button text and color based on unread messages
            if unread_count > 0:
                button7.config(text=f"Group Chat ({unread_count})", bg="red", fg="white")
            else:
                button7.config(text="Group Chat", bg="#2c3e50", fg="white")

            # Check for unread messages every 1 second
            button7.after(1000, group_chat_button, username)  # Update every 1 second

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def on_group_chat_click(username, main_content):
        # Open the group chat sidebar
        open_group_chat_sidebar(username, main_content)

        # Reset the button color to its normal state after clicking
        button7.config(bg="#2c3e50", fg="white")

        # Optionally, mark all unread messages as read
        try:
            cursor.execute("""
                UPDATE groupp_chat_messages 
                SET is_read = TRUE 
                WHERE receiver_user_id IS NULL AND is_read = FALSE
            """)
            db.commit()
        except mysql.connector.Error as err:
            print(f"Error marking messages as read: {err}")

#################################################################################################################

    def create_page5_content():
        # Create a new content for Page 5
        page5_content = tk.Frame(main_content, bg='white')
        page5_content.pack(expand=True, fill="both")

        tk.Label(page5_content, text="View Details", font=('Arial', 24)).pack(pady=20)

        button_width = 20  # Set desired width
        button_height = 2  # Set desired height
        dark_green = '#006400'  # Dark green color
        light_green = '#90EE90'  # Light green color (for active background)

        student_button = tk.Button(page5_content, text='Student', font=('Arial', 14), bg=dark_green, fg='white',
                                width=button_width, height=button_height, activebackground=light_green, command=open_student_window)
        student_button.pack(pady=10, padx=20)

        faculty_button = tk.Button(page5_content, text='Faculty', font=('Arial', 14), bg=dark_green, fg='white',
                           width=button_width, height=button_height, activebackground=light_green, command=open_faculty_window)

        faculty_button.pack(pady=10, padx=20)

    def open_student_window():
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=back_to_page5,
                                bg='#8B008B', fg='white', width=25, height=3,
                                activebackground='#DDA0DD')  # Dark magenta background, light magenta on click
        back_button.pack(pady=10)

        view_button = tk.Button(main_content, text='View All Students', font=('Arial', 14), command=view_students,
                                bg='#8B008B', fg='white', width=25, height=3,
                                activebackground='#DDA0DD')  # Dark magenta background, light magenta on click
        view_button.pack(pady=10)

    def open_student_details(username):
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="Student Details", font=('Arial', 24)).pack(pady=20)

        # Create a frame for the Treeview and scrollbar with the specified size
        detail_frame = tk.Frame(main_content)
        detail_frame.pack(pady=10)

        # Set the size of the frame using the grid geometry manager
        detail_frame.grid_propagate(False)  # Prevent the frame from resizing to fit contents
        detail_frame.config(width=1100, height=500)

        # Create a Treeview widget for student details
        columns = ("Field", "Details")
        tree = ttk.Treeview(detail_frame, columns=columns, show="headings")
        tree.pack(side='left', fill='both', expand=True)

        # Configure the column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=250)  # Adjust width as needed

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(detail_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscroll=scrollbar.set)

        try:
            # Fetch student details for the given username
            cursor.execute("""
                SELECT s.student_id, s.student_name, u.username, u.role, 
                    s.admission_date, s.department, s.semester, 
                    s.admission_number, s.roll_no, s.gender, s.dob, 
                    s.blood_group, s.father_name, s.father_occupation, 
                    s.mother_name, s.mother_occupation, s.address, 
                    s.city, s.country, s.religion, s.caste, 
                    s.pin_code, s.state, s.email, s.phone, 
                    s.parent_phone, s.guardian_name, 
                    s.guardian_relationship, s.guardian_phone, 
                    s.guardian_address 
                FROM students s 
                JOIN users u ON s.user_id = u.id 
                WHERE u.username = %s
            """, (username,))
            student = cursor.fetchone()

            if not student:
                messagebox.showinfo("Info", "No student details found for this username.")
                return

            # Display student details in the Treeview
            field_labels = [
                "Student ID", "Student Name", "Username", "Role",
                "Admission Date", "Department", "Semester", 
                "Admission Number", "Roll No", "Gender", "DOB", 
                "Blood Group", "Father's Name", "Father's Occupation", 
                "Mother's Name", "Mother's Occupation", "Address", 
                "City", "Country", "Religion", "Caste", 
                "Pin Code", "State", "Email", "Phone", 
                "Parent Phone", "Guardian Name", 
                "Guardian Relationship", "Guardian Phone", 
                "Guardian Address"
            ]
            
            # Insert student details into the Treeview
            for label, value in zip(field_labels, student):
                tree.insert("", tk.END, values=(label, value))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        # Back button to return to the previous page
        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=back_to_page5, bg='blue', fg='white')
        back_button.pack(side='left', padx=10, pady=10)

        # Delete Student button
        delete_button = tk.Button(main_content, text='Delete Student', font=('Arial', 14), command=lambda: delete_student(username), bg='blue', fg='white')
        delete_button.pack(side='left', padx=10, pady=10)

    def commit_changes():
        try:
            # Use the same connection to commit changes
            cursor.execute("COMMIT")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while committing changes: {str(e)}")

    def delete_student(username):
        # Confirmation dialog
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this student?"):
            for attempt in range(3):  # Retry up to 3 times
                try:
                    # Fetch the user's ID using the username
                    cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
                    user_id = cursor.fetchone()
                    
                    if user_id:
                        user_id = user_id[0]
                        # Delete the student from the students table
                        cursor.execute("DELETE FROM students WHERE user_id = %s", (user_id,))
                        # Delete the user from the users table
                        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
                        commit_changes()  # Call the commit function
                        messagebox.showinfo("Success", "Student deleted successfully.")
                        back_to_page5()  # Go back to the previous page after deletion
                        return  # Exit the function after successful deletion
                    else:
                        messagebox.showerror("Error", "User not found.")
                    break  # Exit the retry loop if the user is found
                except Exception as e:
                    if "Lock wait timeout exceeded" in str(e):
                        if attempt < 2:  # Retry only if we haven't exhausted attempts
                            time.sleep(1)  # Wait before retrying
                        else:
                            messagebox.showerror("Error", f"An error occurred while deleting the student: {str(e)}")
                    else:
                        messagebox.showerror("Error", f"An error occurred while deleting the student: {str(e)}")

    def show_login_window():
        # Create a new window for login
        login_window = tk.Toplevel()
        login_window.title("Login")

        tk.Label(login_window, text="Enter Username:", font=('Arial', 14)).pack(pady=10)

        username_entry = tk.Entry(login_window, font=('Arial', 14))
        username_entry.pack(pady=10)

        def on_login():
            username = username_entry.get()
            if username:
                cursor.execute("SELECT role FROM users WHERE username = %s", (username,))
                role = cursor.fetchone()

                if role and role[0] == 'student':
                    open_student_details(username)
                    login_window.destroy()  # Close the login window
                else:
                    messagebox.showerror("Error", "Username does not belong to a student.")
            else:
                messagebox.showwarning("Warning", "Please enter a username.")

        login_button = tk.Button(login_window, text="Login", font=('Arial', 14), command=on_login)
        login_button.pack(pady=10)
    # Declare the tree variable globally
    
    tree = None
    def view_students():
        global tree  # Declare the tree variable as global

        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="All Student Details", font=('Arial', 24)).pack(pady=20)

        # Create a frame for the Treeview and scrollbar
        student_frame = tk.Frame(main_content)
        student_frame.pack(pady=10)

        # Create a Treeview widget for listing students
        columns = ("Student ID", "Student Name", "Username", "Role", "Department", "Semester")
        tree = ttk.Treeview(student_frame, columns=columns, show="headings")
        tree.pack(side='left', fill='both', expand=True)

        # Configure the column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=150)  # Adjust width as needed

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(student_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscroll=scrollbar.set)

        # Set a minimum size for the Treeview frame
        student_frame.configure(width=1100, height=400)

        # Create a frame for the department and semester selection
        selection_frame = tk.Frame(main_content)
        selection_frame.pack(pady=20)

        # Create a StringVar to hold the selected department
        department_var = tk.StringVar()
        
        # Create a StringVar to hold the selected semester
        semester_var = tk.StringVar()

        # Create a frame for department section (combobox and button)
        department_frame = tk.Frame(selection_frame)
        department_frame.pack(side='left', padx=20)

        # Create a Combobox for department selection
        department_combobox = ttk.Combobox(department_frame, textvariable=department_var, font=("Helvetica", 12), state='readonly')
        department_combobox['values'] = [
            "B.E Civil Engineering",
            "B.E Computer Science Engineering",
            "B.E Electrical and Electronics Engineering",
            "B.E Electronics and Communication Engineering",
            "B.Tech Information Technology",
            "B.E Mechanical Engineering",
            "B.Tech Artificial Intelligence and Data Science",
            "B.Tech Computer Science and Business Systems",
            "Marine Engineering",
            "Aerospace Engineering",
            "Master of Business Administration (MBA)",
            "Master of Computer Application (MCA)",
            "M.E Power Electronics and Drives",
            "M.E Communication systems",
            "M.E Computer Science Engineering",
            "M.E Engineering Design"
        ]
        department_combobox.pack(padx=10)

        # Create Confirm button for department selection below the department combobox
        confirm_department_button = tk.Button(department_frame, text='Confirm Department', font=("Helvetica", 12), 
                                            command=lambda: filter_students_by_department(department_var.get()), 
                                            bg='blue', fg='white')
        confirm_department_button.pack(pady=10)

        # Create a frame for semester section (combobox and button)
        semester_frame = tk.Frame(selection_frame)
        semester_frame.pack(side='left', padx=20)

        # Create a Combobox for semester selection
        semester_combobox = ttk.Combobox(semester_frame, textvariable=semester_var, font=("Helvetica", 12), state='readonly')
        semester_combobox['values'] = [
            "Semester 1", "Semester 2", "Semester 3", "Semester 4", 
            "Semester 5", "Semester 6", "Semester 7", "Semester 8"
        ]
        semester_combobox.pack(padx=10)

        # Create Confirm button for semester selection below the semester combobox
        confirm_semester_button = tk.Button(semester_frame, text='Confirm Semester', font=("Helvetica", 12), 
                                            command=lambda: filter_students_by_semester(semester_var.get()), 
                                            bg='blue', fg='white')
        confirm_semester_button.pack(pady=10)

        # Create Back button to return to the previous page
        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=open_student_window, bg='blue', fg='white')
        back_button.pack(side='left', padx=10, pady=10)

        # Create View button to open login window
        view_button = tk.Button(main_content, text='View', font=('Arial', 14), command=show_login_window, bg='blue', fg='white')
        view_button.pack(side='left', padx=10, pady=10)

        # Fetch and display all students initially
        display_all_students()


    def display_all_students():
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        try:
            # Execute the query to fetch all students
            cursor.execute("""
                SELECT s.student_id, s.student_name, u.username, u.role, s.department, s.semester 
                FROM students s 
                JOIN users u ON s.user_id = u.id
            """)
            students = cursor.fetchall()

            # Insert all student details into the Treeview
            for student_id, student_name, username, role, department, semester in students:
                tree.insert("", tk.END, values=(student_id, student_name, username, role, department, semester))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while fetching student details: {str(e)}")

    def filter_students_by_department(selected_department):
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        if selected_department:
            try:
                print(f"Filtering students by department: {selected_department}")  # Debugging output
                # Execute the query to fetch students from the selected department
                cursor.execute("""
                    SELECT s.student_id, s.student_name, u.username, u.role, s.department, s.semester 
                    FROM students s 
                    JOIN users u ON s.user_id = u.id 
                    WHERE s.department = %s
                """, (selected_department,))
                students = cursor.fetchall()

                if not students:
                    messagebox.showinfo("Info", "No students found in the selected department.")
                    return

                # Insert filtered student details into the Treeview
                for student_id, student_name, username, role, department, semester in students:
                    tree.insert("", tk.END, values=(student_id, student_name, username, role, department, semester))

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while fetching student details: {str(e)}")

    def filter_students_by_semester(selected_semester):
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        if selected_semester:
            try:
                print(f"Filtering students by semester: {selected_semester}")  # Debugging output
                # Execute the query to fetch students from the selected semester
                cursor.execute("""
                    SELECT s.student_id, s.student_name, u.username, u.role, s.department, s.semester 
                    FROM students s 
                    JOIN users u ON s.user_id = u.id 
                    WHERE s.semester = %s
                """, (selected_semester,))
                students = cursor.fetchall()

                if not students:
                    messagebox.showinfo("Info", "No students found in the selected semester.")
                    return

                # Insert filtered student details into the Treeview
                for student_id, student_name, username, role, department, semester in students:
                    tree.insert("", tk.END, values=(student_id, student_name, username, role, department, semester))

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while fetching student details: {str(e)}")

    def show_users_by_role(role):
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        back_button = tk.Button(main_content, text="Back", font=('Arial', 12), command=display_role_buttons)
        back_button.pack(pady=10, anchor='w')

        tk.Label(main_content, text=f"Users in Role: {role}", font=('Arial', 24)).pack(pady=20)

        tree = ttk.Treeview(main_content, columns=("ID", "Username", "Role", "Action"), show="headings", height=10)
        tree.heading("ID", text="ID")
        tree.heading("Username", text="Username")
        tree.heading("Role", text="Role")
        tree.heading("Action", text="Action")
        tree.column("ID", width=50, anchor='center')
        tree.column("Username", width=200, anchor='center')
        tree.column("Role", width=100, anchor='center')
        tree.column("Action", width=100, anchor='center')
        tree.pack(pady=20, fill="both", expand=True)

        scrollbar = ttk.Scrollbar(main_content, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        try:
            cursor.execute("SELECT id, username, role FROM users WHERE role = %s", (role,))
            users = cursor.fetchall()

            for user in users:
                tree.insert("", tk.END, values=user + ("View",))

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to retrieve user details: {err}")

        tree.bind("<ButtonRelease-1>", lambda event: handle_treeview_click(tree, event))

    def handle_treeview_click(tree, event):
        item = tree.selection()
        if item:
            user_data = tree.item(item, 'values')
            user_id = user_data[0]
            messagebox.showinfo("User Info", f"Viewing details for User ID: {user_id}")

    def back_to_page5():
        for widget in main_content.winfo_children():
            widget.destroy()
        create_page5_content()

    def display_role_buttons():
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        # Create buttons for each role
        roles = ["Student", "Faculty", "HOD", "Principal", "Accountant", "Admin"]
        tk.Label(main_content, text="Select a Role", font=('Arial', 24)).pack(pady=20)

        for role in roles:
            role_button = tk.Button(main_content, text=role, font=('Arial', 14), command=lambda r=role: show_users_by_role(r))
            role_button.pack(pady=5)

        back_button = tk.Button(main_content, text="Back", font=('Arial', 12), command=back_to_page5)
        back_button.pack(pady=10)

###########################################################################################################################

    def open_faculty_window():
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=back_to_page5,
                                bg='#8B008B', fg='white', width=25, height=3,
                                activebackground='#DDA0DD')  # Dark magenta background, light magenta on click
        back_button.pack(pady=10)

        view_button = tk.Button(main_content, text='View All Faculties', font=('Arial', 14), command=view_faculty,
                                bg='#8B008B', fg='white', width=25, height=3,
                                activebackground='#DDA0DD')  # Dark magenta background, light magenta on click
        view_button.pack(pady=10)

    def open_faculty_details(username):
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="Faculty Details", font=('Arial', 24)).pack(pady=20)

        # Create a frame for the Treeview and scrollbar with the specified size
        detail_frame = tk.Frame(main_content)
        detail_frame.pack(pady=10)

        # Set the size of the frame using the grid geometry manager
        detail_frame.grid_propagate(False)  # Prevent the frame from resizing to fit contents
        detail_frame.config(width=1100, height=500)

        # Create a Treeview widget for student details
        columns = ("Field", "Details")
        tree = ttk.Treeview(detail_frame, columns=columns, show="headings")
        tree.pack(side='left', fill='both', expand=True)

        # Configure the column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=250)  # Adjust width as needed

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(detail_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscroll=scrollbar.set)

        try:
            # Fetch faculty details for the given username
            cursor.execute("""
                SELECT f.faculty_id, f.faculty_name, u.username, u.role, 
                    f.department, f.faculty_gender, f.faculty_dob, 
                    f.faculty_blood_group, f.faculty_marital_status, 
                    f.faculty_job_position, f.faculty_address, 
                    f.faculty_city, f.faculty_country, f.faculty_pin_code, 
                    f.faculty_state, f.faculty_email, f.faculty_phone, 
                    f.faculty_guardian_name, f.faculty_guardian_relationship, 
                    f.faculty_guardian_phone, f.faculty_guardian_address 
                FROM faculty f
                JOIN users u ON f.user_id = u.id
                WHERE u.username = %s
            """, (username,))
            faculty = cursor.fetchone()

            if not faculty:
                messagebox.showinfo("Info", "No faculty details found for this username.")
                return

            # Display faculty details in the Treeview (adjust fields and labels as needed)
            field_labels = [
                "Faculty ID", "Faculty Name", "Username", "Role", 
                "Department", "Gender", "DOB", "Blood Group", 
                "Marital Status", "Job Position", "Address", 
                "City", "Country", "Pin Code", "State", 
                "Email", "Phone", "Guardian Name", 
                "Guardian Relationship", "Guardian Phone", 
                "Guardian Address"
            ]

            # Insert student details into the Treeview
            for label, value in zip(field_labels, faculty):
                tree.insert("", tk.END, values=(label, value))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        # Back button to return to the previous page
        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=back_to_page5, bg='blue', fg='white')
        back_button.pack(side='left', padx=10, pady=10)

    def show_faculty_login_window():
        # Create a new window for login
        login_window = tk.Toplevel()
        login_window.title("Login")

        tk.Label(login_window, text="Enter Username:", font=('Arial', 14)).pack(pady=10)

        username_entry = tk.Entry(login_window, font=('Arial', 14))
        username_entry.pack(pady=10)

        def on_login():
            username = username_entry.get()
            if username:
                cursor.execute("SELECT role FROM users WHERE username = %s", (username,))
                role = cursor.fetchone()

                if role and role[0] == 'faculty':
                    open_faculty_details(username)
                    login_window.destroy()  # Close the login window
                else:
                    messagebox.showerror("Error", "Username does not belong to a faculty.")
            else:
                messagebox.showwarning("Warning", "Please enter a username.")

        login_button = tk.Button(login_window, text="Login", font=('Arial', 14), command=on_login)
        login_button.pack(pady=10)
    # Declare the tree variable globally

    tree = None
    def view_faculty():
        global tree  # Declare the tree variable as global

        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="All faculty Details", font=('Arial', 24)).pack(pady=20)

        # Create a frame for the Treeview and scrollbar
        student_frame = tk.Frame(main_content)
        student_frame.pack(pady=10)

        # Create a Treeview widget for listing students
        columns = ("faculty ID", "faculty Name", "Username", "Role", "Department")
        tree = ttk.Treeview(student_frame, columns=columns, show="headings")
        tree.pack(side='left', fill='both', expand=True)

        # Configure the column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=150)  # Adjust width as needed

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(student_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscroll=scrollbar.set)

        # Set a minimum size for the Treeview frame
        student_frame.configure(width=1100, height=400)

        # Create a frame for the department and semester selection
        selection_frame = tk.Frame(main_content)
        selection_frame.pack(pady=20)

        # Create a StringVar to hold the selected department
        department_var = tk.StringVar()

        # Create a frame for department section (combobox and button)
        department_frame = tk.Frame(selection_frame)
        department_frame.pack(side='left', padx=20)

        # Create a Combobox for department selection
        department_combobox = ttk.Combobox(department_frame, textvariable=department_var, font=("Helvetica", 12), state='readonly')
        department_combobox['values'] = [
            "B.E Civil Engineering",
            "B.E Computer Science Engineering",
            "B.E Electrical and Electronics Engineering",
            "B.E Electronics and Communication Engineering",
            "B.Tech Information Technology",
            "B.E Mechanical Engineering",
            "B.Tech Artificial Intelligence and Data Science",
            "B.Tech Computer Science and Business Systems",
            "Marine Engineering",
            "Aerospace Engineering",
            "Master of Business Administration (MBA)",
            "Master of Computer Application (MCA)",
            "M.E Power Electronics and Drives",
            "M.E Communication systems",
            "M.E Computer Science Engineering",
            "M.E Engineering Design"
        ]
        department_combobox.pack(padx=10)

        # Create Confirm button for department selection below the department combobox
        confirm_department_button = tk.Button(department_frame, text='Confirm Department', font=("Helvetica", 12), 
                                            command=lambda: filter_faculty_by_department(department_var.get()), 
                                            bg='blue', fg='white')
        confirm_department_button.pack(pady=10)

        # Create Back button to return to the previous page
        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=open_faculty_window, bg='blue', fg='white')
        back_button.pack(side='left', padx=10, pady=10)

        # Create View button to open login window
        view_button = tk.Button(main_content, text='View', font=('Arial', 14), command=show_faculty_login_window, bg='blue', fg='white')
        view_button.pack(side='left', padx=10, pady=10)

        # Fetch and display all students initially
        display_all_faculty()


    def display_all_faculty():
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        try:
            # Execute the query to fetch all students
            cursor.execute("""
                SELECT s.faculty_id, s.faculty_name, u.username, u.role, s.department 
                FROM faculty s 
                JOIN users u ON s.user_id = u.id
            """)
            faculty = cursor.fetchall()

            # Insert all student details into the Treeview
            for faculty_id, faculty_name, username, role, department in faculty:
                tree.insert("", tk.END, values=(faculty_id, faculty_name, username, role, department))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while fetching student details: {str(e)}")

    def filter_faculty_by_department(selected_department):
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        if selected_department:
            try:
                print(f"Filtering students by department: {selected_department}")  # Debugging output
                # Execute the query to fetch students from the selected department
                cursor.execute("""
                    SELECT s.faculty_id, s.faculty_name, u.username, u.role, s.department 
                    FROM faculty s 
                    JOIN users u ON s.user_id = u.id 
                    WHERE s.department = %s
                """, (selected_department,))
                faculty = cursor.fetchall()

                if not faculty:
                    messagebox.showinfo("Info", "No faculty found in the selected department.")
                    return

                # Insert filtered student details into the Treeview
                for faculty_id, faculty_name, username, role, department in faculty:
                    tree.insert("", tk.END, values=(faculty_id, faculty_name, username, role, department))

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while fetching faculty details: {str(e)}")


    # Sidebar buttons
    button1 = tk.Button(sidebar, width=12, text='  Chat  ', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button1.pack(fill='x')
    button1.config(command=lambda: open_chat_sidebar(username, department, root,role))  # Replace 'student_username' with actual username
    button1.bind("<Enter>", lambda event: button1.configure(bg='blue'))
    button1.bind("<Leave>", lambda event: button1.configure(bg='#2c3e50'))

    button2 = tk.Button(sidebar, text='  Admin Notifications  ', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button2.pack(fill='x')
    button2.config(command=lambda: fetch_and_display_notifications(username,'hod'))  # Replace 'student_username' with actual username
    button2.bind("<Enter>", lambda event: button2.configure(bg='blue'))
    button2.bind("<Leave>", lambda event: button2.configure(bg='#2c3e50'))

    button3 = tk.Button(sidebar, text='principal notification', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button3.pack(fill='x')
    button3.config(command=lambda: fetch_and_display_principal_notifications(username,"hod"))
    button3.bind("<Enter>", lambda event: button3.configure(bg='blue'))
    button3.bind("<Leave>", lambda event: button3.configure(bg='#2c3e50'))

    button4 = tk.Button(sidebar, text='accountant notifiaction', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button4.pack(fill='x')
    button4.config(command=lambda: fetch_and_display_accountant_notifications(username,"hod"))
    button4.bind("<Enter>", lambda event: button4.configure(bg='blue'))
    button4.bind("<Leave>", lambda event: button4.configure(bg='#2c3e50'))

    button5 = tk.Button(sidebar, text='Send Notification', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button5.pack(fill='x')
    button5.config(command=lambda: open_hod_notification_interface)
    button5.bind("<Enter>", lambda event: button5.configure(bg='blue'))
    button5.bind("<Leave>", lambda event: button5.configure(bg='#2c3e50'))

    button6 = tk.Button(sidebar, text='faculty notification', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button6.pack(fill='x')
    button6.config(command=lambda: fetch_and_display_faculty_notifications(username,"hod"))
    button6.bind("<Enter>", lambda event: button6.configure(bg='blue'))
    button6.bind("<Leave>", lambda event: button6.configure(bg='#2c3e50'))

    button7 = tk.Button(sidebar, text='group chat', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button7.pack(fill='x')
    button7.config(command=lambda: on_group_chat_click(username,main_content))
    button7.bind("<Enter>", lambda event: button7.configure(bg='blue'))
    button7.bind("<Leave>", lambda event: button7.configure(bg='#2c3e50'))

    button8 = tk.Button(sidebar, text='User Details', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button8.pack(fill='x')
    button8.config(command=lambda: load_content("User Details"))
    button8.bind("<Enter>", lambda event: button8.configure(bg='blue'))
    button8.bind("<Leave>", lambda event: button8.configure(bg='#2c3e50'))

    button9 = tk.Button(sidebar, text='Back', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button9.pack(fill='x')
    button9.config(command=lambda: switch_window(root,login_window))
    button9.bind("<Enter>", lambda event: button8.configure(bg='blue'))
    button9.bind("<Leave>", lambda event: button8.configure(bg='#2c3e50'))

        # Initial call to set the notification button based on unread messages
    admin_update_notification_button()

    update_chat_button()  # Update the chat button state when the dashboard is created

    principal_update_notification_button()

    accountant_update_notification_button()

    open_hod_notification_interface()

    faculty_update_notification_button()

    group_chat_button(username)

    root.mainloop()

def open_staff_chat_sidebar(username, main_window):
    chat_frame = tk.Frame(main_window)
    chat_frame.pack(side="right", fill="both", expand=True)
    chat_frame.pack_propagate(False)

    # Recipient entry and search button
    recipient_entry = tk.Entry(chat_frame, width=50)
    recipient_entry.insert(0, "Enter recipient username")
    recipient_entry.pack(pady=5)

    search_button = tk.Button(chat_frame, text="Search", command=lambda: search_recipient(recipient_entry.get().strip()))
    search_button.pack(pady=5)

    # Frame to hold recipient chat button
    recipient_button_frame = tk.Frame(chat_frame)
    recipient_button_frame.pack(pady=5)

    # Text widget for displaying chat messages
    msg_text = tk.Text(chat_frame, height=15, width=50, wrap="word", state="disabled")

    # Entry and send button for sending messages
    msg_entry = tk.Entry(chat_frame, width=50)
    send_button = tk.Button(chat_frame, text="Send", command=lambda: send_message(recipient_entry.get().strip(), msg_entry.get().strip()))

    # Label to show unread messages count
    notification_label = tk.Label(chat_frame, text="Unread Messages: 0")
    notification_label.pack_forget()

    unread_messages_label = tk.Label(main_window, text="", fg="red")
    unread_messages_label.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=150)

    def search_recipient(recipient_username):
        # Clear previous buttons
        for widget in recipient_button_frame.winfo_children():
            widget.destroy()

        if not recipient_username:
            messagebox.showerror("Error", "Recipient name cannot be empty.")
            return

        try:
            cursor.execute("SELECT username FROM users WHERE username = %s", (recipient_username,))
            result = cursor.fetchone()

            if result is None:
                messagebox.showerror("Error", f"Account '{recipient_username}' not found in the database.")
            else:
                recipient_button = tk.Button(recipient_button_frame, text=f"Chat with {result[0]}", command=lambda: open_chat_section(result[0]))
                recipient_button.pack(pady=5)
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Search failed: {e}")

    def open_chat_section(recipient_username):
        recipient_entry.pack_forget()
        search_button.pack_forget()
        recipient_button_frame.pack_forget()

        msg_text.pack(pady=10, padx=10, fill="both", expand=True)
        msg_entry.pack(pady=5)
        send_button.pack(pady=5)
        notification_label.pack(pady=5)

        fetch_messages(username, recipient_username)

    def send_message(recipient_username, message):
        if not recipient_username or not message:
            messagebox.showerror("Error", "Recipient and message cannot be empty")
            return

        try:
            cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
            sender_id = cursor.fetchone()

            cursor.execute("SELECT id FROM users WHERE username = %s", (recipient_username,))
            recipient_id = cursor.fetchone()

            if sender_id is None or recipient_id is None:
                messagebox.showerror("Error", "Sender or recipient not found.")
                return

            cursor.execute("""
                INSERT INTO staff_chat_messages (sender_user_id, receiver_user_id, message, timestamp, is_read)
                VALUES (%s, %s, %s, %s, %s)
                """, (sender_id[0], recipient_id[0], message, datetime.now(), False))
            db.commit()

            msg_entry.delete(0, tk.END)
            fetch_messages(username, recipient_username)
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Message sending failed: {e}")

    def fetch_messages(username, recipient_username):
        try:
            cursor.execute("SELECT id FROM users WHERE username=%s", (username,))
            result = cursor.fetchone()

            if result is None:
                messagebox.showerror("Error", f"User '{username}' not found in the database.")
                return

            user_id = result[0]

            cursor.execute("""
                SELECT sender_user_id, message, timestamp 
                FROM staff_chat_messages 
                WHERE (sender_user_id=(SELECT id FROM users WHERE username=%s) 
                    AND receiver_user_id=(SELECT id FROM users WHERE username=%s))
                OR (sender_user_id=(SELECT id FROM users WHERE username=%s) 
                    AND receiver_user_id=(SELECT id FROM users WHERE username=%s))
                ORDER BY timestamp ASC
                """, (username, recipient_username, recipient_username, username))
            messages = cursor.fetchall()

            msg_text.config(state="normal")
            msg_text.delete(1.0, tk.END)

            for msg in messages:
                msg_time = msg[2].strftime("%H:%M")
                message_with_time = f"{msg[1]}\n{msg_time}"

                if msg[0] == user_id:
                    msg_text.insert(tk.END, f"You:\n{message_with_time}\n", 'sent')
                else:
                    msg_text.insert(tk.END, f"{recipient_username}:\n{message_with_time}\n", 'received')

            msg_text.tag_configure('sent', justify='right', foreground='blue')
            msg_text.tag_configure('received', justify='left', foreground='black')
            msg_text.config(state="disabled")
            msg_text.yview_moveto(1)

            cursor.execute("""
                SELECT COUNT(*) FROM staff_chat_messages
                WHERE receiver_user_id=(SELECT id FROM users WHERE username=%s)
                AND sender_user_id=(SELECT id FROM users WHERE username=%s) 
                AND is_read=FALSE
                """, (username, recipient_username))
            unread_count = cursor.fetchone()[0]
            notification_label.config(text=f"Unread Messages: {unread_count}")

            cursor.execute("""
                UPDATE staff_chat_messages SET is_read=TRUE
                WHERE receiver_user_id=(SELECT id FROM users WHERE username=%s)
                AND sender_user_id=(SELECT id FROM users WHERE username=%s)
                AND is_read=FALSE
                """, (username, recipient_username))
            db.commit()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Failed to fetch messages: {e}")

    def show_unread_messages():
        for widget in recipient_button_frame.winfo_children():
            widget.destroy()

        try:
            cursor.execute("""
                SELECT DISTINCT sender_user_id
                FROM staff_chat_messages
                WHERE receiver_user_id=(SELECT id FROM users WHERE username=%s)
                  AND is_read=FALSE
                """, (username,))
            senders = cursor.fetchall()

            if not senders:
                messagebox.showinfo("No Unread Messages", "You have no unread messages.")
                return

            for sender_id in senders:
                cursor.execute("SELECT username FROM users WHERE id=%s", (sender_id[0],))
                sender_username = cursor.fetchone()[0]
                sender_button = tk.Button(recipient_button_frame, text=f"Chat with {sender_username}", command=lambda username=sender_username: open_chat_section(username))
                sender_button.pack(pady=5)
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Failed to fetch unread messages: {e}")

    unread_button = tk.Button(chat_frame, text="Unread Messages", command=show_unread_messages)
    unread_button.pack(pady=5)

    fetch_messages(username, username)

def fetch_and_display_notifications(username, role):
    notifications_window = tk.Toplevel()
    notifications_window.title("Notifications")
    notifications_window.geometry("600x400")

    tk.Label(notifications_window, text=f"Notifications for {role} ({username})", font=('Arial', 20)).pack(pady=10)

    try:
        print(f"Fetching notifications for username: {username}, role: {role}")

        # Updated query to fetch notifications for specific username, role, or general 'all' notifications
        query = """
            SELECT id, message, created_at, is_read 
            FROM adminda_notifications 
            WHERE recipient IN (%s, %s, 'all') 
            ORDER BY created_at DESC
        """
        
        print(f"Executing query with parameters: ({username}, {role})")
        cursor.execute(query, (username, role))
        notifications = cursor.fetchall()
        
        print(f"Fetched notifications: {notifications}")


        if notifications:
            scrollable_frame = tk.Frame(notifications_window)
            scrollable_frame.pack(fill=tk.BOTH, expand=True)

            scrollbar = tk.Scrollbar(scrollable_frame)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            notifications_canvas = tk.Canvas(scrollable_frame, yscrollcommand=scrollbar.set, width=580)
            notifications_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            scrollbar.config(command=notifications_canvas.yview)

            notification_frame = tk.Frame(notifications_canvas)
            notifications_canvas.create_window((0, 0), window=notification_frame, anchor='nw', width=580)

            def update_scrollregion(event):
                notifications_canvas.configure(scrollregion=notifications_canvas.bbox("all"))

            notification_frame.bind("<Configure>", update_scrollregion)

            unread_notifications = []

            for index, (notif_id, message, created_at, is_read) in enumerate(notifications):
                notification_box = tk.Frame(notification_frame, bd=2, relief="groove", padx=10, pady=10, width=580)
                notification_box.grid(row=index, column=0, padx=10, pady=5, sticky='ew')

                bg_color = 'white' if is_read else 'lightcoral'
                notification_box.config(bg=bg_color)

                notification_frame.grid_columnconfigure(0, weight=1)

                message_label = tk.Label(notification_box, text=message, font=('Arial', 14), wraplength=500, justify="left", bg=bg_color)
                message_label.pack(anchor='w')

                date_label = tk.Label(notification_box, text=created_at.strftime("%Y-%m-%d %H:%M:%S"), font=('Arial', 12, 'italic'), anchor='e', bg=bg_color)
                date_label.pack(anchor='e')

                if not is_read:
                    unread_notifications.append(notif_id)

            if not notifications:
                print("No notifications found.")
                tk.Label(notifications_window, text="No notifications available.", font=('Arial', 14)).pack(pady=20)

            # Messages Read button
            def mark_all_as_read():
                for notif_id in unread_notifications:
                    cursor.execute("""UPDATE adminda_notifications SET is_read = TRUE WHERE id = %s""", (notif_id,))
                db.commit()
                print("All unread messages marked as read.")
                for widget in notification_frame.winfo_children():
                    widget.config(bg='white')  # Change color back to normal
                unread_notifications.clear()  # Clear the list after marking

            messages_read_button = tk.Button(notifications_window, text="Messages Read", command=mark_all_as_read)
            messages_read_button.pack(pady=10)

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        messagebox.showerror("Error", f"Failed to fetch notifications. Error: {str(err)}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
        messagebox.showerror("Error", f"An unexpected error occurred. Error: {str(e)}")

def fetch_and_display_principal_notifications(username, role):
    notifications_window = tk.Toplevel()
    notifications_window.title("Notifications")
    notifications_window.geometry("600x400")

    tk.Label(notifications_window, text=f"Notifications for {role} ({username})", font=('Arial', 20)).pack(pady=10)

    try:
        print(f"Fetching notifications for username: {username}, role: {role}")

        # Updated query to fetch notifications for specific username, role, or general 'all' notifications
        query = """
            SELECT id, message, created_at, is_read 
            FROM principal_notifications 
            WHERE recipient IN (%s, %s, 'all') 
            ORDER BY created_at DESC
        """
        
        print(f"Executing query with parameters: ({username}, {role})")
        cursor.execute(query, (username, role))
        notifications = cursor.fetchall()
        
        print(f"Fetched notifications: {notifications}")


        if notifications:
            scrollable_frame = tk.Frame(notifications_window)
            scrollable_frame.pack(fill=tk.BOTH, expand=True)

            scrollbar = tk.Scrollbar(scrollable_frame)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            notifications_canvas = tk.Canvas(scrollable_frame, yscrollcommand=scrollbar.set, width=580)
            notifications_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            scrollbar.config(command=notifications_canvas.yview)

            notification_frame = tk.Frame(notifications_canvas)
            notifications_canvas.create_window((0, 0), window=notification_frame, anchor='nw', width=580)

            def update_scrollregion(event):
                notifications_canvas.configure(scrollregion=notifications_canvas.bbox("all"))

            notification_frame.bind("<Configure>", update_scrollregion)

            unread_notifications = []

            for index, (notif_id, message, created_at, is_read) in enumerate(notifications):
                notification_box = tk.Frame(notification_frame, bd=2, relief="groove", padx=10, pady=10, width=580)
                notification_box.grid(row=index, column=0, padx=10, pady=5, sticky='ew')

                bg_color = 'white' if is_read else 'lightcoral'
                notification_box.config(bg=bg_color)

                notification_frame.grid_columnconfigure(0, weight=1)

                message_label = tk.Label(notification_box, text=message, font=('Arial', 14), wraplength=500, justify="left", bg=bg_color)
                message_label.pack(anchor='w')

                date_label = tk.Label(notification_box, text=created_at.strftime("%Y-%m-%d %H:%M:%S"), font=('Arial', 12, 'italic'), anchor='e', bg=bg_color)
                date_label.pack(anchor='e')

                if not is_read:
                    unread_notifications.append(notif_id)

            if not notifications:
                print("No notifications found.")
                tk.Label(notifications_window, text="No notifications available.", font=('Arial', 14)).pack(pady=20)

            # Messages Read button
            def mark_all_as_read():
                for notif_id in unread_notifications:
                    cursor.execute("""UPDATE principal_notifications SET is_read = TRUE WHERE id = %s""", (notif_id,))
                db.commit()
                print("All unread messages marked as read.")
                for widget in notification_frame.winfo_children():
                    widget.config(bg='white')  # Change color back to normal
                unread_notifications.clear()  # Clear the list after marking

            messages_read_button = tk.Button(notifications_window, text="Messages Read", command=mark_all_as_read)
            messages_read_button.pack(pady=10)

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        messagebox.showerror("Error", f"Failed to fetch notifications. Error: {str(err)}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
        messagebox.showerror("Error", f"An unexpected error occurred. Error: {str(e)}")

def fetch_and_display_accountant_notifications(username, role):
    notifications_window = tk.Toplevel()
    notifications_window.title("Notifications")
    notifications_window.geometry("600x400")

    tk.Label(notifications_window, text=f"Notifications for {role} ({username})", font=('Arial', 20)).pack(pady=10)

    try:
        print(f"Fetching notifications for username: {username}, role: {role}")

        # Updated query to fetch notifications for specific username, role, or general 'all' notifications
        query = """
            SELECT id, message, created_at, is_read 
            FROM accountant_notifications 
            WHERE recipient IN (%s, %s, 'all') 
            ORDER BY created_at DESC
        """
        
        print(f"Executing query with parameters: ({username}, {role})")
        cursor.execute(query, (username, role))
        notifications = cursor.fetchall()
        
        print(f"Fetched notifications: {notifications}")


        if notifications:
            scrollable_frame = tk.Frame(notifications_window)
            scrollable_frame.pack(fill=tk.BOTH, expand=True)

            scrollbar = tk.Scrollbar(scrollable_frame)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            notifications_canvas = tk.Canvas(scrollable_frame, yscrollcommand=scrollbar.set, width=580)
            notifications_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            scrollbar.config(command=notifications_canvas.yview)

            notification_frame = tk.Frame(notifications_canvas)
            notifications_canvas.create_window((0, 0), window=notification_frame, anchor='nw', width=580)

            def update_scrollregion(event):
                notifications_canvas.configure(scrollregion=notifications_canvas.bbox("all"))

            notification_frame.bind("<Configure>", update_scrollregion)

            unread_notifications = []

            for index, (notif_id, message, created_at, is_read) in enumerate(notifications):
                notification_box = tk.Frame(notification_frame, bd=2, relief="groove", padx=10, pady=10, width=580)
                notification_box.grid(row=index, column=0, padx=10, pady=5, sticky='ew')

                bg_color = 'white' if is_read else 'lightcoral'
                notification_box.config(bg=bg_color)

                notification_frame.grid_columnconfigure(0, weight=1)

                message_label = tk.Label(notification_box, text=message, font=('Arial', 14), wraplength=500, justify="left", bg=bg_color)
                message_label.pack(anchor='w')

                date_label = tk.Label(notification_box, text=created_at.strftime("%Y-%m-%d %H:%M:%S"), font=('Arial', 12, 'italic'), anchor='e', bg=bg_color)
                date_label.pack(anchor='e')

                if not is_read:
                    unread_notifications.append(notif_id)

            if not notifications:
                print("No notifications found.")
                tk.Label(notifications_window, text="No notifications available.", font=('Arial', 14)).pack(pady=20)

            # Messages Read button
            def mark_all_as_read():
                for notif_id in unread_notifications:
                    cursor.execute("""UPDATE accountant_notifications SET is_read = TRUE WHERE id = %s""", (notif_id,))
                db.commit()
                print("All unread messages marked as read.")
                for widget in notification_frame.winfo_children():
                    widget.config(bg='white')  # Change color back to normal
                unread_notifications.clear()  # Clear the list after marking

            messages_read_button = tk.Button(notifications_window, text="Messages Read", command=mark_all_as_read)
            messages_read_button.pack(pady=10)

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        messagebox.showerror("Error", f"Failed to fetch notifications. Error: {str(err)}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
        messagebox.showerror("Error", f"An unexpected error occurred. Error: {str(e)}")


def accountant_dashboard_window(username,role):
    root = tk.Tk()
    root.title("Accountant Dashboard")
    root.geometry("1366x768")

    # Header Frame
    header = tk.Frame(root, height=120, bg='#1abc9c')
    header.pack(side="top", fill="x")

    # Sidebar Frame with adjusted width
    sidebar_width = 100  # Adjust this value as needed
    sidebar = tk.Frame(root, width=sidebar_width, bg='#2c3e50')
    sidebar.pack(side="left", fill="y")

    # Main content area
    main_content = tk.Frame(root, bg='white')
    main_content.pack(side="right", expand=True, fill="both")

    def load_content(page_name):
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        if page_name == "Logout":
            root.destroy()
        elif page_name == "User Details":
            create_page5_content()  # Load buttons for roles
            # Add a function call for logout or returning to a previous screen if necessary
        else:
            tk.Label(main_content, text=f"Welcome to {page_name}", font=('Arial', 24)).pack(pady=20)
            

    def admin_update_notification_button():
        try:
            cursor.execute("""
                SELECT COUNT(*) FROM adminda_notifications 
                WHERE recipient IN (%s, 'accountant', 'all') AND is_read = FALSE
            """, (username,))
            unread_count = cursor.fetchone()[0]

            # Update button text and color based on unread notifications
            if unread_count > 0:
                button2.config(text=f"Admin Notifications ({unread_count})", bg="red", fg="white")
            else:
                button2.config(text="Admin Notifications", bg="#2c3e50", fg="white")

            # Check for unread notifications every 1 second
            button2.after(1000, admin_update_notification_button)  # Update every 1 second

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def principal_update_notification_button():
        try:
            cursor.execute("""
                SELECT COUNT(*) FROM principal_notifications 
                WHERE recipient IN (%s, 'accountant', 'all') AND is_read = FALSE
            """, (username,))
            unread_count = cursor.fetchone()[0]

            # Update button text and color based on unread notifications
            if unread_count > 0:
                button3.config(text=f"principal Notifications ({unread_count})", bg="red", fg="white")
            else:
                button3.config(text="principal Notifications", bg="#2c3e50", fg="white")

            # Check for unread notifications every 1 second
            button3.after(1000, principal_update_notification_button)  # Update every 1 second

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def open_accountant_notification_interface():
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="Enter Notification Message:", font=('Arial', 14), bg="white").pack(pady=20)
        notification_entry = tk.Text(main_content, height=5, width=50)
        notification_entry.pack(pady=10)

        tk.Label(main_content, text="Select Recipients:", font=('Arial', 14), bg="white").pack(pady=10)
        role_var = tk.StringVar(value="all")
        roles = ["all", "student", "faculty", "hod"]

        selected_role_label = tk.Label(main_content, text="", font=('Arial', 14), bg="white")
        selected_role_label.pack(pady=10)

        def on_role_change(*args):
            selected_role = role_var.get()
            selected_role_label.config(text=f"Selected Role: {selected_role.capitalize()}")

        role_dropdown = tk.OptionMenu(main_content, role_var, *roles, command=on_role_change)
        role_dropdown.pack(pady=10)

        def send_notification():
            notification_message = notification_entry.get("1.0", "end").strip()
            selected_role = role_var.get()

            if not notification_message:
                messagebox.showerror("Error", "Notification message cannot be empty.")
                return

            try:
                recipients = []
                if selected_role == "all":
                    cursor.execute("SELECT username FROM users")
                else:
                    cursor.execute("SELECT username FROM users WHERE role = %s", (selected_role,))
                recipients = cursor.fetchall()

                # Admin user (if applicable)
                accountant_username = 'accountant'
                if selected_role == "all" or selected_role in ["principal", "faculty", "accountant", "hod"]:
                    recipients = [(accountant_username,)] + recipients if (accountant_username,) not in recipients else recipients

                if recipients:
                    for recipient in recipients:
                        cursor.execute(
                            "INSERT INTO accountant_notifications (message, sender, recipient) VALUES (%s, %s, %s)",
                            (notification_message, accountant_username, recipient[0])
                        )
                    db.commit()
                    messagebox.showinfo("Success", f"Notification sent to all {selected_role.capitalize()}s.")
                else:
                    messagebox.showinfo("Info", f"No {selected_role.capitalize()}s found to send notifications.")

                notification_entry.delete("1.0", "end")

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Failed to send notification. Error: {str(err)}")

        tk.Button(main_content, text="Send Notification", command=send_notification, font=('Arial', 14),
                  bg='#1abc9c', fg='white').pack(pady=20)

    def group_chat_button(username):
        try:
            # Query to count unread messages for the current user in the group chat
            cursor.execute("""
                SELECT COUNT(*) FROM groupp_chat_messages 
                WHERE receiver_user_id IS NULL AND is_read = FALSE
            """)
            unread_count = cursor.fetchone()[0]

            # Update button text and color based on unread messages
            if unread_count > 0:
                button5.config(text=f"Group Chat ({unread_count})", bg="red", fg="white")
            else:
                button5.config(text="Group Chat", bg="#2c3e50", fg="white")

            # Check for unread messages every 1 second
            button5.after(1000, group_chat_button, username)  # Update every 1 second

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def on_group_chat_click(username, main_content):
        # Open the group chat sidebar
        open_group_chat_sidebar(username, main_content)

        # Reset the button color to its normal state after clicking
        button5.config(bg="#2c3e50", fg="white")

        # Optionally, mark all unread messages as read
        try:
            cursor.execute("""
                UPDATE groupp_chat_messages 
                SET is_read = TRUE 
                WHERE receiver_user_id IS NULL AND is_read = FALSE
            """)
            db.commit()
        except mysql.connector.Error as err:
            print(f"Error marking messages as read: {err}")

    def create_page5_content():
        # Create a new content for Page 5
        page5_content = tk.Frame(main_content, bg='white')
        page5_content.pack(expand=True, fill="both")

        tk.Label(page5_content, text="View Details", font=('Arial', 24)).pack(pady=20)

        button_width = 20  # Set desired width
        button_height = 2  # Set desired height
        dark_green = '#006400'  # Dark green color
        light_green = '#90EE90'  # Light green color (for active background)

        student_button = tk.Button(page5_content, text='Student', font=('Arial', 14), bg=dark_green, fg='white',
                                width=button_width, height=button_height, activebackground=light_green, command=open_student_window)
        student_button.pack(pady=10, padx=20)

        faculty_button = tk.Button(page5_content, text='Faculty', font=('Arial', 14), bg=dark_green, fg='white',
                           width=button_width, height=button_height, activebackground=light_green, command=open_faculty_window)

        faculty_button.pack(pady=10, padx=20)

        hod_button = tk.Button(page5_content, text='HOD', font=('Arial', 14), bg=dark_green, fg='white',
                       width=button_width, height=button_height, activebackground=light_green, command=open_hod_window)

        hod_button.pack(pady=10, padx=20)

    def open_student_window():
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=back_to_page5,
                                bg='#8B008B', fg='white', width=25, height=3,
                                activebackground='#DDA0DD')  # Dark magenta background, light magenta on click
        back_button.pack(pady=10)

        view_button = tk.Button(main_content, text='View All Students', font=('Arial', 14), command=view_students,
                                bg='#8B008B', fg='white', width=25, height=3,
                                activebackground='#DDA0DD')  # Dark magenta background, light magenta on click
        view_button.pack(pady=10)

    def open_student_details(username):
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="Student Details", font=('Arial', 24)).pack(pady=20)

        # Create a frame for the Treeview and scrollbar with the specified size
        detail_frame = tk.Frame(main_content)
        detail_frame.pack(pady=10)

        # Set the size of the frame using the grid geometry manager
        detail_frame.grid_propagate(False)  # Prevent the frame from resizing to fit contents
        detail_frame.config(width=1100, height=500)

        # Create a Treeview widget for student details
        columns = ("Field", "Details")
        tree = ttk.Treeview(detail_frame, columns=columns, show="headings")
        tree.pack(side='left', fill='both', expand=True)

        # Configure the column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=250)  # Adjust width as needed

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(detail_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscroll=scrollbar.set)

        try:
            # Fetch student details for the given username
            cursor.execute("""
                SELECT s.student_id, s.student_name, u.username, u.role, 
                    s.admission_date, s.department, s.semester, 
                    s.admission_number, s.roll_no, s.gender, s.dob, 
                    s.blood_group, s.father_name, s.father_occupation, 
                    s.mother_name, s.mother_occupation, s.address, 
                    s.city, s.country, s.religion, s.caste, 
                    s.pin_code, s.state, s.email, s.phone, 
                    s.parent_phone, s.guardian_name, 
                    s.guardian_relationship, s.guardian_phone, 
                    s.guardian_address 
                FROM students s 
                JOIN users u ON s.user_id = u.id 
                WHERE u.username = %s
            """, (username,))
            student = cursor.fetchone()

            if not student:
                messagebox.showinfo("Info", "No student details found for this username.")
                return

            # Display student details in the Treeview
            field_labels = [
                "Student ID", "Student Name", "Username", "Role",
                "Admission Date", "Department", "Semester", 
                "Admission Number", "Roll No", "Gender", "DOB", 
                "Blood Group", "Father's Name", "Father's Occupation", 
                "Mother's Name", "Mother's Occupation", "Address", 
                "City", "Country", "Religion", "Caste", 
                "Pin Code", "State", "Email", "Phone", 
                "Parent Phone", "Guardian Name", 
                "Guardian Relationship", "Guardian Phone", 
                "Guardian Address"
            ]
            
            # Insert student details into the Treeview
            for label, value in zip(field_labels, student):
                tree.insert("", tk.END, values=(label, value))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        # Back button to return to the previous page
        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=back_to_page5, bg='blue', fg='white')
        back_button.pack(side='left', padx=10, pady=10)

    def show_login_window():
        # Create a new window for login
        login_window = tk.Toplevel()
        login_window.title("Login")

        tk.Label(login_window, text="Enter Username:", font=('Arial', 14)).pack(pady=10)

        username_entry = tk.Entry(login_window, font=('Arial', 14))
        username_entry.pack(pady=10)

        def on_login():
            username = username_entry.get()
            if username:
                cursor.execute("SELECT role FROM users WHERE username = %s", (username,))
                role = cursor.fetchone()

                if role and role[0] == 'student':
                    open_student_details(username)
                    login_window.destroy()  # Close the login window
                else:
                    messagebox.showerror("Error", "Username does not belong to a student.")
            else:
                messagebox.showwarning("Warning", "Please enter a username.")

        login_button = tk.Button(login_window, text="Login", font=('Arial', 14), command=on_login)
        login_button.pack(pady=10)
    # Declare the tree variable globally
    
    tree = None
    def view_students():
        global tree  # Declare the tree variable as global

        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="All Student Details", font=('Arial', 24)).pack(pady=20)

        # Create a frame for the Treeview and scrollbar
        student_frame = tk.Frame(main_content)
        student_frame.pack(pady=10)

        # Create a Treeview widget for listing students
        columns = ("Student ID", "Student Name", "Username", "Role", "Department", "Semester")
        tree = ttk.Treeview(student_frame, columns=columns, show="headings")
        tree.pack(side='left', fill='both', expand=True)

        # Configure the column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=150)  # Adjust width as needed

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(student_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscroll=scrollbar.set)

        # Set a minimum size for the Treeview frame
        student_frame.configure(width=1100, height=400)

        # Create a frame for the department and semester selection
        selection_frame = tk.Frame(main_content)
        selection_frame.pack(pady=20)

        # Create a StringVar to hold the selected department
        department_var = tk.StringVar()
        
        # Create a StringVar to hold the selected semester
        semester_var = tk.StringVar()

        # Create a frame for department section (combobox and button)
        department_frame = tk.Frame(selection_frame)
        department_frame.pack(side='left', padx=20)

        # Create a Combobox for department selection
        department_combobox = ttk.Combobox(department_frame, textvariable=department_var, font=("Helvetica", 12), state='readonly')
        department_combobox['values'] = [
            "B.E Civil Engineering",
            "B.E Computer Science Engineering",
            "B.E Electrical and Electronics Engineering",
            "B.E Electronics and Communication Engineering",
            "B.Tech Information Technology",
            "B.E Mechanical Engineering",
            "B.Tech Artificial Intelligence and Data Science",
            "B.Tech Computer Science and Business Systems",
            "Marine Engineering",
            "Aerospace Engineering",
            "Master of Business Administration (MBA)",
            "Master of Computer Application (MCA)",
            "M.E Power Electronics and Drives",
            "M.E Communication systems",
            "M.E Computer Science Engineering",
            "M.E Engineering Design"
        ]
        department_combobox.pack(padx=10)

        # Create Confirm button for department selection below the department combobox
        confirm_department_button = tk.Button(department_frame, text='Confirm Department', font=("Helvetica", 12), 
                                            command=lambda: filter_students_by_department(department_var.get()), 
                                            bg='blue', fg='white')
        confirm_department_button.pack(pady=10)

        # Create a frame for semester section (combobox and button)
        semester_frame = tk.Frame(selection_frame)
        semester_frame.pack(side='left', padx=20)

        # Create a Combobox for semester selection
        semester_combobox = ttk.Combobox(semester_frame, textvariable=semester_var, font=("Helvetica", 12), state='readonly')
        semester_combobox['values'] = [
            "Semester 1", "Semester 2", "Semester 3", "Semester 4", 
            "Semester 5", "Semester 6", "Semester 7", "Semester 8"
        ]
        semester_combobox.pack(padx=10)

        # Create Confirm button for semester selection below the semester combobox
        confirm_semester_button = tk.Button(semester_frame, text='Confirm Semester', font=("Helvetica", 12), 
                                            command=lambda: filter_students_by_semester(semester_var.get()), 
                                            bg='blue', fg='white')
        confirm_semester_button.pack(pady=10)

        # Create Back button to return to the previous page
        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=open_student_window, bg='blue', fg='white')
        back_button.pack(side='left', padx=10, pady=10)

        # Create View button to open login window
        view_button = tk.Button(main_content, text='View', font=('Arial', 14), command=show_login_window, bg='blue', fg='white')
        view_button.pack(side='left', padx=10, pady=10)

        # Fetch and display all students initially
        display_all_students()


    def display_all_students():
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        try:
            # Execute the query to fetch all students
            cursor.execute("""
                SELECT s.student_id, s.student_name, u.username, u.role, s.department, s.semester 
                FROM students s 
                JOIN users u ON s.user_id = u.id
            """)
            students = cursor.fetchall()

            # Insert all student details into the Treeview
            for student_id, student_name, username, role, department, semester in students:
                tree.insert("", tk.END, values=(student_id, student_name, username, role, department, semester))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while fetching student details: {str(e)}")

    def filter_students_by_department(selected_department):
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        if selected_department:
            try:
                print(f"Filtering students by department: {selected_department}")  # Debugging output
                # Execute the query to fetch students from the selected department
                cursor.execute("""
                    SELECT s.student_id, s.student_name, u.username, u.role, s.department, s.semester 
                    FROM students s 
                    JOIN users u ON s.user_id = u.id 
                    WHERE s.department = %s
                """, (selected_department,))
                students = cursor.fetchall()

                if not students:
                    messagebox.showinfo("Info", "No students found in the selected department.")
                    return

                # Insert filtered student details into the Treeview
                for student_id, student_name, username, role, department, semester in students:
                    tree.insert("", tk.END, values=(student_id, student_name, username, role, department, semester))

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while fetching student details: {str(e)}")

    def filter_students_by_semester(selected_semester):
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        if selected_semester:
            try:
                print(f"Filtering students by semester: {selected_semester}")  # Debugging output
                # Execute the query to fetch students from the selected semester
                cursor.execute("""
                    SELECT s.student_id, s.student_name, u.username, u.role, s.department, s.semester 
                    FROM students s 
                    JOIN users u ON s.user_id = u.id 
                    WHERE s.semester = %s
                """, (selected_semester,))
                students = cursor.fetchall()

                if not students:
                    messagebox.showinfo("Info", "No students found in the selected semester.")
                    return

                # Insert filtered student details into the Treeview
                for student_id, student_name, username, role, department, semester in students:
                    tree.insert("", tk.END, values=(student_id, student_name, username, role, department, semester))

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while fetching student details: {str(e)}")

    def show_users_by_role(role):
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        back_button = tk.Button(main_content, text="Back", font=('Arial', 12), command=display_role_buttons)
        back_button.pack(pady=10, anchor='w')

        tk.Label(main_content, text=f"Users in Role: {role}", font=('Arial', 24)).pack(pady=20)

        tree = ttk.Treeview(main_content, columns=("ID", "Username", "Role", "Action"), show="headings", height=10)
        tree.heading("ID", text="ID")
        tree.heading("Username", text="Username")
        tree.heading("Role", text="Role")
        tree.heading("Action", text="Action")
        tree.column("ID", width=50, anchor='center')
        tree.column("Username", width=200, anchor='center')
        tree.column("Role", width=100, anchor='center')
        tree.column("Action", width=100, anchor='center')
        tree.pack(pady=20, fill="both", expand=True)

        scrollbar = ttk.Scrollbar(main_content, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        try:
            cursor.execute("SELECT id, username, role FROM users WHERE role = %s", (role,))
            users = cursor.fetchall()

            for user in users:
                tree.insert("", tk.END, values=user + ("View",))

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to retrieve user details: {err}")

        tree.bind("<ButtonRelease-1>", lambda event: handle_treeview_click(tree, event))

    def handle_treeview_click(tree, event):
        item = tree.selection()
        if item:
            user_data = tree.item(item, 'values')
            user_id = user_data[0]
            messagebox.showinfo("User Info", f"Viewing details for User ID: {user_id}")

    def back_to_page5():
        for widget in main_content.winfo_children():
            widget.destroy()
        create_page5_content()

    def display_role_buttons():
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        # Create buttons for each role
        roles = ["Student", "Faculty", "HOD", "Principal", "Accountant", "Admin"]
        tk.Label(main_content, text="Select a Role", font=('Arial', 24)).pack(pady=20)

        for role in roles:
            role_button = tk.Button(main_content, text=role, font=('Arial', 14), command=lambda r=role: show_users_by_role(r))
            role_button.pack(pady=5)

        back_button = tk.Button(main_content, text="Back", font=('Arial', 12), command=back_to_page5)
        back_button.pack(pady=10)

###########################################################################################################################

    def open_faculty_window():
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=back_to_page5,
                                bg='#8B008B', fg='white', width=25, height=3,
                                activebackground='#DDA0DD')  # Dark magenta background, light magenta on click
        back_button.pack(pady=10)

        view_button = tk.Button(main_content, text='View All Faculties', font=('Arial', 14), command=view_faculty,
                                bg='#8B008B', fg='white', width=25, height=3,
                                activebackground='#DDA0DD')  # Dark magenta background, light magenta on click
        view_button.pack(pady=10)

    def open_faculty_details(username):
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="Faculty Details", font=('Arial', 24)).pack(pady=20)

        # Create a frame for the Treeview and scrollbar with the specified size
        detail_frame = tk.Frame(main_content)
        detail_frame.pack(pady=10)

        # Set the size of the frame using the grid geometry manager
        detail_frame.grid_propagate(False)  # Prevent the frame from resizing to fit contents
        detail_frame.config(width=1100, height=500)

        # Create a Treeview widget for student details
        columns = ("Field", "Details")
        tree = ttk.Treeview(detail_frame, columns=columns, show="headings")
        tree.pack(side='left', fill='both', expand=True)

        # Configure the column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=250)  # Adjust width as needed

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(detail_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscroll=scrollbar.set)

        try:
            # Fetch faculty details for the given username
            cursor.execute("""
                SELECT f.faculty_id, f.faculty_name, u.username, u.role, 
                    f.department, f.faculty_gender, f.faculty_dob, 
                    f.faculty_blood_group, f.faculty_marital_status, 
                    f.faculty_job_position, f.faculty_address, 
                    f.faculty_city, f.faculty_country, f.faculty_pin_code, 
                    f.faculty_state, f.faculty_email, f.faculty_phone, 
                    f.faculty_guardian_name, f.faculty_guardian_relationship, 
                    f.faculty_guardian_phone, f.faculty_guardian_address 
                FROM faculty f
                JOIN users u ON f.user_id = u.id
                WHERE u.username = %s
            """, (username,))
            faculty = cursor.fetchone()

            if not faculty:
                messagebox.showinfo("Info", "No faculty details found for this username.")
                return

            # Display faculty details in the Treeview (adjust fields and labels as needed)
            field_labels = [
                "Faculty ID", "Faculty Name", "Username", "Role", 
                "Department", "Gender", "DOB", "Blood Group", 
                "Marital Status", "Job Position", "Address", 
                "City", "Country", "Pin Code", "State", 
                "Email", "Phone", "Guardian Name", 
                "Guardian Relationship", "Guardian Phone", 
                "Guardian Address"
            ]

            # Insert student details into the Treeview
            for label, value in zip(field_labels, faculty):
                tree.insert("", tk.END, values=(label, value))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        # Back button to return to the previous page
        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=back_to_page5, bg='blue', fg='white')
        back_button.pack(side='left', padx=10, pady=10)

    def show_faculty_login_window():
        # Create a new window for login
        login_window = tk.Toplevel()
        login_window.title("Login")

        tk.Label(login_window, text="Enter Username:", font=('Arial', 14)).pack(pady=10)

        username_entry = tk.Entry(login_window, font=('Arial', 14))
        username_entry.pack(pady=10)

        def on_login():
            username = username_entry.get()
            if username:
                cursor.execute("SELECT role FROM users WHERE username = %s", (username,))
                role = cursor.fetchone()

                if role and role[0] == 'faculty':
                    open_faculty_details(username)
                    login_window.destroy()  # Close the login window
                else:
                    messagebox.showerror("Error", "Username does not belong to a faculty.")
            else:
                messagebox.showwarning("Warning", "Please enter a username.")

        login_button = tk.Button(login_window, text="Login", font=('Arial', 14), command=on_login)
        login_button.pack(pady=10)
    # Declare the tree variable globally

    tree = None
    def view_faculty():
        global tree  # Declare the tree variable as global

        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="All faculty Details", font=('Arial', 24)).pack(pady=20)

        # Create a frame for the Treeview and scrollbar
        student_frame = tk.Frame(main_content)
        student_frame.pack(pady=10)

        # Create a Treeview widget for listing students
        columns = ("faculty ID", "faculty Name", "Username", "Role", "Department")
        tree = ttk.Treeview(student_frame, columns=columns, show="headings")
        tree.pack(side='left', fill='both', expand=True)

        # Configure the column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=150)  # Adjust width as needed

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(student_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscroll=scrollbar.set)

        # Set a minimum size for the Treeview frame
        student_frame.configure(width=1100, height=400)

        # Create a frame for the department and semester selection
        selection_frame = tk.Frame(main_content)
        selection_frame.pack(pady=20)

        # Create a StringVar to hold the selected department
        department_var = tk.StringVar()

        # Create a frame for department section (combobox and button)
        department_frame = tk.Frame(selection_frame)
        department_frame.pack(side='left', padx=20)

        # Create a Combobox for department selection
        department_combobox = ttk.Combobox(department_frame, textvariable=department_var, font=("Helvetica", 12), state='readonly')
        department_combobox['values'] = [
            "B.E Civil Engineering",
            "B.E Computer Science Engineering",
            "B.E Electrical and Electronics Engineering",
            "B.E Electronics and Communication Engineering",
            "B.Tech Information Technology",
            "B.E Mechanical Engineering",
            "B.Tech Artificial Intelligence and Data Science",
            "B.Tech Computer Science and Business Systems",
            "Marine Engineering",
            "Aerospace Engineering",
            "Master of Business Administration (MBA)",
            "Master of Computer Application (MCA)",
            "M.E Power Electronics and Drives",
            "M.E Communication systems",
            "M.E Computer Science Engineering",
            "M.E Engineering Design"
        ]
        department_combobox.pack(padx=10)

        # Create Confirm button for department selection below the department combobox
        confirm_department_button = tk.Button(department_frame, text='Confirm Department', font=("Helvetica", 12), 
                                            command=lambda: filter_faculty_by_department(department_var.get()), 
                                            bg='blue', fg='white')
        confirm_department_button.pack(pady=10)

        # Create Back button to return to the previous page
        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=open_faculty_window, bg='blue', fg='white')
        back_button.pack(side='left', padx=10, pady=10)

        # Create View button to open login window
        view_button = tk.Button(main_content, text='View', font=('Arial', 14), command=show_faculty_login_window, bg='blue', fg='white')
        view_button.pack(side='left', padx=10, pady=10)

        # Fetch and display all students initially
        display_all_faculty()


    def display_all_faculty():
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        try:
            # Execute the query to fetch all students
            cursor.execute("""
                SELECT s.faculty_id, s.faculty_name, u.username, u.role, s.department 
                FROM faculty s 
                JOIN users u ON s.user_id = u.id
            """)
            faculty = cursor.fetchall()

            # Insert all student details into the Treeview
            for faculty_id, faculty_name, username, role, department in faculty:
                tree.insert("", tk.END, values=(faculty_id, faculty_name, username, role, department))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while fetching student details: {str(e)}")

    def filter_faculty_by_department(selected_department):
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        if selected_department:
            try:
                print(f"Filtering students by department: {selected_department}")  # Debugging output
                # Execute the query to fetch students from the selected department
                cursor.execute("""
                    SELECT s.faculty_id, s.faculty_name, u.username, u.role, s.department 
                    FROM faculty s 
                    JOIN users u ON s.user_id = u.id 
                    WHERE s.department = %s
                """, (selected_department,))
                faculty = cursor.fetchall()

                if not faculty:
                    messagebox.showinfo("Info", "No faculty found in the selected department.")
                    return

                # Insert filtered student details into the Treeview
                for faculty_id, faculty_name, username, role, department in faculty:
                    tree.insert("", tk.END, values=(faculty_id, faculty_name, username, role, department))

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while fetching faculty details: {str(e)}")

##########################################################################################################################
    def open_hod_window():
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=back_to_page5,
                                bg='#8B008B', fg='white', width=25, height=3,
                                activebackground='#DDA0DD')  # Dark magenta background, light magenta on click
        back_button.pack(pady=10)

        view_button = tk.Button(main_content, text='View All HOD', font=('Arial', 14), command=view_hod,
                                bg='#8B008B', fg='white', width=25, height=3,
                                activebackground='#DDA0DD')  # Dark magenta background, light magenta on click
        view_button.pack(pady=10)

    def open_hod_details(username):
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="HOD Details", font=('Arial', 24)).pack(pady=20)

        # Create a frame for the Treeview and scrollbar with the specified size
        detail_frame = tk.Frame(main_content)
        detail_frame.pack(pady=10)

        # Set the size of the frame using the grid geometry manager
        detail_frame.grid_propagate(False)  # Prevent the frame from resizing to fit contents
        detail_frame.config(width=1100, height=500)

        # Create a Treeview widget for student details
        columns = ("Field", "Details")
        tree = ttk.Treeview(detail_frame, columns=columns, show="headings")
        tree.pack(side='left', fill='both', expand=True)

        # Configure the column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=250)  # Adjust width as needed

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(detail_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscroll=scrollbar.set)

        try:
            # Fetch faculty details for the given username
            cursor.execute("""
                SELECT f.faculty_id, f.faculty_name, u.username, u.role, 
                    f.department, f.faculty_gender, f.faculty_dob, 
                    f.faculty_blood_group, f.faculty_marital_status, 
                    f.faculty_job_position, f.faculty_address, 
                    f.faculty_city, f.faculty_country, f.faculty_pin_code, 
                    f.faculty_state, f.faculty_email, f.faculty_phone, 
                    f.faculty_guardian_name, f.faculty_guardian_relationship, 
                    f.faculty_guardian_phone, f.faculty_guardian_address 
                FROM hod f
                JOIN users u ON f.user_id = u.id
                WHERE u.username = %s
            """, (username,))
            faculty = cursor.fetchone()

            if not faculty:
                messagebox.showinfo("Info", "No HOD details found for this username.")
                return

            # Display faculty details in the Treeview (adjust fields and labels as needed)
            field_labels = [
                "Faculty ID", "Faculty Name", "Username", "Role", 
                "Department", "Gender", "DOB", "Blood Group", 
                "Marital Status", "Job Position", "Address", 
                "City", "Country", "Pin Code", "State", 
                "Email", "Phone", "Guardian Name", 
                "Guardian Relationship", "Guardian Phone", 
                "Guardian Address"
            ]

            # Insert student details into the Treeview
            for label, value in zip(field_labels, faculty):
                tree.insert("", tk.END, values=(label, value))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        # Back button to return to the previous page
        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=back_to_page5, bg='blue', fg='white')
        back_button.pack(side='left', padx=10, pady=10)

    def show_hod_login_window():
        # Create a new window for login
        login_window = tk.Toplevel()
        login_window.title("Login")

        tk.Label(login_window, text="Enter Username:", font=('Arial', 14)).pack(pady=10)

        username_entry = tk.Entry(login_window, font=('Arial', 14))
        username_entry.pack(pady=10)

        def on_login():
            username = username_entry.get()
            if username:
                cursor.execute("SELECT role FROM users WHERE username = %s", (username,))
                role = cursor.fetchone()

                if role and role[0] == 'hod':
                    open_hod_details(username)
                    login_window.destroy()  # Close the login window
                else:
                    messagebox.showerror("Error", "Username does not belong to a hod.")
            else:
                messagebox.showwarning("Warning", "Please enter a username.")

        login_button = tk.Button(login_window, text="Login", font=('Arial', 14), command=on_login)
        login_button.pack(pady=10)
    # Declare the tree variable globally

    tree = None
    def view_hod():
        global tree  # Declare the tree variable as global

        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="All HOD Details", font=('Arial', 24)).pack(pady=20)

        # Create a frame for the Treeview and scrollbar
        student_frame = tk.Frame(main_content)
        student_frame.pack(pady=10)

        # Create a Treeview widget for listing students
        columns = ("faculty ID", "faculty Name", "Username", "Role", "Department")
        tree = ttk.Treeview(student_frame, columns=columns, show="headings")
        tree.pack(side='left', fill='both', expand=True)

        # Configure the column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=150)  # Adjust width as needed

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(student_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscroll=scrollbar.set)

        # Set a minimum size for the Treeview frame
        student_frame.configure(width=1100, height=400)

        # Create a frame for the department and semester selection
        selection_frame = tk.Frame(main_content)
        selection_frame.pack(pady=20)

        # Create a StringVar to hold the selected department
        department_var = tk.StringVar()

        # Create a frame for department section (combobox and button)
        department_frame = tk.Frame(selection_frame)
        department_frame.pack(side='left', padx=20)

        # Create a Combobox for department selection
        department_combobox = ttk.Combobox(department_frame, textvariable=department_var, font=("Helvetica", 12), state='readonly')
        department_combobox['values'] = [
            "B.E Civil Engineering",
            "B.E Computer Science Engineering",
            "B.E Electrical and Electronics Engineering",
            "B.E Electronics and Communication Engineering",
            "B.Tech Information Technology",
            "B.E Mechanical Engineering",
            "B.Tech Artificial Intelligence and Data Science",
            "B.Tech Computer Science and Business Systems",
            "Marine Engineering",
            "Aerospace Engineering",
            "Master of Business Administration (MBA)",
            "Master of Computer Application (MCA)",
            "M.E Power Electronics and Drives",
            "M.E Communication systems",
            "M.E Computer Science Engineering",
            "M.E Engineering Design"
        ]
        department_combobox.pack(padx=10)

        # Create Confirm button for department selection below the department combobox
        confirm_department_button = tk.Button(department_frame, text='Confirm Department', font=("Helvetica", 12), 
                                            command=lambda: filter_hod_by_department(department_var.get()), 
                                            bg='blue', fg='white')
        confirm_department_button.pack(pady=10)

        # Create Back button to return to the previous page
        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=open_hod_window, bg='blue', fg='white')
        back_button.pack(side='left', padx=10, pady=10)

        # Create View button to open login window
        view_button = tk.Button(main_content, text='View', font=('Arial', 14), command=show_hod_login_window, bg='blue', fg='white')
        view_button.pack(side='left', padx=10, pady=10)

        # Fetch and display all students initially
        display_all_hod()


    def display_all_hod():
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        try:
            # Execute the query to fetch all students
            cursor.execute("""
                SELECT s.faculty_id, s.faculty_name, u.username, u.role, s.department 
                FROM hod s 
                JOIN users u ON s.user_id = u.id
            """)
            faculty = cursor.fetchall()

            # Insert all student details into the Treeview
            for faculty_id, faculty_name, username, role, department in faculty:
                tree.insert("", tk.END, values=(faculty_id, faculty_name, username, role, department))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while fetching student details: {str(e)}")

    def filter_hod_by_department(selected_department):
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        if selected_department:
            try:
                print(f"Filtering students by department: {selected_department}")  # Debugging output
                # Execute the query to fetch students from the selected department
                cursor.execute("""
                    SELECT s.faculty_id, s.faculty_name, u.username, u.role, s.department 
                    FROM hod s 
                    JOIN users u ON s.user_id = u.id 
                    WHERE s.department = %s
                """, (selected_department,))
                faculty = cursor.fetchall()

                if not faculty:
                    messagebox.showinfo("Info", "No hod found in the selected department.")
                    return

                # Insert filtered student details into the Treeview
                for faculty_id, faculty_name, username, role, department in faculty:
                    tree.insert("", tk.END, values=(faculty_id, faculty_name, username, role, department))

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while fetching hod details: {str(e)}")

    # Sidebar buttons
    button1 = tk.Button(sidebar, width=12, text='  Chat  ', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button1.pack(fill='x')
    button1.config(command=lambda: open_staff_chat_sidebar(username, root))
    button1.bind("<Enter>", lambda event: button1.configure(bg='blue'))
    button1.bind("<Leave>", lambda event: button1.configure(bg='#2c3e50'))

    button2 = tk.Button(sidebar, text='  Admin Notifications  ', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button2.pack(fill='x')
    button2.config(command=lambda: fetch_and_display_notifications(username, 'accountant'))  # Pass both username and role
    button2.bind("<Enter>", lambda event: button2.configure(bg='blue'))
    button2.bind("<Leave>", lambda event: button2.configure(bg='#2c3e50'))


    button3 = tk.Button(sidebar, text='principal nottification', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button3.pack(fill='x')
    button3.config(command=lambda: fetch_and_display_principal_notifications(username,"accountant"))
    button3.bind("<Enter>", lambda event: button3.configure(bg='blue'))
    button3.bind("<Leave>", lambda event: button3.configure(bg='#2c3e50'))

    button4 = tk.Button(sidebar, text='Page 4', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button4.pack(fill='x')
    button4.config(command=lambda: open_accountant_notification_interface)
    button4.bind("<Enter>", lambda event: button4.configure(bg='blue'))
    button4.bind("<Leave>", lambda event: button4.configure(bg='#2c3e50'))

    button5 = tk.Button(sidebar, text='group chat', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button5.pack(fill='x')
    button5.config(command=lambda: on_group_chat_click(username,main_content))
    button5.bind("<Enter>", lambda event: button5.configure(bg='blue'))
    button5.bind("<Leave>", lambda event: button5.configure(bg='#2c3e50'))

    button6 = tk.Button(sidebar, text='User Details', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button6.pack(fill='x')
    button6.config(command=lambda: load_content('User Details'))
    button6.bind("<Enter>", lambda event: button6.configure(bg='blue'))
    button6.bind("<Leave>", lambda event: button6.configure(bg='#2c3e50'))

    button7 = tk.Button(sidebar, text='Page 7', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button7.pack(fill='x')
    button7.config(command=lambda: load_content('Page 7'))
    button7.bind("<Enter>", lambda event: button7.configure(bg='blue'))
    button7.bind("<Leave>", lambda event: button7.configure(bg='#2c3e50'))

    button8 = tk.Button(sidebar, text='Back', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button8.pack(fill='x')
    button8.config(command=lambda: switch_window(root,login_window))
    button8.bind("<Enter>", lambda event: button8.configure(bg='blue'))
    button8.bind("<Leave>", lambda event: button8.configure(bg='#2c3e50'))

    button_logout = tk.Button(sidebar, text='Logout', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button_logout.pack(fill='x')
    button_logout.config(command=lambda: load_content('Logout'))
    button_logout.bind("<Enter>", lambda event: button_logout.configure(bg='blue'))
    button_logout.bind("<Leave>", lambda event: button_logout.configure(bg='#2c3e50'))

        # Initial call to set the notification button based on unread messages
    admin_update_notification_button()

    principal_update_notification_button()

    open_accountant_notification_interface()

    group_chat_button(username)

    root.mainloop()

# Principal Dashboard
def principal_dashboard_window(username,role):
    root = tk.Tk()
    root.title("Principal Dashboard")
    root.geometry("1366x768")

    # Header Frame
    header = tk.Frame(root, height=120, bg='#1abc9c')
    header.pack(side="top", fill="x")

    # Sidebar Frame with adjusted width
    sidebar_width = 100  # Adjust this value as needed
    sidebar = tk.Frame(root, width=sidebar_width, bg='#2c3e50')
    sidebar.pack(side="left", fill="y")

    # Main content area
    main_content = tk.Frame(root, bg='white')
    main_content.pack(side="right", expand=True, fill="both")

    def load_content(page_name):
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        if page_name == "Logout":
            root.destroy()
        elif page_name == "view details":
            create_page5_content()
        else:
            tk.Label(main_content, text=f"Welcome to {page_name}", font=('Arial', 24)).pack(pady=20)

    def open_principal_notification_interface():
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="Enter Notification Message:", font=('Arial', 14), bg="white").pack(pady=20)
        notification_entry = tk.Text(main_content, height=5, width=50)
        notification_entry.pack(pady=10)

        tk.Label(main_content, text="Select Recipients:", font=('Arial', 14), bg="white").pack(pady=10)
        role_var = tk.StringVar(value="all")
        roles = ["all", "student", "faculty", "accountant", "hod"]

        selected_role_label = tk.Label(main_content, text="", font=('Arial', 14), bg="white")
        selected_role_label.pack(pady=10)

        def on_role_change(*args):
            selected_role = role_var.get()
            selected_role_label.config(text=f"Selected Role: {selected_role.capitalize()}")

        role_dropdown = tk.OptionMenu(main_content, role_var, *roles, command=on_role_change)
        role_dropdown.pack(pady=10)

        def send_notification():
            notification_message = notification_entry.get("1.0", "end").strip()
            selected_role = role_var.get()

            if not notification_message:
                messagebox.showerror("Error", "Notification message cannot be empty.")
                return

            try:
                recipients = []
                if selected_role == "all":
                    cursor.execute("SELECT username FROM users")
                else:
                    cursor.execute("SELECT username FROM users WHERE role = %s", (selected_role,))
                recipients = cursor.fetchall()

                # Admin user (if applicable)
                principal_username = 'principal'
                if selected_role == "all" or selected_role in ["student", "faculty", "accountant", "hod"]:
                    recipients = [(principal_username,)] + recipients if (principal_username,) not in recipients else recipients

                if recipients:
                    for recipient in recipients:
                        cursor.execute(
                            "INSERT INTO principal_notifications (message, sender, recipient) VALUES (%s, %s, %s)",
                            (notification_message, principal_username, recipient[0])
                        )
                    db.commit()
                    messagebox.showinfo("Success", f"Notification sent to all {selected_role.capitalize()}s.")
                else:
                    messagebox.showinfo("Info", f"No {selected_role.capitalize()}s found to send notifications.")

                notification_entry.delete("1.0", "end")

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Failed to send notification. Error: {str(err)}")

        tk.Button(main_content, text="Send Notification", command=send_notification, font=('Arial', 14),
                  bg='#1abc9c', fg='white').pack(pady=20)
        
    def admin_update_notification_button():
        try:
            cursor.execute("""
                SELECT COUNT(*) FROM adminda_notifications 
                WHERE recipient IN (%s, 'accountant', 'all') AND is_read = FALSE
            """, (username,))
            unread_count = cursor.fetchone()[0]

            # Update button text and color based on unread notifications
            if unread_count > 0:
                button2.config(text=f"Admin Notifications ({unread_count})", bg="red", fg="white")
            else:
                button2.config(text="Admin Notifications", bg="#2c3e50", fg="white")

            # Check for unread notifications every 1 second
            button2.after(1000, admin_update_notification_button)  # Update every 1 second

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def group_chat_button(username):
        try:
            # Query to count unread messages for the current user in the group chat
            cursor.execute("""
                SELECT COUNT(*) FROM groupp_chat_messages 
                WHERE receiver_user_id IS NULL AND is_read = FALSE
            """)
            unread_count = cursor.fetchone()[0]

            # Update button text and color based on unread messages
            if unread_count > 0:
                button4.config(text=f"Group Chat ({unread_count})", bg="red", fg="white")
            else:
                button4.config(text="Group Chat", bg="#2c3e50", fg="white")

            # Check for unread messages every 1 second
            button4.after(1000, group_chat_button, username)  # Update every 1 second

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def on_group_chat_click(username, main_content):
        # Open the group chat sidebar
        open_group_chat_sidebar(username, main_content)

        # Reset the button color to its normal state after clicking
        button4.config(bg="#2c3e50", fg="white")

        # Optionally, mark all unread messages as read
        try:
            cursor.execute("""
                UPDATE groupp_chat_messages 
                SET is_read = TRUE 
                WHERE receiver_user_id IS NULL AND is_read = FALSE
            """)
            db.commit()
        except mysql.connector.Error as err:
            print(f"Error marking messages as read: {err}")

#################################################################################################################

    def create_page5_content():
        # Create a new content for Page 5
        page5_content = tk.Frame(main_content, bg='white')
        page5_content.pack(expand=True, fill="both")

        tk.Label(page5_content, text="View Details", font=('Arial', 24)).pack(pady=20)

        button_width = 20  # Set desired width
        button_height = 2  # Set desired height
        dark_green = '#006400'  # Dark green color
        light_green = '#90EE90'  # Light green color (for active background)

        student_button = tk.Button(page5_content, text='Student', font=('Arial', 14), bg=dark_green, fg='white',
                                width=button_width, height=button_height, activebackground=light_green, command=open_student_window)
        student_button.pack(pady=10, padx=20)

        faculty_button = tk.Button(page5_content, text='Faculty', font=('Arial', 14), bg=dark_green, fg='white',
                           width=button_width, height=button_height, activebackground=light_green, command=open_faculty_window)

        faculty_button.pack(pady=10, padx=20)

        hod_button = tk.Button(page5_content, text='HOD', font=('Arial', 14), bg=dark_green, fg='white',
                       width=button_width, height=button_height, activebackground=light_green, command=open_hod_window)

        hod_button.pack(pady=10, padx=20)

        accountant_button = tk.Button(page5_content, text='Accountant', font=('Arial', 14), bg=dark_green, fg='white',
                              width=button_width, height=button_height, activebackground=light_green, command=open_accountant_window)

        accountant_button.pack(pady=10, padx=20)

    def open_student_window():
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=back_to_page5,
                                bg='#8B008B', fg='white', width=25, height=3,
                                activebackground='#DDA0DD')  # Dark magenta background, light magenta on click
        back_button.pack(pady=10)

        view_button = tk.Button(main_content, text='View All Students', font=('Arial', 14), command=view_students,
                                bg='#8B008B', fg='white', width=25, height=3,
                                activebackground='#DDA0DD')  # Dark magenta background, light magenta on click
        view_button.pack(pady=10)

    def open_student_details(username):
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="Student Details", font=('Arial', 24)).pack(pady=20)

        # Create a frame for the Treeview and scrollbar with the specified size
        detail_frame = tk.Frame(main_content)
        detail_frame.pack(pady=10)

        # Set the size of the frame using the grid geometry manager
        detail_frame.grid_propagate(False)  # Prevent the frame from resizing to fit contents
        detail_frame.config(width=1100, height=500)

        # Create a Treeview widget for student details
        columns = ("Field", "Details")
        tree = ttk.Treeview(detail_frame, columns=columns, show="headings")
        tree.pack(side='left', fill='both', expand=True)

        # Configure the column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=250)  # Adjust width as needed

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(detail_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscroll=scrollbar.set)

        try:
            # Fetch student details for the given username
            cursor.execute("""
                SELECT s.student_id, s.student_name, u.username, u.role, 
                    s.admission_date, s.department, s.semester, 
                    s.admission_number, s.roll_no, s.gender, s.dob, 
                    s.blood_group, s.father_name, s.father_occupation, 
                    s.mother_name, s.mother_occupation, s.address, 
                    s.city, s.country, s.religion, s.caste, 
                    s.pin_code, s.state, s.email, s.phone, 
                    s.parent_phone, s.guardian_name, 
                    s.guardian_relationship, s.guardian_phone, 
                    s.guardian_address 
                FROM students s 
                JOIN users u ON s.user_id = u.id 
                WHERE u.username = %s
            """, (username,))
            student = cursor.fetchone()

            if not student:
                messagebox.showinfo("Info", "No student details found for this username.")
                return

            # Display student details in the Treeview
            field_labels = [
                "Student ID", "Student Name", "Username", "Role",
                "Admission Date", "Department", "Semester", 
                "Admission Number", "Roll No", "Gender", "DOB", 
                "Blood Group", "Father's Name", "Father's Occupation", 
                "Mother's Name", "Mother's Occupation", "Address", 
                "City", "Country", "Religion", "Caste", 
                "Pin Code", "State", "Email", "Phone", 
                "Parent Phone", "Guardian Name", 
                "Guardian Relationship", "Guardian Phone", 
                "Guardian Address"
            ]
            
            # Insert student details into the Treeview
            for label, value in zip(field_labels, student):
                tree.insert("", tk.END, values=(label, value))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        # Back button to return to the previous page
        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=back_to_page5, bg='blue', fg='white')
        back_button.pack(side='left', padx=10, pady=10)

        # Delete Student button
        delete_button = tk.Button(main_content, text='Delete Student', font=('Arial', 14), command=lambda: delete_student(username), bg='blue', fg='white')
        delete_button.pack(side='left', padx=10, pady=10)

    def commit_changes():
        try:
            # Use the same connection to commit changes
            cursor.execute("COMMIT")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while committing changes: {str(e)}")

    def delete_student(username):
        # Confirmation dialog
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this student?"):
            for attempt in range(3):  # Retry up to 3 times
                try:
                    # Fetch the user's ID using the username
                    cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
                    user_id = cursor.fetchone()
                    
                    if user_id:
                        user_id = user_id[0]
                        # Delete the student from the students table
                        cursor.execute("DELETE FROM students WHERE user_id = %s", (user_id,))
                        # Delete the user from the users table
                        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
                        commit_changes()  # Call the commit function
                        messagebox.showinfo("Success", "Student deleted successfully.")
                        back_to_page5()  # Go back to the previous page after deletion
                        return  # Exit the function after successful deletion
                    else:
                        messagebox.showerror("Error", "User not found.")
                    break  # Exit the retry loop if the user is found
                except Exception as e:
                    if "Lock wait timeout exceeded" in str(e):
                        if attempt < 2:  # Retry only if we haven't exhausted attempts
                            time.sleep(1)  # Wait before retrying
                        else:
                            messagebox.showerror("Error", f"An error occurred while deleting the student: {str(e)}")
                    else:
                        messagebox.showerror("Error", f"An error occurred while deleting the student: {str(e)}")

    def show_login_window():
        # Create a new window for login
        login_window = tk.Toplevel()
        login_window.title("Login")

        tk.Label(login_window, text="Enter Username:", font=('Arial', 14)).pack(pady=10)

        username_entry = tk.Entry(login_window, font=('Arial', 14))
        username_entry.pack(pady=10)

        def on_login():
            username = username_entry.get()
            if username:
                cursor.execute("SELECT role FROM users WHERE username = %s", (username,))
                role = cursor.fetchone()

                if role and role[0] == 'student':
                    open_student_details(username)
                    login_window.destroy()  # Close the login window
                else:
                    messagebox.showerror("Error", "Username does not belong to a student.")
            else:
                messagebox.showwarning("Warning", "Please enter a username.")

        login_button = tk.Button(login_window, text="Login", font=('Arial', 14), command=on_login)
        login_button.pack(pady=10)
    # Declare the tree variable globally
    
    tree = None
    def view_students():
        global tree  # Declare the tree variable as global

        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="All Student Details", font=('Arial', 24)).pack(pady=20)

        # Create a frame for the Treeview and scrollbar
        student_frame = tk.Frame(main_content)
        student_frame.pack(pady=10)

        # Create a Treeview widget for listing students
        columns = ("Student ID", "Student Name", "Username", "Role", "Department", "Semester")
        tree = ttk.Treeview(student_frame, columns=columns, show="headings")
        tree.pack(side='left', fill='both', expand=True)

        # Configure the column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=150)  # Adjust width as needed

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(student_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscroll=scrollbar.set)

        # Set a minimum size for the Treeview frame
        student_frame.configure(width=1100, height=400)

        # Create a frame for the department and semester selection
        selection_frame = tk.Frame(main_content)
        selection_frame.pack(pady=20)

        # Create a StringVar to hold the selected department
        department_var = tk.StringVar()
        
        # Create a StringVar to hold the selected semester
        semester_var = tk.StringVar()

        # Create a frame for department section (combobox and button)
        department_frame = tk.Frame(selection_frame)
        department_frame.pack(side='left', padx=20)

        # Create a Combobox for department selection
        department_combobox = ttk.Combobox(department_frame, textvariable=department_var, font=("Helvetica", 12), state='readonly')
        department_combobox['values'] = [
            "B.E Civil Engineering",
            "B.E Computer Science Engineering",
            "B.E Electrical and Electronics Engineering",
            "B.E Electronics and Communication Engineering",
            "B.Tech Information Technology",
            "B.E Mechanical Engineering",
            "B.Tech Artificial Intelligence and Data Science",
            "B.Tech Computer Science and Business Systems",
            "Marine Engineering",
            "Aerospace Engineering",
            "Master of Business Administration (MBA)",
            "Master of Computer Application (MCA)",
            "M.E Power Electronics and Drives",
            "M.E Communication systems",
            "M.E Computer Science Engineering",
            "M.E Engineering Design"
        ]
        department_combobox.pack(padx=10)

        # Create Confirm button for department selection below the department combobox
        confirm_department_button = tk.Button(department_frame, text='Confirm Department', font=("Helvetica", 12), 
                                            command=lambda: filter_students_by_department(department_var.get()), 
                                            bg='blue', fg='white')
        confirm_department_button.pack(pady=10)

        # Create a frame for semester section (combobox and button)
        semester_frame = tk.Frame(selection_frame)
        semester_frame.pack(side='left', padx=20)

        # Create a Combobox for semester selection
        semester_combobox = ttk.Combobox(semester_frame, textvariable=semester_var, font=("Helvetica", 12), state='readonly')
        semester_combobox['values'] = [
            "Semester 1", "Semester 2", "Semester 3", "Semester 4", 
            "Semester 5", "Semester 6", "Semester 7", "Semester 8"
        ]
        semester_combobox.pack(padx=10)

        # Create Confirm button for semester selection below the semester combobox
        confirm_semester_button = tk.Button(semester_frame, text='Confirm Semester', font=("Helvetica", 12), 
                                            command=lambda: filter_students_by_semester(semester_var.get()), 
                                            bg='blue', fg='white')
        confirm_semester_button.pack(pady=10)

        # Create Back button to return to the previous page
        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=open_student_window, bg='blue', fg='white')
        back_button.pack(side='left', padx=10, pady=10)

        # Create View button to open login window
        view_button = tk.Button(main_content, text='View', font=('Arial', 14), command=show_login_window, bg='blue', fg='white')
        view_button.pack(side='left', padx=10, pady=10)

        # Fetch and display all students initially
        display_all_students()


    def display_all_students():
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        try:
            # Execute the query to fetch all students
            cursor.execute("""
                SELECT s.student_id, s.student_name, u.username, u.role, s.department, s.semester 
                FROM students s 
                JOIN users u ON s.user_id = u.id
            """)
            students = cursor.fetchall()

            # Insert all student details into the Treeview
            for student_id, student_name, username, role, department, semester in students:
                tree.insert("", tk.END, values=(student_id, student_name, username, role, department, semester))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while fetching student details: {str(e)}")

    def filter_students_by_department(selected_department):
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        if selected_department:
            try:
                print(f"Filtering students by department: {selected_department}")  # Debugging output
                # Execute the query to fetch students from the selected department
                cursor.execute("""
                    SELECT s.student_id, s.student_name, u.username, u.role, s.department, s.semester 
                    FROM students s 
                    JOIN users u ON s.user_id = u.id 
                    WHERE s.department = %s
                """, (selected_department,))
                students = cursor.fetchall()

                if not students:
                    messagebox.showinfo("Info", "No students found in the selected department.")
                    return

                # Insert filtered student details into the Treeview
                for student_id, student_name, username, role, department, semester in students:
                    tree.insert("", tk.END, values=(student_id, student_name, username, role, department, semester))

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while fetching student details: {str(e)}")

    def filter_students_by_semester(selected_semester):
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        if selected_semester:
            try:
                print(f"Filtering students by semester: {selected_semester}")  # Debugging output
                # Execute the query to fetch students from the selected semester
                cursor.execute("""
                    SELECT s.student_id, s.student_name, u.username, u.role, s.department, s.semester 
                    FROM students s 
                    JOIN users u ON s.user_id = u.id 
                    WHERE s.semester = %s
                """, (selected_semester,))
                students = cursor.fetchall()

                if not students:
                    messagebox.showinfo("Info", "No students found in the selected semester.")
                    return

                # Insert filtered student details into the Treeview
                for student_id, student_name, username, role, department, semester in students:
                    tree.insert("", tk.END, values=(student_id, student_name, username, role, department, semester))

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while fetching student details: {str(e)}")

    def show_users_by_role(role):
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        back_button = tk.Button(main_content, text="Back", font=('Arial', 12), command=display_role_buttons)
        back_button.pack(pady=10, anchor='w')

        tk.Label(main_content, text=f"Users in Role: {role}", font=('Arial', 24)).pack(pady=20)

        tree = ttk.Treeview(main_content, columns=("ID", "Username", "Role", "Action"), show="headings", height=10)
        tree.heading("ID", text="ID")
        tree.heading("Username", text="Username")
        tree.heading("Role", text="Role")
        tree.heading("Action", text="Action")
        tree.column("ID", width=50, anchor='center')
        tree.column("Username", width=200, anchor='center')
        tree.column("Role", width=100, anchor='center')
        tree.column("Action", width=100, anchor='center')
        tree.pack(pady=20, fill="both", expand=True)

        scrollbar = ttk.Scrollbar(main_content, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        try:
            cursor.execute("SELECT id, username, role FROM users WHERE role = %s", (role,))
            users = cursor.fetchall()

            for user in users:
                tree.insert("", tk.END, values=user + ("View",))

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to retrieve user details: {err}")

        tree.bind("<ButtonRelease-1>", lambda event: handle_treeview_click(tree, event))

    def handle_treeview_click(tree, event):
        item = tree.selection()
        if item:
            user_data = tree.item(item, 'values')
            user_id = user_data[0]
            messagebox.showinfo("User Info", f"Viewing details for User ID: {user_id}")

    def back_to_page5():
        for widget in main_content.winfo_children():
            widget.destroy()
        create_page5_content()

    def display_role_buttons():
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        # Create buttons for each role
        roles = ["Student", "Faculty", "HOD", "Principal", "Accountant", "Admin"]
        tk.Label(main_content, text="Select a Role", font=('Arial', 24)).pack(pady=20)

        for role in roles:
            role_button = tk.Button(main_content, text=role, font=('Arial', 14), command=lambda r=role: show_users_by_role(r))
            role_button.pack(pady=5)

        back_button = tk.Button(main_content, text="Back", font=('Arial', 12), command=back_to_page5)
        back_button.pack(pady=10)

###########################################################################################################################

    def open_faculty_window():
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=back_to_page5,
                                bg='#8B008B', fg='white', width=25, height=3,
                                activebackground='#DDA0DD')  # Dark magenta background, light magenta on click
        back_button.pack(pady=10)

        view_button = tk.Button(main_content, text='View All Faculties', font=('Arial', 14), command=view_faculty,
                                bg='#8B008B', fg='white', width=25, height=3,
                                activebackground='#DDA0DD')  # Dark magenta background, light magenta on click
        view_button.pack(pady=10)

    def open_faculty_details(username):
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="Faculty Details", font=('Arial', 24)).pack(pady=20)

        # Create a frame for the Treeview and scrollbar with the specified size
        detail_frame = tk.Frame(main_content)
        detail_frame.pack(pady=10)

        # Set the size of the frame using the grid geometry manager
        detail_frame.grid_propagate(False)  # Prevent the frame from resizing to fit contents
        detail_frame.config(width=1100, height=500)

        # Create a Treeview widget for student details
        columns = ("Field", "Details")
        tree = ttk.Treeview(detail_frame, columns=columns, show="headings")
        tree.pack(side='left', fill='both', expand=True)

        # Configure the column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=250)  # Adjust width as needed

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(detail_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscroll=scrollbar.set)

        try:
            # Fetch faculty details for the given username
            cursor.execute("""
                SELECT f.faculty_id, f.faculty_name, u.username, u.role, 
                    f.department, f.faculty_gender, f.faculty_dob, 
                    f.faculty_blood_group, f.faculty_marital_status, 
                    f.faculty_job_position, f.faculty_address, 
                    f.faculty_city, f.faculty_country, f.faculty_pin_code, 
                    f.faculty_state, f.faculty_email, f.faculty_phone, 
                    f.faculty_guardian_name, f.faculty_guardian_relationship, 
                    f.faculty_guardian_phone, f.faculty_guardian_address 
                FROM faculty f
                JOIN users u ON f.user_id = u.id
                WHERE u.username = %s
            """, (username,))
            faculty = cursor.fetchone()

            if not faculty:
                messagebox.showinfo("Info", "No faculty details found for this username.")
                return

            # Display faculty details in the Treeview (adjust fields and labels as needed)
            field_labels = [
                "Faculty ID", "Faculty Name", "Username", "Role", 
                "Department", "Gender", "DOB", "Blood Group", 
                "Marital Status", "Job Position", "Address", 
                "City", "Country", "Pin Code", "State", 
                "Email", "Phone", "Guardian Name", 
                "Guardian Relationship", "Guardian Phone", 
                "Guardian Address"
            ]

            # Insert student details into the Treeview
            for label, value in zip(field_labels, faculty):
                tree.insert("", tk.END, values=(label, value))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        # Back button to return to the previous page
        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=back_to_page5, bg='blue', fg='white')
        back_button.pack(side='left', padx=10, pady=10)

        # Delete Student button
        delete_button = tk.Button(main_content, text='Delete faculty', font=('Arial', 14), command=lambda: delete_faculty(username), bg='blue', fg='white')
        delete_button.pack(side='left', padx=10, pady=10)

    def commit_changes():
        try:
            # Use the same connection to commit changes
            cursor.execute("COMMIT")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while committing changes: {str(e)}")

    def delete_faculty(username):
        # Confirmation dialog
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this faculty?"):
            for attempt in range(3):  # Retry up to 3 times
                try:
                    # Fetch the user's ID using the username
                    cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
                    user_id = cursor.fetchone()
                    
                    if user_id:
                        user_id = user_id[0]
                        # Delete the student from the students table
                        cursor.execute("DELETE FROM faculty WHERE user_id = %s", (user_id,))
                        # Delete the user from the users table
                        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
                        commit_changes()  # Call the commit function
                        messagebox.showinfo("Success", "faculty deleted successfully.")
                        back_to_page5()  # Go back to the previous page after deletion
                        return  # Exit the function after successful deletion
                    else:
                        messagebox.showerror("Error", "User not found.")
                    break  # Exit the retry loop if the user is found
                except Exception as e:
                    if "Lock wait timeout exceeded" in str(e):
                        if attempt < 2:  # Retry only if we haven't exhausted attempts
                            time.sleep(1)  # Wait before retrying
                        else:
                            messagebox.showerror("Error", f"An error occurred while deleting the faculty: {str(e)}")
                    else:
                        messagebox.showerror("Error", f"An error occurred while deleting the faculty: {str(e)}")

    def show_faculty_login_window():
        # Create a new window for login
        login_window = tk.Toplevel()
        login_window.title("Login")

        tk.Label(login_window, text="Enter Username:", font=('Arial', 14)).pack(pady=10)

        username_entry = tk.Entry(login_window, font=('Arial', 14))
        username_entry.pack(pady=10)

        def on_login():
            username = username_entry.get()
            if username:
                cursor.execute("SELECT role FROM users WHERE username = %s", (username,))
                role = cursor.fetchone()

                if role and role[0] == 'faculty':
                    open_faculty_details(username)
                    login_window.destroy()  # Close the login window
                else:
                    messagebox.showerror("Error", "Username does not belong to a faculty.")
            else:
                messagebox.showwarning("Warning", "Please enter a username.")

        login_button = tk.Button(login_window, text="Login", font=('Arial', 14), command=on_login)
        login_button.pack(pady=10)
    # Declare the tree variable globally

    tree = None
    def view_faculty():
        global tree  # Declare the tree variable as global

        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="All faculty Details", font=('Arial', 24)).pack(pady=20)

        # Create a frame for the Treeview and scrollbar
        student_frame = tk.Frame(main_content)
        student_frame.pack(pady=10)

        # Create a Treeview widget for listing students
        columns = ("faculty ID", "faculty Name", "Username", "Role", "Department")
        tree = ttk.Treeview(student_frame, columns=columns, show="headings")
        tree.pack(side='left', fill='both', expand=True)

        # Configure the column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=150)  # Adjust width as needed

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(student_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscroll=scrollbar.set)

        # Set a minimum size for the Treeview frame
        student_frame.configure(width=1100, height=400)

        # Create a frame for the department and semester selection
        selection_frame = tk.Frame(main_content)
        selection_frame.pack(pady=20)

        # Create a StringVar to hold the selected department
        department_var = tk.StringVar()

        # Create a frame for department section (combobox and button)
        department_frame = tk.Frame(selection_frame)
        department_frame.pack(side='left', padx=20)

        # Create a Combobox for department selection
        department_combobox = ttk.Combobox(department_frame, textvariable=department_var, font=("Helvetica", 12), state='readonly')
        department_combobox['values'] = [
            "B.E Civil Engineering",
            "B.E Computer Science Engineering",
            "B.E Electrical and Electronics Engineering",
            "B.E Electronics and Communication Engineering",
            "B.Tech Information Technology",
            "B.E Mechanical Engineering",
            "B.Tech Artificial Intelligence and Data Science",
            "B.Tech Computer Science and Business Systems",
            "Marine Engineering",
            "Aerospace Engineering",
            "Master of Business Administration (MBA)",
            "Master of Computer Application (MCA)",
            "M.E Power Electronics and Drives",
            "M.E Communication systems",
            "M.E Computer Science Engineering",
            "M.E Engineering Design"
        ]
        department_combobox.pack(padx=10)

        # Create Confirm button for department selection below the department combobox
        confirm_department_button = tk.Button(department_frame, text='Confirm Department', font=("Helvetica", 12), 
                                            command=lambda: filter_faculty_by_department(department_var.get()), 
                                            bg='blue', fg='white')
        confirm_department_button.pack(pady=10)

        # Create Back button to return to the previous page
        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=open_faculty_window, bg='blue', fg='white')
        back_button.pack(side='left', padx=10, pady=10)

        # Create View button to open login window
        view_button = tk.Button(main_content, text='View', font=('Arial', 14), command=show_faculty_login_window, bg='blue', fg='white')
        view_button.pack(side='left', padx=10, pady=10)

        # Fetch and display all students initially
        display_all_faculty()


    def display_all_faculty():
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        try:
            # Execute the query to fetch all students
            cursor.execute("""
                SELECT s.faculty_id, s.faculty_name, u.username, u.role, s.department 
                FROM faculty s 
                JOIN users u ON s.user_id = u.id
            """)
            faculty = cursor.fetchall()

            # Insert all student details into the Treeview
            for faculty_id, faculty_name, username, role, department in faculty:
                tree.insert("", tk.END, values=(faculty_id, faculty_name, username, role, department))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while fetching student details: {str(e)}")

    def filter_faculty_by_department(selected_department):
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        if selected_department:
            try:
                print(f"Filtering students by department: {selected_department}")  # Debugging output
                # Execute the query to fetch students from the selected department
                cursor.execute("""
                    SELECT s.faculty_id, s.faculty_name, u.username, u.role, s.department 
                    FROM faculty s 
                    JOIN users u ON s.user_id = u.id 
                    WHERE s.department = %s
                """, (selected_department,))
                faculty = cursor.fetchall()

                if not faculty:
                    messagebox.showinfo("Info", "No faculty found in the selected department.")
                    return

                # Insert filtered student details into the Treeview
                for faculty_id, faculty_name, username, role, department in faculty:
                    tree.insert("", tk.END, values=(faculty_id, faculty_name, username, role, department))

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while fetching faculty details: {str(e)}")

##########################################################################################################################
    def open_hod_window():
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=back_to_page5,
                                bg='#8B008B', fg='white', width=25, height=3,
                                activebackground='#DDA0DD')  # Dark magenta background, light magenta on click
        back_button.pack(pady=10)

        view_button = tk.Button(main_content, text='View All HOD', font=('Arial', 14), command=view_hod,
                                bg='#8B008B', fg='white', width=25, height=3,
                                activebackground='#DDA0DD')  # Dark magenta background, light magenta on click
        view_button.pack(pady=10)

    def open_hod_details(username):
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="HOD Details", font=('Arial', 24)).pack(pady=20)

        # Create a frame for the Treeview and scrollbar with the specified size
        detail_frame = tk.Frame(main_content)
        detail_frame.pack(pady=10)

        # Set the size of the frame using the grid geometry manager
        detail_frame.grid_propagate(False)  # Prevent the frame from resizing to fit contents
        detail_frame.config(width=1100, height=500)

        # Create a Treeview widget for student details
        columns = ("Field", "Details")
        tree = ttk.Treeview(detail_frame, columns=columns, show="headings")
        tree.pack(side='left', fill='both', expand=True)

        # Configure the column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=250)  # Adjust width as needed

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(detail_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscroll=scrollbar.set)

        try:
            # Fetch faculty details for the given username
            cursor.execute("""
                SELECT f.faculty_id, f.faculty_name, u.username, u.role, 
                    f.department, f.faculty_gender, f.faculty_dob, 
                    f.faculty_blood_group, f.faculty_marital_status, 
                    f.faculty_job_position, f.faculty_address, 
                    f.faculty_city, f.faculty_country, f.faculty_pin_code, 
                    f.faculty_state, f.faculty_email, f.faculty_phone, 
                    f.faculty_guardian_name, f.faculty_guardian_relationship, 
                    f.faculty_guardian_phone, f.faculty_guardian_address 
                FROM hod f
                JOIN users u ON f.user_id = u.id
                WHERE u.username = %s
            """, (username,))
            faculty = cursor.fetchone()

            if not faculty:
                messagebox.showinfo("Info", "No HOD details found for this username.")
                return

            # Display faculty details in the Treeview (adjust fields and labels as needed)
            field_labels = [
                "Faculty ID", "Faculty Name", "Username", "Role", 
                "Department", "Gender", "DOB", "Blood Group", 
                "Marital Status", "Job Position", "Address", 
                "City", "Country", "Pin Code", "State", 
                "Email", "Phone", "Guardian Name", 
                "Guardian Relationship", "Guardian Phone", 
                "Guardian Address"
            ]

            # Insert student details into the Treeview
            for label, value in zip(field_labels, faculty):
                tree.insert("", tk.END, values=(label, value))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        # Back button to return to the previous page
        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=back_to_page5, bg='blue', fg='white')
        back_button.pack(side='left', padx=10, pady=10)

        # Delete Student button
        delete_button = tk.Button(main_content, text='Delete hod', font=('Arial', 14), command=lambda: delete_hod(username), bg='blue', fg='white')
        delete_button.pack(side='left', padx=10, pady=10)

    def commit_changes():
        try:
            # Use the same connection to commit changes
            cursor.execute("COMMIT")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while committing changes: {str(e)}")

    def delete_hod(username):
        # Confirmation dialog
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this hod?"):
            for attempt in range(3):  # Retry up to 3 times
                try:
                    # Fetch the user's ID using the username
                    cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
                    user_id = cursor.fetchone()
                    
                    if user_id:
                        user_id = user_id[0]
                        # Delete the student from the students table
                        cursor.execute("DELETE FROM hod WHERE user_id = %s", (user_id,))
                        # Delete the user from the users table
                        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
                        commit_changes()  # Call the commit function
                        messagebox.showinfo("Success", "hod deleted successfully.")
                        back_to_page5()  # Go back to the previous page after deletion
                        return  # Exit the function after successful deletion
                    else:
                        messagebox.showerror("Error", "User not found.")
                    break  # Exit the retry loop if the user is found
                except Exception as e:
                    if "Lock wait timeout exceeded" in str(e):
                        if attempt < 2:  # Retry only if we haven't exhausted attempts
                            time.sleep(1)  # Wait before retrying
                        else:
                            messagebox.showerror("Error", f"An error occurred while deleting the hod: {str(e)}")
                    else:
                        messagebox.showerror("Error", f"An error occurred while deleting the hod: {str(e)}")

    def show_hod_login_window():
        # Create a new window for login
        login_window = tk.Toplevel()
        login_window.title("Login")

        tk.Label(login_window, text="Enter Username:", font=('Arial', 14)).pack(pady=10)

        username_entry = tk.Entry(login_window, font=('Arial', 14))
        username_entry.pack(pady=10)

        def on_login():
            username = username_entry.get()
            if username:
                cursor.execute("SELECT role FROM users WHERE username = %s", (username,))
                role = cursor.fetchone()

                if role and role[0] == 'hod':
                    open_hod_details(username)
                    login_window.destroy()  # Close the login window
                else:
                    messagebox.showerror("Error", "Username does not belong to a hod.")
            else:
                messagebox.showwarning("Warning", "Please enter a username.")

        login_button = tk.Button(login_window, text="Login", font=('Arial', 14), command=on_login)
        login_button.pack(pady=10)
    # Declare the tree variable globally

    tree = None
    def view_hod():
        global tree  # Declare the tree variable as global

        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="All HOD Details", font=('Arial', 24)).pack(pady=20)

        # Create a frame for the Treeview and scrollbar
        student_frame = tk.Frame(main_content)
        student_frame.pack(pady=10)

        # Create a Treeview widget for listing students
        columns = ("faculty ID", "faculty Name", "Username", "Role", "Department")
        tree = ttk.Treeview(student_frame, columns=columns, show="headings")
        tree.pack(side='left', fill='both', expand=True)

        # Configure the column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=150)  # Adjust width as needed

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(student_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscroll=scrollbar.set)

        # Set a minimum size for the Treeview frame
        student_frame.configure(width=1100, height=400)

        # Create a frame for the department and semester selection
        selection_frame = tk.Frame(main_content)
        selection_frame.pack(pady=20)

        # Create a StringVar to hold the selected department
        department_var = tk.StringVar()

        # Create a frame for department section (combobox and button)
        department_frame = tk.Frame(selection_frame)
        department_frame.pack(side='left', padx=20)

        # Create a Combobox for department selection
        department_combobox = ttk.Combobox(department_frame, textvariable=department_var, font=("Helvetica", 12), state='readonly')
        department_combobox['values'] = [
            "B.E Civil Engineering",
            "B.E Computer Science Engineering",
            "B.E Electrical and Electronics Engineering",
            "B.E Electronics and Communication Engineering",
            "B.Tech Information Technology",
            "B.E Mechanical Engineering",
            "B.Tech Artificial Intelligence and Data Science",
            "B.Tech Computer Science and Business Systems",
            "Marine Engineering",
            "Aerospace Engineering",
            "Master of Business Administration (MBA)",
            "Master of Computer Application (MCA)",
            "M.E Power Electronics and Drives",
            "M.E Communication systems",
            "M.E Computer Science Engineering",
            "M.E Engineering Design"
        ]
        department_combobox.pack(padx=10)

        # Create Confirm button for department selection below the department combobox
        confirm_department_button = tk.Button(department_frame, text='Confirm Department', font=("Helvetica", 12), 
                                            command=lambda: filter_hod_by_department(department_var.get()), 
                                            bg='blue', fg='white')
        confirm_department_button.pack(pady=10)

        # Create Back button to return to the previous page
        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=open_hod_window, bg='blue', fg='white')
        back_button.pack(side='left', padx=10, pady=10)

        # Create View button to open login window
        view_button = tk.Button(main_content, text='View', font=('Arial', 14), command=show_hod_login_window, bg='blue', fg='white')
        view_button.pack(side='left', padx=10, pady=10)

        # Fetch and display all students initially
        display_all_hod()


    def display_all_hod():
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        try:
            # Execute the query to fetch all students
            cursor.execute("""
                SELECT s.faculty_id, s.faculty_name, u.username, u.role, s.department 
                FROM hod s 
                JOIN users u ON s.user_id = u.id
            """)
            faculty = cursor.fetchall()

            # Insert all student details into the Treeview
            for faculty_id, faculty_name, username, role, department in faculty:
                tree.insert("", tk.END, values=(faculty_id, faculty_name, username, role, department))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while fetching student details: {str(e)}")

    def filter_hod_by_department(selected_department):
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        if selected_department:
            try:
                print(f"Filtering students by department: {selected_department}")  # Debugging output
                # Execute the query to fetch students from the selected department
                cursor.execute("""
                    SELECT s.faculty_id, s.faculty_name, u.username, u.role, s.department 
                    FROM hod s 
                    JOIN users u ON s.user_id = u.id 
                    WHERE s.department = %s
                """, (selected_department,))
                faculty = cursor.fetchall()

                if not faculty:
                    messagebox.showinfo("Info", "No hod found in the selected department.")
                    return

                # Insert filtered student details into the Treeview
                for faculty_id, faculty_name, username, role, department in faculty:
                    tree.insert("", tk.END, values=(faculty_id, faculty_name, username, role, department))

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while fetching hod details: {str(e)}")
############################################################################################################################
 
    def open_accountant_window():
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=back_to_page5,
                                bg='#8B008B', fg='white', width=25, height=3,
                                activebackground='#DDA0DD')  # Dark magenta background, light magenta on click
        back_button.pack(pady=10)

        view_button = tk.Button(main_content, text='View All Accountant', font=('Arial', 14), command=view_accountant,
                                bg='#8B008B', fg='white', width=25, height=3,
                                activebackground='#DDA0DD')  # Dark magenta background, light magenta on click
        view_button.pack(pady=10)

    def open_accountant_details(username):
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="accountant Details", font=('Arial', 24)).pack(pady=20)

        # Create a frame for the Treeview and scrollbar with the specified size
        detail_frame = tk.Frame(main_content)
        detail_frame.pack(pady=10)

        # Set the size of the frame using the grid geometry manager
        detail_frame.grid_propagate(False)  # Prevent the frame from resizing to fit contents
        detail_frame.config(width=1100, height=500)

        # Create a Treeview widget for student details
        columns = ("Field", "Details")
        tree = ttk.Treeview(detail_frame, columns=columns, show="headings")
        tree.pack(side='left', fill='both', expand=True)

        # Configure the column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=250)  # Adjust width as needed

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(detail_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscroll=scrollbar.set)

        try:
            # Fetch faculty details for the given username
            cursor.execute("""
                SELECT f.faculty_id, f.faculty_name, u.username, u.role, 
                    f.department, f.faculty_gender, f.faculty_dob, 
                    f.faculty_blood_group, f.faculty_marital_status, 
                    f.faculty_job_position, f.faculty_address, 
                    f.faculty_city, f.faculty_country, f.faculty_pin_code, 
                    f.faculty_state, f.faculty_email, f.faculty_phone, 
                    f.faculty_guardian_name, f.faculty_guardian_relationship, 
                    f.faculty_guardian_phone, f.faculty_guardian_address 
                FROM accountant f
                JOIN users u ON f.user_id = u.id
                WHERE u.username = %s
            """, (username,))
            faculty = cursor.fetchone()

            if not faculty:
                messagebox.showinfo("Info", "No Accountant details found for this username.")
                return

            # Display faculty details in the Treeview (adjust fields and labels as needed)
            field_labels = [
                "Faculty ID", "Faculty Name", "Username", "Role", 
                "Department", "Gender", "DOB", "Blood Group", 
                "Marital Status", "Job Position", "Address", 
                "City", "Country", "Pin Code", "State", 
                "Email", "Phone", "Guardian Name", 
                "Guardian Relationship", "Guardian Phone", 
                "Guardian Address"
            ]

            # Insert student details into the Treeview
            for label, value in zip(field_labels, faculty):
                tree.insert("", tk.END, values=(label, value))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        # Back button to return to the previous page
        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=back_to_page5, bg='blue', fg='white')
        back_button.pack(side='left', padx=10, pady=10)

        # Delete Student button
        delete_button = tk.Button(main_content, text='Delete hod', font=('Arial', 14), command=lambda: delete_accountant(username), bg='blue', fg='white')
        delete_button.pack(side='left', padx=10, pady=10)

    def commit_changes():
        try:
            # Use the same connection to commit changes
            cursor.execute("COMMIT")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while committing changes: {str(e)}")

    def delete_accountant(username):
        # Confirmation dialog
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this accountant?"):
            for attempt in range(3):  # Retry up to 3 times
                try:
                    # Fetch the user's ID using the username
                    cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
                    user_id = cursor.fetchone()
                    
                    if user_id:
                        user_id = user_id[0]
                        # Delete the student from the students table
                        cursor.execute("DELETE FROM accountant WHERE user_id = %s", (user_id,))
                        # Delete the user from the users table
                        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
                        commit_changes()  # Call the commit function
                        messagebox.showinfo("Success", "Accountant deleted successfully.")
                        back_to_page5()  # Go back to the previous page after deletion
                        return  # Exit the function after successful deletion
                    else:
                        messagebox.showerror("Error", "User not found.")
                    break  # Exit the retry loop if the user is found
                except Exception as e:
                    if "Lock wait timeout exceeded" in str(e):
                        if attempt < 2:  # Retry only if we haven't exhausted attempts
                            time.sleep(1)  # Wait before retrying
                        else:
                            messagebox.showerror("Error", f"An error occurred while deleting the accountant: {str(e)}")
                    else:
                        messagebox.showerror("Error", f"An error occurred while deleting the accountant: {str(e)}")

    def show_accountant_login_window():
        # Create a new window for login
        login_window = tk.Toplevel()
        login_window.title("Login")

        tk.Label(login_window, text="Enter Username:", font=('Arial', 14)).pack(pady=10)

        username_entry = tk.Entry(login_window, font=('Arial', 14))
        username_entry.pack(pady=10)

        def on_login():
            username = username_entry.get()
            if username:
                cursor.execute("SELECT role FROM users WHERE username = %s", (username,))
                role = cursor.fetchone()

                if role and role[0] == 'accountant':
                    open_accountant_details(username)
                    login_window.destroy()  # Close the login window
                else:
                    messagebox.showerror("Error", "Username does not belong to a accountant.")
            else:
                messagebox.showwarning("Warning", "Please enter a username.")

        login_button = tk.Button(login_window, text="Login", font=('Arial', 14), command=on_login)
        login_button.pack(pady=10)
    # Declare the tree variable globally

    tree = None
    def view_accountant():
        global tree  # Declare the tree variable as global

        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="All accountant Details", font=('Arial', 24)).pack(pady=20)

        # Create a frame for the Treeview and scrollbar
        student_frame = tk.Frame(main_content)
        student_frame.pack(pady=10)

        # Create a Treeview widget for listing students
        columns = ("faculty ID", "faculty Name", "Username", "Role")
        tree = ttk.Treeview(student_frame, columns=columns, show="headings")
        tree.pack(side='left', fill='both', expand=True)

        # Configure the column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=150)  # Adjust width as needed

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(student_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscroll=scrollbar.set)

        # Set a minimum size for the Treeview frame
        student_frame.configure(width=1100, height=400)

        # Create a frame for the department and semester selection
        selection_frame = tk.Frame(main_content)
        selection_frame.pack(pady=20)

        # Create a frame for department section (combobox and button)
        department_frame = tk.Frame(selection_frame)
        department_frame.pack(side='left', padx=20)

        # Create Back button to return to the previous page
        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=open_accountant_window, bg='blue', fg='white')
        back_button.pack(side='left', padx=10, pady=10)

        # Create View button to open login window
        view_button = tk.Button(main_content, text='View', font=('Arial', 14), command=show_accountant_login_window, bg='blue', fg='white')
        view_button.pack(side='left', padx=10, pady=10)

        # Fetch and display all students initially
        display_all_accountant()


    def display_all_accountant():
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        try:
            # Execute the query to fetch all students
            cursor.execute("""
                SELECT s.faculty_id, s.faculty_name, u.username, u.role
                FROM accountant s 
                JOIN users u ON s.user_id = u.id
            """)
            faculty = cursor.fetchall()

            # Insert all student details into the Treeview
            for faculty_id, faculty_name, username, role in faculty:
                tree.insert("", tk.END, values=(faculty_id, faculty_name, username, role))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while fetching accountant details: {str(e)}")

    # Sidebar buttons
    button1 = tk.Button(sidebar, width=12, text='Send Notification', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button1.pack(fill='x')
    button1.config(command=lambda: open_principal_notification_interface)
    button1.bind("<Enter>", lambda event: button1.configure(bg='blue'))
    button1.bind("<Leave>", lambda event: button1.configure(bg='#2c3e50'))

    button2 = tk.Button(sidebar, text='  Admin Notifications  ', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button2.pack(fill='x')
    button2.config(command=lambda: fetch_and_display_notifications(username, 'principal'))  # Pass username and role
    button2.bind("<Enter>", lambda event: button2.configure(bg='blue'))
    button2.bind("<Leave>", lambda event: button2.configure(bg='#2c3e50'))

    button3 = tk.Button(sidebar, text='Chat', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button3.pack(fill='x')
    button3.config(command=lambda: open_staff_chat_sidebar(username))
    button3.bind("<Enter>", lambda event: button3.configure(bg='blue'))
    button3.bind("<Leave>", lambda event: button3.configure(bg='#2c3e50'))

    button4 = tk.Button(sidebar, text='group chat', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button4.pack(fill='x')
    button4.config(command=lambda: on_group_chat_click(username,main_content))
    button4.bind("<Enter>", lambda event: button4.configure(bg='blue'))
    button4.bind("<Leave>", lambda event: button4.configure(bg='#2c3e50'))

    button5 = tk.Button(sidebar, text='view details', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button5.pack(fill='x')
    button5.config(command=lambda: load_content('view details'))
    button5.bind("<Enter>", lambda event: button5.configure(bg='blue'))
    button5.bind("<Leave>", lambda event: button5.configure(bg='#2c3e50'))

    button6 = tk.Button(sidebar, text='Page 6', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button6.pack(fill='x')
    button6.config(command=lambda: load_content('Page 6'))
    button6.bind("<Enter>", lambda event: button6.configure(bg='blue'))
    button6.bind("<Leave>", lambda event: button6.configure(bg='#2c3e50'))

    button7 = tk.Button(sidebar, text='Page 7', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button7.pack(fill='x')
    button7.config(command=lambda: load_content('Page 7'))
    button7.bind("<Enter>", lambda event: button7.configure(bg='blue'))
    button7.bind("<Leave>", lambda event: button7.configure(bg='#2c3e50'))

    button8 = tk.Button(sidebar, text='Back', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button8.pack(fill='x')
    button8.config(command=lambda: switch_window(root,login_window))
    button8.bind("<Enter>", lambda event: button8.configure(bg='blue'))
    button8.bind("<Leave>", lambda event: button8.configure(bg='#2c3e50'))

    button_logout = tk.Button(sidebar, text='Logout', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button_logout.pack(fill='x')
    button_logout.config(command=lambda: load_content('Logout'))
    button_logout.bind("<Enter>", lambda event: button_logout.configure(bg='blue'))
    button_logout.bind("<Leave>", lambda event: button_logout.configure(bg='#2c3e50'))

    open_principal_notification_interface()

    admin_update_notification_button()

    group_chat_button(username)

    root.mainloop()

# Group Chat Sidebar Function
def open_group_chat_sidebar(username, main_window):
    # Clear the existing content in the main window
    for widget in main_window.winfo_children():
        widget.destroy()

    # Chat frame for messages
    chat_frame = tk.Frame(main_window , background="#c2c2a3")
    chat_frame.pack(side="right", fill="both", expand=True)

    # Adjusting the height and width for larger chat area
    msg_text = tk.Text(chat_frame, height=25, width=70, wrap="word", state="disabled")  # Increased height and width
    msg_text.pack(pady=5)

    msg_entry = tk.Entry(chat_frame, width=70)  # Increased width for message entry
    msg_entry.pack(pady=5)

    # Send button with increased size
    send_button = tk.Button(chat_frame, text="Send",background="#4d2600" ,foreground="white" , command=lambda: send_message(msg_entry.get().strip()), width=10, height=2)
    send_button.pack(pady=5)

    notification_label = tk.Label(chat_frame, text="Unread Messages: 0")
    notification_label.pack()

    # Unread message count initialization
    unread_count = 0

    def send_message(message):
        if not message:
            messagebox.showerror("Error", "Message cannot be empty")
            return

        try:
            print(f"Attempting to find sender ID for username: '{username}'")
            cursor.execute("SELECT id FROM users WHERE LOWER(username) = LOWER(%s)", (username,))
            sender_id = cursor.fetchone()

            if sender_id is None:
                print(f"Sender '{username}' not found in the database. Query returned None.")
                messagebox.showerror("Error", "Sender not found.")
                return
            
            print(f"Sender ID for '{username}' found: {sender_id[0]}")

            # Insert message into the database for group chat with receiver_user_id as NULL
            cursor.execute(""" 
                INSERT INTO groupp_chat_messages (sender_user_id, receiver_user_id, message, timestamp, is_read) 
                VALUES (%s, NULL, %s, %s, %s)
            """, (sender_id[0], message, datetime.now(), False))
            db.commit()

            msg_entry.delete(0, tk.END)  # Clear the message entry
            fetch_messages()  # Refresh chat
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Message sending failed: {e}")

    def fetch_messages():
        nonlocal unread_count  # Access the unread count variable
        try:
            # Fetch all messages regardless of the receiver_user_id
            cursor.execute(""" 
                SELECT sender_user_id, message, timestamp 
                FROM groupp_chat_messages 
                ORDER BY timestamp ASC
            """)
            messages = cursor.fetchall()

            msg_text.config(state="normal")
            msg_text.delete(1.0, tk.END)

            # Reset unread count for this session when fetching messages
            unread_count = 0

            for msg in messages:
                cursor.execute("SELECT username FROM users WHERE id=%s", (msg[0],))
                sender_username = cursor.fetchone()[0]
                msg_time = msg[2].strftime("%H:%M")

                # Determine the message alignment based on the sender
                if sender_username.lower() == username.lower():  # Message sent by the logged-in user
                    msg_text.insert(tk.END, f"{sender_username}: \n{msg[1]} at {msg_time}\n", "sent",)
                else:  # Message received from another user
                    msg_text.insert(tk.END, f"{sender_username}: \n{msg[1]} at {msg_time}\n", "received")
                    unread_count += 1  # Increment unread message count only for received messages

            msg_text.config(state="disabled")

            # Configure message tags for styling
            msg_text.tag_config("sent", foreground="white",background="#0039e6",font=16 , justify="right")  # Sent messages in blue, right-aligned
            msg_text.tag_config("received", foreground="black",font=16 ,justify="left")  # Received messages in black, left-aligned

            msg_text.yview_moveto(1)  # Scroll to the end
            notification_label.config(text=f"Unread Messages: {unread_count}")  # Update notification label
        except mysql.connector.Error as e:
            print(f"Error fetching messages: {e}")

    fetch_messages()  # Load messages when chat opens


# Dashboard Window (varies based on role)
def admin_dashboard_window(username):
    root = tk.Tk()
    root.title("Admin Dashboard")
    root.geometry("1366x768")

    # Header Frame
    header = tk.Frame(root, height=120, bg='#1abc9c')
    header.pack(side="top", fill="x")

    # Sidebar Frame with adjusted width
    sidebar_width = 100  # Adjust this value as needed
    sidebar = tk.Frame(root, width=sidebar_width, bg='#2c3e50')
    sidebar.pack(side="left", fill="y")

    # Main content area
    main_content = tk.Frame(root, bg='white')
    main_content.pack(side="right", expand=True, fill="both")

    def open_notification_interface():
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="Enter Notification Message:", font=('Arial', 14), bg="white").pack(pady=20)
        notification_entry = tk.Text(main_content, height=5, width=50)
        notification_entry.pack(pady=10)

        tk.Label(main_content, text="Select Recipients:", font=('Arial', 14), bg="white").pack(pady=10)
        role_var = tk.StringVar(value="all")
        roles = ["all", "student", "faculty", "accountant", "hod","principal"]

        selected_role_label = tk.Label(main_content, text="", font=('Arial', 14), bg="white")
        selected_role_label.pack(pady=10)

        def on_role_change(*args):
            selected_role = role_var.get()
            selected_role_label.config(text=f"Selected Role: {selected_role.capitalize()}")

        role_dropdown = tk.OptionMenu(main_content, role_var, *roles, command=on_role_change)
        role_dropdown.pack(pady=10)

        def send_notification():
            notification_message = notification_entry.get("1.0", "end").strip()
            selected_role = role_var.get()

            if not notification_message:
                messagebox.showerror("Error", "Notification message cannot be empty.")
                return

            try:
                recipients = []
                if selected_role == "all":
                    cursor.execute("SELECT username FROM users")
                else:
                    cursor.execute("SELECT username FROM users WHERE role = %s", (selected_role,))
                recipients = cursor.fetchall()

                # Admin user (if applicable)
                admin_username = 'admin'
                if selected_role == "all" or selected_role in ["principal", "faculty", "accountant", "hod"]:
                    recipients = [(admin_username,)] + recipients if (admin_username,) not in recipients else recipients

                if recipients:
                    for recipient in recipients:
                        cursor.execute(
                            "INSERT INTO adminda_notifications (message, sender, recipient) VALUES (%s, %s, %s)",
                            (notification_message, admin_username, recipient[0])
                        )
                    db.commit()
                    messagebox.showinfo("Success", f"Notification sent to all {selected_role.capitalize()}s.")
                else:
                    messagebox.showinfo("Info", f"No {selected_role.capitalize()}s found to send notifications.")

                notification_entry.delete("1.0", "end")

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Failed to send notification. Error: {str(err)}")

        tk.Button(main_content, text="Send Notification", command=send_notification, font=('Arial', 14),
                  bg='#1abc9c', fg='white').pack(pady=20)
        
    def group_chat_button(username):
        try:
            # Query to count unread messages for the current user in the group chat
            cursor.execute("""
                SELECT COUNT(*) FROM groupp_chat_messages 
                WHERE receiver_user_id IS NULL AND is_read = FALSE
            """)
            unread_count = cursor.fetchone()[0]

            # Update button text and color based on unread messages
            if unread_count > 0:
                button4.config(text=f"Group Chat ({unread_count})", bg="red", fg="white")
            else:
                button4.config(text="Group Chat", bg="#2c3e50", fg="white")

            # Check for unread messages every 1 second
            button4.after(1000, group_chat_button, username)  # Update every 1 second

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def on_group_chat_click(username, main_content):
        # Open the group chat sidebar
        open_group_chat_sidebar(username, main_content)

        # Reset the button color to its normal state after clicking
        button4.config(bg="#2c3e50", fg="white")

        # Optionally, mark all unread messages as read
        try:
            cursor.execute("""
                UPDATE groupp_chat_messages 
                SET is_read = TRUE 
                WHERE receiver_user_id IS NULL AND is_read = FALSE
            """)
            db.commit()
        except mysql.connector.Error as err:
            print(f"Error marking messages as read: {err}")

    def load_content(page_name):
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()
        if page_name == "Logout":
            root.destroy()
            test()  # Assuming test() is a function that handles the login screen
        elif page_name == "User Details":
            create_page5_content()  # Load buttons for roles
        else:
            tk.Label(main_content, text=f"Welcome to {page_name}", font=('Arial', 24)).pack(pady=20)

#################################################################################################################

    def create_page5_content():
        # Create a new content for Page 5
        page5_content = tk.Frame(main_content, bg='white')
        page5_content.pack(expand=True, fill="both")

        tk.Label(page5_content, text="View Details", font=('Arial', 24)).pack(pady=20)

        button_width = 20  # Set desired width
        button_height = 2  # Set desired height
        dark_green = '#006400'  # Dark green color
        light_green = '#90EE90'  # Light green color (for active background)

        student_button = tk.Button(page5_content, text='Student', font=('Arial', 14), bg=dark_green, fg='white',
                                width=button_width, height=button_height, activebackground=light_green, command=open_student_window)
        student_button.pack(pady=10, padx=20)

        faculty_button = tk.Button(page5_content, text='Faculty', font=('Arial', 14), bg=dark_green, fg='white',
                           width=button_width, height=button_height, activebackground=light_green, command=open_faculty_window)

        faculty_button.pack(pady=10, padx=20)

        hod_button = tk.Button(page5_content, text='HOD', font=('Arial', 14), bg=dark_green, fg='white',
                       width=button_width, height=button_height, activebackground=light_green, command=open_hod_window)

        hod_button.pack(pady=10, padx=20)

        accountant_button = tk.Button(page5_content, text='Accountant', font=('Arial', 14), bg=dark_green, fg='white',
                              width=button_width, height=button_height, activebackground=light_green, command=open_accountant_window)

        accountant_button.pack(pady=10, padx=20)

    def open_student_window():
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=back_to_page5,
                                bg='#8B008B', fg='white', width=25, height=3,
                                activebackground='#DDA0DD')  # Dark magenta background, light magenta on click
        back_button.pack(pady=10)

        view_button = tk.Button(main_content, text='View All Students', font=('Arial', 14), command=view_students,
                                bg='#8B008B', fg='white', width=25, height=3,
                                activebackground='#DDA0DD')  # Dark magenta background, light magenta on click
        view_button.pack(pady=10)

    def open_student_details(username):
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="Student Details", font=('Arial', 24)).pack(pady=20)

        # Create a frame for the Treeview and scrollbar with the specified size
        detail_frame = tk.Frame(main_content)
        detail_frame.pack(pady=10)

        # Set the size of the frame using the grid geometry manager
        detail_frame.grid_propagate(False)  # Prevent the frame from resizing to fit contents
        detail_frame.config(width=1100, height=500)

        # Create a Treeview widget for student details
        columns = ("Field", "Details")
        tree = ttk.Treeview(detail_frame, columns=columns, show="headings")
        tree.pack(side='left', fill='both', expand=True)

        # Configure the column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=250)  # Adjust width as needed

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(detail_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscroll=scrollbar.set)

        try:
            # Fetch student details for the given username
            cursor.execute("""
                SELECT s.student_id, s.student_name, u.username, u.role, 
                    s.admission_date, s.department, s.semester, 
                    s.admission_number, s.roll_no, s.gender, s.dob, 
                    s.blood_group, s.father_name, s.father_occupation, 
                    s.mother_name, s.mother_occupation, s.address, 
                    s.city, s.country, s.religion, s.caste, 
                    s.pin_code, s.state, s.email, s.phone, 
                    s.parent_phone, s.guardian_name, 
                    s.guardian_relationship, s.guardian_phone, 
                    s.guardian_address 
                FROM students s 
                JOIN users u ON s.user_id = u.id 
                WHERE u.username = %s
            """, (username,))
            student = cursor.fetchone()

            if not student:
                messagebox.showinfo("Info", "No student details found for this username.")
                return

            # Display student details in the Treeview
            field_labels = [
                "Student ID", "Student Name", "Username", "Role",
                "Admission Date", "Department", "Semester", 
                "Admission Number", "Roll No", "Gender", "DOB", 
                "Blood Group", "Father's Name", "Father's Occupation", 
                "Mother's Name", "Mother's Occupation", "Address", 
                "City", "Country", "Religion", "Caste", 
                "Pin Code", "State", "Email", "Phone", 
                "Parent Phone", "Guardian Name", 
                "Guardian Relationship", "Guardian Phone", 
                "Guardian Address"
            ]
            
            # Insert student details into the Treeview
            for label, value in zip(field_labels, student):
                tree.insert("", tk.END, values=(label, value))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        # Back button to return to the previous page
        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=back_to_page5, bg='blue', fg='white')
        back_button.pack(side='left', padx=10, pady=10)

        # Delete Student button
        delete_button = tk.Button(main_content, text='Delete Student', font=('Arial', 14), command=lambda: delete_student(username), bg='blue', fg='white')
        delete_button.pack(side='left', padx=10, pady=10)

    def commit_changes():
        try:
            # Use the same connection to commit changes
            cursor.execute("COMMIT")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while committing changes: {str(e)}")

    def delete_student(username):
        # Confirmation dialog
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this student?"):
            for attempt in range(3):  # Retry up to 3 times
                try:
                    # Fetch the user's ID using the username
                    cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
                    user_id = cursor.fetchone()
                    
                    if user_id:
                        user_id = user_id[0]
                        # Delete the student from the students table
                        cursor.execute("DELETE FROM students WHERE user_id = %s", (user_id,))
                        # Delete the user from the users table
                        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
                        commit_changes()  # Call the commit function
                        messagebox.showinfo("Success", "Student deleted successfully.")
                        back_to_page5()  # Go back to the previous page after deletion
                        return  # Exit the function after successful deletion
                    else:
                        messagebox.showerror("Error", "User not found.")
                    break  # Exit the retry loop if the user is found
                except Exception as e:
                    if "Lock wait timeout exceeded" in str(e):
                        if attempt < 2:  # Retry only if we haven't exhausted attempts
                            time.sleep(1)  # Wait before retrying
                        else:
                            messagebox.showerror("Error", f"An error occurred while deleting the student: {str(e)}")
                    else:
                        messagebox.showerror("Error", f"An error occurred while deleting the student: {str(e)}")

    def show_login_window():
        # Create a new window for login
        login_window = tk.Toplevel()
        login_window.title("Login")

        tk.Label(login_window, text="Enter Username:", font=('Arial', 14)).pack(pady=10)

        username_entry = tk.Entry(login_window, font=('Arial', 14))
        username_entry.pack(pady=10)

        def on_login():
            username = username_entry.get()
            if username:
                cursor.execute("SELECT role FROM users WHERE username = %s", (username,))
                role = cursor.fetchone()

                if role and role[0] == 'student':
                    open_student_details(username)
                    login_window.destroy()  # Close the login window
                else:
                    messagebox.showerror("Error", "Username does not belong to a student.")
            else:
                messagebox.showwarning("Warning", "Please enter a username.")

        login_button = tk.Button(login_window, text="Login", font=('Arial', 14), command=on_login)
        login_button.pack(pady=10)
    # Declare the tree variable globally
    
    tree = None
    def view_students():
        global tree  # Declare the tree variable as global

        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="All Student Details", font=('Arial', 24)).pack(pady=20)

        # Create a frame for the Treeview and scrollbar
        student_frame = tk.Frame(main_content)
        student_frame.pack(pady=10)

        # Create a Treeview widget for listing students
        columns = ("Student ID", "Student Name", "Username", "Role", "Department", "Semester")
        tree = ttk.Treeview(student_frame, columns=columns, show="headings")
        tree.pack(side='left', fill='both', expand=True)

        # Configure the column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=150)  # Adjust width as needed

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(student_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscroll=scrollbar.set)

        # Set a minimum size for the Treeview frame
        student_frame.configure(width=1100, height=400)

        # Create a frame for the department and semester selection
        selection_frame = tk.Frame(main_content)
        selection_frame.pack(pady=20)

        # Create a StringVar to hold the selected department
        department_var = tk.StringVar()
        
        # Create a StringVar to hold the selected semester
        semester_var = tk.StringVar()

        # Create a frame for department section (combobox and button)
        department_frame = tk.Frame(selection_frame)
        department_frame.pack(side='left', padx=20)

        # Create a Combobox for department selection
        department_var = ttk.Combobox(department_frame, textvariable=department_var, font=("Helvetica", 12), state='readonly')
        department_var['values'] = [
            "B.E Civil Engineering",
            "B.E Computer Science Engineering",
            "B.E Electrical and Electronics Engineering",
            "B.E Electronics and Communication Engineering",
            "B.Tech Information Technology",
            "B.E Mechanical Engineering",
            "B.Tech Artificial Intelligence and Data Science",
            "B.Tech Computer Science and Business Systems",
            "Marine Engineering",
            "Aerospace Engineering",
            "Master of Business Administration (MBA)",
            "Master of Computer Application (MCA)",
            "M.E Power Electronics and Drives",
            "M.E Communication systems",
            "M.E Computer Science Engineering",
            "M.E Engineering Design"
        ]
        department_var.pack(padx=10)

        confirm_department_button = tk.Button(department_frame, text='Confirm Department', font=("Helvetica", 12), 
                                            command=lambda: filter_students_by_department(department_var.get()), 
                                            bg='blue', fg='white')

        confirm_department_button.pack(pady=10)

        # Create a frame for semester section (combobox and button)
        semester_frame = tk.Frame(selection_frame)
        semester_frame.pack(side='left', padx=20)

        # Create a Combobox for semester selection
        semester_var = ttk.Combobox(semester_frame, textvariable=semester_var, font=("Helvetica", 12), state='readonly')
        semester_var['values'] = [
"1st Semester","2nd Semester","3ed Semester","4th Semester","5th Semester","6th Semester","7th Semester","8th Semester"
        ]
        semester_var.pack(padx=10)

        # Create Confirm button for semester selection below the semester combobox
        confirm_semester_button = tk.Button(semester_frame, text='Confirm Semester', font=("Helvetica", 12), 
                                            command=lambda: filter_students_by_semester(semester_var.get()), 
                                            bg='blue', fg='white')
        confirm_semester_button.pack(pady=10)

        # Create Back button to return to the previous page
        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=open_student_window, bg='blue', fg='white')
        back_button.pack(side='left', padx=10, pady=10)

        # Create View button to open login window
        view_button = tk.Button(main_content, text='View', font=('Arial', 14), command=show_login_window, bg='blue', fg='white')
        view_button.pack(side='left', padx=10, pady=10)

        # Fetch and display all students initially
        display_all_students()


    def display_all_students():
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        try:
            # Execute the query to fetch all students
            cursor.execute("""
                SELECT s.student_id, s.student_name, u.username, u.role, s.department, s.semester 
                FROM students s 
                JOIN users u ON s.user_id = u.id
            """)
            students = cursor.fetchall()

            # Insert all student details into the Treeview
            for student_id, student_name, username, role, department, semester in students:
                tree.insert("", tk.END, values=(student_id, student_name, username, role, department, semester))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while fetching student details: {str(e)}")

    def filter_students_by_department(selected_department):
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        # Check if a department is selected
        if not selected_department:
            messagebox.showwarning("Warning", "Please select a department.")
            return  # Exit the function if no department is selected

        try:
            conn = connect_to_db()  # Establish a connection to the database
            if conn is None:
                messagebox.showerror("Error", "Database connection failed.")
                return

            cursor = conn.cursor()

            # SQL query to fetch students from the selected department with role 'student'
            cursor.execute("""
                SELECT s.student_id, s.student_name, u.username, u.role, s.department, s.semester 
                FROM students s 
                JOIN users u ON s.user_id = u.id 
                WHERE s.department = %s AND u.role = 'student'
            """, (selected_department,))

            students = cursor.fetchall()

            if not students:
                messagebox.showinfo("Info", "No students found in the selected department.")
                return

            # Insert filtered student details into the Treeview
            for student_id, student_name, username, role, department, semester in students:
                tree.insert("", tk.END, values=(student_id, student_name, username, role, department, semester))

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {str(err)}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while fetching student details: {str(e)}")
        finally:
            cursor.close()  # Close the cursor
            conn.close()    # Close the database connection


    def filter_students_by_semester(selected_semester):
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        # Check if a department is selected
        if not selected_semester:
            messagebox.showwarning("Warning", "Please select a semester.")
            return  # Exit the function if no department is selected

        try:
            conn = connect_to_db()  # Establish a connection to the database
            if conn is None:
                messagebox.showerror("Error", "Database connection failed.")
                return

            cursor = conn.cursor()

            # SQL query to fetch students from the selected department with role 'student'
            cursor.execute("""
                SELECT s.student_id, s.student_name, u.username, u.role, s.department, s.semester 
                FROM students s 
                JOIN users u ON s.user_id = u.id 
                WHERE s.semester = %s AND u.role = 'student'
            """, (selected_semester,))

            students = cursor.fetchall()

            if not students:
                messagebox.showinfo("Info", "No students found in the selected Semester.")
                return

            # Insert filtered student details into the Treeview
            for student_id, student_name, username, role, department, semester in students:
                tree.insert("", tk.END, values=(student_id, student_name, username, role, department, semester))

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {str(err)}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while fetching student details: {str(e)}")
        finally:
            cursor.close()  # Close the cursor
            conn.close()    # Close the database connection

    def show_users_by_role(role):
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        back_button = tk.Button(main_content, text="Back", font=('Arial', 12), command=display_role_buttons)
        back_button.pack(pady=10, anchor='w')

        tk.Label(main_content, text=f"Users in Role: {role}", font=('Arial', 24)).pack(pady=20)

        tree = ttk.Treeview(main_content, columns=("ID", "Username", "Role", "Action"), show="headings", height=10)
        tree.heading("ID", text="ID")
        tree.heading("Username", text="Username")
        tree.heading("Role", text="Role")
        tree.heading("Action", text="Action")
        tree.column("ID", width=50, anchor='center')
        tree.column("Username", width=200, anchor='center')
        tree.column("Role", width=100, anchor='center')
        tree.column("Action", width=100, anchor='center')
        tree.pack(pady=20, fill="both", expand=True)

        scrollbar = ttk.Scrollbar(main_content, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        try:
            cursor.execute("SELECT id, username, role FROM users WHERE role = %s", (role,))
            users = cursor.fetchall()

            for user in users:
                tree.insert("", tk.END, values=user + ("View",))

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to retrieve user details: {err}")

        tree.bind("<ButtonRelease-1>", lambda event: handle_treeview_click(tree, event))

    def handle_treeview_click(tree, event):
        item = tree.selection()
        if item:
            user_data = tree.item(item, 'values')
            user_id = user_data[0]
            messagebox.showinfo("User Info", f"Viewing details for User ID: {user_id}")

    def back_to_page5():
        for widget in main_content.winfo_children():
            widget.destroy()
        create_page5_content()

    def display_role_buttons():
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        # Create buttons for each role
        roles = ["Student", "Faculty", "HOD", "Principal", "Accountant", "Admin"]
        tk.Label(main_content, text="Select a Role", font=('Arial', 24)).pack(pady=20)

        for role in roles:
            role_button = tk.Button(main_content, text=role, font=('Arial', 14), command=lambda r=role: show_users_by_role(r))
            role_button.pack(pady=5)

        back_button = tk.Button(main_content, text="Back", font=('Arial', 12), command=back_to_page5)
        back_button.pack(pady=10)

###########################################################################################################################

    def open_faculty_window():
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=back_to_page5,
                                bg='#8B008B', fg='white', width=25, height=3,
                                activebackground='#DDA0DD')  # Dark magenta background, light magenta on click
        back_button.pack(pady=10)

        view_button = tk.Button(main_content, text='View All Faculties', font=('Arial', 14), command=view_faculty,
                                bg='#8B008B', fg='white', width=25, height=3,
                                activebackground='#DDA0DD')  # Dark magenta background, light magenta on click
        view_button.pack(pady=10)

    def open_faculty_details(username):
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="Faculty Details", font=('Arial', 24)).pack(pady=20)

        # Create a frame for the Treeview and scrollbar with the specified size
        detail_frame = tk.Frame(main_content)
        detail_frame.pack(pady=10)

        # Set the size of the frame using the grid geometry manager
        detail_frame.grid_propagate(False)  # Prevent the frame from resizing to fit contents
        detail_frame.config(width=1100, height=500)

        # Create a Treeview widget for student details
        columns = ("Field", "Details")
        tree = ttk.Treeview(detail_frame, columns=columns, show="headings")
        tree.pack(side='left', fill='both', expand=True)

        # Configure the column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=250)  # Adjust width as needed

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(detail_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscroll=scrollbar.set)

        try:
            # Fetch faculty details for the given username
            cursor.execute("""
                SELECT f.faculty_id, f.faculty_name, u.username, u.role, 
                    f.department, f.faculty_gender, f.faculty_dob, 
                    f.faculty_blood_group, f.faculty_marital_status, 
                    f.faculty_job_position, f.faculty_address, 
                    f.faculty_city, f.faculty_country, f.faculty_pin_code, 
                    f.faculty_state, f.faculty_email, f.faculty_phone, 
                    f.faculty_guardian_name, f.faculty_guardian_relationship, 
                    f.faculty_guardian_phone, f.faculty_guardian_address 
                FROM faculty f
                JOIN users u ON f.user_id = u.id
                WHERE u.username = %s
            """, (username,))
            faculty = cursor.fetchone()

            if not faculty:
                messagebox.showinfo("Info", "No faculty details found for this username.")
                return

            # Display faculty details in the Treeview (adjust fields and labels as needed)
            field_labels = [
                "Faculty ID", "Faculty Name", "Username", "Role", 
                "Department", "Gender", "DOB", "Blood Group", 
                "Marital Status", "Job Position", "Address", 
                "City", "Country", "Pin Code", "State", 
                "Email", "Phone", "Guardian Name", 
                "Guardian Relationship", "Guardian Phone", 
                "Guardian Address"
            ]

            # Insert student details into the Treeview
            for label, value in zip(field_labels, faculty):
                tree.insert("", tk.END, values=(label, value))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        # Back button to return to the previous page
        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=back_to_page5, bg='blue', fg='white')
        back_button.pack(side='left', padx=10, pady=10)

        # Delete Student button
        delete_button = tk.Button(main_content, text='Delete faculty', font=('Arial', 14), command=lambda: delete_faculty(username), bg='blue', fg='white')
        delete_button.pack(side='left', padx=10, pady=10)

    def commit_changes():
        try:
            # Use the same connection to commit changes
            cursor.execute("COMMIT")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while committing changes: {str(e)}")

    def delete_faculty(username):
        # Confirmation dialog
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this faculty?"):
            for attempt in range(3):  # Retry up to 3 times
                try:
                    # Fetch the user's ID using the username
                    cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
                    user_id = cursor.fetchone()
                    
                    if user_id:
                        user_id = user_id[0]
                        # Delete the student from the students table
                        cursor.execute("DELETE FROM faculty WHERE user_id = %s", (user_id,))
                        # Delete the user from the users table
                        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
                        commit_changes()  # Call the commit function
                        messagebox.showinfo("Success", "faculty deleted successfully.")
                        back_to_page5()  # Go back to the previous page after deletion
                        return  # Exit the function after successful deletion
                    else:
                        messagebox.showerror("Error", "User not found.")
                    break  # Exit the retry loop if the user is found
                except Exception as e:
                    if "Lock wait timeout exceeded" in str(e):
                        if attempt < 2:  # Retry only if we haven't exhausted attempts
                            time.sleep(1)  # Wait before retrying
                        else:
                            messagebox.showerror("Error", f"An error occurred while deleting the faculty: {str(e)}")
                    else:
                        messagebox.showerror("Error", f"An error occurred while deleting the faculty: {str(e)}")

    def show_faculty_login_window():
        # Create a new window for login
        login_window = tk.Toplevel()
        login_window.title("Login")

        tk.Label(login_window, text="Enter Username:", font=('Arial', 14)).pack(pady=10)

        username_entry = tk.Entry(login_window, font=('Arial', 14))
        username_entry.pack(pady=10)

        def on_login():
            username = username_entry.get()
            if username:
                cursor.execute("SELECT role FROM users WHERE username = %s", (username,))
                role = cursor.fetchone()

                if role and role[0] == 'faculty':
                    open_faculty_details(username)
                    login_window.destroy()  # Close the login window
                else:
                    messagebox.showerror("Error", "Username does not belong to a faculty.")
            else:
                messagebox.showwarning("Warning", "Please enter a username.")

        login_button = tk.Button(login_window, text="Login", font=('Arial', 14), command=on_login)
        login_button.pack(pady=10)
    # Declare the tree variable globally

    tree = None
    def view_faculty():
        global tree  # Declare the tree variable as global

        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="All faculty Details", font=('Arial', 24)).pack(pady=20)

        # Create a frame for the Treeview and scrollbar
        student_frame = tk.Frame(main_content)
        student_frame.pack(pady=10)

        # Create a Treeview widget for listing students
        columns = ("faculty ID", "faculty Name", "Username", "Role", "Department")
        tree = ttk.Treeview(student_frame, columns=columns, show="headings")
        tree.pack(side='left', fill='both', expand=True)

        # Configure the column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=150)  # Adjust width as needed

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(student_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscroll=scrollbar.set)

        # Set a minimum size for the Treeview frame
        student_frame.configure(width=1100, height=400)

        # Create a frame for the department and semester selection
        selection_frame = tk.Frame(main_content)
        selection_frame.pack(pady=20)

        # Create a StringVar to hold the selected department
        department_var = tk.StringVar()

        # Create a frame for department section (combobox and button)
        department_frame = tk.Frame(selection_frame)
        department_frame.pack(side='left', padx=20)

        # Create a Combobox for department selection
        department_var = ttk.Combobox(department_frame, textvariable=department_var, font=("Helvetica", 12), state='readonly')
        department_var['values'] = [
            "B.E Civil Engineering",
            "B.E Computer Science Engineering",
            "B.E Electrical and Electronics Engineering",
            "B.E Electronics and Communication Engineering",
            "B.Tech Information Technology",
            "B.E Mechanical Engineering",
            "B.Tech Artificial Intelligence and Data Science",
            "B.Tech Computer Science and Business Systems",
            "Marine Engineering",
            "Aerospace Engineering",
            "Master of Business Administration (MBA)",
            "Master of Computer Application (MCA)",
            "M.E Power Electronics and Drives",
            "M.E Communication systems",
            "M.E Computer Science Engineering",
            "M.E Engineering Design"
        ]
        department_var.pack(padx=10)

        # Create Confirm button for department selection below the department combobox
        confirm_department_button = tk.Button(department_frame, text='Confirm Department', font=("Helvetica", 12), 
                                            command=lambda: filter_faculty_by_department(department_var.get()), 
                                            bg='blue', fg='white')
        confirm_department_button.pack(pady=10)

        # Create Back button to return to the previous page
        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=open_faculty_window, bg='blue', fg='white')
        back_button.pack(side='left', padx=10, pady=10)

        # Create View button to open login window
        view_button = tk.Button(main_content, text='View', font=('Arial', 14), command=show_faculty_login_window, bg='blue', fg='white')
        view_button.pack(side='left', padx=10, pady=10)

        # Fetch and display all students initially
        display_all_faculty()


    def display_all_faculty():
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        try:
            # Execute the query to fetch all students
            cursor.execute("""
                SELECT s.faculty_id, s.faculty_name, u.username, u.role, s.department 
                FROM faculty s 
                JOIN users u ON s.user_id = u.id
            """)
            faculty = cursor.fetchall()

            # Insert all student details into the Treeview
            for faculty_id, faculty_name, username, role, department in faculty:
                tree.insert("", tk.END, values=(faculty_id, faculty_name, username, role, department))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while fetching student details: {str(e)}")

    def filter_faculty_by_department(selected_department):
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        # Check if a department is selected
        if not selected_department:
            messagebox.showwarning("Warning", "Please select a department.")
            return  # Exit the function if no department is selected

        try:
            conn = connect_to_db()  # Establish a connection to the database
            if conn is None:
                messagebox.showerror("Error", "Database connection failed.")
                return

            cursor = conn.cursor()

            # SQL query to fetch students from the selected department with role 'student'
            cursor.execute("""
                SELECT s.faculty_id, s.faculty_name, u.username, u.role, s.department
                FROM faculty s 
                JOIN users u ON s.user_id = u.id 
                WHERE s.department = %s AND u.role = 'faculty'
            """, (selected_department,))

            faculty = cursor.fetchall()

            if not faculty:
                messagebox.showinfo("Info", "No faculty found in the selected department.")
                return

            # Insert filtered student details into the Treeview
            for faculty_id, faculty_name, username, role, department in faculty:
                tree.insert("", tk.END, values=(faculty_id, faculty_name, username, role, department))

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {str(err)}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while fetching faculty details: {str(e)}")
        finally:
            cursor.close()  # Close the cursor
            conn.close()    # Close the database connection

##########################################################################################################################
    def open_hod_window():
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=back_to_page5,
                                bg='#8B008B', fg='white', width=25, height=3,
                                activebackground='#DDA0DD')  # Dark magenta background, light magenta on click
        back_button.pack(pady=10)

        view_button = tk.Button(main_content, text='View All HOD', font=('Arial', 14), command=view_hod,
                                bg='#8B008B', fg='white', width=25, height=3,
                                activebackground='#DDA0DD')  # Dark magenta background, light magenta on click
        view_button.pack(pady=10)

    def open_hod_details(username):
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="HOD Details", font=('Arial', 24)).pack(pady=20)

        # Create a frame for the Treeview and scrollbar with the specified size
        detail_frame = tk.Frame(main_content)
        detail_frame.pack(pady=10)

        # Set the size of the frame using the grid geometry manager
        detail_frame.grid_propagate(False)  # Prevent the frame from resizing to fit contents
        detail_frame.config(width=1100, height=500)

        # Create a Treeview widget for student details
        columns = ("Field", "Details")
        tree = ttk.Treeview(detail_frame, columns=columns, show="headings")
        tree.pack(side='left', fill='both', expand=True)

        # Configure the column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=250)  # Adjust width as needed

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(detail_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscroll=scrollbar.set)

        try:
            # Fetch faculty details for the given username
            cursor.execute("""
                SELECT f.faculty_id, f.faculty_name, u.username, u.role, 
                    f.department, f.faculty_gender, f.faculty_dob, 
                    f.faculty_blood_group, f.faculty_marital_status, 
                    f.faculty_job_position, f.faculty_address, 
                    f.faculty_city, f.faculty_country, f.faculty_pin_code, 
                    f.faculty_state, f.faculty_email, f.faculty_phone, 
                    f.faculty_guardian_name, f.faculty_guardian_relationship, 
                    f.faculty_guardian_phone, f.faculty_guardian_address 
                FROM hod f
                JOIN users u ON f.user_id = u.id
                WHERE u.username = %s
            """, (username,))
            faculty = cursor.fetchone()

            if not faculty:
                messagebox.showinfo("Info", "No HOD details found for this username.")
                return

            # Display faculty details in the Treeview (adjust fields and labels as needed)
            field_labels = [
                "Faculty ID", "Faculty Name", "Username", "Role", 
                "Department", "Gender", "DOB", "Blood Group", 
                "Marital Status", "Job Position", "Address", 
                "City", "Country", "Pin Code", "State", 
                "Email", "Phone", "Guardian Name", 
                "Guardian Relationship", "Guardian Phone", 
                "Guardian Address"
            ]

            # Insert student details into the Treeview
            for label, value in zip(field_labels, faculty):
                tree.insert("", tk.END, values=(label, value))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        # Back button to return to the previous page
        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=back_to_page5, bg='blue', fg='white')
        back_button.pack(side='left', padx=10, pady=10)

        # Delete Student button
        delete_button = tk.Button(main_content, text='Delete hod', font=('Arial', 14), command=lambda: delete_hod(username), bg='blue', fg='white')
        delete_button.pack(side='left', padx=10, pady=10)

    def commit_changes():
        try:
            # Use the same connection to commit changes
            cursor.execute("COMMIT")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while committing changes: {str(e)}")

    def delete_hod(username):
        # Confirmation dialog
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this hod?"):
            for attempt in range(3):  # Retry up to 3 times
                try:
                    # Fetch the user's ID using the username
                    cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
                    user_id = cursor.fetchone()
                    
                    if user_id:
                        user_id = user_id[0]
                        # Delete the student from the students table
                        cursor.execute("DELETE FROM hod WHERE user_id = %s", (user_id,))
                        # Delete the user from the users table
                        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
                        commit_changes()  # Call the commit function
                        messagebox.showinfo("Success", "hod deleted successfully.")
                        back_to_page5()  # Go back to the previous page after deletion
                        return  # Exit the function after successful deletion
                    else:
                        messagebox.showerror("Error", "User not found.")
                    break  # Exit the retry loop if the user is found
                except Exception as e:
                    if "Lock wait timeout exceeded" in str(e):
                        if attempt < 2:  # Retry only if we haven't exhausted attempts
                            time.sleep(1)  # Wait before retrying
                        else:
                            messagebox.showerror("Error", f"An error occurred while deleting the hod: {str(e)}")
                    else:
                        messagebox.showerror("Error", f"An error occurred while deleting the hod: {str(e)}")

    def show_hod_login_window():
        # Create a new window for login
        login_window = tk.Toplevel()
        login_window.title("Login")

        tk.Label(login_window, text="Enter Username:", font=('Arial', 14)).pack(pady=10)

        username_entry = tk.Entry(login_window, font=('Arial', 14))
        username_entry.pack(pady=10)

        def on_login():
            username = username_entry.get()
            if username:
                cursor.execute("SELECT role FROM users WHERE username = %s", (username,))
                role = cursor.fetchone()

                if role and role[0] == 'hod':
                    open_hod_details(username)
                    login_window.destroy()  # Close the login window
                else:
                    messagebox.showerror("Error", "Username does not belong to a hod.")
            else:
                messagebox.showwarning("Warning", "Please enter a username.")

        login_button = tk.Button(login_window, text="Login", font=('Arial', 14), command=on_login)
        login_button.pack(pady=10)
    # Declare the tree variable globally

    tree = None
    def view_hod():
        global tree  # Declare the tree variable as global

        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="All HOD Details", font=('Arial', 24)).pack(pady=20)

        # Create a frame for the Treeview and scrollbar
        student_frame = tk.Frame(main_content)
        student_frame.pack(pady=10)

        # Create a Treeview widget for listing students
        columns = ("faculty ID", "faculty Name", "Username", "Role", "Department")
        tree = ttk.Treeview(student_frame, columns=columns, show="headings")
        tree.pack(side='left', fill='both', expand=True)

        # Configure the column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=150)  # Adjust width as needed

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(student_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscroll=scrollbar.set)

        # Set a minimum size for the Treeview frame
        student_frame.configure(width=1100, height=400)

        # Create a frame for the department and semester selection
        selection_frame = tk.Frame(main_content)
        selection_frame.pack(pady=20)

        # Create a StringVar to hold the selected department
        department_var = tk.StringVar()

        # Create a frame for department section (combobox and button)
        department_frame = tk.Frame(selection_frame)
        department_frame.pack(side='left', padx=20)

        # Create a Combobox for department selection
        department_var = ttk.Combobox(department_frame, textvariable=department_var, font=("Helvetica", 12), state='readonly')
        department_var['values'] = [
            "B.E Civil Engineering",
            "B.E Computer Science Engineering",
            "B.E Electrical and Electronics Engineering",
            "B.E Electronics and Communication Engineering",
            "B.Tech Information Technology",
            "B.E Mechanical Engineering",
            "B.Tech Artificial Intelligence and Data Science",
            "B.Tech Computer Science and Business Systems",
            "Marine Engineering",
            "Aerospace Engineering",
            "Master of Business Administration (MBA)",
            "Master of Computer Application (MCA)",
            "M.E Power Electronics and Drives",
            "M.E Communication systems",
            "M.E Computer Science Engineering",
            "M.E Engineering Design"
        ]
        department_var.pack(padx=10)

        # Create Confirm button for department selection below the department combobox
        confirm_department_button = tk.Button(department_frame, text='Confirm Department', font=("Helvetica", 12), 
                                            command=lambda: filter_hod_by_department(department_var.get()), 
                                            bg='blue', fg='white')
        confirm_department_button.pack(pady=10)

        # Create Back button to return to the previous page
        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=open_hod_window, bg='blue', fg='white')
        back_button.pack(side='left', padx=10, pady=10)

        # Create View button to open login window
        view_button = tk.Button(main_content, text='View', font=('Arial', 14), command=show_hod_login_window, bg='blue', fg='white')
        view_button.pack(side='left', padx=10, pady=10)

        # Fetch and display all students initially
        display_all_hod()


    def display_all_hod():
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        try:
            # Execute the query to fetch all students
            cursor.execute("""
                SELECT s.faculty_id, s.faculty_name, u.username, u.role, s.department 
                FROM hod s 
                JOIN users u ON s.user_id = u.id
            """)
            faculty = cursor.fetchall()

            # Insert all student details into the Treeview
            for faculty_id, faculty_name, username, role, department in faculty:
                tree.insert("", tk.END, values=(faculty_id, faculty_name, username, role, department))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while fetching student details: {str(e)}")

    def filter_hod_by_department(selected_department):
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        # Check if a department is selected
        if not selected_department:
            messagebox.showwarning("Warning", "Please select a department.")
            return  # Exit the function if no department is selected

        try:
            conn = connect_to_db()  # Establish a connection to the database
            if conn is None:
                messagebox.showerror("Error", "Database connection failed.")
                return

            cursor = conn.cursor()

            # SQL query to fetch students from the selected department with role 'student'
            cursor.execute("""
                SELECT s.faculty_id, s.faculty_name, u.username, u.role, s.department
                FROM hod s 
                JOIN users u ON s.user_id = u.id 
                WHERE s.department = %s AND u.role = 'hod'
            """, (selected_department,))

            faculty = cursor.fetchall()

            if not faculty:
                messagebox.showinfo("Info", "No hod found in the selected department.")
                return

            # Insert filtered student details into the Treeview
            for faculty_id, faculty_name, username, role, department in faculty:
                tree.insert("", tk.END, values=(faculty_id, faculty_name, username, role, department))

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {str(err)}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while fetching hod details: {str(e)}")
        finally:
            cursor.close()  # Close the cursor
            conn.close()    # Close the database connection
############################################################################################################################
 
    def open_accountant_window():
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=back_to_page5,
                                bg='#8B008B', fg='white', width=25, height=3,
                                activebackground='#DDA0DD')  # Dark magenta background, light magenta on click
        back_button.pack(pady=10)

        view_button = tk.Button(main_content, text='View All Accountant', font=('Arial', 14), command=view_accountant,
                                bg='#8B008B', fg='white', width=25, height=3,
                                activebackground='#DDA0DD')  # Dark magenta background, light magenta on click
        view_button.pack(pady=10)

    def open_accountant_details(username):
        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="accountant Details", font=('Arial', 24)).pack(pady=20)

        # Create a frame for the Treeview and scrollbar with the specified size
        detail_frame = tk.Frame(main_content)
        detail_frame.pack(pady=10)

        # Set the size of the frame using the grid geometry manager
        detail_frame.grid_propagate(False)  # Prevent the frame from resizing to fit contents
        detail_frame.config(width=1100, height=500)

        # Create a Treeview widget for student details
        columns = ("Field", "Details")
        tree = ttk.Treeview(detail_frame, columns=columns, show="headings")
        tree.pack(side='left', fill='both', expand=True)

        # Configure the column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=250)  # Adjust width as needed

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(detail_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscroll=scrollbar.set)

        try:
            # Fetch faculty details for the given username
            cursor.execute("""
                SELECT f.faculty_id, f.faculty_name, u.username, u.role, 
                    f.department, f.faculty_gender, f.faculty_dob, 
                    f.faculty_blood_group, f.faculty_marital_status, 
                    f.faculty_job_position, f.faculty_address, 
                    f.faculty_city, f.faculty_country, f.faculty_pin_code, 
                    f.faculty_state, f.faculty_email, f.faculty_phone, 
                    f.faculty_guardian_name, f.faculty_guardian_relationship, 
                    f.faculty_guardian_phone, f.faculty_guardian_address 
                FROM accountant f
                JOIN users u ON f.user_id = u.id
                WHERE u.username = %s
            """, (username,))
            faculty = cursor.fetchone()

            if not faculty:
                messagebox.showinfo("Info", "No Accountant details found for this username.")
                return

            # Display faculty details in the Treeview (adjust fields and labels as needed)
            field_labels = [
                "Faculty ID", "Faculty Name", "Username", "Role", 
                "Department", "Gender", "DOB", "Blood Group", 
                "Marital Status", "Job Position", "Address", 
                "City", "Country", "Pin Code", "State", 
                "Email", "Phone", "Guardian Name", 
                "Guardian Relationship", "Guardian Phone", 
                "Guardian Address"
            ]

            # Insert student details into the Treeview
            for label, value in zip(field_labels, faculty):
                tree.insert("", tk.END, values=(label, value))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        # Back button to return to the previous page
        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=back_to_page5, bg='blue', fg='white')
        back_button.pack(side='left', padx=10, pady=10)

        # Delete Student button
        delete_button = tk.Button(main_content, text='Delete hod', font=('Arial', 14), command=lambda: delete_accountant(username), bg='blue', fg='white')
        delete_button.pack(side='left', padx=10, pady=10)

    def commit_changes():
        try:
            # Use the same connection to commit changes
            cursor.execute("COMMIT")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while committing changes: {str(e)}")

    def delete_accountant(username):
        # Confirmation dialog
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this accountant?"):
            for attempt in range(3):  # Retry up to 3 times
                try:
                    # Fetch the user's ID using the username
                    cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
                    user_id = cursor.fetchone()
                    
                    if user_id:
                        user_id = user_id[0]
                        # Delete the student from the students table
                        cursor.execute("DELETE FROM accountant WHERE user_id = %s", (user_id,))
                        # Delete the user from the users table
                        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
                        commit_changes()  # Call the commit function
                        messagebox.showinfo("Success", "Accountant deleted successfully.")
                        back_to_page5()  # Go back to the previous page after deletion
                        return  # Exit the function after successful deletion
                    else:
                        messagebox.showerror("Error", "User not found.")
                    break  # Exit the retry loop if the user is found
                except Exception as e:
                    if "Lock wait timeout exceeded" in str(e):
                        if attempt < 2:  # Retry only if we haven't exhausted attempts
                            time.sleep(1)  # Wait before retrying
                        else:
                            messagebox.showerror("Error", f"An error occurred while deleting the accountant: {str(e)}")
                    else:
                        messagebox.showerror("Error", f"An error occurred while deleting the accountant: {str(e)}")

    def show_accountant_login_window():
        # Create a new window for login
        login_window = tk.Toplevel()
        login_window.title("Login")

        tk.Label(login_window, text="Enter Username:", font=('Arial', 14)).pack(pady=10)

        username_entry = tk.Entry(login_window, font=('Arial', 14))
        username_entry.pack(pady=10)

        def on_login():
            username = username_entry.get()
            if username:
                cursor.execute("SELECT role FROM users WHERE username = %s", (username,))
                role = cursor.fetchone()

                if role and role[0] == 'accountant':
                    open_accountant_details(username)
                    login_window.destroy()  # Close the login window
                else:
                    messagebox.showerror("Error", "Username does not belong to a accountant.")
            else:
                messagebox.showwarning("Warning", "Please enter a username.")

        login_button = tk.Button(login_window, text="Login", font=('Arial', 14), command=on_login)
        login_button.pack(pady=10)
    # Declare the tree variable globally

    tree = None
    def view_accountant():
        global tree  # Declare the tree variable as global

        # Clear the main content area
        for widget in main_content.winfo_children():
            widget.destroy()

        tk.Label(main_content, text="All accountant Details", font=('Arial', 24)).pack(pady=20)

        # Create a frame for the Treeview and scrollbar
        student_frame = tk.Frame(main_content)
        student_frame.pack(pady=10)

        # Create a Treeview widget for listing students
        columns = ("faculty ID", "faculty Name", "Username", "Role")
        tree = ttk.Treeview(student_frame, columns=columns, show="headings")
        tree.pack(side='left', fill='both', expand=True)

        # Configure the column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=150)  # Adjust width as needed

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(student_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscroll=scrollbar.set)

        # Set a minimum size for the Treeview frame
        student_frame.configure(width=1100, height=400)

        # Create a frame for the department and semester selection
        selection_frame = tk.Frame(main_content)
        selection_frame.pack(pady=20)

        # Create a frame for department section (combobox and button)
        department_frame = tk.Frame(selection_frame)
        department_frame.pack(side='left', padx=20)

        # Create Back button to return to the previous page
        back_button = tk.Button(main_content, text='Back', font=('Arial', 14), command=open_accountant_window, bg='blue', fg='white')
        back_button.pack(side='left', padx=10, pady=10)

        # Create View button to open login window
        view_button = tk.Button(main_content, text='View', font=('Arial', 14), command=show_accountant_login_window, bg='blue', fg='white')
        view_button.pack(side='left', padx=10, pady=10)

        # Fetch and display all students initially
        display_all_accountant()


    def display_all_accountant():
        global tree  # Access the global tree variable

        # Clear existing entries in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        try:
            # Execute the query to fetch all students
            cursor.execute("""
                SELECT s.faculty_id, s.faculty_name, u.username, u.role
                FROM accountant s 
                JOIN users u ON s.user_id = u.id
            """)
            faculty = cursor.fetchall()

            # Insert all student details into the Treeview
            for faculty_id, faculty_name, username, role in faculty:
                tree.insert("", tk.END, values=(faculty_id, faculty_name, username, role))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while fetching accountant details: {str(e)}")


    def get_total_students():
        db = connect_to_db()  # Establish a database connection
        if db is None:
            print("Database connection failed.")
            return 0  # Return 0 if connection fails

        cursor = db.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM users WHERE role = 'student'")  # Query to count students
            result = cursor.fetchone()  # Fetch the result

            # Debugging print statements
            print("Query executed successfully. Result fetched:", result)

            # Return count, or 0 if no result
            return result[0] if result is not None else 0  
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return 0  # Return 0 on error
        finally:
            cursor.close()  # Close the cursor
            db.close()      # Close the database connection

    # Example of using the function
    total_students = get_total_students()
    print(f"Total number of students: {total_students}")

    def get_total_faculty():
        db = connect_to_db()  # Establish a database connection
        if db is None:
            print("Database connection failed.")
            return 0  # Return 0 if connection fails

        cursor = db.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM users WHERE role = 'faculty'")  # Query to count faculty
            result = cursor.fetchone()  # Fetch the result
            return result[0] if result is not None else 0  # Return count, or 0 if no result
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return 0  # Return 0 on error
        finally:
            cursor.close()  # Close the cursor
            db.close()      # Close the database connection

    def get_total_hod():
        db = connect_to_db()  # Establish a database connection
        if db is None:
            print("Database connection failed.")
            return 0  # Return 0 if connection fails

        cursor = db.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM users WHERE role = 'hod'")  # Query to count faculty
            result = cursor.fetchone()  # Fetch the result
            return result[0] if result is not None else 0  # Return count, or 0 if no result
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return 0  # Return 0 on error
        finally:
            cursor.close()  # Close the cursor
            db.close()      # Close the database connection

    def get_total_accountant():
        db = connect_to_db()  # Establish a database connection
        if db is None:
            print("Database connection failed.")
            return 0  # Return 0 if connection fails

        cursor = db.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM users WHERE role = 'accountant'")  # Query to count faculty
            result = cursor.fetchone()  # Fetch the result
            return result[0] if result is not None else 0  # Return count, or 0 if no result
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return 0  # Return 0 on error
        finally:
            cursor.close()  # Close the cursor
            db.close()      # Close the database connection

    def get_total_principal():
        db = connect_to_db()  # Establish a database connection
        if db is None:
            print("Database connection failed.")
            return 0  # Return 0 if connection fails

        cursor = db.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM users WHERE role = 'principal'")  # Query to count faculty
            result = cursor.fetchone()  # Fetch the result
            return result[0] if result is not None else 0  # Return count, or 0 if no result
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return 0  # Return 0 on error
        finally:
            cursor.close()  # Close the cursor
            db.close()      # Close the database connection

    def get_total_users():
        db = connect_to_db()  # Establish a database connection
        if db is None:
            print("Database connection failed.")
            return 0  # Return 0 if connection fails

        cursor = db.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM users ")  # Query to count faculty
            result = cursor.fetchone()  # Fetch the result
            return result[0] if result is not None else 0  # Return count, or 0 if no result
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return 0  # Return 0 on error
        finally:
            cursor.close()  # Close the cursor
            db.close()      # Close the database connection

    # Function to create buttons for various roles
    def users_count_window():
        # Clear the main content frame
        for widget in main_content.winfo_children():
            widget.destroy()

        # Create a new frame for Page 6 content
        page6_frame = tk.Frame(main_content, bg='white')
        page6_frame.pack(expand=True, fill='both')

        # Button settings
        button_width = 18  # Set a fixed width for the buttons

        # Optional: Add an empty row for spacing
        page6_frame.grid_rowconfigure(0, minsize=50)  # Add 50 pixels of space above

        # Create the buttons for different roles using grid for horizontal alignment
        student_button = tk.Button(page6_frame, text='Student', font=('Arial', 14), 
                                    fg='white', bg='#8B4513', relief='flat', width=button_width, command=show_student_count)
        student_button.grid(row=1, column=0, padx=10, pady=10)  # First button
        student_button.bind("<Enter>", lambda event: student_button.configure(bg='#A0522D'))
        student_button.bind("<Leave>", lambda event: student_button.configure(bg='#8B4513'))

        faculty_button = tk.Button(page6_frame, text='Faculty', font=('Arial', 14), 
                                    fg='white', bg='#8B4513', relief='flat', width=button_width, command=show_faculty_count)
        faculty_button.grid(row=1, column=1, padx=10, pady=10)  # Second button
        faculty_button.bind("<Enter>", lambda event: faculty_button.configure(bg='#A0522D'))
        faculty_button.bind("<Leave>", lambda event: faculty_button.configure(bg='#8B4513'))

        hod_button = tk.Button(page6_frame, text='HOD', font=('Arial', 14), 
                                fg='white', bg='#8B4513', relief='flat', width=button_width, command=show_hod_count)
        hod_button.grid(row=1, column=2, padx=10, pady=10)  # Third button
        hod_button.bind("<Enter>", lambda event: hod_button.configure(bg='#A0522D'))
        hod_button.bind("<Leave>", lambda event: hod_button.configure(bg='#8B4513'))

        accountant_button = tk.Button(page6_frame, text='Accountant', font=('Arial', 14), 
                                        fg='white', bg='#8B4513', relief='flat', width=button_width, command=show_accountant_count)
        accountant_button.grid(row=1, column=3, padx=10, pady=10)  # Fourth button
        accountant_button.bind("<Enter>", lambda event: accountant_button.configure(bg='#A0522D'))
        accountant_button.bind("<Leave>", lambda event: accountant_button.configure(bg='#8B4513'))

        principal_button = tk.Button(page6_frame, text='Principal', font=('Arial', 14), 
                                        fg='white', bg='#8B4513', relief='flat', width=button_width, command=show_principal_count)
        principal_button.grid(row=1, column=4, padx=10, pady=10)  # Fifth button
        principal_button.bind("<Enter>", lambda event: principal_button.configure(bg='#A0522D'))
        principal_button.bind("<Leave>", lambda event: principal_button.configure(bg='#8B4513'))

        total_button = tk.Button(page6_frame, text='Total Users', font=('Arial', 14), 
                                        fg='white', bg='#8B4513', relief='flat', width=button_width, command=show_total_users)
        total_button.place(x=10 , y=200)  # Fifth button
        total_button.bind("<Enter>", lambda event: total_button.configure(bg='#A0522D'))
        total_button.bind("<Leave>", lambda event: total_button.configure(bg='#8B4513'))

        # Label to show total student count
        global student_count_label  # Declare global variable to access in other functions
        student_count_label = tk.Label(page6_frame, text='', font=('Arial', 14), bg='white')
        student_count_label.place(x=30, y=130 )  # Center the label below buttons

        global faculty_count_label
        faculty_count_label = tk.Label(page6_frame, text="", font=('Arial', 14), bg='white')
        faculty_count_label.place(x=280 ,y=130)

        global hod_count_label
        hod_count_label = tk.Label(page6_frame, text="", font=('Arial', 14), bg='white')
        hod_count_label.place(x=510 ,y=130)

        global accountant_count_label
        accountant_count_label = tk.Label(page6_frame, text="", font=('Arial', 14), bg='white')
        accountant_count_label.place(x=720 ,y=130)

        global principal_count_label
        principal_count_label = tk.Label(page6_frame, text="", font=('Arial', 14), bg='white')
        principal_count_label.place(x=950,y=130)

        global total_count_label
        total_count_label = tk.Label(page6_frame, text="", font=('Arial', 14), bg='white')
        total_count_label.place(x=30, y=260)

    # Function to show the total student count
    def show_student_count():
        total_students = get_total_students()  # Get the total student count
        student_count_label.config(text=f'Total Students: {total_students}')  # Update the label with count
    def show_faculty_count():
        total_faculty = get_total_faculty()
        faculty_count_label.config(text=f"Total Faculty: {total_faculty}")
    def show_hod_count():
        total_hod = get_total_hod()
        hod_count_label.config(text=f"Total HOD: {total_hod}")
    def show_accountant_count():
        total_accountant = get_total_accountant()
        accountant_count_label.config(text=f"Total Accountant: {total_accountant}")
    def show_principal_count():
        total_principal = get_total_principal()
        principal_count_label.config(text=f"Total Principal: {total_principal}")
    def show_total_users():
        total_users = get_total_users()
        total_count_label.config(text=f"Total Principal: {total_users}")

    button3 = tk.Button(sidebar, text='send_notification', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button3.pack(fill='x')
    button3.config(command=open_notification_interface)
    button3.bind("<Enter>", lambda event: button3.configure(bg='blue'))
    button3.bind("<Leave>", lambda event: button3.configure(bg='#2c3e50'))

    button4 = tk.Button(sidebar, text='group chat', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button4.pack(fill='x')
    button4.config(command=lambda: on_group_chat_click(username,main_content))
    button4.bind("<Enter>", lambda event: button4.configure(bg='blue'))
    button4.bind("<Leave>", lambda event: button4.configure(bg='#2c3e50'))

    button5 = tk.Button(sidebar, text='Users Details', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button5.pack(fill='x')
    button5.config(command=lambda: load_content('User Details'))
    button5.bind("<Enter>", lambda event: button5.configure(bg='blue'))
    button5.bind("<Leave>", lambda event: button5.configure(bg='#2c3e50'))

    # Create a button in the sidebar for Users Count
    button6 = tk.Button(sidebar, text='Users Count', font=('Arial', 14), 
                        fg='white', bg='#2c3e50', relief='flat') 
    button6.pack(fill='x')
    button6.config(command=users_count_window)  # Call the function directly
    button6.bind("<Enter>", lambda event: button6.configure(bg='blue'))
    button6.bind("<Leave>", lambda event: button6.configure(bg='#2c3e50'))


    button7 = tk.Button(sidebar, text='Page 7', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button7.pack(fill='x')
    button7.config(command=lambda: load_content('Page 7'))
    button7.bind("<Enter>", lambda event: button7.configure(bg='blue'))
    button7.bind("<Leave>", lambda event: button7.configure(bg='#2c3e50'))

    button8 = tk.Button(sidebar, text='Back', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button8.pack(fill='x')
    button8.config(command=lambda: switch_window(root,login_window))
    button8.bind("<Enter>", lambda event: button8.configure(bg='blue'))
    button8.bind("<Leave>", lambda event: button8.configure(bg='#2c3e50'))

    button_logout = tk.Button(sidebar, text='Logout', font=('Arial', 14), fg='white', bg='#2c3e50', relief='flat')
    button_logout.pack(fill='x')
    button_logout.config(command=lambda: load_content('Logout'))
    button_logout.bind("<Enter>", lambda event: button_logout.configure(bg='blue'))
    button_logout.bind("<Leave>", lambda event: button_logout.configure(bg='#2c3e50'))
    
    # Simulating calling open_notification_interface to test
    open_notification_interface()

    group_chat_button(username)

    root.mainloop()


def test():
    print("button clicked")

# Main window
window = tk.Tk()
window.title("STUDENT MANAGEMENT SYSTEM")
window.geometry("1366x768")

# Load and display background image
image_path = "a3.jpg"  # Path to your image
image = Image.open(image_path)
image = image.resize((1366, 768), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)
background_label = tk.Label(window, image=photo)
background_label.place(relwidth=1, relheight=1)
# Style configurations
style = ttk.Style()
style.configure("TLabel", font=("arial", 14))
style.configure("TEntry", font=("arial", 12), padding=5)
style.configure("TButton", font=("arial", 16), padding=5, relief="raised")


# Create a standard button with specific styles
logbutton = tk.Button(
    window,
    text="LOGIN",
    command=login_window,
    bg="black",  # Dark blue background
    fg="white",    # White font color
    font=("Arial", 20),  # Increased font size
    relief="raised",
    padx=20,  # Increased padding for width
    pady=10   # Increased padding for height
)

# Function to change the button color when hovered over
def on_enter(e):
    logbutton['bg'] = 'white'  # Light blue on hover

# Function to change the button color back when not hovered
def on_leave(e):
    logbutton['bg'] = 'black'  # Dark blue

# Bind hover events
logbutton.bind("<Enter>", on_enter)
logbutton.bind("<Leave>", on_leave)

# Position the button
logbutton.place(x=600, y=300)


window.mainloop()
