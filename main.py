import customtkinter as ctk


def open_dashboard(name):
    # Create the main FinSight window
    app = ctk.CTk()

    app.title("FinSight")
    app.geometry("1000x650")

    # Welcome message
    title = ctk.CTkLabel(
        app,
        text=f"Welcome to FinSight, {name}! 🚀",
        font=("Arial", 32, "bold")
    )
    title.pack(pady=(70, 10))

    # Subtitle
    subtitle = ctk.CTkLabel(
        app,
        text="Your financial eyes for growth.",
        font=("Arial", 18)
    )
    subtitle.pack(pady=(0, 50))

    # Dashboard container
    overview = ctk.CTkFrame(app)
    overview.pack(
        padx=40,
        pady=20,
        fill="x"
    )

    # Balance section
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

    # Income section
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

    # Expenses section
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

    # Temporary message
    coming_soon = ctk.CTkLabel(
        app,
        text="Your business dashboard starts here.",
        font=("Arial", 16)
    )
    coming_soon.pack(pady=40)

    # Keep the dashboard open
    app.mainloop()