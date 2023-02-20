from tkinter import *
import datetime as dt
import pytz as tz
from timezone_calc import change_timezone_from_utc, change_timezone_to_utc, stringtoDate
PADDING = 30
FONT = ("Calibri", 24, "normal")
TIMEZONE_ID = {
    0:'Asia/Calcutta',
    1:'America/Vancouver',
    2:'Australia/Queensland', 
    3:'Japan',
    4:'GMT'
}
BG_COLOR = "#7489db"


class TimezoneFrame:
    def __init__(self, ui, window, text:str, timezone_id:str):
        self.window = ui.window
        self.ui = ui
        self.timezone_id = timezone_id
        self.timezone = tz.timezone(TIMEZONE_ID[timezone_id])
        self.update_image = PhotoImage(file="update.png")

        self.current_time_label = Label(self.window, text=text, bg=BG_COLOR)
        self.current_time_label.grid(row=timezone_id, column=0)
        self.current_time_entry = Entry(self.window, font=FONT, width=16)
        self.current_time_entry.grid(row=timezone_id, column=1, sticky='w',padx=(PADDING, PADDING))
        self.update_button = Button(self.window, image=self.update_image, command=lambda:self.update_times())
        self.update_button.grid(row=timezone_id, column=2)
    
    def update_times(self):
        new_date = stringtoDate(self.current_time_entry.get())
        self.ui.main_time = change_timezone_to_utc(new_date, self.timezone, self.ui.utc_timezone)
        self.ui.update_all_times()

class UserInterface:
    def __init__(self, window):
        self.utc_timezone = tz.timezone('UTC')
        self.main_time = dt.datetime.now(self.utc_timezone)
        self.window = window
        self.window.title("Timezone thing")
        self.window.config(padx=PADDING, pady=PADDING, bg=BG_COLOR)

        self.timezone_list = []
        self.timezone_list.append(TimezoneFrame(self, window, "Cyan (IST)", 0))
        self.timezone_list.append(TimezoneFrame(self, window, "Tin (PST)", 1))
        self.timezone_list.append(TimezoneFrame(self, window, "Ashwin (AEST)", 2))
        self.timezone_list.append(TimezoneFrame(self, window, "Potla (JST)", 3))
        self.timezone_list.append(TimezoneFrame(self, window, "Masala (GMT)", 4))

        donload_image = PhotoImage(file="donload.png")
        self.current_time_button = Button(self.window, image=donload_image, command=self.change_to_current_time)
        self.current_time_button.image = donload_image
        self.current_time_button.grid(row=5, column=0, columnspan=3)
        self.update_all_times()
    
    def update_all_times(self):
        for timezone_element in self.timezone_list:
            converted_time = change_timezone_from_utc(self.main_time, timezone_element.timezone)
            timezone_element.current_time_entry.delete(0, 'end')
            timezone_element.current_time_entry.insert(0, str(converted_time)[:16])
    
    def change_to_current_time(self):
        self.main_time = dt.datetime.now(self.utc_timezone)
        self.update_all_times()
    
        
window = Tk()
UserInterface(window)
window.mainloop()