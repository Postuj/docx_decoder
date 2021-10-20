from bs4 import BeautifulSoup as bs
import base64, os
import tkinter as tk
from tkinter import filedialog

if not os.path.exists('./odkodowane'):
    os.makedirs('./odkodowane')

root = tk.Tk()
root.withdraw()

raw_files = filedialog.askopenfilenames()
source_files = [f for f in raw_files if f.endswith('.xml')]

for source in source_files:
    body = []
    with open(source, "r") as f:
        body = f.readlines()
        body = "".join(body)
        soup = bs(body, "xml")

    files = soup.find_all('dtsf:Plik')

    for file in files:
        filename = './odkodowane/' + file.find('dtsf:Nazwa').text
        content = file.find('dtsf:Zawartosc').text
        content_bytes = content.encode('utf-8')
        with open(filename, 'wb') as result_file:
            decoded_file_data = base64.decodebytes(content_bytes)
            result_file.write(decoded_file_data)
