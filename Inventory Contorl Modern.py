import customtkinter
from inventory_top_classes import *
from inventoryuserlogin import *
from welcomeframe import *
from Inventory_Updater_Classes import * 
from Reports_Classes import *
from NewProducts import *

class App(customtkinter.CTk):
    def __init__(self):

        super().__init__()
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.title("Inventory Control System")
        self.geometry('800x500')
        self.resizable(False, False)
        self.my_frame = LoginFrame(master=self)
        self.my_frame.pack(padx=20, pady=80)
        self.toplevel_window = None

    def new_product_line(self):
        self.destroy_frames()
        self.my_frame = NewProducts(master = self)
        self.my_frame.place(x=0,y=0)

    def inventory_updates(self):
        self.destroy_frames()
        self.my_frame = MainFrame(master = self)
        self.my_frame.place(x = 0, y = 0)
        
    def generate_reports(self):
        self.destroy_frames()
        self.my_frame = ReportsFrame(master =self)
        self.my_frame2 = AnalyticsFrame(master = self)
        self.my_frame.place(x = 0, y =0)
        self.my_frame2.place(x = 350, y = 0)

    def replace_frame_main_page(self):
        self.destroy_frames()
        self.my_frame = MainInventoryView(master = self)
        self.my_frame2 = InventoryView(master = self)
        self.my_frame3 = ButtonsFrame(master = self)
        self.my_frame.place(x = 165, y = 0)
        self.my_frame3.place(x = 570, y = 20)
        self.my_frame2.place(x = 0, y = 0)

    def replace_frame_register_page(self):
        self.destroy_frames()
        self.my_frame = RegisterFrame(master=self)
        self.my_frame.pack(padx=20, pady=80)

    def regi_to_login(self):
        self.destroy_frames()
        self.my_frame = LoginFrame(master=self)
        self.my_frame.pack(padx=20, pady=80)
    
    def back_button(self):
        self.destroy_frames()
        self.replace_frame_main_page()

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self) 
            self.toplevel_window.attributes("-topmost", True)
        else:
            self.toplevel_window.focus()

    def top_level_succes(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ProductUpdateSuccess(self)
            self.toplevel_window.attributes("-topmost", True)
        else:
            self.toplevel_window.focus()

    def report_top_success(self):
         if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ReportSuccess(self)
            self.toplevel_window.attributes("-topmost", True)
         else:
            self.toplevel_window.focus()

    def destroy_frames(self):
        frame_names = ['my_frame', 'my_frame2', 'my_frame3']
        for frame_name in frame_names:
            if hasattr(self, frame_name):
                frame = getattr(self, frame_name)
                frame.destroy()

    def item_list_maker(self):
        conn = sqlite3.connect(r"C:\Users\bnofi\OneDrive\Desktop\Python Code Builds\Inventory Control System\inventory.db")
        cursor = conn.cursor()
        cursor.execute("SELECT product_name FROM Inventory_Trial")
        product_names = [name[0] for name in cursor.fetchall()]
        conn.close()
        return product_names
    
app = App()
app.mainloop()
