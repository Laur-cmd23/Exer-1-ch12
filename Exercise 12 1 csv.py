import csv
import os
from datetime import datetime

filename = "guest_book.csv"

# Create file with headers if it doesn't exist
try:
    with open(filename, "x", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Name"])
except FileExistsError:
    pass

while True:
    name = input("Enter your name (or 'quit' to exit): ")

    if name.lower() == "quit":
        print("Exiting guest book. Goodbye!")
        break

    # DATE only (no time)
    date_today = datetime.now().strftime("%Y-%m-%d")

    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date_today, name])

    print(f"Hello {name}, your visit has been recorded.\n")
