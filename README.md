# CLI Bookstore POS & Inventory Manager 📚

## Overview
A lightweight, terminal-based Point-of-Sale (POS) system developed for a school. This application handles bookstore transactions, generates formatted receipts, and manages inventory persistence using JSON.

## Key Features
* **Persistent Inventory:** Automatically loads and updates stock levels from a `stock.json` database, ensuring inventory data is saved between sessions.
* **Thermal Receipt Generation:** Produces `.txt` receipts formatted specifically for 32-column thermal printers, saved in a local `receipts/` directory with timestamps.
* **Input Validation:** Includes robust error handling to prevent invalid selections or overselling of stock (e.g., preventing sales if Quantity > Stock).

## How It Works
1.  **Initialization:** Checks for `stock.json`. If missing, it initializes a default stock list (e.g., Maths Pry 3, Notebooks).
2.  **Transaction Loop:** Displays a catalog, accepts item codes/quantities, and calculates totals.
3.  **Checkout:** * Deducts items from the JSON inventory file.
    * Generates a receipt with Date, School Name, and Itemized List.

## How to Run
1.  Ensure you have Python installed.
2.  Download `main.py`.
3.  Run the script in your terminal:
    ```bash
    python main.py
    ```
4.  Follow the on-screen prompts to select items by number.
