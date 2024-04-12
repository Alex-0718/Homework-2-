# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution

tokenB -> tokenA -> tokenD -> tokenC -> tokenB

swap, tokenB -> tokenA, AmountIn = 5000000000000000000, AmountOut = 5655321988655321988  
swap, tokenA -> tokenD, AmountIn = 5655321988655321988, AmountOut = 2458781317097933552  
swap, tokenD -> tokenC, AmountIn = 2458781317097933552, AmountOut = 5088927293301515695  
swap, tokenB -> tokenA, AmountIn = 5000000000000000000, AmountOut = 5655321988655321988  
swap, tokenB -> tokenA, AmountIn = 5000000000000000000, AmountOut = 5655321988655321988  

the final tokenB balance: 20129888944077446732

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution

In Automated Market Makers (AMMs), slippage refers to the deviation between the expected price and the actual execution price when conducting a trade. This deviation occurs because the asset ratio in the liquidity pool changes due to the impact of your trade. While Uniswap V2 cannot completely eliminate slippage, it employs the constant product equation (x * y = k) to minimize it as much as possible.

Suppose I want to exchange 1 ETH for DAI, and the pool initially contains 100 ETH and 10,000 DAI (k = 1,000,000). When I swap for DAI, the amount of ETH in the pool decreases while the amount of DAI increases, altering the pool's ratio and affecting the price.

For example, after exchanging for DAI, the pool becomes 99 ETH and 10,100 DAI. Using the new pool ratio, the price of 1 DAI would be slightly higher than before (k = 990,000). This represents slippage.

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution

The rationale behind subtracting a minimum liquidity upon initial liquidity minting in the mint function of the UniswapV2Pair contract is to prevent very small liquidity positions from being created, which could potentially lead to inefficient use of the liquidity pool and increased risk of impermanent loss for liquidity providers.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution

The intention behind using a specific formula to obtain liquidity when depositing tokens in the UniswapV2Pair contract is to ensure that the deposited tokens are balanced against the existing reserves in the liquidity pool, maintaining the constant product invariant. This helps to prevent manipulation of the liquidity pool and maintain efficient trading conditions for users.

## Problem 5    
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution

A sandwich attack is a type of frontrunning in decentralized exchanges. Attackers monitor pending transactions, quickly place trades to manipulate prices, and profit by executing trades before and after a target transaction. This can impact you during a swap by causing slippage, resulting in less favorable prices.
