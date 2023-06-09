#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int n, e;
int u, v;

bool one_go = true;
bool two_go = true;

long long min_w1;
long long min_w2;
long long min_w;

struct q_no {
    int cost;
    int v;

    bool operator < (q_no now)const
    {
        if (cost > now.cost)
        {
            return true;
        }
        if (cost < now.cost)
        {
            return false;
        }
        return false;
    }
};

vector<q_no> b_gp[802];

int dist[802];

void di_init()
{
    for (int i = 0; i < n+1; i++)
    {
            dist[i] = 21e8;
    }
    return;
}

void mw_count(int sv, int ev)
{
    priority_queue<q_no> pq = {};
    pq.push({ 0,sv });
    dist[sv] = 0;

    while (!pq.empty())
    {
        q_no now_n = pq.top();
        pq.pop();

        int n_v, n_cost;

        if (dist[now_n.v] < now_n.cost) continue;

        for (int s = 0; s < b_gp[now_n.v].size(); s++)
        {
            q_no to_n = b_gp[now_n.v][s];

            n_cost = dist[now_n.v] + to_n.cost;
            if (dist[to_n.v] <= n_cost) continue;

            dist[to_n.v] = n_cost;
            pq.push({ n_cost, to_n.v });
        }
    }
    return;
}

int main() {
    cin >> n >> e;

    for (int i = 0; i < e; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;

        b_gp[a].push_back({ c,b });
        b_gp[b].push_back({ c,a });
    }

    cin >> u >> v;
    // 경로1
    di_init();
    mw_count(1, u);
    min_w1 += dist[u];

    di_init();
    mw_count(u, v);
    min_w1 += dist[v];

    di_init();
    mw_count(v, n);
    min_w1 += dist[n];

    // 경로2
    di_init();
    mw_count(1, v);
    min_w2 += dist[v];

    di_init();
    mw_count(v, u);
    min_w2 += dist[u];

    di_init();
    mw_count(u, n);
    min_w2 += dist[n];

    min_w = min(min_w1, min_w2);

    if (min_w1 >= 21e8 && min_w2 >= 21e8)
    {
        cout << -1 << endl;
    }
    else {
        cout << min_w << endl;
    }

    return 0;
};
