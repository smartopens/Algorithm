#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>

using namespace std;

int n;
int nums[1002];
int dp[1002];

int dfs(int now, int now_n)
{
    if (now < 1)
    {
        return 0;
    }

    if (dp[now] != -1)
    {
        return dp[now];
    }

    dp[now] = 0;

    for (int i = now-1; i > 0; i--)
    {
        if (nums[i] < now_n)
        {
            dp[now] = max(dp[now], dfs(i, nums[i]) + nums[i]);
        }
    }

    return dp[now];
};

int main() {
    cin >> n;

    for (int i = 1; i < n+1; i++)
    {
        cin >> nums[i];
    }

    for (int i = 0; i < n+2; i++)
    {
        dp[i] = -1;
    }

    int o_sum = dfs(n+1,21e8);

    cout << o_sum << endl;
    return 0;
}
