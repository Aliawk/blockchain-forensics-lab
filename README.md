## Current Progress

### Completed

- Bitcoin transaction fundamentals
- UTXO model, inputs and outputs
- TXID and `vout` tracing
- Transaction fee analysis
- Bitcoin address and script types
- Address reuse analysis
- Common Input Ownership Heuristic (CIOH)
- Change-output heuristics
- Fan-in and fan-out patterns
- UTXO consolidation
- CoinJoin fundamentals and heuristic limitations
- Peel-chain analysis
- Real on-chain Bitcoin transaction tracing
- Address profiling
- Separating deterministic observations from heuristic conclusions

### Cases

#### Case 01 — UTXO Analysis
Synthetic Bitcoin transactions used to understand UTXOs, transaction fees, input/output relationships and basic forensic heuristics.

**Status:** Completed

#### Case 02 — Bitcoin Transaction Tracing
Real public Bitcoin transactions analyzed across multiple hops.

The investigation included:

- Following specific UTXOs between transactions
- Identifying recurring peel-chain-like behavior
- Comparing multiple transaction branches
- Analyzing address reuse
- Identifying repeated transaction characteristics
- Evaluating possible continuation/change outputs
- Documenting attribution limitations
- Separating confirmed on-chain evidence from analytical hypotheses

**Status:** Completed

### Currently Learning

**Ethereum Forensics**

Next topics:

- Ethereum account model
- EOAs and smart contracts
- ETH transactions
- Gas and transaction fees
- Internal calls
- Events and logs
- ERC-20 token transfers
- USDT and USDC tracing
- Smart-contract interactions
- DEX and DeFi analysis
- Cross-chain tracing

---

## Investigation Principle

Throughout this project, findings are separated into four categories:

**Observation → Hypothesis → Supporting Evidence → Limitation**

A transaction relationship that can be verified directly on-chain is treated differently from a heuristic inference or real-world attribution.

The objective is not only to trace cryptocurrency, but to understand **what the available evidence can and cannot establish**.