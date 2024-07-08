import csv

csv_file = 'FoodTruckData.csv'
columns_to_read = ['Permit_Type', 'Permit_ID', 'NumberTrucks']
column_data = {col: [] for col in columns_to_read}

try:
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for col in columns_to_read:
                column_data[col].append(row[col])

    print(f'{"Permit_Type":<15} {"Permit_ID":<15} {"NumberTrucks":<15}')
    for i in range(len(column_data[columns_to_read[0]])):
        for col in columns_to_read:
            print(f'{column_data[col][i]:<15}', end=' ')
        print()

except FileNotFoundError:
    print(f'Error: The file "{csv_file}" was not found.')

except KeyError as e:
    print(f'Error: Column "{e}" not found in the CSV file.')

except Exception as e:
    print(f'Error: {e}')
