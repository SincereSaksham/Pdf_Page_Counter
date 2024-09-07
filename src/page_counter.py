#works only for the pdf files for now
#importing required modules
import os
import pdfplumber

#function that opens up the pdf files and gets the pages of each file
def count_pdf_pages_with_pdfplumber(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            num_pages = len(pdf.pages)
            return num_pages
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return None

#function that counts the pages of pdf files stored in a folder. 
def get_pdf_page_count(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Invalid folder path: {folder_path}")
        return

    total_pages = 0
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            print(f"Processing {filename}...")

            # Count the number of pages in the PDF
            page_count = count_pdf_pages_with_pdfplumber(file_path)
            if page_count is not None:
                total_pages += page_count
                print(f"{filename} has {page_count} pages.\n")
            else:
                print(f"Failed to count pages for {filename}.")

    print(f"Total pages in all PDF files: {total_pages}")

# Usage example:
folder_path = input("Enter the folder path: ")
get_pdf_page_count(folder_path)
