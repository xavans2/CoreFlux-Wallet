import json
import os

WALLET_FILE = "wallet.json"


def create_wallet():
    import hashlib
    import os

    private = os.urandom(32).hex()
    public = hashlib.sha256(private.encode()).hexdigest()

    data = {
        "private_key": private,
        "public_key": public,
        "balance": 0
    }

    with open(WALLET_FILE, "w") as f:
        json.dump(data, f, indent=4)

    print("🪪 Wallet created:", public)


def show_wallet():
    with open(WALLET_FILE) as f:
        data = json.load(f)

    print("🪪 ADDRESS:", data["public_key"])
    print("💰 BALANCE:", data["balance"])
