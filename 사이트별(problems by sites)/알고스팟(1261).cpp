#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

int n, m;
int board[102][102];
int vi[102][102];
int dp[102][102];

int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };

struct p_no {
    int cost;
    int r;
    int c;

    bool operator < (p_no now) const {
        if (cost > now.cost) {
            return true;
        }
        if (cost < now.cost) {
            return false;
        }
        return false;
    }
};

int min_wb = 21e8;

void ag_run()
{
    priority_queue<p_no> pq = {};
    pq.push({ 0,1,1 });
    dp[1][1] = 0;

    while (!pq.empty())
    {
        p_no now = pq.top();
        pq.pop();

        int nr, nc, n_cost;
        
        if (dp[now.r][now.c] < now.cost) continue;

        for (int i = 0; i < 4; i++)
        {
            nr = now.r + dr[i];
            nc = now.c + dc[i];

            if (1 > nr || n < nr || 1 > nc || m < nc) continue;

            n_cost = now.cost + board[nr][nc];
            if (dp[nr][nc] <= n_cost) continue;
            dp[nr][nc] = n_cost;
            pq.push({ n_cost , nr, nc });
        }
    }

    return;
};

int main() {
    cin >> m >> n;

    for (int r = 1; r < n+1; r++)
    {
        for (int c = 1; c < m+1; c++)
        {
            char tmp;
            cin >> tmp;
            board[r][c] = (int)(tmp -'0');
        }
    }

    for (int r = 1; r < n + 1; r++)
    {
        for (int c = 1; c < m + 1; c++)
        {
            dp[r][c] = 21e8;
        }
    }

    ag_run();

    min_wb = dp[n][m];
    cout << min_wb << endl;
    return 0;
};
