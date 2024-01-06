#include <iostream>
#include <vector>
#include <cstring>
#include <queue>

using namespace std;

int n, m;

vector<int> f_gp[2002];
int f_pa[2002];
int pa_num[2002];
int vi[2002];

bool ps = false;
int max_pn;
int now_pn;

bool f_count(int pv, int pn, int a)
{
	if (a >= 4)
	{
		return true;
	}

	int to_v;
	for (int s = 0; s < f_gp[pv].size(); s++)
	{
		to_v = f_gp[pv][s];

		if (vi[to_v] != 0) continue;

		now_pn += 1;
		vi[to_v] = 1;

		if (f_count(to_v, pn + 1, a + 1))
		{
			return true;
		}
		vi[to_v] = 0;
	}

	return false;
}

int main()
{
	cin >> n >> m;
	for (int pv = 1; pv < n + 1; pv++)
	{
		f_pa[pv] = pv;
	}

	int fa, fb;
	for (int i = 0; i < m; i++)
	{
		cin >> fa >> fb;
		//Union(fa+1, fb+1);
		f_gp[fa+1].push_back(fb+1);
		f_gp[fb+1].push_back(fa+1);
	}

	max_pn = 0;
	for (int pv = 1; pv < n + 1; pv++)
	{
		//memset(vi, 0, sizeof(vi));
		vi[pv] = 1;
		if (f_count(pv, 1, 0) == true) {
			ps = true;
			break;
		}
		vi[pv] = 0;
	}

	if (ps == true)
	{
		cout << 1 << endl;
	}
	else if (ps == false)
	{
		cout << 0 << endl;
	}
	return 0;
}