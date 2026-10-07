import json
from pathlib import Path
from decimal import Decimal

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = BASE_DIR / "cases" / "01-utxo-analysis" / "transactions.json"

SATS_PER_BTC = 100_000_000


def btc_to_sats(amount_btc):
    return int(amount_btc * SATS_PER_BTC)


# Load transaction data
with open(DATA_FILE, "r", encoding="utf-8") as file:
    transactions = json.load(file, parse_float=Decimal)


# Create lookup table:
# TXID -> transaction
transaction_lookup = {
    tx["txid"]: tx for tx in transactions
}


def find_previous_output(prev_txid, prev_vout):
    """
    Find the UTXO referenced by a transaction input.
    """

    previous_transaction = transaction_lookup.get(prev_txid)

    if previous_transaction is None:
        return None

    for output in previous_transaction["outputs"]:
        if output["vout"] == prev_vout:
            return output

    return None


def get_input_amount(tx_input):
    """
    Determine an input's value.

    For traced inputs, derive the value from the referenced
    previous transaction output.

    Direct amounts are supported for the simplified starting
    inputs in this educational dataset.
    """

    if "prev_txid" in tx_input and "prev_vout" in tx_input:

        previous_output = find_previous_output(
            tx_input["prev_txid"],
            tx_input["prev_vout"]
        )

        if previous_output is None:
            raise ValueError(
                f"Referenced UTXO not found: "
                f"{tx_input['prev_txid']}:vout{tx_input['prev_vout']}"
            )

        return previous_output["amount"]

    if "amount" in tx_input:
        return tx_input["amount"]

    raise ValueError("Input contains no usable amount or UTXO reference")


# Analyze transactions
for transaction in transactions:

    txid = transaction["txid"]
    inputs = transaction["inputs"]
    outputs = transaction["outputs"]

    print("\n========================================")
    print("BITCOIN TRANSACTION ANALYSIS")
    print("========================================")
    print("Transaction:", txid)

    # ----------------------------------------
    # Inputs
    # ----------------------------------------

    total_input = 0

    print("\nINPUTS")

    for tx_input in inputs:

        amount = get_input_amount(tx_input)
        amount_sats = btc_to_sats(amount)
        total_input += amount_sats

        if "prev_txid" in tx_input:

            prev_txid = tx_input["prev_txid"]
            prev_vout = tx_input["prev_vout"]

            previous_output = find_previous_output(
                prev_txid,
                prev_vout
            )

            print(
                f"{prev_txid}:vout{prev_vout} -> "
                f"{previous_output['address']} -> "
                f"{amount_sats:,} sats"
            )

        else:

            print(
                f"{tx_input['address']} -> "
                f"{amount_sats:,} sats"
            )

    # ----------------------------------------
    # Outputs
    # ----------------------------------------

    total_output = 0

    print("\nOUTPUTS")

    for tx_output in outputs:

        amount_sats = btc_to_sats(tx_output["amount"])
        total_output += amount_sats

        print(
            f"vout {tx_output['vout']} -> "
            f"{tx_output['address']} -> "
            f"{amount_sats:,} sats"
        )

    # ----------------------------------------
    # Transaction summary
    # ----------------------------------------

    transaction_fee = total_input - total_output

    if transaction_fee < 0:
        raise ValueError(
            f"{txid}: outputs exceed inputs"
        )

    print("\nSUMMARY")
    print(f"Total input:  {total_input:,} sats")
    print(f"Total output: {total_output:,} sats")
    print(f"Fee:          {transaction_fee:,} sats")

    # ----------------------------------------
    # Common-input ownership heuristic
    # ----------------------------------------

    if len(inputs) > 1:

        print("\nFORENSIC OBSERVATION")
        print("Multiple inputs detected.")
        print(
            "Possible common-input ownership relationship."
        )
        print(
            "Limitation: This is a heuristic, not proof of "
            "common ownership (for example, CoinJoin may "
            "combine inputs from different participants)."
        )

    # ----------------------------------------
    # Simple change-output heuristic
    # ----------------------------------------

    if len(outputs) > 1:

        smallest_output = min(
            outputs,
            key=lambda output: output["amount"]
        )

        print("\nCHANGE HEURISTIC")
        print(
            "Possible change candidate:",
            smallest_output["address"]
        )
        print("Confidence: Low")
        print(
            "Reason: Smallest output in a multi-output "
            "transaction."
        )
        print(
            "Limitation: Output size alone cannot determine "
            "whether an output is change."
        )

    # ----------------------------------------
    # UTXO tracing
    # ----------------------------------------

    traced_input_found = False

    for tx_input in inputs:

        if "prev_txid" not in tx_input:
            continue

        if not traced_input_found:
            print("\nUTXO TRACE")
            traced_input_found = True

        prev_txid = tx_input["prev_txid"]
        prev_vout = tx_input["prev_vout"]

        previous_output = find_previous_output(
            prev_txid,
            prev_vout
        )

        print(
            f"{prev_txid}:vout{prev_vout} "
            f"({previous_output['address']}, "
            f"{btc_to_sats(previous_output['amount']):,} sats)"
        )

        print(
            f"    -> spent by {txid}"
        )