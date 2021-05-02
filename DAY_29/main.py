from tkinter import *
from tkinter import messagebox
import random
from pyperclip import copy

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pass_len = nr_letters + nr_symbols + nr_numbers
    password = ""
    password_letters = 0
    password_symbols = 0
    password_numbers = 0

    for i in range(0, pass_len):
        char = random.randint(0, 2)
        if char == 0 and password_letters <= nr_letters:
            password += letters[random.randint(0, 25)]
            password_letters += 1
        if char == 1 and password_symbols <= nr_symbols:
            password += symbols[random.randint(0, 8)]
            password_symbols += 1
        if char == 2 and password_numbers <= nr_numbers:
            password += numbers[random.randint(0, 9)]
            password_numbers += 1

    password_entry.insert(0, password)
    copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_to_file():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message="Please don't leave fields empty!")

    else:

        is_ok = messagebox.askokcancel(title=website,
                                       message=f'These are the details entered: \nEmail/Username: {username}\n'
                                               f'Password: {password}\nIs it okay to save?')
        if is_ok:
            with open('passwords.txt', mode='a') as data:
                data.write(f'{website} | {username} | {password}\n')
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

password_label = Label(text='Password:')

password_label.grid(column=0, row=3)

# Entries

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, 'trixterthe@gmail.com')

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons

generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save_to_file)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
