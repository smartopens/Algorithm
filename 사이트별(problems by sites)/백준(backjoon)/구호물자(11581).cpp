#include <iostream>
#include <vector>

using namespace std;

int n, m;

vector<int> r_gp[102];
int vi[102];

bool can_cycle;

bool s_deliver(int rv)
{
	int to_v;
	for (int s = 0; s < r_gp[rv].size(); s++)
	{
		to_v = r_gp[rv][s];
		if (to_v != n && vi[to_v] != 0)
		{
			can_cycle = true;
			return false;
		}

		if (vi[to_v] != 0) continue;

		vi[to_v] = 1;
		if (s_deliver(to_v) == false) continue;
		vi[to_v] = 0;
	}

	return true;
}

int main()
{
	cin >> n;
	int ra, rb;
	for (int rv = 0; rv < n - 1; rv++)
	{
		cin >> m;
		for (int s = 0; s < m; s++)
		{
			cin >> rb;
			r_gp[rv+1].push_back(rb);
		}
	}

	can_cycle = false;
	vi[1] = 1;
	s_deliver(1);

	if (can_cycle == false)
	{
		cout << "NO CYCLE\n";
	}
	else
	{
		cout << "CYCLE\n";
	}
	return 0;
}