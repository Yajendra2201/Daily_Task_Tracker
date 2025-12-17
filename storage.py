import json

def load_data():
    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)
            return data.get("tasks", [])
    except FileNotFoundError:
        return []

def save_tasks(tasks):

    with open("tasks.json", "w") as file:
        json.dump({"tasks": tasks}, file)
