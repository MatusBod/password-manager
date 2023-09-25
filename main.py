from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    selected_letters = [random.choice(letters) for _ in range(nr_letters)]
    selected_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    selected_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = selected_letters + selected_symbols + selected_numbers

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_pass():
    website = website_entry.get()
    email = email_entry.get()
    passw = password_entry.get()
    if len(website) == 0 or len(passw) == 0 or len(email) == 0:
        messagebox.showerror(title="oops", message="Fields are not populated")
    else:
        is_ok = messagebox.askokcancel(title=website, message=(f"entered details:\nEmail: {email}\nPassword: {passw}"
                                                               f"Is it OK?"))
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {passw} \n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

Password_label = Label(text="Password:")
Password_label.grid(row=3, column=0)

website_entry = Entry(width=53)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.focus()

email_entry = Entry(width=53)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_entry.insert(0, "super.matus@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, sticky="w")

generate_button = Button(text="Generate password", command=generate_password)
generate_button.grid(row=3, column=2, sticky="w")

add_button = Button(text="add", width=45, command=save_pass)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()
