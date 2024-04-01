#include<iostream>
#include <vector>
#include <queue>
#include <set>

using namespace std;

int n, t;
int t_sys[102][102][4];
int vi[102][102][4][4];

int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };

struct d_no
{
    int di;
    int pre_di;
};

// 상 우 하 좌
vector<d_no> di_info[12]
=
{
    {{0,1},{1,1},{2,1},},
    {{3,0},{0,0},{1,0},},
    {{0,3},{3,3},{2,3},},
    {{3,2},{2,2},{1,2},},
    {{0,1},{1,1}},
    {{3,0},{0,0}},
    {{3,3},{2,3}},
    {{2,2},{1,2}},
    {{1,1},{2,1}},
    {{0,0},{1,0}},
    {{0,3},{3,3}},
    {{3,2},{2,2}},
};

struct q_no
{
    int r;
    int c;
    int t;
    int di;
};

int tn;
set<pair<int, int>> tn_set;


void c_move()
{
    queue<q_no> q;
    q.push({ 0,0,0,0 });
    vi[0][0][0][0] = 1;

    tn_set.insert(make_pair(0, 0));

    int now_di, now_t, r, c;
    while (!q.empty())
    {
        q_no cv = q.front();
        q.pop();

        now_di = cv.di;
        now_t = cv.t;

        int d_t = t_sys[cv.r][cv.c][now_t % 4];
        int tr, tc;

        if (di_info[d_t][0].pre_di != now_di) continue;
        for (int s = 0; s < di_info[d_t].size(); s++)
        {
            tr = cv.r + dr[di_info[d_t][s].di];
            tc = cv.c + dc[di_info[d_t][s].di];

            if (0 > tr || n - 1 < tr || 0 > tc || n - 1 < tc) continue;
            if (vi[tr][tc][now_t % 4][di_info[d_t][s].di] != 0) continue;

            if (now_t + 1 <= t)
            {
                vi[tr][tc][now_t  % 4][di_info[d_t][s].di] = 1;
                tn += 1;
                tn_set.insert(make_pair(tr, tc));
                q.push({ tr,tc,now_t + 1, di_info[d_t][s].di });
            }
        }
    }

}

int main(int argc, char** argv)
{
    // 교통 시스템 정보 입력
    cin >> n >> t;
    int in_di;
    for (int r = 0; r < n; r++)
    {
        for (int c = 0; c < n; c++)
        {
            for (int di = 0; di < 4; di++)
            {
                cin >> in_di;
                t_sys[r][c][di] = in_di - 1;
            }
        }
    }

    int now_t = 0;
    tn = 0;
    c_move();

    cout << tn_set.size() << endl;
    return 0;
}