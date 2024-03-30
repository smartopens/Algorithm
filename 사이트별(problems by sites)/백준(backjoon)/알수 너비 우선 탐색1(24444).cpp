#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int n, m;
int r;

vector<int> b_gp[100002];
int vi[100002];

int v_ord[100002];
int now_ord;

void v_count()
{
	queue<int> q = {};
	q.push( r );
	
	vi[r] = 1;
	v_ord[r] = now_ord;
	now_ord += 1;

	while (!q.empty())
	{
		int qv = q.front();
		q.pop();

		int to_v;
		for (int s = 0; s < b_gp[qv].size(); s++)
		{
			to_v = b_gp[qv][s];

			if (vi[to_v] != 0) continue;

			vi[to_v] = 1;
			v_ord[to_v] = now_ord;
			now_ord += 1;
			q.push(to_v);
		}
	}
}

int main()
{
	cin >> n >> m >> r;
	int ga, gb;
	for (int i = 0; i < m; i++)
	{
		cin >> ga >> gb;
		b_gp[ga].push_back(gb);
		b_gp[gb].push_back(ga);
	}

	for (int gv = 1; gv < n+1; gv++)
	{
		sort(b_gp[gv].begin(), b_gp[gv].end());
	}

	now_ord = 1;
	v_count();

	for (int bv = 1; bv < n + 1; bv++)
	{
		cout << v_ord[bv] << "\n";
	}
	return 0;
}