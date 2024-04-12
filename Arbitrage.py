import itertools

def calculate_exchange(x, y, delta_x):
    numerator = 997 * delta_x * y
    denominator = 1000 * x + 997 * delta_x
    return float(numerator / denominator)

def generate_token_permutations(liquidity):
    tokens = set()
    for key in liquidity.keys():
        tokens.update(key)
    return sorted(tokens)

def get_permutations_starting_with_B(tokens):
    perms = []
    for i in range(3, len(tokens) + 1):
        els = [list(x) for x in itertools.permutations(tokens, i) if x[0] == 'tokenB']
        perms.extend(els)
    return perms

def calculate_arbitrage(liquidity, tokens):
    arbitrage_opportunities = []
    for token_sequence in tokens:
        units = 5.0
        for idx in range(len(token_sequence) - 1):
            x, y = min(token_sequence[idx], token_sequence[idx + 1]), max(token_sequence[idx], token_sequence[idx + 1])
            units = calculate_exchange(liquidity[(x, y)][0], liquidity[(x, y)][1], units)
        x, y = min(token_sequence[-1], token_sequence[0]), max(token_sequence[-1], token_sequence[0])
        units = calculate_exchange(liquidity[(x, y)][0], liquidity[(x, y)][1], units)
        if units > 20:
            arbitrage_opportunities.append((units, token_sequence))
    return sorted(arbitrage_opportunities, reverse=True)

def display_arbitrage_opportunities(arbitrage_opportunities):
    for value, arbitrage in arbitrage_opportunities:
        print('->'.join(arbitrage), end='')
        print(f'->{arbitrage[0]}, {arbitrage[0]} ', end='')
        print(f'balance={value}')

if __name__ == "__main__":
    liquidity = {
        ("tokenA", "tokenB"): (17, 10),
        ("tokenA", "tokenC"): (11, 7),
        ("tokenA", "tokenD"): (15, 9),
        ("tokenA", "tokenE"): (21, 5),
        ("tokenB", "tokenC"): (36, 4),
        ("tokenB", "tokenD"): (13, 6),
        ("tokenB", "tokenE"): (25, 3),
        ("tokenC", "tokenD"): (30, 12),
        ("tokenC", "tokenE"): (10, 8),
        ("tokenD", "tokenE"): (60, 25),
    }
    
    tokens = generate_token_permutations(liquidity)
    token_permutations = get_permutations_starting_with_B(tokens)
    arbitrage_opportunities = calculate_arbitrage(liquidity, token_permutations)
    display_arbitrage_opportunities(arbitrage_opportunities)
