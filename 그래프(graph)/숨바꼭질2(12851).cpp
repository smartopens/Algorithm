#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <queue>

using namespace std;

int n, k;
int min_t = 21e8;
int c_num;

int vi[200002][20];

struct q_no {
    int v;
    int jn;
};

void b_find(int sv)
{
    queue<q_no> q = {};
    q.push({ sv,0 });

    vi[sv][0] = 1;

    while (!q.empty())
    {
        q_no now_n = q.front();
        q.pop();

        int to_v, jn;
        jn = now_n.jn;

        if (now_n.v == k)
        {
            if (min_t > vi[now_n.v][jn] - 1)
            {
                min_t = vi[now_n.v][jn] - 1;
                c_num = 1;
            }
            else if (min_t == vi[now_n.v][jn] - 1)
            {
                c_num += 1;
            }
            continue;
        }

        if (vi[now_n.v][jn] - 1 >= min_t)
        {
            continue;
        }

        to_v = now_n.v * 2;

        if (to_v > 200000 || jn+1 > 20) continue;
        if (vi[to_v][jn + 1] != 0 && vi[to_v][jn+1] < vi[now_n.v][jn]+1) continue;

        q.push({ to_v,jn + 1 });
        vi[to_v][jn + 1] = vi[now_n.v][jn] + 1;

        for (int di = -1; di < 2; di += 2)
        {
            to_v = now_n.v + di;

            if (to_v < 0 || to_v > 200000 || jn+1 > 20) continue;
            if (vi[to_v][jn] != 0 && vi[to_v][jn] < vi[now_n.v][jn]+1) continue;

            q.push({ to_v,jn  });
            vi[to_v][jn] = vi[now_n.v][jn] + 1;
        }

    }
    return;
}

int main() {
    cin >> n >> k;

    /*for (int i = 0; i < 200002; i++)
    {
        for (int j = 0; j < 20; j++)
        {
            vi[i][j] = 21e8;
        }
    }*/
    
    b_find(n);
    cout << min_t << endl;
    cout << c_num << endl;
    return 0;
};
