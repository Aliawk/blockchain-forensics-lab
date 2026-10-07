# Blockchain Forensics Lab

A practical learning laboratory for blockchain forensics, cryptocurrency tracing, on-chain analysis, and investigative methodology.

The goal of this repository is to develop practical skills for analyzing cryptocurrency transactions, tracing the movement of funds, identifying transaction patterns, evaluating forensic heuristics, and documenting findings without overstating what the blockchain evidence can prove.

> **Status:** Active learning project.  
> Topics marked as planned are areas I am currently working toward and should not be interpreted as completed expertise.

---

## Objectives

This lab is designed to build practical knowledge in:

- Bitcoin transaction analysis
- UTXO tracing
- Transaction graph analysis
- Forensic heuristics
- Wallet and address clustering
- CoinJoin and obfuscation analysis
- Ethereum and EVM transaction analysis
- ERC-20 token tracing
- DeFi transaction analysis
- Cross-chain tracing
- OSINT and entity attribution
- Investigative documentation
- Python-based analysis tooling

A central principle throughout the project is separating:

**Observation → Hypothesis → Supporting Evidence → Confidence → Limitation**

---

# Learning Roadmap

## 1. Bitcoin Fundamentals — In Progress

Understand the data model behind Bitcoin before attempting more advanced tracing.

### Topics

- Bitcoin transactions
- Inputs and outputs
- UTXO model
- TXID
- Output indexes (`vout`)
- Previous transaction references
- Satoshis
- Transaction fees
- Following spent outputs
- Transaction chains

### Practical work

- Parse synthetic Bitcoin transaction data
- Calculate total inputs and outputs
- Calculate transaction fees
- Identify specific UTXOs using `TXID:vout`
- Follow a UTXO into a subsequent transaction
- Validate transaction relationships

---

## 2. Bitcoin Transaction Tracing — In Progress

Learn how value can be followed through multiple Bitcoin transactions.

### Topics

- Multi-hop tracing
- Transaction graphs
- Address reuse
- Fan-in patterns
- Fan-out patterns
- UTXO consolidation
- Batch transactions
- Peel chains
- Transaction timelines

### Investigation questions

- Where did the funds originate?
- Where were they sent?
- Which UTXO was spent?
- Which outputs continue the flow?
- Where does deterministic tracing end?
- Which conclusions require heuristics?

---

## 3. Forensic Heuristics — In Progress

Study techniques used to generate investigative hypotheses from blockchain activity.

### Topics

- Common Input Ownership Heuristic
- Change-address heuristics
- Address clustering
- Wallet clustering
- Output-value analysis
- Spending-pattern analysis
- Address reuse
- Behavioral patterns

### Analytical principles

A heuristic is not proof.

Each finding should distinguish between:

- Direct blockchain observation
- Deterministic transaction relationship
- Heuristic inference
- External attribution
- Unknown or inconclusive information

Confidence levels and alternative explanations should be documented where appropriate.

---

## 4. CoinJoin & Obfuscation Analysis — Planned

Understand techniques that can make straightforward blockchain tracing unreliable.

### Topics

- CoinJoin fundamentals
- Equal-output patterns
- Multi-party transactions
- Why Common Input Ownership can fail
- Change ambiguity
- Mixing concepts
- Layering
- Multi-hop obfuscation
- Limits of deterministic tracing

### Investigation focus

Learn when normal wallet-clustering assumptions should **not** be applied and how uncertainty should be documented.

---

## 5. Real Bitcoin Investigation — Planned

Move from synthetic transaction data to public blockchain data.

### Tasks

- Inspect real transactions using blockchain explorers
- Identify inputs and outputs
- Locate specific `TXID:vout` references
- Follow funds across multiple transactions
- Identify transaction patterns
- Build transaction timelines
- Create transaction graphs
- Record evidence sources
- Document findings and limitations

The goal is to produce a complete Bitcoin investigation case based entirely on public blockchain information.

---

## 6. Attribution & OSINT — Planned

Blockchain addresses identify blockchain activity, not automatically real-world identities.

### Topics

- Address vs wallet vs entity vs person
- Entity attribution
- Exchange attribution
- Service identification
- Public wallet labels
- OSINT methodology
- Corroborating blockchain findings with external information
- Attribution confidence
- False attribution risks

### Core principle

An address being connected to another address does not automatically prove that the same person controls both.

---

## 7. Exchanges & VASPs — Planned

Understand how centralized cryptocurrency services affect an investigation.

### Topics

- Exchange deposit addresses
- Withdrawal transactions
- Hot wallets
- Cold wallets
- Wallet consolidation
- Batch withdrawals
- Service clusters
- KYC boundaries
- On-chain vs off-chain evidence

### Investigation focus

Understand what can be determined from the blockchain and when additional information from a service provider would be required.

---

# Ethereum Forensics

## 8. Ethereum Fundamentals — Planned

Understand how Ethereum differs from Bitcoin.

### Topics

- Account-based model
- Externally Owned Accounts (EOAs)
- Smart contracts
- Nonces
- Gas
- Transaction fees
- Contract interaction
- Internal calls
- Events and logs
- Ethereum explorers

### Comparison

Bitcoin:

`UTXO → UTXO → UTXO`

