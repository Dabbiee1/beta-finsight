import customtkinter as ctk


# -----------------------------
# Helper function
# -----------------------------

def center_window(window, width, height):

    # Ask the operating system for the screen dimensions.
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the x and y coordinates
    # needed to place the window in the center.
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Apply the calculated position and size.
    window.geometry(f"{width}x{height}+{x}+{y}")


# -----------------------------
# Dashboard
# -----------------------------

def open_dashboard(app, name):

    # ---------------------------------
    # Reconfigure the existing window
    # ---------------------------------

    app.title("FinSight")
    app.geometry("1000x650")

    # -----------------------------
    # Top-right user name
    # -----------------------------

    account_name = ctk.CTkLabel(
        app,
        text=f"{name} ▼",
        font=("Arial", 15, "bold")
    )

    account_name.place(
        relx=0.96,
        rely=0.04,
        anchor="ne"
    )

    # -----------------------------
    # Main heading
    # -----------------------------

    heading = ctk.CTkLabel(
        app,
        text="Your business starts right here.",
        font=("Arial", 32, "bold")
    )

    heading.pack(
        pady=(80, 45)
    )

    # -----------------------------
    # Dashboard overview
    # -----------------------------

    overview = ctk.CTkFrame(app)

    overview.pack(
        padx=40,
        pady=20,
        fill="x"
    )

    # Balance
    balance = ctk.CTkLabel(
        overview,
        text="Current Balance\n₦0.00",
        font=("Arial", 20, "bold")
    )

    balance.pack(
        side="left",
        expand=True,
        padx=20,
        pady=30
    )

    # Income
    income = ctk.CTkLabel(
        overview,
        text="Income\n₦0.00",
        font=("Arial", 20, "bold")
    )

    income.pack(
        side="left",
        expand=True,
        padx=20,
        pady=30
    )

    # Expenses
    expenses = ctk.CTkLabel(
        overview,
        text="Expenses\n₦0.00",
        font=("Arial", 20, "bold")
    )

    expenses.pack(
        side="left",
        expand=True,
        padx=20,
        pady=30
    )

    # -----------------------------
    # "What's next?"
    # -----------------------------

    next_text = ctk.CTkLabel(
        app,
        text="What's next?",
        font=("Arial", 18, "italic")
    )

    next_text.pack(
        side="bottom",
        pady=30
    )

    # -----------------------------
    # Welcome popup
    # -----------------------------

    welcome = ctk.CTkToplevel(app)

    welcome.title("FinSight")
    center_window(
        welcome,
        450,
        220
    )

    # Keep the popup associated with the dashboard.
    welcome.transient(app)

    # Put it above the dashboard.
    welcome.lift()

    # Welcome text
    welcome_title = ctk.CTkLabel(
        welcome,
        text=f"Welcome to FinSight, {name}! 🚀",
        font=("Arial", 24, "bold")
    )

    welcome_title.pack(
        pady=(55, 10)
    )

    # Subtitle
    welcome_subtitle = ctk.CTkLabel(
        welcome,
        text="Your financial eyes for growth",
        font=("Arial", 15)
    )

    welcome_subtitle.pack()

    # Hide the popup after 3.5 seconds.
    welcome.after(
        3500,
        welcome.withdraw
    )
