import csv
import random
from datetime import datetime, timedelta


def generate_data(start_date, end_date):
    data = []
    current_date = start_date
    while current_date <= end_date:
        data.append(("Lake", current_date.strftime("%Y-%m-%d %H:%M:%S"),
                     round(random.randint(1, 9)+random.random(), 10), "2020-10-05"))
        current_date += timedelta(hours=1)
    return data


# Generate the data for the fifth file
data = generate_data(datetime(2001, 1, 1), datetime(2020, 10, 1))
# Write the data to the fifth file
with open("Lake_20201005.txt", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Application", "date", "amount", "load_date"])
    for row in data:
        writer.writerow(row)

# Generate the data for the fourth file
data = generate_data(datetime(2002, 1, 1), datetime(2020, 10, 1))
with open("Lake_20201004.txt", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Application", "date", "amount", "load_date"])
    for row in data:
        writer.writerow(row)

# Generate the data for the third file
data = generate_data(datetime(2003, 1, 1), datetime(2020, 10, 1))
with open("Lake_20201003.txt", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Application", "date", "amount", "load_date"])
    for row in data:
        writer.writerow(row)

# Generate the data for the second file
data = generate_data(datetime(2004, 1, 1), datetime(2020, 10, 1))
with open("Lake_20201002.txt", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Application", "date", "amount", "load_date"])
    for row in data:
        writer.writerow(row)

# Generate the data for the first file
data = generate_data(datetime(2005, 1, 1), datetime(2020, 10, 1))
with open("Lake_20201001.txt", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Application", "date", "amount", "load_date"])
    for row in data:
        writer.writerow(row)
