import json
import os

root_config_path = '.lumine'

os.makedirs(root_config_path, exist_ok=True)

def use(config_name: str) -> list:
    if os.path.exists(f"{root_config_path}/{config_name}.json"):
        with open(f"{root_config_path}/{config_name}.json", "r", encoding="utf-8") as f:
            config = json.loads(f.read())

    else:
        with open(f"{root_config_path}/{config_name}.json", "w", encoding="utf-8") as f:
            f.write("{}")
            config = {}

    return [config_name, config]

def sync(config: list) -> None:
    with open(f"{root_config_path}/{config[0]}.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(config[1], ensure_ascii=False, indent=2))

def set(config: list, key: str, content) -> list:
    config[1][key] = content

    return config

def get(config: list, key: str, fallback=None):
    content = config[1].get(key, fallback)

    return content
