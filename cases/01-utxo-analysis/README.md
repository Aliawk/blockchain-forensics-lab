# Case 01 – UTXO Analysis

## Objective

The objective of this case is to understand the Bitcoin UTXO model and how transaction relationships can be analyzed from a blockchain-forensics perspective.

The case uses synthetic transaction data to practice tracing inputs and outputs without relying on assumptions about real-world identities.

## Dataset

The transactions used in this case are stored in:

`transactions.json`

Each transaction contains inputs and outputs that can be analyzed to determine:

- Total input value
- Total output value
- Transaction fee
- Newly created UTXOs
- Previously consumed UTXOs
- Possible transaction relationships

## UTXO Model

Bitcoin does not store balances in the same way as a traditional bank account.

Instead, Bitcoin uses **Unspent Transaction Outputs (UTXOs)**.

A transaction consumes existing UTXOs as inputs and creates new UTXOs as outputs.

A specific UTXO can be referenced using:

`TXID:vout`

For example:

`TX-001:1`

refers to output index 1 of transaction `TX-001`.

## Transaction Fees

Bitcoin transaction fees are calculated as:

`Total Inputs - Total Outputs = Transaction Fee`

The fee is not represented as a separate transaction output.

For example:

`0.80000000 BTC - 0.79950000 BTC = 0.00050000 BTC`

This corresponds to:

`50,000 satoshis`

## Change-Output Analysis

A transaction may contain a payment output and a change output returning funds to the sender.

However, the blockchain does not explicitly label an output as change.

Change identification therefore requires heuristics.

Possible indicators include:

- Output value
- Address/script type
- Address reuse
- Subsequent spending behavior
- Transaction structure

The smallest or largest output should **not automatically be classified as change**.

## Common Input Ownership Heuristic

The Common Input Ownership Heuristic (CIOH) assumes that addresses used together as inputs may be controlled by the same entity because the transaction requires authorization to spend each input.

Example:

```text
Address A ─┐
           ├── Transaction
Address B ─┘
```

This may suggest common control of A and B.

However, this is a **heuristic and not proof of ownership**.

Collaborative transactions such as CoinJoin can invalidate this assumption.

## Fan-In and Fan-Out

Two transaction structures examined during the case were:

**Fan-in**

Multiple inputs are consolidated into fewer outputs.

```text
A ─┐
B ─┼──► Transaction ───► X
C ─┘
```

**Fan-out**

One or a small number of inputs create many outputs.

```text
                  ┌──► A
Input ─► TX ──────┼──► B
                  ├──► C
                  └──► D
```

These patterns can provide useful information about wallet behavior but do not independently identify the entity controlling the addresses.

## CoinJoin and Heuristic Limitations

CoinJoin demonstrates why blockchain heuristics must be applied carefully.

Multiple independent participants can contribute inputs to the same transaction, often creating several outputs with identical or similar values.

This can make it difficult to determine which output corresponds to which participant.

As a result:

- Common input ownership may become unreliable.
- Change-output identification becomes more difficult.
- Transaction structure alone cannot establish ownership.

## Forensic Principles

This case established several principles used throughout the rest of the project:

1. Follow specific UTXOs rather than assuming an address represents an account.
2. Distinguish direct blockchain observations from analytical hypotheses.
3. Transaction relationships do not automatically establish common ownership.
4. Address ownership cannot normally be determined from blockchain data alone.
5. Heuristics should be supported by multiple independent indicators.
6. Alternative explanations should be considered before drawing conclusions.

## Tooling

A small Python analysis tool was developed in:

`tools/btc-analyzer/analyze.py`

The tool is used to calculate transaction values and assist with analysis of the synthetic dataset.

The purpose of the tool is to support the forensic analysis rather than replace manual investigation and interpretation.

## Key Takeaways

This case provided the foundation for later Bitcoin investigations by establishing how UTXOs are created, consumed and traced.

The most important lesson is that blockchain data can establish transaction relationships with high certainty, while conclusions about ownership, intent and identity usually require additional evidence.