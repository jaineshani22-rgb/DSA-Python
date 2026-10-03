class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        rows,cols=len(dungeon),len(dungeon[0])

        dp=[[float('inf')]*(cols+1)for _ in range(rows+1)]

        dp[rows][cols-1]=1
        dp[rows-1][cols]=1

        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                min_health_after=min(dp[i+1][j],dp[i][j+1])
                dp[i][j]=max(1,min_health_after-dungeon[i][j])
        return dp[0][0]        