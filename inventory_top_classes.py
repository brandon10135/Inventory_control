import customtkinter

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x150")
        self.title("Inventory Control System")

        self.label = customtkinter.CTkLabel(self, text="Registration Succesful!")
        self.label.pack(padx=20, pady=20)

        button = customtkinter.CTkButton(self,text='Ok', command = self.destroy_me)
        button.pack(pady=12,padx=10)

    def destroy_me(self):
        self.destroy()

class ProductUpdateSuccess(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x125")
        self.title("Inventory Control System")


        self.label = customtkinter.CTkLabel(self, text="Update action successful")
        self.label.pack(padx=20, pady=20)

        button = customtkinter.CTkButton(self,text='Ok', command = self.destroy_me)
        button.pack(pady=12,padx=10)

    def destroy_me(self):
        self.destroy()

class ReportSuccess(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x125")
        self.title("Inventory Control System")


        self.label = customtkinter.CTkLabel(self, text="Report Generated Succesfuly")
        self.label.pack(padx=20, pady=20)

        button = customtkinter.CTkButton(self,text='Ok', command = self.destroy_me)
        button.pack(pady=12,padx=10)

    def destroy_me(self):
        self.destroy()