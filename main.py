import tkinter as tk

def authetication():
    a = "Access granted"
    b = "Access denied"
    ogpassword = ("admin")
    password_entered = input("Enter your password: ")
    if password_entered == ogpassword:
        print(a)
    else:
        print(b)
authetication()

GUI = tk.Tk()
GUI.resizable(width=False, height=False)
GUI.geometry("500x500")
GUI.configure(bg="#FBEAEB")
GUIFRAME = tk.Frame(master=GUI)
GUIFRAME.pack()
GUI.configure(background="whitehs")
GUItitle= tk.Label(GUI, text = "Welcome to my page")
GUItitle.pack()
GUI.mainloop()