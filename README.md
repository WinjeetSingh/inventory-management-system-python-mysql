# 📦 CLI Inventory Management System

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1.svg?logo=mysql&logoColor=white)
![Security](https://img.shields.io/badge/Security-Parameterized_Queries-brightgreen.svg)

## 📌 Project Overview
The **CLI Inventory Management System** is a lightweight, secure, command-line application designed to handle standard retail or warehouse inventory operations. Built with Python and backed by a MySQL database, it provides full CRUD (Create, Read, Update, Delete) functionality while enforcing secure database connectivity and data integrity.

This project demonstrates strong backend fundamentals, including interactive terminal user interfaces, database session management, and algorithmic filtering for stock alerts.

## ✨ Key Features
* **Full CRUD Capabilities:** Seamlessly add new products, view the entire inventory, update pricing/quantities, and remove discontinued items.
* **Low Stock Monitoring:** An automated filtering system that queries the database to instantly flag products with a stock quantity below a critical threshold (< 5 units).
* **Secure Database Connection:** Utilizes Python's `getpass` module to securely prompt for database credentials at runtime, ensuring sensitive passwords are not hardcoded into the source code.
* **SQL Injection Prevention:** Implements parameterized queries (`%s`) via `mysql.connector` to sanitize all user inputs and protect the database against malicious injection attacks.
* **Graceful Error Handling:** Wraps database connections and queries in `try-except` blocks to prevent unexpected application crashes and provide readable error logs.

## 🗄️ Database Schema
The system operates on the `inventory_db` database, utilizing a highly normalized `products` table.

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `product_id` | INT | PRIMARY KEY, AUTO_INCREMENT | Unique identifier for each product |
| `name` | VARCHAR(100) | NOT NULL | The descriptive name of the item |
| `price` | DECIMAL(10,2) | NOT NULL | The monetary value of the item |
| `quantity` | INT | NOT NULL | Current stock level |

## 💻 Tech Stack
* **Language:** Python 3.x
* **Database:** MySQL
* **Libraries:** `mysql-connector-python`, `getpass`

## 🚀 Installation & Setup Guide

### 1. Database Configuration
Ensure you have MySQL installed and running on your local machine.
1. Open your MySQL command line or workbench.
2. Execute the provided SQL script to initialize the database:
   ```bash
   source combine1&2_Database_file.sql;
