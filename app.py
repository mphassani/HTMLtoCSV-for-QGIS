import tkinter as tk
from tkinter import filedialog
from bs4 import BeautifulSoup
import csv


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
    with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Label', 'Value'])  # Header row
        csv_writer.writerows(data)

    print("CSV file created successfully: output.csv")


def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(
        title="Select an HTML file", filetypes=[("HTML files", "*.html")])

    if file_path:
        convert_html_to_csv(file_path)
    else:
        print("No file selected. Exiting.")


if __name__ == "__main__":
    main()
