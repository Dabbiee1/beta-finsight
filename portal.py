import customtkinter as ctk
import main


# Configure the appearance of FinSight
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def authentication():
    # Create the login window
    portal = ctk.CTk()

    portal.title("FinSight Login")
    portal.geometry("500x500")

    # FinSight title
    title = ctk.CTkLabel(
        portal,
        text="FinSight",
        font=("Arial", 32, "bold")
    )
    title.pack(pady=(70, 10))

    # Subtitle
    subtitle = ctk.CTkLabel(
        portal,
        text="Your financial eyes for growth",
        font=("Arial", 16)
    )
    subtitle.pack(pady=(0, 40))

    # Name input
    name_entry = ctk.CTkEntry(
        portal,
        placeholder_text="Enter your name",
        width=280,
        height=40
    )
    name_entry.pack(pady=10)

    # Error / information message
    message = ctk.CTkLabel(
        portal,
        text="",
        font=("Arial", 14)
    )
    message.pack(pady=10)

    # What happens when the button is clicked
    def login():
        name = name_entry.get().strip()

        if name:
            portal.destroy()
            main.open_dashboard(name)
        else:
            message.configure(text="Please enter your name.")

    # Login button
    login_button = ctk.CTkButton(
        portal,
        text="Enter FinSight",
        command=login,
        width=200,
        height=40
    )
    login_button.pack(pady=20)

    # Keep the login window open
    portal.mainloop()


# Start the login screen
if __name__ == "__main__":
    authentication()