Ethereum:

`Account → Transaction → Account / Contract`

---

## 9. ERC-20 Token Analysis — Planned

Learn how token movements are represented and traced on Ethereum.

### Topics

- ERC-20 standard
- Token contracts
- Token transfers
- `Transfer` events
- `transfer()`
- `transferFrom()`
- Token approvals
- Stablecoins
- USDT
- USDC
- Token balances
- Contract interactions

### Practical work

Trace token movements independently from native ETH transfers.

---

## 10. DeFi Analysis — Planned

Study how cryptocurrency flows through decentralized financial protocols.

### Topics

- Decentralized exchanges
- Swaps
- Liquidity pools
- Router contracts
- Wrapped assets
- Stablecoins
- Smart-contract interactions
- Multi-step transactions

### Investigation focus

Follow value through:

`Wallet → DEX → Token Swap → Wallet`

rather than treating every contract interaction as a simple payment.

---

## 11. Cross-Chain Tracing — Planned

Learn how investigations continue when assets move between blockchains.

### Topics

- Blockchain bridges
- Bridge deposits
- Bridge withdrawals
- Chain hopping
- Wrapped assets
- Asset conversion
- Timing and value correlation
- Cross-chain attribution limitations

Example:

`Bitcoin → Exchange → USDT → Ethereum → Bridge → Another Chain`

The goal is to understand where relationships are deterministic and where they become analytical hypotheses.

---

# Investigation Methodology

## 12. Evidence & Documentation — Planned

Technical analysis must be reproducible and clearly documented.

### Method

1. Define the investigative question
2. Identify known addresses or transactions
3. Record data sources
4. Trace transactions
5. Identify relevant patterns
6. Apply appropriate heuristics
7. Separate observations from interpretations
8. Consider alternative explanations
9. Assign confidence
10. Document limitations
11. Produce a reproducible conclusion

### Reporting structure

Investigation reports will contain:

- Executive summary
- Scope
- Known starting information
- Data sources
- Methodology
- Transaction timeline
- Transaction graph
- Address analysis
- Fund-flow analysis
- Findings
- Alternative explanations
- Limitations
- Confidence assessment
- Recommended next investigative steps

---

# Tools

## BTC Analyzer — In Progress

Python-based educational Bitcoin transaction analyzer.

Current capabilities:

- Load transaction data from JSON
- Convert BTC to satoshis
- Calculate transaction fees
- Identify multiple inputs
- Identify possible change candidates
- Resolve previous transaction outputs
- Trace `TXID:vout` relationships
- Display forensic observations and limitations

Planned:

- Multi-hop tracing
- Transaction graph generation
- Address clustering
- Pattern detection
- CSV export
- Timeline generation
- Real public blockchain data ingestion

---

## ETH Analyzer — Planned

Planned Ethereum analysis tool for:

- ETH transfers
- ERC-20 transfers
- Contract interactions
- Event/log extraction
- Address activity
- Transaction tracing

---

## Transaction Visualizer — Planned

Graph-based visualization of cryptocurrency transaction flows.

Planned features:

- Transaction nodes
- Address nodes
- Directed fund flows
- Value labels
- Multi-hop tracing
- Cluster visualization
- Exportable investigation graphs

---

# Cases

The repository will gradually contain practical investigation exercises.

```text
cases/
├── 01-utxo-analysis/
├── 02-bitcoin-tracing/
├── 03-peel-chain-analysis/
├── 04-coinjoin-analysis/
├── 05-wallet-clustering/
├── 06-bitcoin-investigation/
├── 07-ethereum-tracing/
├── 08-token-analysis/
├── 09-defi-analysis/
└── 10-cross-chain-analysis/
```

Each case should document:

- Objective
- Dataset
- Method
- Observations
- Analysis
- Heuristics used
- Findings
- Confidence
- Alternative explanations
- Limitations

---

# Repository Structure

```text
blockchain-forensics-lab/
│
├── cases/
│   └── 01-utxo-analysis/
│       ├── README.md
│       └── transactions.json
│
├── docs/
│   └── forensic-heuristics.md
│
├── tools/
│   ├── btc-analyzer/
│   │   └── analyze.py
│   ├── eth-analyzer/
│   └── transaction-visualizer/
│
└── README.md
```

---

# Final Goal

The final stage of the lab will combine the individual skills into complete simulated cryptocurrency investigations.

A case may involve a flow such as:

```text
Known Address
      │
      ▼
   Bitcoin
      │
      ▼
 Peel Chain
      │
      ▼
  CoinJoin?
      │
      ▼
   Exchange
      │
      ▼
 ETH / Stablecoin
      │
      ▼
     DEX
      │
      ▼
    Bridge
      │
      ▼
 Another Chain
```

The objective will not simply be to follow arrows.

The investigation must explain:

- What can be proven from blockchain data
- What can only be inferred
- Which heuristics were used
- Where those heuristics may fail
- What external information would strengthen attribution
- How confident each conclusion is

---

## Disclaimer

This repository is an educational project focused on blockchain analysis and digital forensics.

Cases use synthetic data, test data, or publicly available blockchain information. The purpose is to develop investigative and analytical skills while documenting the limitations of blockchain attribution.
