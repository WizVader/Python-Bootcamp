from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # Eazy Level - Order not randomised:
    # e.g. 4 letter, 2 symbol, 2 number = JduE&!91

    # Hard Level - Order of characters randomised:
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

    count_letters = 0
    count_symbols = 0
    count_numbers = 0

    password = ""

    while count_letters < nr_letters or count_numbers < nr_numbers or count_symbols < nr_symbols:
        if count_letters < nr_letters and count_numbers < nr_numbers and count_symbols < nr_symbols:
            choice = random.randint(0, 2)
            if choice == 0:
                random_generator = letters[random.randint(0, len(letters) - 1)]
                password += random_generator
                count_letters += 1
            elif choice == 1:
                random_generator = symbols[random.randint(0, len(symbols) - 1)]
                password += random_generator
                count_symbols += 1
            else:
                random_generator = numbers[random.randint(0, len(numbers) - 1)]
                password += random_generator
                count_numbers += 1
        elif count_letters < nr_letters and count_numbers < nr_numbers:
            choice = random.randint(0, 1)
            if choice == 0:
                random_generator = letters[random.randint(0, len(letters) - 1)]
                password += random_generator
                count_letters += 1
            elif choice == 1:
                random_generator = symbols[random.randint(0, len(symbols) - 1)]
                password += random_generator
                count_symbols += 1
        elif count_numbers < nr_numbers and count_symbols < nr_symbols:
            choice = random.randint(1, 2)
            if choice == 1:
                random_generator = symbols[random.randint(0, len(symbols) - 1)]
                password += random_generator
                count_symbols += 1
            else:
                random_generator = numbers[random.randint(0, len(numbers) - 1)]
                password += random_generator
                count_numbers += 1
        elif count_letters < nr_letters:
            random_generator = letters[random.randint(0, len(letters) - 1)]
            password += random_generator
            count_letters += 1
        elif count_symbols < nr_symbols:
            random_generator = symbols[random.randint(0, len(symbols) - 1)]
            password += random_generator
            count_symbols += 1
        else:
            random_generator = numbers[random.randint(0, len(numbers) - 1)]
            password += random_generator
            count_numbers += 1

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_username_label_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    is_ok = False

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Warning", message="Do not leave the fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered : \nEmail: {email}\nPassword: "
                                               f"{password}\nIs it okay to save?")

    if is_ok:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            data = new_data
        else:
            data.update(new_data)

        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message="Details not found.")

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img, anchor=CENTER)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=('Arial', 12))
website_label.grid(row=1, column=0)

website_entry = Entry(window, width=33)
website_entry.grid(row=1, column=1, columnspan=1, sticky="e")

website_search = Button(window, text="Search", width=14, command=find_password)
website_search.grid(row=1, column=2, sticky="w")

email_username_label = Label(text="Email/Username:", font=('Arial', 12))
email_username_label.grid(row=2, column=0)

email_username_label_entry = Entry(window, width=51)
email_username_label_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:", font=('Arial', 12))
password_label.grid(row=3, column=0)

password_entry = Entry(window, width=33)
password_entry.grid(row=3, column=1, sticky="e")

generate_password_button = Button(window, text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="w")

add_button = Button(text="Add", width=52, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
