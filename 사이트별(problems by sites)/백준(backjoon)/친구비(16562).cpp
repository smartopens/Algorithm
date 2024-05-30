#include <iostream>

using namespace std;

int n, m;
int k;

int pa[10002];
int g_co[10002];
int g_vi[10002];

int Find(int fv)
{
	if (fv == pa[fv])
	{
		return fv;
	}
	
	return pa[fv] = Find(pa[fv]);
}

void Union(int fv1, int fv2)
{
	int pv1 = Find(fv1);
	int pv2 = Find(fv2);

	if (pv1 == pv2)
	{
		return;
	}

	pa[pv2] = pv1;
	g_co[pv1] = min(g_co[pv1], g_co[pv2]);
}

int main()
{
	cin >> n >> m;
	cin >> k;

	for (int fv = 1; fv < n + 1; fv++)
	{
		cin >> g_co[fv];
	}

	for (int s = 1; s < n + 1; s++)
	{
		pa[s] = s;
	}

	int fa, fb;
	for (int s=0; s<m; s++)
	{
		cin >> fa >> fb;
		
		if (Find(fa) != Find(fb))
		{
			Union(fa, fb);
		}
	}

	int co_sn = 0;
	int p_gv;
	for (int gv = 1; gv < n + 1; gv++)
	{
		p_gv = Find(gv);
		if (g_vi[p_gv] != 0) continue;

		g_vi[p_gv] = 1;
		co_sn += g_co[p_gv];
	}

	if (co_sn > k)
	{
		cout << "Oh no" << "\n";
	}
	else
	{
		cout << co_sn << "\n";
	}
	return 0;
}