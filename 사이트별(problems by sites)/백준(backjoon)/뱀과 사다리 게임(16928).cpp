#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <queue>

using namespace std;

int n, m;

struct bo_no {
    int id;
    int to_n;
};

bo_no board[10][10];

int vi[10][10];

struct q_no {
    int r;
    int c;
};

int dr, dc;

int min_m;

void g_count()
{
    vi[0][0] = 1;

    queue<q_no> q = {};
    q.push({0,0});

    while (!q.empty())
    {
        q_no now = q.front();
        q.pop();

        int nr, nc, n_num;

        if (now.r == 9 && now.c == 9)
        {
            min_m = vi[now.r][now.c] - 1;
            return;
        }

        for (int i = 1; i < 7; i++)
        {
            n_num = now.r * 10 + now.c + i;
            nr = n_num / 10;
            nc = n_num % 10;

            if (n_num >= 100) continue;

            int nr2;
            int nc2;
            if (board[nr][nc].id != 0)
            {
                nr2 = board[nr][nc].to_n / 10;
                nc2 = board[nr][nc].to_n % 10;

                if (vi[nr2][nc2]!= 0) continue;
                vi[nr2][nc2] = vi[now.r][now.c] + 1;
                q.push({ nr2, nc2 });

            }
            else {
                if (vi[nr][nc] != 0) continue;
                vi[nr][nc] = vi[now.r][now.c] + 1;
                q.push({ nr, nc });
            }
        }
    }
    return;
}

int main() {
    cin >> n >> m;

    for (int i = 0; i < n; i++)
    {
        int x, y;
        cin >> x >> y;
        x -= 1;
        y -= 1;

        board[x / 10][x % 10] = { 1,y };
    }

    for (int i = 0; i < m; i++)
    {
        int x, y;
        cin >> x >> y;
        x -= 1;
        y -= 1;

        board[x / 10][x % 10] = { 1,y };
    }

    dr = 0;
    dc = 0;
    g_count();
    cout << min_m << endl;

    return 0;
};
