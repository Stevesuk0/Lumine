import os
import yaml

root_config_path = ".lumine"

os.makedirs(root_config_path, exist_ok=True)


def use(config_name: str) -> list:
    path = f"{root_config_path}/{config_name}.yaml"

    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f) or {}
    else:
        config = {}
        with open(path, "w", encoding="utf-8") as f:
            yaml.safe_dump(
                config,
                f,
                allow_unicode=True,
                sort_keys=False
            )

    return [config_name, config]


def sync(config: list) -> None:
    path = f"{root_config_path}/{config[0]}.yaml"

    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(
            config[1],
            f,
            allow_unicode=True,
            sort_keys=False
        )

def raw_sync(config: list, content) -> None:
    path = f"{root_config_path}/{config[0]}.yaml"

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def set(config: list, key: str, content) -> list:
    config[1][key] = content
    return config


def get(config: list, key: str, fallback=None):
    return config[1].get(key, fallback)