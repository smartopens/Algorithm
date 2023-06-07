#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstring>
#include <queue>

using namespace std;

int n, m;
char ti_forest[52][52];
int g_vi[52][52];
int w_vi[52][52];

int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };

int sr, sc;
int er, ec;
int min_t = 21e8;

struct pa {
    int r;
    int c;
};

queue<pa> go_q;
queue<pa> wa_q;

void go_run()
{
    go_q.push({ sr,sc });
    g_vi[sr][sc] = 1;
    
    while (!go_q.empty())
    {
        int gq_s = go_q.size();

        queue<pa> wa_tmp = {};

        while (!wa_q.empty())
        {
            pa w_no = wa_q.front();
            wa_q.pop();

            int w_nr, w_nc;

            for (int i = 0; i < 4; i++)
            {
                w_nr = w_no.r + dr[i];
                w_nc = w_no.c + dc[i];

                if (0 > w_nr || n <= w_nr || 0 > w_nc || m <= w_nc) continue;
                if (ti_forest[w_nr][w_nc] == 'X') continue;
                if (w_vi[w_nr][w_nc] != 0) continue;
                if (w_nr == er && w_nc == ec) continue;

                ti_forest[w_nr][w_nc] = '*';
                w_vi[w_nr][w_nc] = 1;
                wa_tmp.push({ w_nr, w_nc });
            }
        }

        while (!wa_tmp.empty())
        {
            wa_q.push({ wa_tmp.front() });
            wa_tmp.pop();
        }

        for (int s = 0; s < gq_s; s++)
        {
            pa go_no = go_q.front();
            go_q.pop();

            int nr, nc;
            for (int i = 0; i < 4; i++)
            {
                nr = go_no.r + dr[i];
                nc = go_no.c + dc[i];

                if (0 > nr || n <= nr || 0 > nc || m <= nc) continue;
                if (ti_forest[nr][nc] == 'X') continue;
                if (ti_forest[nr][nc] == '*') continue;
                if (g_vi[nr][nc] != 0) continue;

                go_q.push({ nr,nc });
                g_vi[nr][nc] = g_vi[go_no.r][go_no.c] + 1;

                if (nr == er && nc == ec) {
                    min_t = g_vi[nr][nc] - 1;
                    return;
                }

            }
        }
    }
};

int main() {
    cin >> n >> m;

    for (int r = 0; r < n; r++)
    {
        for (int c = 0; c < m; c++)
        {
            char c_now;
            cin >> c_now;

            if (c_now == 'D')
            {
                er = r;
                ec = c;
            }
            else if (c_now == 'S')
            {
                sr = r;
                sc = c;
            }
            else if (c_now == '*')
            {
                wa_q.push({ r,c });
                w_vi[r][c] = 1;
            }
            ti_forest[r][c] = c_now;
        }
    }

    go_run();

    if (min_t == 21e8) {
        cout << "KAKTUS" << endl;
    }
    else {
        cout << min_t << endl;
    }
    return 0;
};
