two-sum:
- idea: use hash map but store history as we walk forward

contains duplicate:
- idea: use sets. single pass. O(1) lookup

best time to buy and sell stock:
- idea: track two metrics--minPrice and maxProfit. (like twoPointers)

product of array except self:
- idea: reuse computations. prod = l x r
- trick: minimize space further by rolling multiplications in a single array, (one output array, instead of l and r arrays).
