import customtkinter as ctk
from main import open_dashboard


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


app = ctk.CTk()

app.title("FinSight Login")
app.geometry("500x400")


# -----------------------------
# Login title
# -----------------------------

title = ctk.CTkLabel(
    app,
    text="Welcome to FinSight",
    font=("Arial", 28, "bold")
)

title.pack(pady=(60, 10))


subtitle = ctk.CTkLabel(
    app,
    text="Enter your name to continue"
)

subtitle.pack(pady=5)


# -----------------------------
# Name entry
# -----------------------------

name_entry = ctk.CTkEntry(
    app,
    placeholder_text="Your name",
    width=300
)

name_entry.pack(pady=20)


# -----------------------------
# Error message
# -----------------------------

message = ctk.CTkLabel(
    app,
    text=""
)

message.pack(pady=5)


# -----------------------------
# Login function
# -----------------------------

def login():
    name = name_entry.get().strip()

    if not name:
        message.configure(
            text="Please enter your name."
        )
        return

    # Hide login widgets
    for widget in app.winfo_children():
        widget.destroy()

    # Open dashboard
    open_dashboard(app, name)


# -----------------------------
# Login button
# -----------------------------

login_button = ctk.CTkButton(
    app,
    text="Continue",
    command=login
)

login_button.pack(pady=20)


app.mainloop()