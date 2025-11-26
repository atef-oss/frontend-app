import os
import json
from typing import Any, Dict, Optional

def read_json_file(file_path: str) -> Optional[Dict[str, Any]]:
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as file:
        return json.load(file)

def write_json_file(file_path: str, data: Dict[str, Any]) -> None:
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def create_directory_if_not_exists(directory_path: str) -> None:
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def get_file_extension(file_name: str) -> str:
    return os.path.splitext(file_name)[1]

def is_valid_file_path(file_path: str) -> bool:
    return os.path.isfile(file_path)

def merge_dictionaries(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    return {**dict1, **dict2}