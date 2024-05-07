#include <iostream>
#include <vector>
#include <queue>

using namespace std;

typedef long long ll;

int n, m;

int c_sight[100002];

struct r_no
{
	int to;
	ll co;

	bool operator < (r_no now) const
	{
		if (co > now.co)
		{
			return true;
		}
		if (co < now.co)
		{
			return false;
		}
		return false;
	}
};

vector<r_no> r_gp[100002];

ll dists[100002];

void back_start()
{
	priority_queue<r_no> pq;
	pq.push({ 0,0 });

	for (int pv = 0; pv < n; pv++)
	{
		dists[pv] = 10e9;
	}
	dists[0] = 0;
	while (!pq.empty())
	{
		r_no now_p = pq.top();
		pq.pop();

		if (dists[now_p.to] < now_p.co) continue;

		int to_v;
		ll to_co;
		for (int s = 0; s < r_gp[now_p.to].size(); s++)
		{
			to_v = r_gp[now_p.to][s].to;
			to_co = dists[now_p.to] + r_gp[now_p.to][s].co;

			if (to_v != n-1 && c_sight[to_v] != 0) continue;
			if (dists[to_v] <= to_co) continue;

			dists[to_v] = to_co;
			pq.push({ to_v,to_co });
		}
	}
}

int main()
{
	cin >> n >> m;
	for (int i = 0; i < n; i++)
	{
		cin >> c_sight[i];
	}

	int in_a, in_b, in_t;
	for (int i = 0; i < m; i++)
	{
		cin >> in_a >> in_b >> in_t;
		r_gp[in_a].push_back({ in_b, in_t });
		r_gp[in_b].push_back({ in_a, in_t });
	}

	back_start();

	if (dists[n - 1] == 10e9)
	{
		cout << -1 << endl;
	}
	else
	{
		cout << dists[n - 1] << endl;
	}

	return 0;
}