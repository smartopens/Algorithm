#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;

ll max_w;
int n;

struct j_no
{
    int w;
    int co;
};

j_no jews[1000002];
ll j_dp[102][100002];

ll j_count(int a, ll now_w)
{

    if (a > n)
    {
        return 0;
    }

    if (j_dp[a][now_w] != 0)
    {
        return j_dp[a][now_w];
    }

    int to_jv, to_co;
    ll max_jew = 0;
    if (now_w >= jews[a].w)
    {
        max_jew = max(j_count(a + 1, now_w), j_count(a + 1, now_w - jews[a].w) + jews[a].co);
    }
    else
    {
        return j_count(a + 1, now_w);
    }

    return j_dp[a][now_w] = max_jew;
}

int main(int argc, char** argv)
{
    cin >> n >> max_w;
    int in_w, in_co;
    for (int i = 1; i < n + 1; i++)
    {
        cin >> in_w >> in_co;
        jews[i] = { in_w, in_co };
    }

    for (int r = 1; r < n + 1; r++)
    {
        for (int c = 0; c < max_w + 1; c++)
        {
            j_dp[r][c] = 0;
        }
    }

    ll answer = j_count(1, max_w);

    cout << answer << endl;
    return 0;
}