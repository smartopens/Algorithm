#define _CRT_SECURE_NO_WARNINGS

#include <iostream>

using namespace std;

int n, m;
char ground[252][252];
int vi[252][252];

int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };

int st_num;
int wt_num;

int s_num;
int w_num;

void sw_battle(int r, int c)
{
    if (ground[r][c] == 'o') {
        s_num += 1;
    }
    else if (ground[r][c] == 'v') {
        w_num += 1;
    }

    vi[r][c] = 1;

    int nr = 0;
    int nc = 0;
    for (int i = 0; i < 4; i++) {
        nr = r + dr[i];
        nc = c + dc[i];

        if (0 > nr || n - 1 < nr || 0 > nc || m - 1 < nc) continue;
        if (ground[nr][nc] == '#') continue;
        if (vi[nr][nc] != 0) continue;
        sw_battle(nr, nc);
    }
};

void run_check(int r, int c)
{
    vi[r][c] = 1;
    int nr = 0;
    int nc = 0;
    for (int i = 0; i < 4; i++) {
        nr = r + dr[i];
        nc = c + dc[i];

        if (0 > nr || n - 1 < nr || 0 > nc || m - 1 < nc) continue;
        if (ground[nr][nc] == '#') continue;
        if (vi[nr][nc] != 0) continue;
        run_check(nr, nc);
    }
}

int main() {
    cin >> n >> m;
    
    for (int r = 0; r < n; r++)
    {
        for (int c = 0; c < m; c++)
        {
            cin >> ground[r][c];
            if (ground[r][c] == '#') {
                vi[r][c] = 1;
            }
        }
    }

    for (int r = 0; r < n; r++)
    {
        if (vi[r][0] == 1 || ground[r][0] == '#') continue;
        run_check(r, 0);

        if (vi[r][m-1] == 1 || ground[r][m-1] == '#') continue;
        run_check(r, m-1);
    }

    for (int c = 0; c < m; c++)
    {
        if (vi[0][c] == 1 || ground[0][c] == '#') continue;
        run_check(0, c);

        if (vi[m-1][c] == 1 || ground[m-1][c] == '#') continue;
        run_check(m - 1,c);
    }

    for (int r = 0; r < n; r++)
    {
        for (int c = 0; c < m; c++)
        {
            if (vi[r][c] != 0) continue;
            if (ground[r][c] == '#') continue;

            s_num = 0;
            w_num = 0;
            sw_battle(r,c);

            if (w_num >= s_num) {
                wt_num += w_num;
            }
            else {
                st_num += s_num;
            }
        }
    }

    cout << st_num << " " << wt_num << endl;
    return 0;
};
