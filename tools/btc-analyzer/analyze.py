import json
from pathlib import Path
from decimal import Decimal

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = BASE_DIR / "cases" / "01-utxo-analysis" / "transactions.json"
SATS_PER_BTC = 100_000_000

def btc_to_sats(amount_btc):
    return int(amount_btc * SATS_PER_BTC)

with open(DATA_FILE, "r", encoding="utf-8") as file:
    transaction = json.load(file, parse_float=Decimal)

inputs = transaction["inputs"]
outputs = transaction["outputs"]

total_input = 0

for tx_input in inputs:
    total_input = total_input + btc_to_sats(tx_input["amount"])

total_output = 0

for tx_output in outputs:
    total_output = total_output + btc_to_sats(tx_output["amount"])

transaction_fee = total_input - total_output

print("Total input:", total_input, "sats")
print("Total output:", total_output, "sats")
print("Transaction fee:", transaction_fee, "sats")
