from itertools import combinations
def tsp_dp(distances):
    n = len(distances)
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0
    for mask in range(1 << n):
        for i in range(n):
            if mask & (1 << i):
                for j in range(n):
                    if mask & (1 << j) and i != j:
                        dp[mask][i] = min(dp[mask][i], dp[mask ^ (1 << i)][j] + distances[j][i])
    
    min_cost = min(dp[(1 << n) - 1][i] + distances[i][0] for i in range(1, n))
    
    return min_cost
if __name__ == "__main__":
    distances = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    result = tsp_dp(distances)
    print("Minimum cost of visiting all cities:", result)
