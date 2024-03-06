# The instructions are asking for a script to analyze an NGINX server log with the following objectives:

# Determine the top 10 visitors by IP address.
# Calculate the error rate per endpoint.

                           
import csv
from collections import Counter

# Initialize counters
ip_counter = Counter()
err_per_endpoint = {}

# Open the server log file
with open('server_log.csv', 'r') as csvfile:
    # Create a CSV reader object
    log_reader = csv.reader(csvfile)
    # Skip the header row if there is one
    next(log_reader, None)
    
    # Process each log entry
    for row in log_reader:
        # Parse the row to extract needed data
        ip_address = row[0]  # Assuming IP address is the first column
        request_data = row[1].split()  # Assuming the request log is the second column
        status_code = request_data[8]
        endpoint = request_data[6]
        
        # Update the IP address counter
        ip_counter[ip_address] += 1

        # If the endpoint doesn't exist in the dictionary, add it with a new Counter
        if endpoint not in err_per_endpoint:
            err_per_endpoint[endpoint] = Counter()

        # Increment the status code counter for this endpoint
        err_per_endpoint[endpoint][status_code] += 1

# Output the top 10 IP addresses
print("Top 10 IP addresses:")
for ip, count in ip_counter.most_common(10):
    print(f"{ip}: {count}")

# Output the error rate per endpoint
print("\nError rate per endpoint:")
for endpoint, counter in err_per_endpoint.items():
    # Calculate the total number of requests for the endpoint
    total_requests = sum(counter.values())
    # Calculate the number of error responses (4xx and 5xx status codes)
    error_responses = sum(count for status, count in counter.items() if status.startswith('4') or status.startswith('5'))
    # Calculate the error rate
    error_rate = (error_responses / total_requests) * 100
    print(f"{endpoint}: {error_rate:.2f}%")
