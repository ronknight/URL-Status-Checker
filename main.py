import os
import requests
import csv

# Specify the directory you want to check
directory = '/path/to/your/directory'

# Get all filenames in the directory
filenames = os.listdir(directory)

# Filter for .png files
png_filenames = [f for f in filenames if f.endswith('.png')]

# Convert filenames to URLs
base_url = 'http://example.com/'  # Replace with your base URL
urls = [base_url + f for f in png_filenames]

# Prepare to write to CSV
with open('url_status.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["URL", "Status"])

    # Check if URLs exist and write to CSV
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                writer.writerow([url, 'Exists'])
            else:
                writer.writerow([url, 'Does not exist'])
        except requests.ConnectionError:
            writer.writerow([url, 'Failed to connect'])