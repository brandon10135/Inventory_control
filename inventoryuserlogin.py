import customtkinter
import hashlib
import sqlite3

class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self,text='Login')
        self.label.pack(pady=12,padx=10)
        
        self.user_entry= customtkinter.CTkEntry(self,placeholder_text="Username")
        self.user_entry.pack(pady=12,padx=10)
        
        self.user_pass= customtkinter.CTkEntry(self,placeholder_text="Password",show="*")
        self.user_pass.pack(pady=12,padx=10)
        
        button = customtkinter.CTkButton(self,text='Login', command=self.check)
        button.pack(pady=12,padx=10)

        self.label_login_warning = customtkinter.CTkLabel(self,text='Please enter correct information',text_color = 'red')

    def check(self):
        user_entered_password = self.user_pass.get()
        user_entered_username = self.user_entry.get()

        if not user_entered_password or not user_entered_username:
            self.label_login_warning.pack(pady=12,padx=10)
            self.label_login_warning.configure(text="Username or password cannot be blank")
        else:
            encypted_password = hashlib.sha256(user_entered_password.encode()).hexdigest()

            conn = sqlite3.connect(r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\user_login\Support_docs\user_storage.db")
            cursor = conn.cursor()
            cursor.execute("SELECT password FROM users WHERE username=?", (user_entered_username,))
            stored_password = cursor.fetchone()

            if stored_password is not None and stored_password[0] == encypted_password:
                self.master.replace_frame_main_page()
            else:
                self.label_login_warning.pack(pady=12,padx=10)
                self.label_login_warning.configure(text="Incorrect username or password")

class RegisterFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self,text='Register')
        self.label.pack(pady=12,padx=10)
        
        self.user_entry= customtkinter.CTkEntry(self,placeholder_text="Username")
        self.user_entry.pack(pady=12,padx=10)
        
        self.user_pass= customtkinter.CTkEntry(self,placeholder_text="Enter New Password",show="*")
        self.user_pass.pack(pady=12,padx=10)

        self.user_pass_again= customtkinter.CTkEntry(self,placeholder_text="Enter New Password",show="*")
        self.user_pass_again.pack(pady=12,padx=10)
        
        button = customtkinter.CTkButton(self,text='Register user',command = self.encrypt_store)
        button.pack(pady=12,padx=10)

        button = customtkinter.CTkButton(self,text='Back to main page',command = self.master.replace_frame_main_page)
        button.pack(pady=12,padx=10)        

        self.label_login_warning = customtkinter.CTkLabel(self,text_color = 'red')

    def encrypt_store(self):
        user_entered_username = self.user_entry.get()
        user_entered_password = self.user_pass.get()
        user_entered_password_again = self.user_pass_again.get()
#Check and see if the boxes are blank 
        if not user_entered_password or not user_entered_username:
            self.label_login_warning.pack(pady=12,padx=10)
            self.label_login_warning.configure(text="Username or password cannot be blank")
#Ensure the password actually match eachother
        elif user_entered_password != user_entered_password_again:
            self.label_login_warning.pack(pady=12,padx=10)
            self.label_login_warning.configure(text="Password and confirm password do not match")
#Encrypt and store the passwords inside the database
        else:
            encypted_password = hashlib.sha256(user_entered_password.encode()).hexdigest()
            conn = sqlite3.connect(r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\user_login\Support_docs\user_storage.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user_entered_username, encypted_password))
            conn.commit()
            conn.close()
            self.master.replace_frame_main_page()
            self.master.open_toplevel()
