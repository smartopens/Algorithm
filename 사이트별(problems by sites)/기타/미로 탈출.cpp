#include <string>
#include <vector>
#include <queue>

using namespace std;

int n, m;
int min_tm;
int sr, sc, lr, lc, er, ec;
bool can_escape;

int vi[102][102][2];

struct m_no
{
    int r;
    int c;
    int le_on;
};

int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };

void escape_mirror(vector<string> maps)
{
    queue <m_no> q;
    q.push({ sr,sc,0 });
    vi[sr][sc][0] = 1;

    while (!q.empty())
    {
        m_no qv = q.front();
        q.pop();

        int tr, tc;
        for (int di = 0; di < 4; di++)
        {
            tr = qv.r + dr[di];
            tc = qv.c + dc[di];

            if (0 > tr || n - 1 < tr || 0 > tc || m - 1 < tc) continue;
            if (maps[tr][tc] == 'X') continue;
            // 레버에 도착하는 경우
            if (tr == lr && tc == lc)
            {
                if (qv.le_on == 1) continue;
                if (vi[tr][tc][qv.le_on + 1] != 0) continue;

                vi[tr][tc][qv.le_on + 1] = vi[qv.r][qv.c][qv.le_on] + 1;
                q.push({ tr,tc,qv.le_on + 1 });

            }
            // 레버에 도착하지 않는 경우
            else
            {
                if (vi[tr][tc][qv.le_on] != 0) continue;
                // 레버를 당기고 출구에 도착하는 경우
                if (tr == er && tc == ec && qv.le_on == 1)
                {
                    can_escape = true;
                    min_tm = vi[qv.r][qv.c][qv.le_on];
                    return;
                }

                vi[tr][tc][qv.le_on] = vi[qv.r][qv.c][qv.le_on] + 1;
                q.push({ tr, tc, qv.le_on });

            }

        }
    }
}

int solution(vector<string> maps) {
    n = maps.size();
    m = maps[0].length();

    for (int r = 0; r < n; r++)
    {
        for (int c = 0; c < m; c++)
        {
            if (maps[r][c] == 'S')
            {
                sr = r;
                sc = c;
            }
            else if (maps[r][c] == 'L')
            {
                lr = r;
                lc = c;
            }
            else if (maps[r][c] == 'E')
            {
                er = r;
                ec = c;
            }
        }
    }

    can_escape = false;
    min_tm = 21e8;
    escape_mirror(maps);

    if (can_escape == false)
    {
        return -1;
    }
    else
    {
        return min_tm;
    }
}