import customtkinter as ctk
import json
import os

transactions = []

DATA_FILE = "transactions.json"

products = []

PRODUCTS_FILE = "products.json"

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

def load_products():
    global products

    if os.path.exists(PRODUCTS_FILE):
        with open(PRODUCTS_FILE, "r") as file:
            products = json.load(file)

def save_products():
    with open(PRODUCTS_FILE, "w") as file:
        json.dump(products, file, indent=4)

def add_product(name, quantity, cost, selling_price, reorder_level):
    product = {
        "name": name,
        "quantity": quantity,
        "cost": cost,
        "selling_price": selling_price,
        "reorder_level": reorder_level
    }

    products.append(product)
    save_products()

def record_stock(name, quantity, cost, selling_price, reorder_level):
    for product in products:
        if product["name"].lower() == name.lower():
            product["quantity"] += quantity
            product["cost"] = cost
            product["selling_price"] = selling_price
            product["reorder_level"] = reorder_level
            save_products()
            return

    add_product(
        name,
        quantity,
        cost,
        selling_price,
        reorder_level
    )

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
    load_products()
    # ---------------------------------
    # Reconfigure the existing window
    # ---------------------------------

    app.title("FinSight")
    app.geometry("1000x650")

    # ---------------------------------
    # Scrollable dashboard content
    # ---------------------------------

    dashboard_frame = ctk.CTkScrollableFrame(
        app,
        width=900,
        height=560
    )

    dashboard_frame.pack(
        padx=20,
        pady=(70, 10),
        fill="both",
        expand=True
    )
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
        dashboard_frame,
        text="Your business starts right here.",
        font=("Arial", 32, "bold")
    )

    heading.pack(
        pady=(80, 45)
    )

    # -----------------------------
    # Dashboard overview
    # -----------------------------

    overview = ctk.CTkFrame(dashboard_frame)

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
    # Current Stock
    # -----------------------------

    stock_title = ctk.CTkLabel(
        dashboard_frame,
        text="Current Stock",
        font=("Arial", 20, "bold")
    )

    stock_title.pack(
        pady=(25, 10)
    )

    stock_frame = ctk.CTkFrame(
        dashboard_frame,
        width=850
    )

    stock_frame.pack(
        padx=20,
        pady=(0, 15),
        fill="x"
    )

    # -----------------------------
    # Recent Transactions
    # -----------------------------

    transaction_title = ctk.CTkLabel(
        dashboard_frame,
        text="Recent Transactions",
        font=("Arial", 20, "bold")
    )

    transaction_title.pack(
        pady=(25, 10)
    )

    transaction_frame = ctk.CTkFrame(
        dashboard_frame,
        width=850,
    )

    transaction_frame.pack(
        padx=20,
        pady=(0, 15),
        fill="x"
    )

    # -----------------------------
    # Insights
    # -----------------------------

    insight_title = ctk.CTkLabel(
        dashboard_frame,
        text="Insights",
        font=("Arial", 20, "bold")
    )

    insight_title.pack(
        pady=(25, 10)
    )

    insight_frame = ctk.CTkFrame(
        dashboard_frame,
        width=850
    )

    insight_frame.pack(
        padx=20,
        pady=(0, 20),
        fill="x"
    )
    # -----------------------------
    # Update stock list
    # -----------------------------

    def update_stock_list():

        # Remove old stock widgets.
        for widget in stock_frame.winfo_children():
            widget.destroy()

        # Show message if there is no stock.
        if not products:
            ctk.CTkLabel(
                stock_frame,
                text="No stock recorded yet."
            ).pack(
                pady=10
            )

            return

        # Display every product.
        for product in products:

            product_row = ctk.CTkFrame(
                stock_frame,
                corner_radius=10
            )

            product_row.pack(
                fill="x",
                padx=10,
                pady=5
            )

            product_name = ctk.CTkLabel(
                product_row,
                text=product["name"],
                font=("Arial", 14, "bold"),
                anchor="w"
            )

            product_name.pack(
                side="left",
                padx=15,
                pady=10
            )

            quantity_label = ctk.CTkLabel(
                product_row,
                text=f"Quantity: {product['quantity']}",
                font=("Arial", 13)
            )

            quantity_label.pack(
                side="left",
                padx=15
            )

            price_label = ctk.CTkLabel(
                product_row,
                text=f"Selling: ₦{product['selling_price']:,.2f}",
                font=("Arial", 13)
            )

            price_label.pack(
                side="right",
                padx=15
            )

    # -----------------------------
    # Delete transaction
    # -----------------------------

    def delete_transaction(transaction):

        transactions.remove(transaction)

        save_transactions()

        update_transaction_list()
        update_financial_summary()
        update_insights()

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
            update_insights()

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
            transaction_row = ctk.CTkFrame(
                transaction_frame,
                corner_radius=10
            )

            transaction_row.pack(
                fill="x",
                padx=10,
                pady=5
            )

            transaction_text = (
                f"{transaction['type']}\n"
                f"{transaction['name']}"
            )

            ctk.CTkLabel(
                transaction_row,
                text=transaction_text,
                font=("Arial", 14, "bold"),
                anchor="w"
            ).pack(
                side="left",
                padx=15,
                pady=10
            )

            ctk.CTkLabel(
                transaction_row,
                text=f"₦{transaction['amount']:,.2f}",
                font=("Arial", 14, "bold")
            ).pack(
                side="right",
                padx=15,
                pady=10
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
    # Insights
    # -----------------------------

    def update_insights():

        # Remove old insight widgets
        for widget in insight_frame.winfo_children():
            widget.destroy()

        if not transactions:
            empty_label = ctk.CTkLabel(
                insight_frame,
                text="Record some transactions to see your financial insights.",
                font=("Arial", 14)
            )
            empty_label.pack(pady=15)
            return

        total_income = sum(
            t["amount"] for t in transactions
            if t["type"] == "Income"
        )

        total_expenses = sum(
            t["amount"] for t in transactions
            if t["type"] == "Expense"
        )

        balance = total_income - total_expenses

        # Biggest expense
        expenses = [
            t for t in transactions
            if t["type"] == "Expense"
        ]

        biggest_expense = max(
            expenses,
            key=lambda t: t["amount"]
        ) if expenses else None

        # Financial message
        if balance > 0:
            health_message = "You're currently spending less than you're earning."
        elif balance < 0:
            health_message = "Your expenses currently exceed your income."
        else:
            health_message = "Your income and expenses are currently balanced."

        # Financial health
        health_label = ctk.CTkLabel(
            insight_frame,
            text=f"Financial Health\n{health_message}",
            font=("Arial", 15, "bold"),
            wraplength=750
        )
        health_label.pack(pady=(10, 15))

        # Biggest expense
        if biggest_expense:
            biggest_label = ctk.CTkLabel(
                insight_frame,
                text=(
                    f"Biggest Expense\n"
                    f"{biggest_expense['name']} — "
                    f"₦{biggest_expense['amount']:,.2f}"
                ),
                font=("Arial", 14)
            )
            biggest_label.pack(pady=(5, 15))
        # Spending Breakdown
        expense_totals = {}

        for transaction in expenses:
            name = transaction["name"]
            expense_totals[name] = expense_totals.get(name, 0) + transaction["amount"]

        breakdown_title = ctk.CTkLabel(
            insight_frame,
            text="Spending Breakdown",
            font=("Arial", 15, "bold")
        )
        breakdown_title.pack(pady=(12, 8))

        if expense_totals:
            largest_amount = max(expense_totals.values())

            for name, amount in sorted(
                    expense_totals.items(),
                    key=lambda item: item[1],
                    reverse=True
            ):
                row = ctk.CTkFrame(
                    insight_frame,
                    fg_color="transparent"
                )
                row.pack(fill="x", padx=40, pady=4)

                name_label = ctk.CTkLabel(
                    row,
                    text=name,
                    font=("Arial", 13),
                    width=140,
                    anchor="w"
                )
                name_label.pack(side="left")

                bar = ctk.CTkProgressBar(
                    row,
                    width=400
                )
                bar.pack(side="left", padx=10)

                # Show the amount relative to the largest expense
                bar.set(amount / largest_amount)

                amount_label = ctk.CTkLabel(
                    row,
                    text=f"₦{amount:,.2f}",
                    font=("Arial", 13),
                    width=130,
                    anchor="e"
                )
                amount_label.pack(side="right")

        # Remaining balance
        balance_label = ctk.CTkLabel(
            insight_frame,
            text=f"Money Remaining\n₦{balance:,.2f}",
            font=("Arial", 14)
        )
        balance_label.pack(pady=(15, 20))
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
            update_insights()

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
    # Record Stock
    # -----------------------------

    def record_stock_window():

        stock_window = ctk.CTkToplevel(app)

        stock_window.title("Record Stock")
        stock_window.geometry("500x550")

        stock_window.transient(app)
        stock_window.grab_set()
        stock_window.focus_force()

        # -----------------------------
        # Window title
        # -----------------------------

        title = ctk.CTkLabel(
            stock_window,
            text="Record Stock",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=20)

        # -----------------------------
        # Product name
        # -----------------------------

        name_entry = ctk.CTkEntry(
            stock_window,
            placeholder_text="Product name",
            width=300
        )

        name_entry.pack(pady=10)

        # -----------------------------
        # Quantity
        # -----------------------------

        quantity_entry = ctk.CTkEntry(
            stock_window,
            placeholder_text="Quantity received",
            width=300
        )

        quantity_entry.pack(pady=10)

        # -----------------------------
        # Cost per unit
        # -----------------------------

        cost_entry = ctk.CTkEntry(
            stock_window,
            placeholder_text="Cost per unit",
            width=300
        )

        cost_entry.pack(pady=10)

        # -----------------------------
        # Selling price
        # -----------------------------

        selling_price_entry = ctk.CTkEntry(
            stock_window,
            placeholder_text="Selling price per unit",
            width=300
        )

        selling_price_entry.pack(pady=10)

        # -----------------------------
        # Reorder level
        # -----------------------------

        reorder_entry = ctk.CTkEntry(
            stock_window,
            placeholder_text="Reorder level",
            width=300
        )

        reorder_entry.pack(pady=10)

        # -----------------------------
        # Status
        # -----------------------------

        status_label = ctk.CTkLabel(
            stock_window,
            text=""
        )

        status_label.pack(pady=5)

        # -----------------------------
        # Save stock
        # -----------------------------

        def save_stock():

            name = name_entry.get().strip()
            quantity_text = quantity_entry.get().strip()
            cost_text = cost_entry.get().strip()
            selling_price_text = selling_price_entry.get().strip()
            reorder_text = reorder_entry.get().strip()

            if not name or not quantity_text or not cost_text or not selling_price_text or not reorder_text:
                status_label.configure(
                    text="Please fill in all fields."
                )
                return

            try:
                quantity = int(quantity_text)
                cost = float(cost_text.replace(",", ""))
                selling_price = float(selling_price_text.replace(",", ""))
                reorder_level = int(reorder_text)

            except ValueError:
                status_label.configure(
                    text="Please enter valid numbers."
                )
                return

            if quantity <= 0:
                status_label.configure(
                    text="Quantity must be greater than 0."
                )
                return

            if cost < 0 or selling_price < 0:
                status_label.configure(
                    text="Prices cannot be negative."
                )
                return

            if reorder_level < 0:
                status_label.configure(
                    text="Reorder level cannot be negative."
                )
                return

            record_stock(
                name,
                quantity,
                cost,
                selling_price,
                reorder_level
            )

            update_stock_list()

            status_label.configure(
                text="Stock recorded!"
            )

            name_entry.delete(0, "end")
            quantity_entry.delete(0, "end")
            cost_entry.delete(0, "end")
            selling_price_entry.delete(0, "end")
            reorder_entry.delete(0, "end")

            name_entry.focus()

        # -----------------------------
        # Save button
        # -----------------------------

        save_button = ctk.CTkButton(
            stock_window,
            text="Record Stock",
            command=save_stock
        )

        save_button.pack(pady=20)

        name_entry.focus()

    # -----------------------------
    # Record transaction button
    # -----------------------------

    record_button = ctk.CTkButton(
        dashboard_frame,
        text="Record a Transaction",
        command=lambda: record_transaction
    )

    record_button.pack(
        pady=10
    )

    stock_button = ctk.CTkButton(
        dashboard_frame,
        text="Record Stock",
        command=record_stock_window
    )

    stock_button.pack(pady=10)

    # -----------------------------
    # "What's next?"
    # -----------------------------

    next_text = ctk.CTkLabel(
        dashboard_frame,
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
    update_stock_list()
    update_transaction_list()
    update_financial_summary()
    update_insights()

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