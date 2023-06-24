import csv

# Read the input CSV file
with open('/home/mint/Desktop/1.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)

# Read the additional data CSV file
with open('/home/mint/Desktop/2.csv', 'r') as file:
    reader = csv.reader(file)
    additional_data = list(reader)

# Extract column names and corresponding values from additional data
additional_columns = {}
for data_row in additional_data:
    column_name = data_row[0]
    column_values = data_row[1:]
    additional_columns[column_name] = column_values

# Add the title row from the second file to the first file
headers_additional = additional_data[0]
headers = rows[0] + headers_additional[1:]
updated_rows = [headers]

# Add the data rows from the first file
for row in rows:
    time = row[4]
    year = time[:4]  # Extract the year from the time value

    if year in additional_columns:
        column_values = additional_columns[year]
        updated_row = row + column_values[1:]
    else:
        updated_row = row + [''] * (len(headers_additional) - 1)
    
    updated_rows.append(updated_row)

# Combine the headers and updated rows
updated_rows = updated_rows[:1] + updated_rows[1:]

# Write the updated data to a new CSV file
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(updated_rows)

print("CSV file updated successfully.")





