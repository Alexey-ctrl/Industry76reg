from json_class import JsonFile as jf
from industry_dist import industry
from math import ceil

url = "http://openapi.clearspending.ru/restapi/v3/contracts/select/?customerregion=76&industrial="
file = jf('industry', url)
id_industry = [i for i in industry.keys()]
for i in id_industry[3:4]:
    data_json = list()
    pages = ceil(int(file.get_json_from_url(url=f'{url}{i}')['contracts']["total"]) / 50)
    pages_count = 0
    for page in range(1, pages + 1):
        print(f"{i} : {page}/{pages}")
        data_json.append(file.get_json_from_url(url=f'{url}{i}&page={page}'))
        pages_count += 1
        if pages_count == 250:
            file.create_json_file_from_list(data_json, file_name=f"json_data/industry_{i}_{page}")
            data_json = list()
            pages_count = 0
    file.create_json_file_from_list(data_json, file_name=f"json_data/industry_{i}")
