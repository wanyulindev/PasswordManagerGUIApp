from tkinter import *

# slelect the messagebox module, and right clicke to "GO TO" and select "Implementation"
# to check out how it's been written
# messagebox is not a class, it's a module, so it's not included in * under tkinter
from tkinter import messagebox

import random
import string

# import pyperclip to get rid of copy/paste hell work
import pyperclip

# FONT_NAME = "Arial"
# EGGSHELL = "#FCE6C9"
FONT_NAME= "Calibri"
FLORALWHITE = "#FFFAF0"
GAINSBORO = "#DCDCDC"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = "".join(random.choice(characters) for i in range(random.randint(6, 12)))
    # password_input.config(text=generated_password)
    # print(generated_password)

    password_input.delete(0, END)
    password_input.insert(0, generated_password)
    # simply using pyperclip function for copy/paste:
    pyperclip.copy(generated_password)




# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    # file = open("MyPass.txt", "w")

    # "a" - Append - will append to the end of the file
    # file = open("MyPass.txt", "a")
    # file.write(f"\n\n{website_input}\n{email_username_input}\n{password_input}")
    # file.close()

    # To fetch the current entry text, use the get method:
    # s = e.get()
    website_info= website_input.get()
    email_username_info= email_username_input.get()
    password_info = password_input.get()


    # (Have Validation): Show Warnings if user left some blanks

    # if not website_info or email_username_info or password_info:
    #     messagebox.showwarning(title="You left some blanks!",
    #                            message="Please filled up the blanks.")

    # Always check what's my variable type, and write correct codes with it!
    # ex: website_info is a str, so we are using len() here to validate the blanks:
    if len(website_info) == 0 or len(email_username_info) == 0 or len(password_info) == 0:
        messagebox.showwarning(title="You left some blanks!",
                               message="Please filled up the blanks.")

    else:
        # set as boolean to let user choose whether save data or not:
        # And see after messagebox.askokcancel, it returns as a bool!
        # That's why we can assign it as an "is_true"!
        is_true = messagebox.askokcancel(title="Almost done..",
                                         message="Please double check with all the info, and hit 'OK'! ")

        if is_true:
            # using with open method will automatically close the file without close()
            with open("MyPass.txt", "a") as file:
                file.write(f"\n\n{website_info}\n{email_username_info}\n{password_info}")

            website_input.delete(0, END)
            email_username_input.delete(0, END)
            email_username_input.insert(0, "mypass@gmail.com")
            password_input.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)
# canvas.pack()


website = Label(text="Website: ", font=(FONT_NAME, 16), fg=FLORALWHITE)
website.grid(column=0, row=1)
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
# put curser in the blank
website_input.focus()

email_username = Label(text="Email/Username: ", font=(FONT_NAME, 16), fg=FLORALWHITE)
email_username.grid(column=0, row=2)
email_username_input = Entry(width=35)
email_username_input.grid(column=1, row=2, columnspan=2)
# demo what to put / get rid of redundant work
email_username_input.insert(0, "mypass@gmail.com")

password = Label(text="Password: ", font=(FONT_NAME, 16), fg=FLORALWHITE)
password.grid(column=0, row=3)
password_input = Entry(width=18)
password_input.grid(column=1, row=3)


generate_password = Button(text="Generate Password", command=password_generator)
generate_password.grid(column=2, row=3)

add= Button(text="Add", width=32, command=save_password)
add.grid(column=1, row=4, columnspan=2)


window.mainloop()