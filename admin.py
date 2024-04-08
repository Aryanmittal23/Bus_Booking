from tkinter import messagebox
from tkinter import *
import subprocess

def open_admin():
        subprocess.run(["python","admin_use.py"])
        root.destroy()


def check_login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()


        

    # Replace the following condition with your actual authentication logic
    if entered_username == "shivansh" and entered_password == "1234":
        messagebox.showinfo("Login Successful", "Welcome, " + entered_username + "!")
        open_admin()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
root = Tk()
root.title("Login Form")
root.geometry("300x300")
# Create and place the widgets in the window
Label(root, text="Username:").pack(pady=10)
username_entry = Entry(root)
username_entry.pack(pady=10)

Label(root, text="Password:").pack(pady=10)
password_entry = Entry(root, show="*")  # Use show="*" to hide the password
password_entry.pack(pady=10)

login_button = Button(root, text="Login", command=check_login)
login_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
