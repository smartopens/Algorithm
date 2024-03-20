#include <iostream>

using namespace std;

int n, m;
int up_map[102][102];
int down_map[102][102];

int tar_tn[102];

int main()
{
	cin >> n >> m;
	int w1, w2;
	for (int i = 0; i < m; i++)
	{
		cin >> w1 >> w2;
		up_map[w2][w1] = 1;
		down_map[w1][w2] = 1;
	}

	// 무거운 관계 정립
	for (int k = 1; k < n + 1; k++)
	{
		for (int s = 1; s < n + 1; s++)
		{
			for (int e = 1; e < n + 1; e++)
			{
				if (up_map[s][k] != 0 && up_map[k][e] != 0)
				{
					up_map[s][e] = 1;
				}
			}
		}
	}

	// 가벼운 관계 정립
	for (int k = 1; k < n + 1; k++)
	{
		for (int s = 1; s < n + 1; s++)
		{
			for (int e = 1; e < n + 1; e++)
			{
				if (down_map[s][k] != 0 && down_map[k][e] != 0)
				{
					down_map[s][e] = 1;
				}
			}
		}
	}

	int all_tn = 0;
	for (int tv = 1; tv < n + 1; tv++)
	{
		all_tn = n-1;
		for (int tv2 = 1; tv2 < n + 1; tv2++)
		{
			if (tv == tv2) continue;
			if (up_map[tv][tv2] == 1 || down_map[tv][tv2] == 1)
			{
				all_tn -= 1;
			}
		}
		tar_tn[tv] = all_tn;
	}

	for (int tv = 1; tv < n + 1; tv++)
	{
		cout << tar_tn[tv] << endl;
	}
	return 0;
}