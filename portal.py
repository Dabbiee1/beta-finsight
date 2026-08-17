
def hello(to="Dabbie"):
    return f"Hello {to}!"

import customtkinter as ctk
def authentication():
    #configure appearance of window
       ctk.set_appearance_mode("dark")
       ctk.set_default_color_theme("blue")
       portal = ctk.CTk()
       portal.title("Finsight Login")
       portal.geometry("400x400")
    #text you'd find on it
       title = ctk.CTkLabel(
        portal,
        text="User Login",
        font=("Arial", 18, "bold")
            )
       title.pack(pady="40")
       subtitle = ctk.CTkLabel(
       portal,
       text="Enter your name to continue",
       font=("Arial", 16)
       )
       subtitle.pack(pady=10)

       name_entry = ctk.CTkEntry(
       portal,
       placeholder_text="Enter your name"
       )
       name_entry.pack(pady=10)
       def login():
             name = name_entry.get().strip().title()
             if name == "Dabbie":
                 portal.withdraw()
                 import main
             else:
                 subtitle.configure(text="Sorry, you're not Dabbie 😭")
       login_button = ctk.CTkButton(
             portal,
             text="Enter FinSight",
             command=login
              )
       login_button.pack(pady=20)
       portal.mainloop()

if "__main__" == __name__:
    authentication()

