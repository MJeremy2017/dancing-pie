def dice_throw(target):
    # dp[i][j]: the last time is i given target j
    dp = [[0 for _ in range(target+1)] for _ in range(7)]

    ans = 0
    for i in range(1, 7):
        for j in range(target):
            if j == 0:
                dp[i][j] = 0
            elif j == i:
                dp[i][j] = 1
            else:
                for k in range(1, 7):
                    dp[i][j] += dp[k][j-i]

    for i in range(1, 7):
        ans += dp[i][target]
    return ans
