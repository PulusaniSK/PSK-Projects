import json
import csv

def json_to_csv(json_file_path, csv_file_path):
    try:
        # Open and load the JSON file
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)

        # Open the CSV file for writing
        with open(csv_file_path, mode='w', newline='') as csv_file:
            # Create a CSV writer object
            csv_writer = csv.writer(csv_file)

            # Write the header
            if isinstance(data, list) and len(data) > 0:
                header = data[0].keys()
                csv_writer.writerow(header)

                # Write the data rows
                for row in data:
                    csv_writer.writerow(row.values())

        print(f"JSON data successfully written to {csv_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
json_file_path = 'input.json'  # The path to your JSON file
csv_file_path = 'output.csv'   # The path to your output CSV file
json_to_csv(json_file_path, csv_file_path)
