# ...existing code...
import os
import json
from datetime import datetime

# POS settings
# Had to create this variable because the printer has a character limit
LINE_WIDTH = 32  # Adjust to your printer width

# Catalog and stock
item_catalog = {
    "Maths Pry 3": 1500,
    "Biology Pry 2": 1700,
    "Notebook (60p)": 200,
    "Pen (Blue)": 100,
    "Ruler (30cm)": 150,
    "Calc. (Sci.)": 2500,
    "Pencil": 50
}

stock_file = "stock.json"

if os.path.exists(stock_file):
    with open(stock_file, "r") as f:
        item_stock = json.load(f)
else:
    item_stock = {
        "Maths Pry 3": 100,
        "Biology Pry 2": 100,
        "Notebook (60p)": 100,
        "Pen (Blue)": 100,
        "Ruler (30cm)": 100,
        "Calc. (Sci.)": 100,
        "Pencil": 100
    }

os.makedirs("receipts", exist_ok=True)

# Display items
print("=== ABC SUPREME GROUP OF SCHOOLS RECEIPT ===\nAvailable Items:")
for i, (item, price) in enumerate(item_catalog.items(), 1):
    print(f"{i}. {item} - N{price}")
print("\nEnter 'done' when you're finished.\n")

# Purchases
# Use a dict to aggregate quantities for the same item (prevent duplicates)
purchases = {}  # item_name -> {'price': unit_price, 'qty': total_qty}
item_names = list(item_catalog)
while True:
    choice = input("Enter item number or 'done': ").strip()
    if choice.lower() == 'done':
        break

    if not choice.isdigit() or not (1 <= int(choice) <= len(item_names)):
        print("Invalid choice.")
        continue

    item = item_names[int(choice)-1]
    quantity = input(f"Enter quantity for '{item}': ").strip()

    if not quantity.isdigit():
        print("Invalid quantity.")
        continue

    qty = int(quantity)

    if qty > item_stock[item]:
        print(f"Only {item_stock[item]} left.")
        continue

    # Deduct stock and aggregate purchase quantity
    item_stock[item] -= qty
    if item in purchases:
        purchases[item]['qty'] += qty
    else:
        purchases[item] = {'price': item_catalog[item], 'qty': qty}

if not purchases:
    print("No items selected. Exiting.")
    exit()

# Receipt
total = sum(data['price'] * data['qty'] for data in purchases.values())
lines = [
    "ABC SUPREME GROUP OF SCHOOLS".center(LINE_WIDTH),
    "SCHOOL BOOKSTORE".center(LINE_WIDTH),
    "-" * LINE_WIDTH,
    f"DATE: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
    "-" * LINE_WIDTH,
    f"{'ITEM':16}{'QTY':<4}{'UNIT':<7}{'TOTAL':<5}"
]

# Add purchased items (now aggregated, no duplicates)
for name, data in purchases.items():
    price = data['price']
    qty = data['qty']
    lines.append(f"{name:16}{qty:<4}N{price:<6}N{price*qty:<5}")

# Footer
lines += [
    "-" * LINE_WIDTH,
    f"{'TOTAL:':<25}N{total}",
    "-" * LINE_WIDTH,
    "Thank you for your purchase!".center(LINE_WIDTH)
]

receipt_text = "\n".join(lines)

# Save
filename = f"receipts/receipt_{datetime.now().strftime('%d%m%Y_%H%M%S')}.txt"
with open(filename, "w") as f:
    f.write(receipt_text)
with open(stock_file, "w") as f:
    json.dump(item_stock, f)

print(f"\n Receipt saved to {filename}")
print("\n=== RECEIPT ===\n" + receipt_text)
# ...existing code...