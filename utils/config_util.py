# global_settings.py
import json

def get_settings():
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

CONFIG = get_settings()