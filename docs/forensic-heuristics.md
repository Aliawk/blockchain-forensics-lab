# Bitcoin Forensic Heuristics

This document summarizes Bitcoin transaction heuristics used throughout the blockchain forensics lab.

Heuristics can support an investigation but should not be treated as proof of ownership, identity or intent.

## Common Input Ownership Heuristic (CIOH)

When multiple Bitcoin addresses provide inputs to the same transaction, they may be controlled by the same entity because each input must be authorized for spending.

### Indicator

```text
Address A ─┐
           ├── Transaction
Address B ─┘
```

### Possible Interpretation

Addresses A and B may belong to the same wallet or entity.

### Limitation

This assumption can fail in collaborative transactions such as CoinJoin, where multiple independent users intentionally provide inputs to the same transaction.

**Confidence:** Context dependent.

---

## Change-Output Heuristic

Bitcoin transactions often create a payment output and another output returning remaining funds to the sender.

The blockchain does not explicitly identify which output represents change.

### Possible Indicators

- Output value
- Address type
- Address reuse
- Transaction structure
- Subsequent spending behavior
- Similarity with previous transactions

### Limitation

Neither the smallest nor largest output should automatically be classified as change.

Multiple indicators should be considered.

---

## Peel-Chain Pattern

A peel chain occurs when funds are repeatedly spent through a sequence of transactions where part of the value is separated and the remaining value continues to another transaction.

Example:

```text
1.00 BTC
   │
   ├── 0.05 BTC
   └── 0.94 BTC
          │
          ├── 0.04 BTC
          └── 0.89 BTC
                 │
                 └── continues...
```

### Possible Indicators

- Repeated transaction structure
- One output repeatedly spent onward
- Gradually decreasing continuation value
- Similar fees
- Similar address or script types

### Limitation

Peel-chain-like behavior does not prove that all addresses in the sequence are controlled by the same entity.

---

## Address Reuse

Address reuse occurs when the same Bitcoin address participates in multiple transactions.

Repeated activity can provide useful behavioral information and make transaction relationships easier to investigate.

### Limitation

An active or heavily reused address does not reveal the real-world identity of its controller.

External attribution data is required to associate an address with a person, exchange, service or organization.

---

## Fan-In

Fan-in describes transactions where multiple inputs are combined into fewer outputs.

```text
A ─┐
B ─┼──► Transaction ───► X
C ─┘
```

This can occur during wallet consolidation or service activity.

### Limitation

Transaction structure alone does not determine why consolidation occurred or who controls the inputs.

---

## Fan-Out

Fan-out describes transactions where one or a small number of inputs create many outputs.

```text
                  ┌──► A
Input ─► TX ──────┼──► B
                  ├──► C
                  └──► D
```

This can appear in batch payments, exchange withdrawals or other wallet activity.

### Limitation

The structure alone cannot determine the purpose of the transaction.

---

## CoinJoin Indicators

CoinJoin combines inputs from multiple participants into a single transaction to make ownership relationships more difficult to determine.

Possible indicators include:

- Multiple inputs
- Multiple outputs
- Several equal-value outputs
- Transaction structures designed to reduce input-output linkage

### Investigative Impact

CoinJoin can weaken:

- Common Input Ownership Heuristic
- Change-output identification
- Input-to-output attribution

Equal outputs can create an anonymity set where blockchain data alone does not establish which participant controls which output.

---

## Behavioral Indicators

Individual transaction characteristics may be weak evidence.

Repeated characteristics across multiple transactions can provide stronger analytical signals.

Examples include:

- Repeated transaction fees
- Similar input/output structures
- Similar script types
- Consistent spending intervals
- Repeated continuation patterns

These indicators can support a hypothesis but should not independently be treated as proof of common ownership.

---

## Evidence vs Inference

Blockchain investigations should distinguish between direct observations and analytical conclusions.

### Observation

Something directly verifiable from blockchain data.

Example:

> Output 1 of Transaction A was spent as an input in Transaction B.

### Hypothesis

An interpretation of observed behavior.

Example:

> Output 1 may represent wallet change.

### Supporting Evidence

Additional observations that strengthen the hypothesis.

Example:

> The output was subsequently spent using the same recurring transaction structure observed across several previous transactions.

### Limitation

Factors preventing a stronger conclusion.

Example:

> Blockchain data alone does not establish that the addresses are controlled by the same entity.

## Core Principle

**Blockchain relationships can often be proven. Ownership, identity and intent usually cannot.**

A forensic conclusion should therefore clearly distinguish:

**Observation → Hypothesis → Supporting Evidence → Limitation**