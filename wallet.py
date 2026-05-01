# wallet.py
import json

class Wallet:
    def __init__(self):
        with open("wallet.json") as f:
            self.data = json.load(f)

    def get_balance(self):
        return self.data["balance"]

    def get_address(self):
        return self.data["public_key"]

    def add_balance(self, amount):
        self.data["balance"] += amount
        self._save()

    def _save(self):
        with open("wallet.json", "w") as f:
            json.dump(self.data, f, indent=4)

    def show(self):
        print("🪪 ADDRESS:", self.get_address())
        print("💰 BALANCE:", self.get_balance())
