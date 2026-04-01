Expense Tracker (Python CLI App)
Overview

This is a simple command-line Expense Tracker application written in Python. It allows users to record and view their daily expenses in an easy and organized way.

The program runs in a loop and provides a menu where users can:

Add a new expense
View all recorded expenses
Exit the application
Features
➕ Add new expenses with:
Amount
Category
Description
📋 View all saved expenses
🔁 Continuous menu system (runs until user exits)
🧠 Simple and beginner-friendly logic
🛠️ Technologies Used
Python (Core language)
No external libraries required
📂 Project Structure
expense_tracker.py
README.md
▶️ How It Works
1. Add Expense

The user inputs:

Amount (numeric value)
Category (e.g., Food, Transport, Bills)
Description (short explanation)

The expense is stored in a list as a dictionary:

{
  "amount": amount,
  "category": category,
  "description": description
}
2. View Expenses
Displays all saved expenses in a numbered list

If no expenses exist, it shows:

No expenses yet.
3. Menu System

The application runs in an infinite loop until the user chooses to quit:

===== Expense Tracker =====
1. Add Expense
2. View Expenses
3. Quit
▶️ How to Run
Step 1: Install Python

Make sure Python is installed on your system.

Step 2: Run the Program
python expense_tracker.py
📸 Example Usage
===== Expense Tracker =====
1. Add Expense
2. View Expenses
3. Quit

Choose option: 1
Enter amount: 500
Enter category: Food
Enter description: Lunch

Expense added!

👨‍💻 Author

Developed by Habumugisha Emmanuel

📄 License

This project is open-source and free to use for learning purposes.
