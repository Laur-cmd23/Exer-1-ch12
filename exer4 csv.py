import csv

# Read the CSV file created in Exercise 3
with open('countries.csv', 'r', encoding='UTF8') as f:
    reader = csv.DictReader(f)

    print("List of Countries:\n")

    for row in reader:
        print(f"Name: {row['name']}")
        print(f"Area: {row['area']} sq. km")
        print(f"Country Code 2: {row['country_code2']}")
        print(f"Country Code 3: {row['country_code3']}")
        print("-" * 30)
