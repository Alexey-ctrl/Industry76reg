from json_class import JsonFile as jf
from csv import writer
from industry_dist import industry
import os

file = jf()
with open('data.csv', 'w', newline="", encoding="utf-8") as csv_file:
    csv_writer = writer(csv_file, delimiter=';')
    csv_writer.writerow(["Industry", "Customer", "Products", "Price", "Date"])
    for i in os.listdir("json_data"):
        json = file.get_json_from_file(f"json_data/{i[:-5]}")
        industry_info = list()
        for contract in json:
            for data in contract['contracts']['data']:
                industry_info.append((industry[i[9]], data.get('customer', {}).get('fullName', ""),
                                      data['products'][0].get("OKDP", {"name": ""}).get("name"), data.get('price'),
                                      data.get("publishDate")))
        for contract in industry_info:
            csv_writer.writerow([col for col in contract])
