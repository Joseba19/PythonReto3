import json

with open("config.json", "r") as f:
    config = json.load(f)

print(config['database']['host'])            # localhost
print(config['features']['enable_logging'])  # True