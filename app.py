import tkinter as tk
from tkinter import filedialog
from bs4 import BeautifulSoup
import csv
import os


def convert_html_to_csv(html_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract data from the HTML
    data = []
    for p in soup.find_all('p'):
        text = p.get_text()
        label, value = text.split(': ')
        data.append([label, value])

    # Write the extracted data into a CSV file
    output_file_name = os.path.splitext(
        os.path.basename(html_file_path))[0] + ".csv"
    with open(output_file_name, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Label', 'Value'])  # Header row
        csv_writer.writerows(data)

    print(f"CSV file created successfully: {output_file_name}")


def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_paths = filedialog.askopenfilenames(
        title="Select HTML files", filetypes=[("HTML files", "*.html")])

    if file_paths:
        for file_path in file_paths:
            convert_html_to_csv(file_path)
    else:
        print("No files selected. Exiting.")


if __name__ == "__main__":
    main()
