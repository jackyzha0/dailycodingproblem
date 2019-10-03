s1 = "yeet"
s2 = "skrt"

# min number of adds, deletes, subs between the two strings
def editDist(s1, s2):
    dp = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
    for i in range(len(dp[0])):
        dp[0][i] = i
    for j in range(len(dp)):
        dp[j][0] = j

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            # print(dp[i][j])
            # print(s1[j-1], s2[i-1])
            if s1[j-1] == s2[i-1]:
                dp[i][j] = min(dp[i-1][j-1], dp[i][j-1] + 1, dp[i-1][j] + 1)
            else:
                dp[i][j] = min(dp[i-1][j-1] + 1, dp[i][j-1] + 1, dp[i-1][j] + 1)

    return dp[-1][-1]

print(editDist(s1, s2))
