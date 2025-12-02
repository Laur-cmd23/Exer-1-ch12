import csv

filename = "guest_book.csv"

try:
    with open(filename, "r") as file:
        reader = csv.reader(file)
        
        # Skip header row
        next(reader)

        print("=== Guest Book Records ===")
        
        for row in reader:
            date, name = row
            print(f"Date: {date} | Name: {name}")

except FileNotFoundError:
    print("Error: guest_book.csv was not found. Run Programming Exercise 1 first.")
except Exception as e:
    print("An error occurred:", e)
