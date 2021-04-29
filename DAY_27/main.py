from tkinter import *


# Button Clicked Function

# def button_clicked():
#     my_label.config(text=my_entry.get())
#
#
# def upgrading():
#     my_entry.delete(0, END)
#     my_entry.insert(0, 'Upgrading')
def calculate():
    miles = int(miles_entry.get())
    kilometers = miles * 1.609
    kilometer_label.config(text=kilometers)

window = Tk()
window.title("First GUI Program")
window.config(padx=20, pady=20)



# Miles Label

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Miles Entry

miles_entry = Entry(width=7)
miles_entry.grid(column=1, row=0)

# Is Equal to Label

is_eq_label = Label(text="is equal to")
is_eq_label.grid(column=0, row=1)

#Calculated Kilometer Label

kilometer_label = Label(text='0')
kilometer_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Calculate Button

calculate_button = Button(text='Calculate', command=calculate)
calculate_button.grid(column=1, row=2)


window.mainloop()
