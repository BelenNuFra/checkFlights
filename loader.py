import csv 

def save_csv(transformed_data):

    # Defining the CSV file name
    file_name = "test.csv"

    # Specifying the field names for the Python CSV header
    fields = ['flight_date', 'flight_status', 'dep_airport', 'dep_timezone', 'dep_iata', 'dep_terminal', 'dep_gate', 'dep_scheduled', 'dep_estimated', 'dep_actual', 'dep_delay', 'arr_airport', 'arr_timezone', 'arr_iata', 'arr_terminal', 'arr_gate', 'arr_scheduled', 'arr_estimated', 'arr_actual', 'arr_delay', 'airline_name', 'airline_iata', 'flight_number', 'flight_iata']


    # Writing the Python dictionary to a CSV file
    try:
            with open(file_name, mode='w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                
                # Write the header based on the Python dictionary keys
                writer.writeheader()
                
                # Write the actual data rows
                writer.writerows(transformed_data)
            print(f"Successfully saved Python data to {file_name}")
    except IOError:
            print("An error occurred while writing the Python CSV file.")