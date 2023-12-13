#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 각 노드의 방문 순서를 출력하기
// s1, s2, s3, ... (3,2,2), (2,4,5), (2,1,1)

int n, m, r;
vector<int> gp[100002];

int gp_order[100002];
int vi[100002];
int on;

void o_count(int gv)
{
	on += 1;
	gp_order[gv] = on;
	vi[gv] = 1;

	int to_v;
	for (int s = 0; s < gp[gv].size(); s++)
	{
		to_v = gp[gv][s];
		if (vi[to_v] != 0) continue;
		
		o_count(to_v);
	}
}

int main()
{
	cin >> n >> m >> r;
	int in_a, in_b;
	for (int i = 0; i < m; i++)
	{
		cin >> in_a >> in_b;
		gp[in_a].push_back(in_b);
		gp[in_b].push_back(in_a);
	}
	
	for (int s = 1; s < n + 1; s++)
	{
		sort(gp[s].begin(), gp[s].end());
	}

	on = 0;
	o_count(r);

	for (int v = 1; v < n + 1; v++)
	{
		cout << gp_order[v] << "\n";
	}

	return 0;
}