#include <iostream>

using namespace std;

int n, m;
int pa[500002];

int Find(int nv)
{
	if (pa[nv] == nv)
	{
		return pa[nv];
	}

	return pa[nv] = Find(pa[nv]);
}

void Union(int na, int nb)
{
	int p_na = Find(na);
	int p_nb = Find(nb);

	if (p_na == p_nb) return;

	pa[p_nb] = p_na;
}

int main()
{
	cin >> n >> m;
	int na, nb;
	bool cycle_on = false;
	for (int s = 0; s < n; s++)
	{
		pa[s] = s;
	}

	int c_tn = 0;
	for (int tv = 0; tv < m; tv++)
	{
		cin >> na >> nb;
		
		if (cycle_on == true) continue;

		if (Find(na) != Find(nb))
		{
			Union(na, nb);
		}
		else
		{
			cycle_on = true;
			c_tn = tv + 1;
		}
	}

	if (cycle_on == false)
	{
		cout << 0 << "\n";
	}
	else
	{
		cout << c_tn << "\n";
	}
	return 0;
}