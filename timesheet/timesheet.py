import csv

def total_hours(csv_file):
    total = 0
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row['hours worked'])
    return total

if __name__ == "__main__":
    csv_file = 'path_to_your_csv_file.csv'  # Replace with your actual CSV file path
    print(f"Total hours worked: {total_hours(csv_file)}")