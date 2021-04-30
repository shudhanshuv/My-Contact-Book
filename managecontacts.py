from tkinter import *
from tkinter.ttk import *

class ManageContactsFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.style = Style()

        self.style.configure('TFrame', background = 'white')

        self.pack(side = TOP, fill = BOTH, expand = TRUE)

        self.add_new_contact_frame = Frame(self)
        self.add_new_contact_frame.place(relx=.5,rely=.5,anchor=CENTER)

        self.name_label = Label(self.add_new_contact_frame, text = "Name:")
        self.name_label.grid(row = 0, column = 0)

        self.name_entry = Entry(self.add_new_contact_frame)
        self.name_entry.grid(row = 0, column = 1)

        self.phone_number_label = Label(self.add_new_contact_frame,
        text = "Phone Number:")
        self.phone_number_label.grid(row = 1, column = 0)

        self.phone_number_entry = Entry(self.add_new_contact_frame)
        self.phone_number_entry.grid(row = 1, column = 1)

        self.email_id_label = Label(self.add_new_contact_frame,
        text = "Email Id:")
        self.email_id_label.grid(row = 2, column = 0)

        self.email_id_entry = Entry(self.add_new_contact_frame)
        self.email_id_entry.grid(row = 2, column = 1)

        self.city_label = Label(self.add_new_contact_frame,
        text = "City: ")
        self.city_label.grid(row = 3, column = 0)

        self.city_combobox = Combobox(self.add_new_contact_frame,
        state='readonly',values=('Greater Noida','Noida','Delhi',
        'Mumbai', 'Banglore'))
        self.city_combobox.grid(row = 3, column = 1)

        self.add_button = Button(self.add_new_contact_frame,
        text = "Add")
        self.add_button.grid(row = 4, column = 1)


