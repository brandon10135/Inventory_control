from tkinter import Label,Frame,ttk
import tkinter as tk
import datetime
import hashlib
import sqlite3
import pandas as pd
from PIL import ImageTk, Image

class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = FirstFrame(self) # set first frame to appear here
        self.frame.place(x = 600,y = 50)
        self.frame.configure(bg="white")

        self.iconPath = r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\Support Folder\login.png"
        self.icon = ImageTk.PhotoImage(Image.open(self.iconPath))
        self.icon_size = Label(self.master, image = self.icon)
        self.icon_size.place(x=65,y=50)

    def change(self, frame):
        self.frame.destroy() # delete currrent frame
        self.icon_size.destroy()
        self.frame = frame(self)
        self.frame.configure(bg= 'white')
        self.frame.pack()

    def change_to_registration(self,frame):
        self.frame.destroy()
        self.icon_size.destroy()
        self.frame = frame(self)
        self.frame.configure(bg="white")
        self.frame.place(x = 350, y = 50)

    def regi_to_login(self,frame):
        self.frame.destroy()

        self.iconPath = r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\Support Folder\login.png"
        self.icon = ImageTk.PhotoImage(Image.open(self.iconPath))
        self.icon_size = Label(self.master, image = self.icon)
        self.icon_size.place(x=65,y=50)

        self.frame = frame(self)
        self.frame.place(x = 600,y = 50)
        self.frame.configure(bg="white")

class FirstFrame(tk.Frame,MainApp):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

        master.title("Welcome to your inventory control!")
        master.geometry("925x500+300+200")
        master.configure(bg = "white")

        self.status = tk.Label(self, fg='red',bg="white")
        self.status.pack()

#Creating the username labels and entry box

        heading = tk.Label(self, text = 'Sign in', fg = '#57a1f8', bg = 'white', font = ('Microsoft YaHei UI Light', 23, 'bold'))
        heading.pack()
        blank = tk.Label(self,text = " ",bg="white")
        blank.pack()
        self.username_entry = tk.Entry(self,width = '25',fg = 'black', border = 0, bg = 'white' ,font = ('Microsoft YaHei UI Light', 11))
        self.username_entry.pack()
        self.username_entry.insert(0,'Username')
        Frame(self,width =200,height=2,bg = 'black').pack()
        blank = tk.Label(self,text = " ",bg="white")
        blank.pack()

#Creating the password labels and entry box

        self.pwd = tk.Entry(self, show="*",width = '25',fg = 'black', border = 0, bg = 'white' ,font = ('Microsoft YaHei UI Light', 11))
        self.pwd.pack()
        self.pwd.insert(0,'Password')
        Frame(self,width =200,height=2,bg = 'black').pack()
        self.pwd.bind('<Return>', self.check)
        blank = tk.Label(self,text = " ",bg="white")
        blank.pack()

#Creating the buttons for the first userlogin frame

        btn = tk.Button(self, text="Sign In",width = 27, pady = 7, bg = '#57a1f8', fg = 'white', command=self.check)
        btn.pack()
        blank = tk.Label(self,text = " ",bg="white")
        btn.pack()
        blank = tk.Label(self,text = " ",bg="white")
        blank.pack()
        btn = tk.Button(self, text="Register", command=self.register_use_frame,width = 27, pady = 7, bg = '#57a1f8', fg = 'white')
        btn.pack()

#Clearing the inserted words in the username and password lines

        self.username_entry.bind("<Button-1>", lambda event: self.username_entry.delete(0, tk.END))
        self.pwd.bind("<Button-1>", lambda event: self.pwd.delete(0, tk.END))

