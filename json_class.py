import requests
import json


class JsonFile:
    def __init__(self, file_name="None", url="None"):
        self.file_name = file_name
        self.url = url

    def get_request(self, url=None):
        req = requests.get(self.url) if url is None else requests.get(url)
        assert req.status_code == 200, f"Ошибка : {req.status_code}"
        return req

    def get_json_from_url(self, url=None):
        req = self.get_request() if url is None else self.get_request(url)
        return json.loads(req.text)

    def get_json_from_file(self, file_name=None):
        file = self.file_name if file_name is None else file_name
        with open(f"{file}.json", "r", encoding='utf8') as f:
            jn = json.load(f)
        return jn

    def create_json_file_from_url(self, url=None, file_name=None):
        fn = self.file_name if file_name is None else file_name
        jsn = self.get_json_from_url() if url is None else self.get_json_from_url(url)
        with open(f"{fn}.json", "w", encoding='utf8') as file:
            json.dump(jsn, file, indent=3, ensure_ascii=False)

    def create_json_file_from_list(self, jsn, file_name=None):
        fn = self.file_name if file_name is None else file_name
        with open(f"{fn}.json", "w", encoding='utf8') as file:
            json.dump(jsn, file, indent=3, ensure_ascii=False)
