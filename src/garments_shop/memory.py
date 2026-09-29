import json

def save_memory(memory):
    with open("memory.json", "w") as file:
        json.dump(memory, file)

def load_memory():
    try:
        with open("memory.json","r") as file:
            return json.load(file)

    except FileNotFoundError:
        return {}

def remember(key,value):
    memory = load_memory()
    memory[key] = value
    save_memory(memory)

def get_memory(key):
    memory = load_memory()
    return memory.get(key)

def forget(key):
    memory = load_memory()
    if key in memory:
       del memory[key]
       save_memory(memory)

    