#Function to check the password and allow you into the main program if it matches

    def check(self, event=None):
        user_entered_password = self.pwd.get()
        user_entered_username = self.username_entry.get()

        encypted_password = hashlib.sha256(user_entered_password.encode()).hexdigest()

        with open(r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\Support Folder\credentials.txt", "r") as user_database:
            for lines in user_database:
                stored_username,stored_password = lines.strip().split(",")
                print(stored_username,stored_password)
                if stored_username == user_entered_username and stored_password == encypted_password:
                     self.master.change(SecondFrame)
                else:
                    self.status.config(text="Wrong password or username entry")
    
#Switch the frame to register user when they click on the button

    def register_use_frame(self):
        self.master.change_to_registration(RegisterFrame)

class RegisterFrame(tk.Frame):

    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

        master.title("Registration Form")
        master.geometry("925x500+300+200")

        heading = tk.Label(self, text = 'Registration Form', fg = '#57a1f8', bg = 'white', font = ('Microsoft YaHei UI Light', 23, 'bold'))
        heading.pack()
        blank = tk.Label(self,text = " ",bg = 'white')
        blank.pack()

        self.new_username_entry = tk.Entry(self,width = '25',fg = 'black', border = 0, bg = 'white' ,font = ('Microsoft YaHei UI Light', 11))
        self.new_username_entry.pack()
        self.new_username_entry.insert(0,'Enter new username')
        Frame(self,width =200,height=2,bg = 'black').pack()

        blank = tk.Label(self,text = " ",bg = 'white')
        blank.pack()

        self.new_password_entry = tk.Entry(self,width = '25',fg = 'black', border = 0, bg = 'white' ,font = ('Microsoft YaHei UI Light', 11))
        self.new_password_entry.pack()
        self.new_password_entry.insert(0,'Enter new password')
        Frame(self,width =200,height=2,bg = 'black').pack()

        blank = tk.Label(self,text = "" ,bg = 'white')
        blank.pack()
      
        self.new_password_entry_again = tk.Entry(self,width = '25',fg = 'black', border = 0, bg = 'white' ,font = ('Microsoft YaHei UI Light', 11))
        self.new_password_entry_again.pack()
        self.new_password_entry_again.insert(0,'Enter new password again')
        Frame(self,width =200,height=2,bg = 'black').pack()

        blank = tk.Label(self,text = " ",bg = 'white')
        blank.pack()

        btn = tk.Button(self, text="Register", command=self.encrypt_store,width = 27, pady = 7, bg = '#57a1f8', fg = 'white')
        btn.pack()

        self.new_username_entry.bind("<Button-1>", lambda event: self.new_username_entry.delete(0, tk.END))
        self.new_password_entry.bind("<Button-1>", lambda event: self.new_password_entry.delete(0, tk.END))
        self.new_password_entry_again.bind("<Button-1>", lambda event: self.new_password_entry_again.delete(0, tk.END))

    def encrypt_store(self):
        self.status_wrong = tk.Label(self, fg='red')
        self.status_wrong.pack()

        user_entered_username = self.new_username_entry.get()
        user_entered_password = self.new_password_entry.get()
        user_entered_password_again = self.new_password_entry_again.get()

        if user_entered_password == user_entered_password_again:
            sha256 = hashlib.sha256()
            encypted_password = hashlib.sha256(user_entered_password.encode()).hexdigest()
            with open(r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\Support Folder\credentials.txt", 'a') as user_name_storage:
                user_name_storage.write(f"{user_entered_username},")
                user_name_storage.write(f"{encypted_password}\n")
            self.master.regi_to_login(FirstFrame)
        else:
             self.status_wrong.config(text="Your passwords did not match each other.")

class SecondFrame(tk.Frame):

    def __init__(self, master = None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Inventory Control System")
        master.geometry("925x500")
        lbl = tk.Label(self, text='Inventory Control Add/Remove', font = ('Helvetica',16))
        lbl.pack()

# GUI controls for adding entire new items to the inventory 

        self.product = tk.Entry(self,width = '25',fg = 'black', border = 0, bg = '#D3D3D3' ,font = ('Microsoft YaHei UI Light', 11))
        self.product.pack()
        self.product.insert(0,'Enter new prodcut here')
        Frame(self,width =200,height=2,bg = 'black').pack()
      
        self.product_number = tk.Entry(self,width = '25',fg = 'black', border = 0, bg = '#D3D3D3' ,font = ('Microsoft YaHei UI Light', 11))
        self.product_number.pack()
        self.product_number.insert(0,'Enter new prodcut count here')
        Frame(self,width =200,height=2,bg = 'black').pack()
     
        self.minimum = tk.Entry(self,width = '25',fg = 'black', border = 0, bg = '#D3D3D3' ,font = ('Microsoft YaHei UI Light', 11))
        self.minimum.pack()
        self.minimum.insert(0,'Enter product minimum count here')
        Frame(self,width =200,height=2,bg = 'black').pack()
     
        btn = tk.Button(self, text="Add to Inventory", command=self.add_item,width = 27, pady = 7, bg = '#57a1f8', fg = 'white')
        btn.pack()

#Remove entire products from database GUI controls begin here 

        self.product_remove = tk.Entry(self,width = '25',fg = 'black', border = 0, bg = '#D3D3D3' ,font = ('Microsoft YaHei UI Light', 11))
        self.product_remove.pack()
        self.product_remove.insert(0,'Enter product to delete')
        Frame(self,width =200,height=2,bg = 'black').pack()
    
        btn = tk.Button(self, text="Remove from Inventory", command=self.remove_item,width = 27, pady = 7, bg = '#57a1f8', fg = 'white')
        btn.pack()
   
#Begins the interface controls for updating inventory stock levels
     
        self.product_name = tk.Entry(self,width = '25',fg = 'black', border = 0, bg = '#D3D3D3' ,font = ('Microsoft YaHei UI Light', 11))
        self.product_name.pack()
        self.product_name.insert(0,'Enter prodcut here to update here')
        Frame(self,width =200,height=2,bg = 'black').pack()

        self.product_number_addition = tk.Entry(self,width = '25',fg = 'black', border = 0, bg = '#D3D3D3' ,font = ('Microsoft YaHei UI Light', 11))
        self.product_number_addition.pack()
        self.product_number_addition.insert(0,'Enter product count to update')
        Frame(self,width =200,height=2,bg = 'black').pack()

        btn = tk.Button(self, text="Update Inventory", command=self.update_item,width = 27, pady = 7, bg = '#57a1f8', fg = 'white')
        btn.pack()

#Creating the report buttons

        btn = tk.Button(self, text="Get Full Report", command=self.full_report,width = 27, pady = 7, bg = '#57a1f8', fg = 'white')
        btn.pack()
        btn = tk.Button(self, text="Get Minimum Report", command=self.minimum_count,width = 27, pady = 7, bg = '#57a1f8', fg = 'white')
        btn.pack()

#Delete the text for write in boxes here when you click on them

        self.product_name.bind("<Button-1>", lambda event: self.product_name.delete(0, tk.END))
        self.product_number_addition.bind("<Button-1>", lambda event: self.product_number_addition.delete(0, tk.END))
        self.product_remove.bind("<Button-1>", lambda event: self.product_remove.delete(0, tk.END))
        self.product.bind("<Button-1>", lambda event: self.product.delete(0, tk.END))
        self.product_number.bind("<Button-1>", lambda event: self.product_number.delete(0, tk.END))
        self.minimum.bind("<Button-1>", lambda event: self.minimum.delete(0, tk.END))

#######################################################################################################################################

    def user_entry_check1(self,product_count):
        try:
            product_count = int(product_count)
            return product_count
        except ValueError:
            self.status = tk.Label(self, fg='red',bg="white")
            self.status.config(text="Please enter a valid number")
            self.status.pack()
    
    def user_entry_check2(self,product_minimum):
        try:
            product_minimum = int(product_minimum)
            return product_minimum
        except ValueError:
            self.status = tk.Label(self, fg='red',bg="white")
            self.status.config(text="Please enter a valid number")
            self.status.pack()
    
    def add_item(self):
        conn = sqlite3.connect(r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\inventory.db")
        cursor = conn.cursor()

        product_name = self.product.get()
        product_count =  self.product_number.get()
        product_minimum = self.minimum.get()

        product_count = self.user_entry_check1(product_count)
        product_minimum = self.user_entry_check2(product_minimum)

        cursor.execute("SELECT product_name FROM Inventory_Trial")
        rows = cursor.fetchall()

        for names in rows:
            if names[0] == product_name:
                self.status_no = tk.Label(self, fg='Red',bg="white")
                self.status_no.pack()
                self.status_no.config(text="Product already exists inside inventory.")
                return
            
        cursor.execute("INSERT INTO Inventory_Trial (product_name, product_count,product_minimum) VALUES (?, ?, ?)", (product_name, product_count,product_minimum))
        conn.commit()
        conn.close()

        self.status_go = tk.Label(self, fg='Green',bg="white")
        self.status_go.pack()
        self.status_go.config(text="Product succesfully added to database.")

    def remove_item(self):

        conn = sqlite3.connect(r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\inventory.db")
        cursor = conn.cursor()

        product_name = self.product_remove.get()

        cursor.execute("DELETE FROM Inventory_Trial WHERE product_name=?", (product_name,))
        conn.commit()
        conn.close()

    def update_item(self):

        conn = sqlite3.connect(r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\inventory.db")
        cursor = conn.cursor()

        product_name = self.product_name.get()
        product_count = self.product_number_addition.get()

        product_count = self.user_entry_check1(product_count)

        cursor.execute(f"UPDATE Inventory_Trial SET product_count = product_count + {product_count} WHERE product_name = '{product_name}'")
        conn.commit()
        conn.close()
        
    def minimum_count(self):
        now = datetime.datetime.now()
        conn = sqlite3.connect(r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\inventory.db")
        df = pd.read_sql_query("SELECT * FROM Inventory_Trial WHERE product_count < product_minimum", conn)
        file_name = f"Minimum_Inventory_Report_{now.strftime('%Y-%m-%d')}.xlsx"
        df.to_excel(rf"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\Excel docs\{file_name}", index=False)
        conn.close()

    def full_report(self):
        now = datetime.datetime.now()
        conn = sqlite3.connect(r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\inventory.db")
        df = pd.read_sql_query("SELECT * FROM Inventory_Trial", conn)
        file_name = f"Full_Inventory_Report_{now.strftime('%Y-%m-%d')}.xlsx"
        df.to_excel(rf"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\Excel docs\{file_name}", index=False)
        conn.close()

    def global_sql_lists():
        conn = sqlite3.connect(r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\inventory.db")
        cursor = conn.cursor()

        query = "SELECT product_name FROM Inventory_Trial"
        cursor.execute(query)
        products = [row[0] for row in cursor.fetchall()]
        conn.close() 
        return products

if __name__=="__main__":
    app=MainApp()
    app.mainloop()