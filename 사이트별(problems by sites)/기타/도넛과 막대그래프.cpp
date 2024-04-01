#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int n, m;

vector<int> gp[1000002];
int in_n[1000002];
int out_n[1000002];
int first_v[1000002];
int vi[1000002];

int sv;
int do_n;
int mak_n;
int e_n;

vector<int> solution(vector<vector<int>> edges) {
    // ��������, ����, ����, 8��
    m = edges.size();

    for (int s = 0; s < m; s++)
    {
        out_n[edges[s][0]] += 1;
        in_n[edges[s][1]] += 1;

        n = max({ n, edges[s][0], edges[s][1] });
    }

    mak_n = 0;
    e_n = 0;
    for (int gv = 1; gv < n + 1; gv++)
    {
        // ���� ���� ã��
        if (out_n[gv] >= 2 && in_n[gv] == 0)
        {
            sv = gv;
        }
        // ���� �׷���
        else if (out_n[gv] == 0)
        {
            mak_n += 1;
        }
        // 8�� �׷���
        else if (out_n[gv] == 2 && in_n[gv] >= 2)
        {
            e_n += 1;
        }
    }

    do_n = out_n[sv] - mak_n - e_n;

    vector<int> answer = {};
    answer = { sv, do_n, mak_n, e_n };
    return answer;
}