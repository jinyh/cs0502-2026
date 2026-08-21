"""L06：用反例和状态数量比较贪心、递归与记忆化。"""


def greedy_change(amount, coins):
    chosen = []
    for coin in sorted(coins, reverse=True):
        while amount >= coin:
            amount -= coin
            chosen.append(coin)
    return chosen if amount == 0 else None


def optimal_change(amount, coins):
    best = [None] * (amount + 1)
    best[0] = []
    for current in range(1, amount + 1):
        candidates = [best[current - coin] + [coin] for coin in coins if coin <= current and best[current - coin] is not None]
        if candidates:
            best[current] = min(candidates, key=len)
    return best[amount]


def count_paths_naive(steps, counter):
    counter[0] += 1
    if steps <= 1:
        return 1
    return count_paths_naive(steps - 1, counter) + count_paths_naive(steps - 2, counter)


def count_paths_memoized(steps, memo, counter):
    counter[0] += 1
    if steps <= 1:
        return 1
    if steps not in memo:
        memo[steps] = count_paths_memoized(steps - 1, memo, counter) + count_paths_memoized(steps - 2, memo, counter)
    return memo[steps]


def main():
    coins, amount = [1, 3, 4], 6
    print("贪心找零:", greedy_change(amount, coins))
    print("最少硬币:", optimal_change(amount, coins))

    naive_calls = [0]
    memo_calls = [0]
    ways = count_paths_naive(10, naive_calls)
    count_paths_memoized(10, {}, memo_calls)
    print("走 10 级台阶的方法数:", ways)
    print("朴素递归调用:", naive_calls[0], "记忆化调用:", memo_calls[0])


if __name__ == "__main__":
    main()
