#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int t;
int n, m;

vector<int> c_gp[1002];
int vi[1002];
int c_reco[1002];

bool num_ok;
bool to_can_match;
void c_assign(int cv, int cn)
{
	// 다른색으로 연동하기
	int to_v;
	for (int s = 0; s < c_gp[cv].size(); s++)
	{
		to_v = c_gp[cv][s];
		if (c_reco[cv] == c_reco[to_v])
		{
			to_can_match = false;
		}
		if (vi[to_v] != 0) continue;

		if (c_reco[cv] == 5)
		{
			c_reco[to_v] = 2;
			vi[to_v] = 1;

			c_assign(to_v,cn+1);
		}
		else if (c_reco[cv] == 2)
		{
			c_reco[to_v] = 5;
			vi[to_v] = 1;

			c_assign(to_v,cn+1);
		}
	}
}

int main()
{
	cin >> t;
	int in_a, in_b;
	for (int tc = 0; tc < t; tc++)
	{
		cin >> n >> m;
		for (int s = 1; s < n+1; s++)
		{
			c_gp[s].clear();
			vi[s] = 0;
			c_reco[s] = 0;
		}

		for (int i = 0; i < m; i++)
		{
			cin >> in_a >> in_b;
			c_gp[in_a].push_back(in_b);
			c_gp[in_b].push_back(in_a);
		}

		to_can_match = true;
		for (int cv = 1; cv < n + 1; cv++)
		{
			if (vi[cv] != 0) continue;
			vi[cv] = 1;
			c_reco[cv] = 5;
			c_assign(cv, 1);
		}

		// 두가지 색상으로 가능한지 보기
		/*bool can_c_match = true;
		int now_c;
		for (int cv = 1; cv < n + 1; cv++)
		{
			now_c = c_reco[cv];
			for (int s = 0; s < c_gp[cv].size(); s++)
			{
				if (now_c == c_gp[cv][s])
				{
					can_c_match = false;
					break;
				}
			}
			if (can_c_match == false) break;
		}*/

		if (to_can_match == false)
		{
			cout << "impossible" << "\n";
		}
		else
		{
			cout << "possible" << "\n";
		}
	}

	return 0;
}