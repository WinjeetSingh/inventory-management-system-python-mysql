"""
Inventory Management System
Author: Winjeet Singh

Description:
This script provides a command-line interface for managing a MySQL-backed 
inventory database. It allows users to add, view, update, and delete products, 
as well as check for low-stock alerts.
"""

import mysql.connector
from mysql.connector import Error
import getpass # Allows secure password input

def connect_to_database():
    """
    Establishes a connection to the MySQL database.
    Prompts the user for a password to avoid hardcoding credentials.
    """
    try:
        # Prompt for password securely in the terminal
        db_password = getpass.getpass(prompt="Enter MySQL 'root' password to connect: ")
        
        db = mysql.connector.connect(
            host="localhost",
            user="root",      
            password=db_password,  
            database="inventory_db"
        )
        if db.is_connected():
            print("\n Successfully connected to the inventory database.")
            return db
    except Error as e:
        print(f" Error connecting to MySQL: {e}")
        return None

# ---------------- CORE FUNCTIONS ----------------

def add_product(db, cursor):
    """Prompts user for product details and inserts a new record into the database."""
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    qty = int(input("Enter quantity: "))

    # Using parameterized queries (%s) to prevent SQL injection attacks
    sql = "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)"
    values = (name, price, qty)
    
    try:
        cursor.execute(sql, values)
        db.commit()
        print(" Product added successfully!")
    except Error as e:
        print(f" Failed to add product: {e}")

def view_products(cursor):
    """Retrieves and formats all products currently in the inventory."""
    cursor.execute("SELECT * FROM products")
    records = cursor.fetchall()

    print("\nID | Name | Price | Quantity")
    print("-" * 40)
    for row in records:
        print(row)

def update_product(db, cursor):
    """Updates the price and quantity of an existing product based on its ID."""
    pid = int(input("Enter product ID to update: "))
    price = float(input("Enter new price: "))
    qty = int(input("Enter new quantity: "))

    sql = "UPDATE products SET price=%s, quantity=%s WHERE product_id=%s"
    values = (price, qty, pid)
    
    cursor.execute(sql, values)
    db.commit()
    print(" Product updated!")

def delete_product(db, cursor):
    """Removes a product completely from the database using its ID."""
    pid = int(input("Enter product ID to delete: "))
    cursor.execute("DELETE FROM products WHERE product_id=%s", (pid,))
    db.commit()
    print(" Product deleted!")

def low_stock(cursor):
    """Filters and displays products that have a stock quantity below 5."""
    cursor.execute("SELECT * FROM products WHERE quantity < 5")
    records = cursor.fetchall()

    print("\n LOW STOCK PRODUCTS ")
    print("-" * 40)
    if not records:
        print("All products are sufficiently stocked.")
    else:
        for row in records:
            print(row)

# ---------------- MAIN MENU ----------------

def main():
    """Main execution loop for the terminal interface."""
    db = connect_to_database()
    
    # If connection fails, exit the script safely
    if db is None:
        return
        
    cursor = db.cursor()

    while True:
        print("\n===== INVENTORY MANAGEMENT =====")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Low Stock Alert")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            add_product(db, cursor)
        elif choice == "2":
            view_products(cursor)
        elif choice == "3":
            update_product(db, cursor)
        elif choice == "4":
            delete_product(db, cursor)
        elif choice == "5":
            low_stock(cursor)
        elif choice == "6":
            print("Exiting system. Have a great day!")
            break
        else:
            print(" Invalid choice! Please select a number between 1 and 6.")

    # Always close the connection when the program finishes
    cursor.close()
    db.close()

# This ensures the menu only runs if the script is executed directly
if __name__ == "__main__":
    main()