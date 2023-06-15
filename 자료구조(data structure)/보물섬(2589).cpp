#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstring>
#include <queue>

using namespace std;

int n, m;
int t_dist;

char t_land[52][52];

struct q_no {
    int r;
    int c;
};

int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };

void di_count(int sr, int sc)
{
    queue<q_no> q = {};
    q.push({ sr,sc });
    
    int vi[52][52] = {};
    vi[sr][sc] = 1;

    while(!q.empty())
    {
        q_no now_n = q.front();
        q.pop();

        if (t_dist < vi[now_n.r][now_n.c] - 1)
        {
            t_dist = vi[now_n.r][now_n.c] - 1;
        }

        int nr, nc;
        for (int i = 0; i < 4; i++)
        {
            nr = now_n.r + dr[i];
            nc = now_n.c + dc[i];

            if (0 > nr || n <= nr || 0 > nc || m <= nc) continue;
            if (t_land[nr][nc] != 'L') continue;
            if (vi[nr][nc] != 0) continue;

            q.push({ nr,nc });
            vi[nr][nc] = vi[now_n.r][now_n.c] + 1;
        }

    }
    return;
};

int main() {
    cin >> n >> m;

    for (int r = 0; r < n; r++)
    {
        for (int c = 0; c < m; c++)
        {
            cin >> t_land[r][c];
        }
    }

    for (int sr = 0; sr < n; sr++)
    {
        for (int sc = 0; sc < m; sc++)
        {
            if (t_land[sr][sc] != 'L') continue;
            di_count(sr, sc);
        }
    }

    cout << t_dist << endl;
    return 0;
};
