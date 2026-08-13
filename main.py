import customtkinter as ctk
def hello(to):
    print(f"Hello {to}!")
hello()
name = input("What's your name? ").strip().title()
hello(name)

def authentication():
       ctk.set_appearance_mode("dark")
       ctk.set_default_color_theme("grey")
       window = ctk.CTk()
       window.title("User Login")
       window.geometry("400x400")
       title = ctk.CTkLabel()

# Configure appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Create the window
app = ctk.CTk()

app.title("FinSight")
app.geometry("1000x650")

# Welcome text
title = ctk.CTkLabel(
    app,
    text="Welcome to FinSight 🚀",
    font=("Arial", 32, "bold")
)

title.pack(pady=60)

subtitle = ctk.CTkLabel(
    app,
    text="Smart Financial Management for Small Businesses",
    font=("Arial", 18)
)

subtitle.pack(pady=(10, 40)  )


byline = ctk.CTkLabel(
    app,
    text="...your financial eyes for growth",
    font=("Arial", 14, "italic")
)
byline.pack()
# Start the application

app.mainloop()