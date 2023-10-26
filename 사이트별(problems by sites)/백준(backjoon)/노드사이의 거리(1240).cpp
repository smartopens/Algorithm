#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int n, m;

struct g_no {
	int to;
	int co;
};

vector<g_no> gp[1002];
int vi[1002];

int v_dist;
vector<int> dists;

void dfs(int v, int ev, int co)
{
	if (v == ev)
	{
		v_dist = co;
		return;
	}

	int to_v;

	for (int s = 0; s < gp[v].size(); s++)
	{
		to_v = gp[v][s].to;

		if (vi[to_v] == 0)
		{
			vi[to_v] = 1;
			dfs(to_v, ev, co + gp[v][s].co);
		};
	}

}

int main()
{
	cin >> n >> m;
	
	int av, bv, co;
	for (int i = 0; i < n-1; i++)
	{
		cin >> av >> bv >> co;
		gp[av].push_back({ bv,co });
		gp[bv].push_back({ av,co });
	}

	for (int i = 0; i < m; i++)
	{
		cin >> av >> bv;
			
		v_dist = 0;
		memset(vi, 0, sizeof(vi));
		
		vi[av] = 1;
		dfs(av, bv, 0);
		
		dists.push_back(v_dist);
	}

	for (int i = 0; i < dists.size(); i++)
	{
		cout << dists[i] << "\n";
	}
	return 0;
}
