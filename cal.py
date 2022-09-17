import customtkinter

import datetime
from tkcalendar import *

customtkinter.set_appearance_mode("Dark")

mydate = datetime.datetime.now()
mydate.strftime("%B")

class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("My Calendar")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_right = customtkinter.CTkFrame(master=self)

        md = str(mydate)
        y = int(md[0:4])
        m = int(md[5:7])
        d = int(md[8:10])

        self.frame_right = Calendar(self, selectmode="day",year = y, month = m, day = d)

        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

    def on_closing(self, event=0):
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
