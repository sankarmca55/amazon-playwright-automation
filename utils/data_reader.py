import json

from pathlib import Path

project_root = Path(__file__).parent.parent

#Login test data
json_file = project_root / "test_data" / "login_data.json"

with open(json_file) as file:
    login_data = json.load(file)

    print(f"Loaded login data from {json_file}: {login_data}")


# Search test data
json_file = project_root / "test_data" / "search_data.json"

with open(json_file) as file:
    search_data = json.load(file)

    print(f"Loaded search data from {json_file}: {search_data}")
