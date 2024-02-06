#include <iostream>
#include <vector>

using namespace std;

int n, m;

vector<int> big_dl[100];
vector<int> small_dl[100];

int b_map[100][100];
int s_map[100][100];

int not_mn;

int main()
{
	cin >> n >> m;
	int da, db;
	for (int i = 0; i < m; i++)
	{
		cin >> da >> db;
		if (b_map[db][da] == 1) continue;

		big_dl[db].push_back(da);
		small_dl[da].push_back(db);
		b_map[db][da] = 1;
		s_map[da][db] = 1;
	}

	for (int dv = 1; dv < n + 1; dv++)
	{
		// 啊涵款 包拌 沥府
		int to_dl = 0;
		for (int s = 0; s < big_dl[dv].size(); s++)
		{
			to_dl = big_dl[dv][s];
			for (int k = 0; k < small_dl[dv].size(); k++)
			{
				if (s_map[to_dl][small_dl[dv][k]] == 1) continue;
				small_dl[to_dl].push_back(small_dl[dv][k]);

				s_map[to_dl][small_dl[dv][k]] = 1;
			}
		}

		// 公芭款 包拌 沥府
		for (int s = 0; s < small_dl[dv].size(); s++)
		{
			to_dl = small_dl[dv][s];
			for (int k = 0; k < big_dl[dv].size(); k++)
			{
				if (b_map[to_dl][big_dl[dv][k]] == 1) continue;
				big_dl[to_dl].push_back(big_dl[dv][k]);

				b_map[to_dl][big_dl[dv][k]] = 1;
				//bs_map[big_dl[dv][k]][to_dl] = 1;
			}
		}
	}

	not_mn = 0;
	int mid_cn = n / 2;
	for (int dv = 1; dv < n + 1; dv++)
	{
		if (big_dl[dv].size() > mid_cn || small_dl[dv].size() > mid_cn)
		{
			not_mn += 1;
		}
	}

	cout << not_mn << endl;
	return 0;
}