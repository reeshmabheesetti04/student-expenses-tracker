"""
Student Smart Expense Manager
Author: Bheesetti Reeshma
Description:
A Python-based application to track and analyze student expenses
using CSV file storage with category-wise summary and monthly budget alerts.
"""

import csv
import os
from datetime import date

FILE_NAME = "expenses.csv"
MONTHLY_BUDGET = 5000


def add_expense():
    """Function to add a new expense record."""

    expense_id = input("Enter Expense ID (unique number): ")

    # Date input (default: today)
    expense_date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if expense_date.strip() == "":
        expense_date = str(date.today())

    # Amount validation
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be positive. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    category = input("Enter category (Food/Hostel/College/Shopping): ")
    note = input("Enter note: ")

    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["ID", "Date", "Amount", "Category", "Note"])
        writer.writerow([expense_id, expense_date, amount, category, note])

    print("✅ Expense added successfully!\n")


def calculate_total():
    """Calculate total expenses from CSV file."""
    total = 0

    if not os.path.isfile(FILE_NAME):
        return total

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header

        for row in reader:
            if len(row) >= 3:
                try:
                    total += float(row[2])
                except ValueError:
                    continue

    return total


def view_expenses():
    """Display all expenses and category-wise summary."""

    total = 0
    category_totals = {"Food": 0, "Shopping": 0, "Hostel": 0, "College": 0}

    print("\n--- Expense Records ---")
    print("ID | Date | Amount | Category | Note")
    print("-" * 70)

    if not os.path.isfile(FILE_NAME):
        print("No expenses found.\n")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header

        for row in reader:
            if len(row) < 5:
                continue

            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")

            try:
                amount = float(row[2])
                total += amount
                if row[3] in category_totals:
                    category_totals[row[3]] += amount
            except ValueError:
                continue

    print("-" * 70)
    print(f"Total Expenses: {total}")

    print("\nCategory-wise Summary:")
    for cat, amt in category_totals.items():
        print(f"{cat}: {amt}")

    # Budget Alert
    if total > MONTHLY_BUDGET:
        print("\n⚠️ Alert: You have exceeded your monthly budget!")
    else:
        print("\n✅ You are within your monthly budget.")

    print("\n")


def main():
    """Main menu loop."""

    while True:
        print("\n=== Student Smart Expense Manager ===")
        print("1. Add Expense")
        print("2. View Expenses & Summary")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            confirm = input("Are you sure you want to exit? (yes/no): ")
            if confirm.lower() == "yes":
                print("Thank you for using Student Smart Expense Manager!")
                break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()