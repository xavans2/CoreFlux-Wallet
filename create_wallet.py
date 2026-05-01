# create_wallet.py
import os
import json
import hashlib

def generate_wallet():
    private_key = os.urandom(32).hex()
    public_key = hashlib.sha256(private_key.encode()).hexdigest()

    wallet = {
        "private_key": private_key,
        "public_key": public_key,
        "balance": 0
    }

    with open("wallet.json", "w") as f:
        json.dump(wallet, f, indent=4)

    print("🪪 Wallet created!")
    print("Public key:", public_key)

if __name__ == "__main__":
    generate_wallet()
