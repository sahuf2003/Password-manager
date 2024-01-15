from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
def get_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list+=[random.choice(symbols) for char in range(nr_symbols)]
    password_list+=[random.choice(numbers) for char in range(nr_numbers)]


    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
    pyperclip.copy(password)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=20,pady=20)

canvas = Canvas(height=200,width=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=image)
canvas.grid(row=0,column=1)

def add():
    username = email_entry.get()
    website = web_entry.get()
    password = pass_entry.get()
    if len(username) == 0 or len(password) == 0:
        messagebox.askokcancel(title="error",message="it is empty")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered \n website:{website}"
                                                 f" \nUsername :{username}\n password:{password}")
        if is_ok:
            with open("password_manager.txt",'a') as file:
                file.write(f"webiste: {website}|| Username:{username}|| Password:{password}\n")
            web_entry.delete(0,END)
            pass_entry.delete(0,END)
#labels
website_label=Label(text="Website")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2,column=0)
pass_label= Label(text="Password:")
pass_label.grid(row=3,column=0)

#Entries
web_entry = Entry(width=35)
web_entry.focus()
web_entry.grid(row=1,column=1,columnspan=2)
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
pass_entry = Entry(width=21)
pass_entry.grid(row=3,column=1)

#Buttons

gen_pass_label = Button(text="Generate Password",command=get_password)
gen_pass_label.grid(row=3,column=2)
add_button = Button(text="Add",width=36,command=add)
add_button.grid(row=4,column=1,columnspan=2)

#Buttons

window.mainloop()
