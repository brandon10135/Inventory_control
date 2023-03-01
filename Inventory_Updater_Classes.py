import customtkinter
import sqlite3
import datetime

class MainFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self,text='Update existing inventory items')
        self.label.grid(row=0, column=0, pady=12, padx=10)
        self.listbox_product = customtkinter.CTkComboBox(self,values=self.master.item_list_maker())
        self.listbox_product.grid(row=1, column=0, pady=12, padx=10)
        self.product_count= customtkinter.CTkEntry(self,placeholder_text="Input amount")
        self.product_count.grid(row=2, column=0, pady=12, padx=10)
        button = customtkinter.CTkButton(self,text='Update product counts', command = self.update_item)
        button.grid(row=3, column=0, pady=12, padx=10)

        self.label = customtkinter.CTkLabel(self,text='Update reorder quantity')
        self.label.grid(row=0, column=1, pady=12, padx=10)

        self.listbox_product_new = customtkinter.CTkComboBox(self,values=self.master.item_list_maker())
        self.listbox_product_new.grid(row=1, column=1, pady=12, padx=10)
        
        self.product_reordercount= customtkinter.CTkEntry(self,placeholder_text= "Input new reorder count")
        self.product_reordercount.grid(row=2, column=1, pady=12, padx=10)
        button = customtkinter.CTkButton(self,text='Update product reorder', command = self.update_item_reorder)
        button.grid(row=3, column=1, pady=12, padx=10)

        self.label = customtkinter.CTkLabel(self,text='Update existing inventory minimum')
        self.label.grid(row=0, column=2, pady=12, padx=10)
        self.listbox_product_min = customtkinter.CTkComboBox(self,values=self.master.item_list_maker())
        self.listbox_product_min.grid(row=1, column=2, pady=12, padx=10)
        self.product_count_min= customtkinter.CTkEntry(self,placeholder_text="Input new minimum")
        self.product_count_min.grid(row=2, column=2, pady=12, padx=10)
        button = customtkinter.CTkButton(self,text='Update product minimum', command = self.update_minimum)
        button.grid(row=3, column=2, pady=12, padx=10)

        self.label = customtkinter.CTkLabel(self,text='Update existing inventory maximum')
        self.label.grid(row=0, column=3, pady=12, padx=10)
        self.listbox_product_max = customtkinter.CTkComboBox(self,values=self.master.item_list_maker())
        self.listbox_product_max.grid(row=1, column=3, pady=12, padx=10)
        self.product_count_max= customtkinter.CTkEntry(self,placeholder_text="Input new maximum")
        self.product_count_max.grid(row=2, column=3, pady=12, padx=10)
        button = customtkinter.CTkButton(self,text='Update product maximum', command = self.update_maximum)
        button.grid(row=3, column=3, pady=12, padx=10)

        self.label = customtkinter.CTkLabel(self,text='Item ID')
        self.label.grid(row=4, column=0, pady=12, padx=10)
        self.listbox_product_item_id = customtkinter.CTkComboBox(self,values=self.master.item_list_maker())
        self.listbox_product_item_id.grid (row = 5, column = 0, pady=12, padx=10)
        self.product_count_idnew= customtkinter.CTkEntry(self,placeholder_text="Input new Item ID")
        self.product_count_idnew.grid(row=6, column=0, pady=12, padx=10)
        button_1 = customtkinter.CTkButton(self,text='Update Item ID', command = self.update_item_id)
        button_1.grid(row=7, column=0, pady=12, padx=10)

        self.label = customtkinter.CTkLabel(self,text='Location')
        self.label.grid(row=4, column=1, pady=12, padx=10)
        self.listbox_product_location = customtkinter.CTkComboBox(self,values=self.master.item_list_maker())
        self.listbox_product_location.grid (row = 5, column = 1, pady=12, padx=10)
        self.product_supplier_info= customtkinter.CTkEntry(self,placeholder_text="Input new Location")
        self.product_supplier_info.grid(row=6, column=1, pady=12, padx=10)
        button_2 = customtkinter.CTkButton(self,text='Update Location', command = self.update_location)
        button_2.grid(row=7, column=1, pady=12, padx=10)

        self.label = customtkinter.CTkLabel(self,text='Internal Cost')
        self.label.grid(row=4, column=2, pady=12, padx=10)
        self.listbox_product_internal = customtkinter.CTkComboBox(self,values=self.master.item_list_maker())
        self.listbox_product_internal.grid (row = 5, column = 2, pady=12, padx=10)
        self.product_internal_cost= customtkinter.CTkEntry(self,placeholder_text="Input new internal cost")
        self.product_internal_cost.grid(row=6, column=2, pady=12, padx=10)
        button_3 = customtkinter.CTkButton(self,text='Update Internal cost', command = self.update_internal_cost)
        button_3.grid(row=7, column=2, pady=12, padx=10)

        self.label = customtkinter.CTkLabel(self,text='External Cost')
        self.label.grid(row=4, column=3, pady=12, padx=10)
        self.listbox_product_external = customtkinter.CTkComboBox(self,values=self.master.item_list_maker())
        self.listbox_product_external.grid (row = 5, column = 3, pady=12, padx=10)
        self.product_external_cost= customtkinter.CTkEntry(self,placeholder_text="Input new external cost")
        self.product_external_cost.grid(row=6, column=3, pady=12, padx=10)
        button_4 = customtkinter.CTkButton(self,text='Update External Cost', command = self.update_external_cost)
        button_4.grid(row=7, column=3, pady=12, padx=10) 

        button_4 = customtkinter.CTkButton(self,text='Back to Main Page', command = self.master.replace_frame_main_page)
        button_4.grid(row=8, column=0, pady=12, padx=10) 

    def update_item(self):

        conn = sqlite3.connect(r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\inventory.db")
        cursor = conn.cursor()

        product_name = self.listbox_product.get()
        product_count = self.product_count.get()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("UPDATE Inventory_Trial SET product_count = product_count + ? WHERE product_name = ?", (product_count, product_name))
        self.analytics_count_updater(product_count,product_name,timestamp)
        conn.commit()
        conn.close()
        self.master.top_level_succes()
    
    def update_item_reorder(self):
        conn = sqlite3.connect(r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\inventory.db")
        cursor = conn.cursor()

        product_name = self.listbox_product_new.get()
        product_count = self.product_reordercount.get()

        cursor.execute("UPDATE Inventory_Trial SET reorder_count = ? WHERE product_name = ?", (product_count, product_name))
        conn.commit()
        conn.close()
        self.master.top_level_succes()

    def update_minimum(self):
        conn = sqlite3.connect(r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\inventory.db")
        cursor = conn.cursor()

        product_name = self.listbox_product_min.get()
        product_count = self.product_count_min.get()

        cursor.execute("UPDATE Inventory_Trial SET product_minimum = ? WHERE product_name = ?", (product_count, product_name))
        conn.commit()
        conn.close()
        self.master.top_level_succes()

    def update_maximum(self):
        conn = sqlite3.connect(r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\inventory.db")
        cursor = conn.cursor()

        product_name = self.listbox_product_max.get()
        product_count = self.product_count_max.get()

        cursor.execute("UPDATE Inventory_Trial SET product_maximum = ? WHERE product_name = ?", (product_count, product_name))
        conn.commit()
        conn.close()
        self.master.top_level_succes()

    def update_item_id(self):
        conn = sqlite3.connect(r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\inventory.db")
        cursor = conn.cursor()

        product_name = self.listbox_product_item_id.get()
        product_count = self.product_count_idnew.get()

        cursor.execute("UPDATE Inventory_Trial SET Item_ID = ? WHERE product_name = ?", (product_count, product_name))
        conn.commit()
        conn.close()
        self.master.top_level_succes()    

    def update_internal_cost(self):
        conn = sqlite3.connect(r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\inventory.db")
        cursor = conn.cursor()

        product_name = self.listbox_product_internal.get()
        product_count = self.product_internal_cost.get()

        cursor.execute("UPDATE Inventory_Trial SET Internal_cost = ? WHERE product_name = ?", (product_count, product_name))
        conn.commit()
        conn.close()
        self.master.top_level_succes()  

    def update_external_cost(self):
        conn = sqlite3.connect(r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\inventory.db")
        cursor = conn.cursor()

        product_name = self.listbox_product_external.get()
        product_count = self.product_external_cost.get()

        cursor.execute("UPDATE Inventory_Trial SET external_cost = ? WHERE product_name = ?", (product_count, product_name))
        conn.commit()
        conn.close()
        self.master.top_level_succes()  

    def update_location(self):
        conn = sqlite3.connect(r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\inventory.db")
        cursor = conn.cursor()

        product_name = self.listbox_product_location.get()
        product_count = self.product_supplier_info.get()

        cursor.execute("UPDATE Inventory_Trial SET location = ? WHERE product_name = ?", (product_count, product_name))
        conn.commit()
        conn.close()
        self.master.top_level_succes()  

    def analytics_count_updater(self,product_count,product_name,timestamp):
        conn = sqlite3.connect(r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\inventory_analytics.db")
        cursor = conn.cursor()
        print('here')

        if product_count[0] == "-":
            cursor.execute("INSERT INTO Analytics (product_count_used, product_name, timestamp) VALUES (?, ?, ?)", (product_count[1:], product_name, timestamp))
            conn.commit()
            conn.close()
        else:
            cursor.execute("INSERT INTO Analytics (product_count_added, product_name, timestamp) VALUES (?, ?, ?)", (product_count, product_name, timestamp))
            conn.commit()
            conn.close()