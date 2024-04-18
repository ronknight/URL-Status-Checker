import os
import requests
import csv
import time
from tqdm import tqdm

# Specify the directory you want to check
# This is the directory where the .png files are located
directory = r'C:\Users\rona\OneDrive - 4sgm.com\Email Catalog\products'

# Get all filenames in the directory
# This will return a list of all files in the specified directory
filenames = os.listdir(directory)

# Filter for .png files
# This will return a new list containing only the filenames that end with .png
png_filenames = [f for f in filenames if f.endswith('.png')]

# Convert filenames to URLs
# This will convert each .png filename to a URL by removing the file extension and appending it to the base URL
base_url = 'https://www.4sgm.com/product/'  # Updated base URL
urls = [base_url + os.path.splitext(f)[0] + '/index.html' for f in png_filenames]

# Write the header to the CSV file
# This opens the CSV file in write mode and writes the header row
with open('url_status.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["URL", "Status", "Status Code"])  # Add "Status Code" column

# Check if URLs exist and write to CSV
# This loop goes through each URL, makes a GET request, and writes the status to the CSV file
for url in tqdm(urls):
    with open('url_status.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        try:
            response = requests.get(url)
            status_code = response.status_code  # Get status code
            # If the status code is 200, the URL exists and 'Exists' is written to the CSV file
            if status_code == 200:
                writer.writerow([url, 'Exists', status_code])
            # If the status code is not 200, the URL does not exist and 'Does not exist' is written to the CSV file
            else:
                writer.writerow([url, 'Does not exist', status_code])
        # If a connection error occurs, 'Failed to connect' is written to the CSV file
        except requests.ConnectionError:
            writer.writerow([url, 'Failed to connect', 'N/A'])  # Write 'N/A' for status code in case of connection error

    time.sleep(30)  # Sleep for 30 seconds
    # This pauses the script for 30 seconds after each request to prevent the server from blocking the IP due to too many requests