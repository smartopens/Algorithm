#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>

using namespace std;

int n;
int p_cost[1002][3];
int dp[1002][3];
int min_cost;

int dfs(int c_id, int n_c)
{

    if (dp[c_id][n_c] != -1)
    {
        return dp[c_id][n_c];
    }

    int r_cost = 10e8;
    int g_cost = 10e8;
    int b_cost = 10e8;

    if (n_c == 0)
    {
        g_cost = dfs(c_id - 1, 1);
        b_cost = dfs(c_id - 1, 2);
    }
    else if (n_c == 1)
    {
        r_cost = dfs(c_id - 1, 0);
        b_cost = dfs(c_id - 1, 2);
    }
    else if (n_c == 2)
    {
        g_cost = dfs(c_id - 1, 1);
        r_cost = dfs(c_id - 1, 0);
    }

    int min_c = min({ r_cost,g_cost ,b_cost });

    if (min_c == r_cost) {
        dp[c_id][n_c] = r_cost + p_cost[c_id][n_c];
    }
    else if (min_c == g_cost) {
        dp[c_id][n_c] = g_cost + p_cost[c_id][n_c];
    }
    else if (min_c == b_cost) {
        dp[c_id][n_c] = b_cost + p_cost[c_id][n_c];
    }
    return dp[c_id][n_c];
}
int main() {
    cin >> n;

    for (int r = 1; r < n + 1; r++)
    {
        for (int c = 0; c < 3; c++)
        {
            cin >> p_cost[r][c];
        }
    }

    for (int r = 0; r < n + 1; r++)
    {
        for (int c = 0; c < 3; c++)
        {
            dp[r][c] = -1;
        }
    }
    for (int r = 0; r < 3; r++)
    {
        dp[1][r] = p_cost[1][r];
    }

    min_cost = min({ dfs(n,0),dfs(n,1),dfs(n,2) });
    cout << min_cost << endl;
    return 0;
};
