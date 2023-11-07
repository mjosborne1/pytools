import pathlib
import json

SKIP_DIRS = ["assets", "temp", "templates"]
EXTS = ["json"]

def get_all_files(root, exclude=SKIP_DIRS):
    for item in root.iterdir():
        if item.name in exclude:
            continue
        for ext in EXTS:
            if item.name.match(ext):
                yield item
        if item.is_dir():
            yield from get_all_files(item)

def get_json_files(root):
    for item in root.glob("*.json"):
        if item.is_file():
            yield item

def check_coding(itm):   
    if isinstance(itm,dict):
        if 'coding' in itm:
            print("Vals: %s" % list(itm.values()))
        elif isinstance(itm.values(),dict):    
            for kv in itm.values.items():
                if 'coding' in kv:
                    print("Vals: %s" % list(kv.values()))

def search_json_file(file):
    with open(file, 'r') as f:
        data = json.load(f)
        if isinstance(data,dict):
            for kv in data.items():
                check_coding(kv[1])                   

