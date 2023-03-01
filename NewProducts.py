import customtkinter
import sqlite3

class NewProducts(customtkinter.CTkFrame):
        def __init__(self, master, **kwargs):
            super().__init__(master, **kwargs)
#Setting up the entire page of entry boxes for inputting a new product
            self.label_new = customtkinter.CTkLabel(self,text='Input entirely new product here')
            self.label_new.grid(row=0, column=0, columnspan=6, pady=10, padx=10)
            self.new_product_name= customtkinter.CTkEntry(self, placeholder_text="Input product name")
            self.new_product_name.grid(row=1, column=0, columnspan=2, pady=10, padx=10)
            self.new_product_count= customtkinter.CTkEntry(self, placeholder_text="Input product quantity")
            self.new_product_count.grid(row=2, column=0, columnspan=2, pady=10, padx=10)
            self.new_product_minimum= customtkinter.CTkEntry(self, placeholder_text="Input product min.")
            self.new_product_minimum.grid(row=3, column=0, columnspan=2, pady=10, padx=10)
            self.new_product_maximum= customtkinter.CTkEntry(self, placeholder_text="Input product max.")
            self.new_product_maximum.grid(row=4, column=0, columnspan=2, pady=10, padx=10)
            self.new_product_reorder= customtkinter.CTkEntry(self, placeholder_text="Input reorder quantity")
            self.new_product_reorder.grid(row=1, column=2, columnspan=2, pady=10, padx=10)
            self.new_product_item= customtkinter.CTkEntry(self, placeholder_text="Input product ID")
            self.new_product_item.grid(row=2, column=2, columnspan=2, pady=10, padx=10) 
            self.new_product_lead= customtkinter.CTkEntry(self, placeholder_text="Input product leadtime")
            self.new_product_lead.grid(row=3, column=2, columnspan=2, pady=10, padx=10)           
            self.new_product_cost= customtkinter.CTkEntry(self, placeholder_text="Input internal cost")
            self.new_product_cost.grid(row=4, column=2, columnspan=2, pady=10, padx=10)  
            self.new_product_external= customtkinter.CTkEntry(self, placeholder_text="Input external cost")
            self.new_product_external.grid(row=1, column=4, columnspan=2, pady=10, padx=10)              
            self.new_product_location= customtkinter.CTkEntry(self, placeholder_text="Input location")
            self.new_product_location.grid(row=2, column=4, columnspan=2, pady=10, padx=10)   
            self.new_product_uom= customtkinter.CTkEntry(self, placeholder_text="Input UOM")
            self.new_product_uom.grid(row=3, column=4, columnspan=2, pady=10, padx=10)  
            self.feedback_label = customtkinter.CTkLabel(self, text='', text_color = 'red')
            self.feedback_label.grid(row=4, column=4, pady=12, padx=10)
            button = customtkinter.CTkButton(self, text='Create new product line', command=self.add_item_final)
            button.grid(row=6, column= 0, columnspan = 6, pady=10, padx=10)
            self.label_new = customtkinter.CTkLabel(self, text='Delete product line here')
            self.label_new.grid(row=7, column=0, columnspan=2, pady=6, padx=10)
            self.new_product_name_delete= customtkinter.CTkEntry(self, placeholder_text="Enter product")
            self.new_product_name_delete.grid(row=8, column=0, columnspan=2, pady=12, padx=10)
            button = customtkinter.CTkButton(self, text='Delete product', command=self.remove_item_final)
            button.grid(row=9, column=0, pady=12, padx=10)
            button = customtkinter.CTkButton(self, text='Back to main page', command=self.master.replace_frame_main_page)
            button.grid(row=10, column=0, pady=12, padx=10)            
             
        def add_item(self):
            conn = sqlite3.connect(r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\inventory.db")
            cursor = conn.cursor()
#Get all of the new product entry box values
            product_name = self.new_product_name.get()
            product_count =  self.new_product_count.get()
            product_minimum = self.new_product_minimum.get()
            product_maximum = self.new_product_maximum.get()
            product_reorder = self.new_product_reorder.get()
            product_id = self.new_product_item.get()
            product_leadtime = self.new_product_lead.get()
            product_internal = self.new_product_cost.get()
            product_external = self.new_product_external.get()
            product_location = self.new_product_location.get()
            product_uom = self.new_product_uom.get()
#Insert the new product entry values into the SQLite database
            cursor.execute("SELECT product_name,Item_ID FROM Inventory_Trial")
            rows = cursor.fetchall()
            product_names = [row[0] for row in rows]
            product_ids = [i[1] for i in rows]
            if product_name in product_names:
                #Warning message telling them their product is already entered into the database with the same name
                self.feedback_label.configure(text='Product name already entered')
                self.after(3000, self.clear_feedback_label)
            if product_id in product_ids:
                self.feedback_label.configure(text='Product ID already entered')
                self.after(3000, self.clear_feedback_label)
            else:
                #Inserting the information into the database if the product name does not exist in the database
                cursor.execute("INSERT INTO Inventory_Trial (product_name, product_count,product_minimum,product_maximum,reorder_count,Item_ID,Lead_time,Internal_cost,external_cost,location,UOM) VALUES (?, ?, ?, ?, ?,?,?,?,?,?,?)", (product_name, product_count,product_minimum,product_maximum,product_reorder,product_id,product_leadtime,product_internal,product_external,product_location,product_uom))
                conn.commit()
                self.master.top_level_succes()
            conn.close()

        def remove_item(self):
            conn = sqlite3.connect(r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\inventory.db")
            cursor = conn.cursor()
            product_name = self.new_product_name_delete.get()
            cursor.execute("DELETE FROM Inventory_Trial WHERE product_name=?", (product_name,))
            conn.commit()
            conn.close()

        def add_item_final(self):
            self.add_item()

        def remove_item_final(self):
            self.remove_item()
            self.master.top_level_succes()

        def clear_feedback_label(self):
            self.feedback_label.configure(text='')
