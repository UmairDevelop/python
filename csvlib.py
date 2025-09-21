from pathlib import Path
import csv, os

row = [
    ["Name", "Age", "City"],
    ["Umair", 25, "Lahore"],
    ["Ali", 30, "Karachi"],
    ["Ayesha", 28, "Islamabad"]
]

# Ensure the directory exists before changing into it
# Write CSV data to a file
if os.path.exists('csv_folder'):
    os.chdir("csv_folder")
    with open('people.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(row)
else:
    (Path.cwd()/"csv_folder").mkdir(exist_ok=True)
    os.chdir("csv_folder")
    with open('people.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(row)

# Read CSV data from a file
with open('people.csv', 'r') as f:
    reader = csv.reader(f)
    for r in reader:
        print(r)

# Using DictWriter and DictReader
with open('people_dict.csv', 'w', newline='') as f:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Name": "Umair", "Age": 25, "City": "Lahore"})
    writer.writerow({"Name": "Ali", "Age": 29, "City": "Islamabad"})
    writer.writerow({"Name": "Areeba", "Age": 22, "City": "Lahore"})

with open('people_dict.csv', 'r') as f:
    reader = csv.DictReader(f)
    for r in reader:
        print(r["Name"], r["City"])