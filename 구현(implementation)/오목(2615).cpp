#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstring>

using namespace std;

int n, m;
int board[20][20];
int vi[20][20];

bool w_win;
bool b_win;

int w_r, w_c;
int b_r, b_c;

void w_count(int sr, int sc, int c)
{
    int nr = sr;
    int nc = sc+1;
    int l_num = 1;

    vi[sr][sc] = 1;
    vi[nr][nc] = 1;
    while (nc < m && board[nr][nc] == c)
    {
        l_num += 1;
        nc += 1;
        vi[nr][nc] = 1;
    }

    if (l_num == 5)
    {
        if (c == 1) {
            b_win = true;
            b_r = sr;
            b_c = sc;
        }
        else if (c == 2) {
            w_win = true;
            w_r = sr;
            w_c = sc;
        }
    }
    return;
};

void h_count(int sr, int sc, int c)
{
    int nr = sr + 1;
    int nc = sc;
    int l_num = 1;

    vi[sr][sc] = 1;
    vi[nr][nc] = 1;
    while (nr < n && board[nr][nc] == c)
    {
        l_num += 1;
        nr += 1;
        vi[nr][nc] = 1;
    }

    if (l_num == 5)
    {
        if (c == 1) {
            b_win = true;
            b_r = sr;
            b_c = sc;
        }
        else if (c == 2) {
            w_win = true;
            w_r = sr;
            w_c = sc;
        }
    }
    return;
};

void rd_count(int sr, int sc, int c)
{
    int nr = sr + 1;
    int nc = sc + 1;
    int l_num = 1;

    vi[sr][sc] = 1;
    vi[nr][nc] = 1;
    while (nr < n && nc < m && board[nr][nc] == c)
    {
        l_num += 1;
        nr += 1;
        nc += 1;
        vi[nr][nc] = 1;
    }

    //cout <<sr << " " << sc <<  endl;
    //for (int r = 0; r < n; r++)
    //{
    //    for (int c = 0; c < m; c++)
    //    {
    //        cout << vi[r][c] << " ";
    //    }
    //    cout << endl;
    //}
    //cout << endl;
    if (l_num == 5)
    {
        if (c == 1) {
            b_win = true;
            b_r = sr;
            b_c = sc;
        }
        else if (c == 2) {
            w_win = true;
            w_r = sr;
            w_c = sc;
        }
    }
    return;
};

void ru_count(int sr, int sc, int c)
{
    int nr = sr - 1;
    int nc = sc + 1;
    int l_num = 1;

    vi[sr][sc] = 1;
    vi[nr][nc] = 1;
    while (nr > -1 && nc < m && board[nr][nc] == c)
    {
        l_num += 1;
        nr -= 1;
        nc += 1;
        vi[nr][nc] = 1;
    }

    if (l_num == 5)
    {
        if (c == 1) {
            b_win = true;
            b_r = sr;
            b_c = sc;
        }
        else if (c == 2) {
            w_win = true;
            w_r = sr;
            w_c = sc;
        }
    }
    return;
};

int main() {
    n = 19;
    m = 19;

    for (int r = 0; r < n; r++)
    {
        for (int c = 0; c < m; c++)
        {
            cin >> board[r][c];
        }
    }

    memset(vi, 0, sizeof(vi));
    for (int r = 0; r < n; r++)
    {
        for (int c = 0; c < m; c++)
        {
            if (vi[r][c] != 0) continue;
            if (board[r][c] != 1) continue;
            if (b_win == true) continue;

            w_count(r, c, 1);
        }
    }

    memset(vi, 0, sizeof(vi));
    for (int r = 0; r < n; r++)
    {
        for (int c = 0; c < m; c++)
        {
            if (vi[r][c] != 0) continue;
            if (board[r][c] != 1) continue;
            if (b_win == true) continue;

            h_count(r, c, 1);
        }
    }

    memset(vi, 0, sizeof(vi));
    for (int r = 0; r < n; r++)
    {
        for (int c = 0; c < m; c++)
        {
            if (vi[r][c] != 0) continue;
            if (board[r][c] != 1) continue;
            if (b_win == true) continue;

            rd_count(r, c, 1);
        }
    }

    memset(vi, 0, sizeof(vi));
    for (int r = n-1; r > 0; r--)
    {
        for (int c = 0; c < m; c++)
        {
            if (vi[r][c] != 0) continue;
            if (board[r][c] != 1) continue;
            if (b_win == true) continue;

            ru_count(r, c, 1);
        }
    }

    memset(vi, 0, sizeof(vi));
    for (int r = 0; r < n; r++)
    {
        for (int c = 0; c < m; c++)
        {
            if (vi[r][c] != 0) continue;
            if (board[r][c] != 2) continue;
            if (w_win == true) continue;

            w_count(r, c, 2);
        }
    }

    memset(vi, 0, sizeof(vi));
    for (int r = 0; r < n; r++)
    {
        for (int c = 0; c < m; c++)
        {
            if (vi[r][c] != 0) continue;
            if (board[r][c] != 2) continue;
            if (w_win == true) continue;

            h_count(r, c, 2);
        }
    }

    memset(vi, 0, sizeof(vi));
    for (int r = 0; r < n; r++)
    {
        for (int c = 0; c < m; c++)
        {
            if (vi[r][c] != 0) continue;
            if (board[r][c] != 2) continue;
            if (w_win == true) continue;

            rd_count(r, c, 2);
        }
    }

    memset(vi, 0, sizeof(vi));
    for (int r = n - 1; r > 0; r--)
    {
        for (int c = 0; c < m; c++)
        {
            if (vi[r][c] != 0) continue;
            if (board[r][c] != 2) continue;
            if (w_win == true) continue;

            ru_count(r, c, 2);
        }
    }

    b_r += 1;
    b_c += 1;

    w_r += 1;
    w_c += 1;

    if (b_win == true)
    {
        cout << 1 << endl;
        cout << b_r << " " << b_c << endl;
    }
    else if (w_win == true)
    {
        cout << 2 << endl;
        cout << w_r << " " << w_c << endl;
    }
    else {
        cout << 0 << endl;
    }
    return 0;
};
