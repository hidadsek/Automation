import json
import os


class DataHelper:
    @staticmethod
    def read_json(path):
        cwd = os.path.dirname(__file__)
        file_to_open = os.path.join(cwd, path)
        with open(file_to_open) as f:
            data = json.load(f)
        return data
