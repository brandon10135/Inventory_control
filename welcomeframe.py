import customtkinter
import sqlite3

class InventoryView(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self,text='Items needing reorder' + "\n" + "Name and QTY OH")
        self.label.pack(pady=6,padx=5)
        self.reorder_count_updater()

    def reorder_count_updater(self):
        textbox = customtkinter.CTkTextbox(self)
        textbox.configure(font=("Courier", 12), width=160, height=425)
        textbox.pack()

        conn = sqlite3.connect(r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\inventory.db")

        cursor = conn.cursor()
        cursor.execute("SELECT product_name, product_count FROM Inventory_Trial WHERE (product_count - reorder_count BETWEEN 0 AND 10) OR (product_count < reorder_count);")
        product_data = cursor.fetchall()

        if product_data:
            # Get the maximum length of the product name string
            max_product_name_length = max([len(str(row[0])) for row in product_data]) + 1

            for row in product_data:
                product_name_end = str(row[0]).ljust(max_product_name_length, " ")
                product_count = str(row[1])
                textbox.insert("0.0", product_name_end + product_count + "\n" + "\n")
        else:
            textbox.insert("0.0", "No data found.")

class MainInventoryView(customtkinter.CTkFrame):
     def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self,text='Items in Inventory'+"\n" + "Name, QTY OH, Reorder QTY, UOM, Location")
        self.label.pack(pady=6,padx=5)

        textbox = customtkinter.CTkTextbox(self)
        textbox.configure(font=("Courier", 12), width=400, height=425)
        textbox.pack()

        conn = sqlite3.connect(r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\inventory.db")

        cursor = conn.cursor()
        cursor.execute("SELECT product_name, product_count, reorder_count, UOM, location FROM Inventory_Trial")
        product_data = cursor.fetchall()

        if product_data:
            # Get the maximum length of the product name string
            max_product_name_length = max([len(str(row[0])) for row in product_data]) + 2
            max_product_count_length = max([len(str(row[1])) for row in product_data]) + 2
            max_product_reorder_count_length = max([len(str(row[2])) for row in product_data]) + 2
            max_product_measure_count_length = max([len(str(row[3])) for row in product_data]) + 2
            for row in product_data:
                product_name_end = str(row[0]).ljust(max_product_name_length, " ")
                product_count = str(row[1]).ljust(max_product_count_length," ")
                product_reorder = str(row[2]).ljust(max_product_reorder_count_length," ")
                product_measure = str(row[3]).ljust(max_product_measure_count_length," ")
                product_location = str(row[4])
                textbox.insert("0.0", product_name_end + product_count + product_reorder + product_measure + product_location + "\n" + "\n")
        else:
            textbox.insert("0.0", "No data found.")

class ButtonsFrame(customtkinter.CTkFrame):
     def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        button = customtkinter.CTkButton(self,text='Update Product Attributes', command = self.master.inventory_updates)
        button.configure(width = 200, height = 50)
        button.pack(pady=20,padx=5)

        button = customtkinter.CTkButton(self,text='Generate Reports', command = self.master.generate_reports)
        button.configure(width = 200, height = 50)
        button.pack(pady=10,padx=15)
     
        button = customtkinter.CTkButton(self,text='Input New Product',command = self.master.new_product_line)
        button.configure(width = 200, height = 50)
        button.pack(pady=20,padx=5)

        button = customtkinter.CTkButton(self,text='Register New Users',command = self.master.replace_frame_register_page)
        button.configure(width = 200, height = 50)
        button.pack(pady=20,padx=5)

        button = customtkinter.CTkButton(self,text='Logout',command = self.master.regi_to_login)
        button.configure(width = 200, height = 50)
        button.pack(pady=20,padx=5)       


