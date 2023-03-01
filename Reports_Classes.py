import customtkinter
import sqlite3
import pandas as pd
import datetime

class ReportsFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self, text='Create reports here')
        self.label.grid(row=0, column=0, columnspan=2, pady=12, padx=10)

        button = customtkinter.CTkButton(self, text='Create Full report', command=self.report_full_successful)
        button.grid(row=1, column=0, pady=12, padx=10)

        button = customtkinter.CTkButton(self, text='Create Minimum report', command=self.report_minimum_successful)
        button.grid(row=2, column=0, pady=12, padx=10)

        button = customtkinter.CTkButton(self, text='Create Maximum report', command=self.report_maximum_success)
        button.grid(row=3, column=0, pady=12, padx=10)

        button = customtkinter.CTkButton(self, text='Create Reorder report', command=self.reorder_report_success)
        button.grid(row=4, column=0, pady=12, padx=10)

#Create a list to add values from the listbox to and generate custom report
        self.selected_values = []

        self.listbox = customtkinter.CTkComboBox(self, values = self.master.item_list_maker())
        self.listbox.grid(row=0, rowspan=4, column=1, pady=12, padx=10)

        button = customtkinter.CTkButton(self, text='Add to report list', command=self.get_value_and_show_label)
        button.grid(row=3, column=1, pady=12, padx=10)

        self.feedback_label = customtkinter.CTkLabel(self, text='', text_color = 'green')
        self.feedback_label.grid(row=4, column=1, pady=12, padx=10)

        button = customtkinter.CTkButton(self, text='Generate Custom report', command=self.custom_report_success)
        button.grid(row=5, column=1, pady=12, padx=10)

        button_4 = customtkinter.CTkButton(self, text='Back to Main Page', command=self.master.replace_frame_main_page)
        button_4.grid(row=6, column=0, columnspan=2, pady=12, padx=10)

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
    
    def maximum_report(self):
        now = datetime.datetime.now()
        conn = sqlite3.connect(r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\inventory.db")
        df = pd.read_sql_query("SELECT * FROM Inventory_Trial WHERE product_count > product_maximum", conn)
        file_name = f"Maximum_Inventory_Report_{now.strftime('%Y-%m-%d')}.xlsx"
        df.to_excel(rf"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\Excel docs\{file_name}", index=False)
        conn.close()
    
    def reorder_report(self):
        now = datetime.datetime.now()
        conn = sqlite3.connect(r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\inventory.db")
        df = pd.read_sql_query("SELECT * FROM Inventory_Trial WHERE product_count < reorder_count", conn)
        file_name = f"Reorder_Inventory_Report_{now.strftime('%Y-%m-%d')}.xlsx"
        df.to_excel(rf"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\Excel docs\{file_name}", index=False)
        conn.close()

    def get_value(self):
        selected_value = self.listbox.get()
        self.selected_values.append(selected_value)
        return self.selected_values
    
    def generate_custom_report(self):
        now = datetime.datetime.now()
        conn = sqlite3.connect(r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\inventory.db")
        combined_df = pd.DataFrame()
        for value in self.selected_values:
            query = "SELECT * FROM Inventory_Trial WHERE product_name='" + value + "'"
            df = pd.read_sql_query(query, conn)
            combined_df = pd.concat([combined_df, df], ignore_index=True)
        file_name = f"Custom_Inventory_Report1_{now.strftime('%Y-%m-%d')}.xlsx"
        combined_df.to_excel(rf"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\Excel docs\{file_name}", index=False)

    def report_minimum_successful(self):
        self.minimum_count()
        self.master.report_top_success()

    def report_full_successful(self):
        self.full_report()
        self.master.report_top_success()
    
    def report_maximum_success(self):
        self.maximum_report()
        self.master.report_top_success()
    
    def reorder_report_success(self):
        self.reorder_report()
        self.master.report_top_success()
    
    def custom_report_success(self):
        self.generate_custom_report()
        self.master.report_top_success()

    def get_value_and_show_label(self):
        self.get_value()
        self.feedback_label.configure(text='Added to report list')
        self.after(3000, self.clear_feedback_label)

    def clear_feedback_label(self):
        self.feedback_label.configure(text='')

class AnalyticsFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
#Setting up the ranges of option boxes for the day, month and year. Also setting up the current year as the default option for the boxes
        days_of_month = [str(day) for day in range(1, 32)]
        months_of_year =[str(month) for month in range(1,13)]
        current_year = datetime.datetime.now().year
        years = [str(year) for year in range(1980, current_year + 1)]
        now = datetime.datetime.now()
        current_year = now.strftime("%Y")
#Setting up the optionboxes for the start year of when to pull analytics
        self.label = customtkinter.CTkLabel(self, text='Start Day')
        self.label.grid(row=0, column=0, pady=6, padx=10)
        self.combobox_days = customtkinter.CTkOptionMenu(self,values=days_of_month)
        self.combobox_days.grid(row=1, column=0, padx = 10, pady = 6)

        self.label = customtkinter.CTkLabel(self, text='Start Month')
        self.label.grid(row=2, column=0, pady=6, padx=10)
        self.combobox_month = customtkinter.CTkOptionMenu(self,values=months_of_year)
        self.combobox_month.grid(row=3, column=0, padx = 10, pady = 6)

        self.combobox_year = customtkinter.CTkOptionMenu(self, values=years)
        self.combobox_year.set(current_year)
        self.combobox_year.grid(row=5, column=0, padx = 10, pady = 6) 

#Setting up the end of timeframe for when to pull analytics
        self.label = customtkinter.CTkLabel(self, text='End Day')
        self.label.grid(row=0, column=1, pady=6, padx=10)
        self.combobox_days_end = customtkinter.CTkOptionMenu(self,values=days_of_month)
        self.combobox_days_end.grid(row=1, column=1, padx = 10, pady = 6)

        self.label = customtkinter.CTkLabel(self, text='End Month')
        self.label.grid(row=2, column=1, pady=6, padx=10)
        self.combobox_month_end = customtkinter.CTkOptionMenu(self,values=months_of_year)
        self.combobox_month_end.grid(row=3, column=1, padx = 10, pady = 6)

        self.label = customtkinter.CTkLabel(self, text='End Year')
        self.label.grid(row=4, column=1, pady=6, padx=10)

        self.combobox_year_end = customtkinter.CTkOptionMenu(self, values=years)
        self.combobox_year_end.set(current_year)
        self.combobox_year_end.grid(row=5, column=1, padx = 10, pady = 6) 
#Setting up buttons and labels to create a list to add values to and create a list for pulling specified products
        self.listbox_product = customtkinter.CTkComboBox(self,values=self.master.item_list_maker())
        self.listbox_product.grid(row = 6, column = 0, pady=12, padx=10)

        self.feedback_label = customtkinter.CTkLabel(self, text='', text_color = 'green')
        self.feedback_label.grid(row=7, column=0, columnspan = 2, pady=12, padx=10)

        button = customtkinter.CTkButton(self,command = self.get_value_and_show_label, text = 'Add to report')
        button.grid(row = 6, column = 1, pady=12, padx=10)

        button = customtkinter.CTkButton(self, text = 'Generate report', command = self.final_analytic_pull)
        button.grid(row = 8, column = 0, columnspan = 2, pady=6, padx=10)

        self.selected_values = []

    def analytic_pull(self):
        start_day = self.combobox_days.get()
        start_month = self.combobox_month.get()
        start_year = self.combobox_year.get()
        end_day = self.combobox_days_end.get()
        end_month = self.combobox_month_end.get()
        end_year = self.combobox_year_end.get()

        now = datetime.datetime.now()
        conn = sqlite3.connect(r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\inventory_analytics.db")
        cursor = conn.cursor()
        combined_df = pd.DataFrame()

        for value in self.selected_values:
            query = "SELECT * FROM Analytics WHERE product_name=? AND timestamp BETWEEN ? AND ?"
            cursor.execute(query, (value, start_year + "-" + start_month + "-" + start_day, end_year + "-" + end_month + "-" + end_day))
            results = cursor.fetchall()
            df = pd.DataFrame(results)
            combined_df = pd.concat([combined_df, df], ignore_index=True)

        file_name = f"Analytics__Report_{now.strftime('%Y-%m-%d')}.xlsx"
        combined_df.to_excel(rf"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\Excel docs\{file_name}", index=False)

    def get_value(self):
        selected_value = self.listbox_product.get()
        self.selected_values.append(selected_value)
        return self.selected_values

    def get_value_and_show_label(self):
        self.get_value()
        self.feedback_label.configure(text='Added to report list')
        self.after(3000, self.clear_feedback_label)

    def clear_feedback_label(self):
        self.feedback_label.configure(text='')
    
    def final_analytic_pull(self):
        self.analytic_pull()
        self.master.report_top_success()
