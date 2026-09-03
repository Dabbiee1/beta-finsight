import customtkinter as ctk
import json
import os

transactions = []

DATA_FILE = "transactions.json"

def load_transactions():
    global transactions

    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                transactions = json.load(file)
        except (json.JSONDecodeError, OSError):
            transactions = []


def save_transactions():

    with open(DATA_FILE, "w") as file:
        json.dump(transactions, file, indent=4)

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

    # Load previously saved transactions.
    load_transactions()

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
    # Financial calculations
    # -----------------------------

    def update_financial_summary():

        total_income = sum(
            transaction["amount"]
            for transaction in transactions
            if transaction["type"] == "Income"
        )

        total_expenses = sum(
            transaction["amount"]
            for transaction in transactions
            if transaction["type"] == "Expense"
        )

        current_balance = total_income - total_expenses

        balance.configure(
            text=f"Current Balance\n₦{current_balance:,.2f}"
        )

        income.configure(
            text=f"Income\n₦{total_income:,.2f}"
        )

        expenses.configure(
            text=f"Expenses\n₦{total_expenses:,.2f}"
        )

    # -----------------------------
    # Recent Transactions
    # -----------------------------

    transaction_title = ctk.CTkLabel(
        app,
        text="Recent Transactions",
        font=("Arial", 20, "bold")
    )

    transaction_title.pack(
        pady=(5, 5)
    )

    transaction_frame = ctk.CTkScrollableFrame(
        app,
        width=850,
        height=100
    )

    transaction_frame.pack(
        padx=40,
        pady=5,
        fill="x"
    )

    # -----------------------------
    # Delete transaction
    # -----------------------------

    def delete_transaction(transaction):

        transactions.remove(transaction)

        save_transactions()

        update_transaction_list()
        update_financial_summary()

    def edit_transaction(transaction):

        edit_window = ctk.CTkToplevel(app)

        edit_window.title("Edit Transaction")
        edit_window.geometry("500x450")

        # Keep window above dashboard.
        edit_window.transient(app)
        edit_window.grab_set()
        edit_window.focus_force()

        # -----------------------------
        # Window title
        # -----------------------------

        title = ctk.CTkLabel(
            edit_window,
            text="Edit Transaction",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=20)

        # -----------------------------
        # Transaction name
        # -----------------------------

        transaction_name_entry = ctk.CTkEntry(
            edit_window,
            width=300
        )

        transaction_name_entry.pack(pady=10)

        transaction_name_entry.insert(
            0,
            transaction["name"]
        )

        # -----------------------------
        # Amount
        # -----------------------------

        amount_entry = ctk.CTkEntry(
            edit_window,
            width=300
        )

        amount_entry.pack(pady=10)

        amount_entry.insert(
            0,
            f"{transaction['amount']:,.2f}"
        )

        # -----------------------------
        # Transaction type
        # -----------------------------

        type_menu = ctk.CTkOptionMenu(
            edit_window,
            values=[
                "Income",
                "Expense"
            ],
            width=300
        )

        type_menu.pack(pady=10)

        type_menu.set(
            transaction["type"]
        )

        # -----------------------------
        # Status message
        # -----------------------------

        status_label = ctk.CTkLabel(
            edit_window,
            text=""
        )

        status_label.pack(pady=5)

        # -----------------------------
        # Save changes
        # -----------------------------

        def save_changes():

            transaction_name = (
                transaction_name_entry
                .get()
                .strip()
            )

            amount_text = (
                amount_entry
                .get()
                .strip()
            )

            transaction_type = type_menu.get()

            # Check empty fields.
            if not transaction_name or not amount_text:
                status_label.configure(
                    text="Please fill in all fields."
                )

                return

            # Check amount.
            try:

                amount = float(
                    amount_text.replace(",", "")
                )

            except ValueError:

                status_label.configure(
                    text="Please enter a valid amount."
                )

                return

            # Prevent zero/negative amounts.
            if amount <= 0:
                status_label.configure(
                    text="Amount must be greater than 0."
                )

                return

            # Update existing transaction.
            transaction["name"] = transaction_name
            transaction["amount"] = amount
            transaction["type"] = transaction_type

            #Save transaction
            save_transactions()

            # Refresh dashboard.
            update_transaction_list()
            update_financial_summary()

            # Close edit window.
            edit_window.destroy()

        # -----------------------------
        # Save button
        # -----------------------------

        save_button = ctk.CTkButton(
            edit_window,
            text="Save Changes",
            command=save_changes
        )

        save_button.pack(pady=20)

        # Automatically place cursor
        # in the transaction name field.
        transaction_name_entry.focus()

    # -----------------------------
    # Update transaction list
    # -----------------------------

    def update_transaction_list():

        # Remove old transaction widgets.
        for widget in transaction_frame.winfo_children():
            widget.destroy()

        # Show message if there are no transactions.
        if not transactions:
            ctk.CTkLabel(
                transaction_frame,
                text="No transactions recorded yet."
            ).pack(
                pady=10
            )

            return

        # Display every transaction.
        for transaction in transactions:
            transaction_row = ctk.CTkFrame(transaction_frame)
            transaction_row.pack(
                fill="x",
                padx=10,
                pady=3
            )

            transaction_text = (
                f"{transaction['type']}  |  "
                f"{transaction['name']}  |  "
                f"₦{transaction['amount']:,.2f}"
            )

            ctk.CTkLabel(
                transaction_row,
                text=transaction_text,
                font=("Arial", 14)
            ).pack(
                side="left",
                padx=10,
                pady=5
            )

            edit_button = ctk.CTkButton(
                transaction_row,
                text="Edit",
                width=80,
                command=lambda t=transaction: edit_transaction(t)
            )

            edit_button.pack(
                side="right",
                padx=5,
                pady=5
            )

            delete_button = ctk.CTkButton(
                transaction_row,
                text="Delete",
                width=80,
                command=lambda t=transaction: delete_transaction(t)
            )

            delete_button.pack(
                side="right",
                padx=10,
                pady=5
            )
    # -----------------------------
    # Record Transaction
    # -----------------------------

    def record_transaction():

        transaction_window = ctk.CTkToplevel(app)

        transaction_window.title(
            "Record Transaction"
        )

        transaction_window.geometry(
            "500x450"
        )

        # Keep window above dashboard.
        transaction_window.transient(app)
        transaction_window.grab_set()
        transaction_window.focus_force()

        # -----------------------------
        # Window title
        # -----------------------------

        title = ctk.CTkLabel(
            transaction_window,
            text="Record a Transaction",
            font=("Arial", 24, "bold")
        )

        title.pack(
            pady=20
        )

        # -----------------------------
        # Transaction name
        # -----------------------------

        transaction_name_entry = ctk.CTkEntry(
            transaction_window,
            placeholder_text="Transaction name",
            width=300
        )

        transaction_name_entry.pack(
            pady=10
        )

        # -----------------------------
        # Amount
        # -----------------------------

        amount_entry = ctk.CTkEntry(
            transaction_window,
            placeholder_text="Amount",
            width=300
        )

        amount_entry.pack(
            pady=10
        )

        # -----------------------------
        # Transaction type
        # -----------------------------

        type_menu = ctk.CTkOptionMenu(
            transaction_window,
            values=[
                "Income",
                "Expense"
            ],
            width=300
        )

        type_menu.pack(
            pady=10
        )

        # -----------------------------
        # Status message
        # -----------------------------

        status_label = ctk.CTkLabel(
            transaction_window,
            text=""
        )

        status_label.pack(
            pady=5
        )

        # -----------------------------
        # Save transaction
        # -----------------------------

        def save_transaction():

            transaction_name = (
                transaction_name_entry
                .get()
                .strip()
            )

            amount_text = (
                amount_entry
                .get()
                .strip()
            )

            transaction_type = type_menu.get()

            # Check empty fields.
            if not transaction_name or not amount_text:

                status_label.configure(
                    text="Please fill in all fields."
                )

                return

            # Check amount.
            try:

                amount = float(amount_text.replace(",", ""))

            except ValueError:

                status_label.configure(
                    text="Please enter a valid amount."
                )

                return

            # Prevent zero/negative amounts.
            if amount <= 0:

                status_label.configure(
                    text="Amount must be greater than 0."
                )

                return

            # Store transaction.
            transactions.append(
                {
                    "name": transaction_name,
                    "amount": amount,
                    "type": transaction_type
                }
            )

            # Save transaction to file.
            save_transactions()

            
            # Update dashboard.
            update_transaction_list()
            update_financial_summary()

            # Confirmation.
            status_label.configure(
                text="Transaction saved!"
            )

            # Clear fields.
            transaction_name_entry.delete(
                0,
                "end"
            )

            amount_entry.delete(
                0,
                "end"
            )

        # -----------------------------
        # Save button
        # -----------------------------

        save_button = ctk.CTkButton(
            transaction_window,
            text="Save Transaction",
            command=save_transaction
        )

        save_button.pack(
            pady=20
        )

        # Automatically place cursor
        # in the transaction name field.
        transaction_name_entry.focus()

    # -----------------------------
    # Record transaction button
    # -----------------------------

    record_button = ctk.CTkButton(
        app,
        text="Record a Transaction",
        command=record_transaction
    )

    record_button.pack(
        pady=10
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
        pady=20
    )

    # -----------------------------
    # Start dashboard with
    # current financial totals.
    # -----------------------------

    update_transaction_list()
    update_financial_summary()

    # -----------------------------
    # Welcome popup
    # -----------------------------

    welcome = ctk.CTkToplevel(app)

    welcome.title(
        "FinSight"
    )

    # Get dashboard position and size.
    app.update_idletasks()

    app_x = app.winfo_x()
    app_y = app.winfo_y()
    app_width = app.winfo_width()
    app_height = app.winfo_height()

    # Popup size.
    popup_width = 450
    popup_height = 220

    # Center popup over dashboard.
    x = app_x + (
        app_width - popup_width
    ) // 2

    y = app_y + (
        app_height - popup_height
    ) // 2

    # Set popup position.
    welcome.geometry(
        f"{popup_width}x{popup_height}+{x}+{y}"
    )

    # Keep popup associated with dashboard.
    welcome.transient(app)

    # Put popup above dashboard.
    welcome.lift()

    # -----------------------------
    # Welcome title
    # -----------------------------

    welcome_title = ctk.CTkLabel(
        welcome,
        text=f"Welcome to FinSight, {name}! 🚀",
        font=("Arial", 24, "bold")
    )

    welcome_title.pack(
        pady=(55, 10)
    )

    # -----------------------------
    # Welcome subtitle
    # -----------------------------

    welcome_subtitle = ctk.CTkLabel(
        welcome,
        text="Your financial eyes for growth",
        font=("Arial", 15)
    )

    welcome_subtitle.pack()

    # Hide popup after 2 seconds.
    welcome.after(
        2000,
        welcome.withdraw
    )