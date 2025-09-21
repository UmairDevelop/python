from pathlib import Path
import json, os

data = {
    "name": "Umair Ahmad",
    "age": 25,
    "city": "Lahore",
    "skills": ["Python", "JavaScript", "C++"]
}

# Ensure the directory exists before changing into it
# Write JSON data to a file
if os.path.exists('json_folder'):
    os.chdir("json_folder")
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=2)
else:
    (Path.cwd()/"json_folder").mkdir(exist_ok=True)
    os.chdir("json_folder")
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=2)

# Read JSON data from a file
with open('data.json', 'r') as f:
    content = json.load(f)
    print(content)

# Convert to JSON string and back
json_content = json.dumps(data, indent=2)

# Convert JSON string back to Python object
parser = json.loads(json_content)
print(parser["skills"][0])