from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) ==0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any field empty.")
    else:
        is_ok = messagebox.askokcancel(title="website", message=f"These are the details entered: \nEmail:{email}\n"
                                                        f"Password: {password} \nIs it ok to save")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e", pady=5)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="e", pady=5)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e", pady=5)

# Entries
entry_width = 30  # Standard width for all entries
website_entry = Entry(width=entry_width)
website_entry.grid(row=1, column=1, pady=5, sticky="w", columnspan=1)
website_entry.focus()
email_entry = Entry(width=entry_width)
email_entry.grid(row=2, column=1, pady=5, sticky="w", columnspan=1)
email_entry.insert(0,"@gmail.com")
password_entry = Entry(width=entry_width - 0)
password_entry.grid(row=3, column=1, pady=5, sticky="w", columnspan=1)

# Buttons
button_width = 18  # Standard width for all buttons
generate_password_button = Button(text="Generate Password", width=button_width, command=generate_password)
generate_password_button.grid(row=3, column=2, pady=5, sticky="w")

add_button = Button(text="Add", width=button_width * 1, command=save)
add_button.grid(row=4, column=2, columnspan=2, pady=5)

























window.mainloop()