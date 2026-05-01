import json

def add_reward(amount):
    with open("wallet.json") as f:
        data = json.load(f)

    data["balance"] += amount

    with open("wallet.json", "w") as f:
        json.dump(data, f, indent=4)
