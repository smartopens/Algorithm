#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

int n, m;
vector<string> board;
int vi[102][102];

int sr, sc;
int er, ec;

int to_dr, to_dc;

int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };

int min_mn;

struct re_no
{
    int r;
    int c;
};

void move(int r, int c, int di)
{
    vector<int> to = { 0,0 };
    int tr, tc;
    tr = r;
    tc = c;
    while (true)
    {
        // 밖에 나가는 경우
        if (0 > tr + dr[di] || n - 1 < tr + dr[di] || 0 > tc + dc[di] || m - 1 < tc + dc[di]) break;

        // 장애물 만나는 경우
        if (board[tr + dr[di]][tc + dc[di]] == 'D') break;

        tr += dr[di];
        tc += dc[di];
    }

    to[0] = tr;
    to[1] = tc;

    if (0 > tr + dr[di] || n - 1 < tr + dr[di] || 0 > tc + dc[di] || m - 1 > tc + dc[di])
    {
        tr = tr - dr[di];
        tc = tc - dc[di];
    }

    to_dr = tr;
    to_dc = tc;

    return;
}

// 로봇 이동하기
void ro_move()
{
    queue<re_no> q;
    q.push({ sr,sc });

    vi[sr][sc] = 1;

    while (!q.empty())
    {
        re_no qv = q.front();
        q.pop();

        vector<int> to_mv = { 0,0 };
        int tr, tc;

        to_dr = 0;
        to_dc = 0;
        for (int di = 0; di < 4; di++)
        {
            move(qv.r, qv.c, di);
            tr = to_dr;
            tc = to_dc;

            if (vi[tr][tc] != 0) continue;

            vi[tr][tc] = vi[qv.r][qv.c] + 1;

            if (tr == er && tc == ec)
            {
                min_mn = vi[tr][tc] - 1;
                return;
            }
            q.push({ tr,tc });
        }
    }

}

int main() {
    vector<string> board_back = { "...D..R", ".D.G...", "....D.D", "D....D.", "..D...." };
    board = board_back;
    n = board.size();
    m = board[0].length();

    for (int r = 0; r < n; r++)
    {
        for (int c = 0; c < m; c++)
        {
            if (board[r][c] == 'R')
            {
                sr = r;
                sc = c;
            }
            else if (board[r][c] == 'G')
            {
                er = r;
                ec = c;
            }
        }
    }

    min_mn = 21e8;
    cout << n << " " << m << endl;
    //ro_move();

    if (min_mn == 21e8)
    {
        cout << -1;
    }
    else
    {
        cout << min_mn;
    }

    return 0;
}