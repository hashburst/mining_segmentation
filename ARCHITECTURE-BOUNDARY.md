# HashBurst mining segmentation integration boundary

This repository owns mining segmentation logic: grouping/partitioning workers and cluster-miners by capability, algorithm and mining objective.

It is a specialist engine consumed by `hashburst/mining-accelerator` and coordinated at runtime by `hashburst/node`.

It does not own HVM consensus/APoW protocol rules, generic node lifecycle, TEP, or the full-node installer. Segmentation may propose placement/budgets but cannot override protected HVM/TEP/storage capacity.
