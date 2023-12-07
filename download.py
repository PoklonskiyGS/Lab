import pandas
import sys
import requests
import os

strip_chars = ' \t'

if len(sys.argv) < 3:
    raise "Error, filename or/and start number is not provided. Exiting..."
    
filename = sys.argv[1]

# dataset = pandas.read_csv(filename, sep=';')

# for index, row in dataset.iterrows():
#     url = row[1].strip(strip_chars)
#     tmp_file_name = f"{filename}_image_{index}"

#     if not os.path.exists(tmp_file_name):
#         content = requests.get(url, verify=False).content
#         print(f"Writing {len(content)} bytes to #{index} file")
#         with open(tmp_file_name, 'wb') as file:
#             file.write(content)

# print(index)
with open("simple.csv") as inp:
    for i, line in enumerate(inp.readlines()):
        line = line.strip()
        name, url = line.split(";")
        tmp_file_name = f"{filename}_image_{i}"

        if not os.path.exists(tmp_file_name):
            resp = requests.get(url, timeout=20, verify=False)
            with open(tmp_file_name, 'wb') as file:
                file.write(resp.content)
