## Objective

The objective of this investigation was to trace Bitcoin funds across multiple transactions using public blockchain data and evaluate whether recurring transaction patterns could indicate peel-chain-like behavior.

The investigation focused on distinguishing directly observable blockchain evidence from heuristic conclusions.

## Method

The investigation was performed manually using public Bitcoin blockchain data.

The analysis included:

- Following spent UTXOs between transactions
- Comparing input and output values
- Examining transaction fees
- Profiling receiving addresses
- Comparing subsequent spending behavior
- Investigating alternative branches when the transaction pattern changed

## Observations

The investigated transaction sequence repeatedly displayed transactions with one input and two outputs.

Several consecutive transactions also used a transaction fee of 846 satoshis.

During the initial part of the trace, one relatively small output was created while the larger output was subsequently spent in another transaction.

At transaction `e264653d...`, this pattern changed. The transaction created two substantially sized outputs:

- `0.10486020 BTC`
- `0.05550835 BTC`

Because the previous value pattern had changed, both branches required further investigation rather than automatically treating the largest output as the continuation.

## Address Profiling

The `0.10486020 BTC` output was sent to a heavily reused P2WPKH address.

At the time of analysis, the address showed:

- 71 transactions
- Approximately 2.1366 BTC received
- Zero current balance
- No unspent outputs

This activity demonstrates significant address reuse but does not establish whether the address belongs to an individual, exchange, service or another entity.

The `0.05550835 BTC` output was sent to an address with significantly less transaction history.

That output was subsequently spent in another transaction producing:

- `0.00151306 BTC`
- `0.05398683 BTC`

The larger output continued the transaction structure observed earlier in the investigation.

## Analysis

The recurring spending structure is consistent with peel-chain-like behavior.

Supporting indicators include:

- Repeated one-input/two-output transactions
- One output repeatedly being spent onward
- Similar transaction structure across multiple hops
- Repeated transaction fees of 846 satoshis

However, these indicators do not prove that all addresses involved are controlled by the same wallet or entity.

The investigation also demonstrates why output value alone is insufficient for identifying change. At the point where the transaction structure changed, following only the largest output would have produced a different tracing path.

Subsequent spending behavior provided additional evidence for evaluating the alternative branch.

## Limitations

The blockchain data establishes which UTXOs were created and subsequently spent.

It does not independently establish:

- The real-world identity of the wallet owner
- That all investigated addresses belong to the same entity
- That a suspected continuation output is definitely change
- The purpose of the transactions
- Whether the heavily reused address belongs to an exchange or other service

External attribution data would be required to make stronger conclusions about ownership or identity.

## Conclusion

The investigated transaction sequence displays recurring characteristics consistent with peel-chain-like behavior.

The case demonstrates that transaction tracing should not rely on a single heuristic. Output values, transaction structure, address behavior and subsequent spending should instead be evaluated together.

Most importantly, directly observable blockchain relationships must be separated from hypotheses about wallet ownership, transaction purpose and real-world identity.