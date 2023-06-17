#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstring>
#include <string>
#include <queue>

using namespace std;

int l, n, m;
char s_bd[30][30][30];
int vi[30][30][30];

int sl, sr, sc;
int el, er, ec;

struct p_no {
    int f;
    int r;
    int c;
};

int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };
int min_d;

void escape_sb()
{
    queue<p_no>q = {};
    q.push({ sl,sr,sc });
    
    vi[sl][sr][sc] = 1;
    while (!q.empty())
    {
        p_no now_n = q.front();
        q.pop();

        if (now_n.f == el && now_n.r == er && now_n.c == ec)
        {
            min_d = vi[now_n.f][now_n.r][now_n.c] - 1;
            return;
        }

        int nf, nr, nc;
        for (int i = 0; i < 4; i++)
        {
            nr = now_n.r + dr[i];
            nc = now_n.c + dc[i];
            
            if (0 > nr || n <= nr || 0 > nc || m <= nr) continue;
            if (vi[now_n.f][nr][nc] != 0) continue;
            if (s_bd[now_n.f][nr][nc] == '#') continue;

            vi[now_n.f][nr][nc] = vi[now_n.f][now_n.r][now_n.c] + 1;
            q.push({ now_n.f , nr, nc });
        }
        for (int i = -1; i < 2; i+=2)
        {
            nf = now_n.f+i;
            nr = now_n.r;
            nc = now_n.c;

            if (0 > nf || l <= nf) continue;
            if (vi[nf][nr][nc] != 0) continue;
            if (s_bd[nf][nr][nc] == '#') continue;

            vi[nf][nr][nc] = vi[now_n.f][nr][nc] + 1;
            q.push({ nf , nr, nc });
        }
    }
    return;
}

int main() {
    while (true)
    {
        cin >> l >> n >> m;
        if (l == 0 && n == 0 && m == 0) break;

        memset(vi, 0, sizeof(vi));
        min_d = -1;
        string in_e = "";

        for (int i = 0; i < l; i++)
        {
            for (int r = 0; r < n; r++)
            {
                for (int c = 0; c < m; c++)
                {
                    cin >> s_bd[i][r][c];
                    
                    if (s_bd[i][r][c] == 'S') {
                        sl = i;
                        sr = r;
                        sc = c;
                    }
                    else if (s_bd[i][r][c] == 'E') {
                        el = i;
                        er = r;
                        ec = c;
                    }
                }
            }
            getline(cin, in_e);
        }

        escape_sb();
        if (min_d == -1) {
            cout << "Trapped!" << endl;
        }
        else {
            cout << "Escaped in " << min_d << " minute(s)." << endl;
        }
    }
    return 0;
};
