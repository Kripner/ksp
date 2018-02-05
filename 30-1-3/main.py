H = 4
# sorted
values = [1, 2, 5, 10, 20, 50, 100]
weights = [10, 1, 2, 4, 9, 13, 28]
coins = [0, 0, 1, 1]
K, L = 10, 10

max_possible_buying_value = 0
for i in range(min(K, len(coins))):
    max_possible_buying_value += values[coins[len(coins) - i - 1]]

memo_1 = [[None] * max_possible_buying_value for _ in range(len(coins))]


def max_weight(max_index, requested_value):
    if requested_value == 0:
        return 0
    if requested_value < 0 or max_index == -1:
        return -1
    if memo_1[max_index][requested_value - 1] is not None:
        return memo_1[max_index][requested_value - 1]
    optimal_weight = max_weight(max_index - 1, requested_value)
    if values[coins[max_index]] <= requested_value:
        value, weight = values[coins[max_index]], weights[coins[max_index]]
        alternative_optimal_weight = max_weight(max_index - 1, requested_value - value)
        if alternative_optimal_weight != -1 and (
                optimal_weight == -1 or optimal_weight < alternative_optimal_weight + weight):
            optimal_weight = alternative_optimal_weight + weight
    memo_1[max_index][requested_value - 1] = optimal_weight
    return optimal_weight


print(max_weight(len(coins) - 1, H))
for row in memo_1:
    for n in row:
        print(n, end='\t\t\t')
    print()

memo_2 = []
def max_weight_unbounded(requested_value):
    pass


for i in range(H, max_possible_buying_value):
    buying_weight = max_weight(len(coins) - 1, i)
    back_weight = max_weight_unbounded(buying_weight - H)
