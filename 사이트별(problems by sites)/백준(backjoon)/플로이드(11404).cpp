#include <iostream>

using namespace std;

int n, m;
int c_map[102][102];

int main()
{
	cin >> n >> m;
	int sc, ec, co;
	for (int r = 1; r < n + 1; r++)
	{
		for (int c = 1; c < n + 1; c++)
		{
			if (r == c) continue;
			c_map[r][c] = 21e8;
		}
	}

	for (int i = 0; i < m; i++)
	{
		cin >> sc >> ec >> co;
		if (co < c_map[sc][ec])
		{
			c_map[sc][ec] = co;
		}
	}

	// 도시간 최소 거리 기록하기
	for (int k = 1; k < n + 1; k++)
	{
		for (int sv = 1; sv < n + 1; sv++)
		{
			for (int ev = 1; ev < n + 1; ev++)
			{
				if (c_map[sv][k] != 21e8 && c_map[k][ev] != 21e8)
				{
					c_map[sv][ev] = min(c_map[sv][ev], c_map[sv][k] + c_map[k][ev]);
				}
			}
		}
	}

	// 도시간 최소 비용 출력
	for (sc = 1; sc < n + 1; sc++)
	{
		for (ec = 1; ec < n + 1; ec++)
		{
			if (c_map[sc][ec] == 21e8)
			{
				cout << 0 << " ";
			}
			else
			{
				cout << c_map[sc][ec] << " ";
			}
		}
		cout << endl;
	}

	return 0;
}