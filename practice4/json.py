import json
with open("sample-data.json", "w", encoding="utf-8") as file:
    data = json.load(file)
    json.dump(data)
    