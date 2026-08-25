import customtkinter as ctk
import main


# -----------------------------
# FinSight appearance
# -----------------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# -----------------------------
# Login
# -----------------------------

def authentication():

    # Create the ONE main application window.
    # We will reuse this same window for the dashboard.
    app = ctk.CTk()

    app.title("FinSight Login")
    app.geometry("500x500")

    # Frame containing the login interface
    login_frame = ctk.CTkFrame(app)
    login_frame.pack(
        expand=True,
        padx=40,
        pady=40
    )

    # FinSight title
    title = ctk.CTkLabel(
        login_frame,
        text="FinSight",
        font=("Arial", 32, "bold")
    )
    title.pack(pady=(50, 10))

    # Subtitle
    subtitle = ctk.CTkLabel(
        login_frame,
        text="Your financial eyes for growth",
        font=("Arial", 16)
    )
    subtitle.pack(pady=(0, 35))

    # Name input
    name_entry = ctk.CTkEntry(
        login_frame,
        placeholder_text="Enter your name",
        width=280,
        height=40
    )
    name_entry.pack(pady=10)

    # Message for invalid input
    message = ctk.CTkLabel(
        login_frame,
        text="",
        font=("Arial", 14)
    )
    message.pack(pady=10)

    # This function runs when the user presses the button.
    def login():

        full_name = name_entry.get().strip()

        # Make sure the user entered something.
        if not full_name:
            message.configure(
                text="Please enter your name."
            )
            return

        # Get only the first name.
        first_name = full_name.split()[0]

        # Remove the login interface.
        login_frame.destroy()

        # Turn the same application window into the dashboard.
        main.open_dashboard(app, first_name)

    # Login button
    login_button = ctk.CTkButton(
        login_frame,
        text="Enter FinSight",
        command=login,
        width=200,
        height=40
    )
    login_button.pack(pady=20)

    # Keep the application running.
    app.mainloop()


# Only start the login screen when this file is run directly.
if __name__ == "__main__":
    authentication()