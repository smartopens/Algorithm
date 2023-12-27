#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

// 시간복잡도: 4^6, 4천

int n;
int num_board[5][5];

unordered_map<string, int> sn_map;

int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };

void get_sn(int vr, int vc, int a, string sn)
{
	if (a > 5)
	{
		sn_map[sn] += 1;
		return;
	}
	int to_r, to_c;
	sn += (char)(num_board[vr][vc] + '0');

	for (int i = 0; i < 4; i++)
	{
		to_r = vr + dr[i];
		to_c = vc + dc[i];
		if (0 > to_r || n - 1 < to_r || 0 > to_c || n - 1 < to_c) continue;

		get_sn(to_r, to_c, a+1, sn);
	}
}

int main()
{
	n = 5;
	for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < n; c++)
		{
			cin >> num_board[r][c];
		}
	}

	for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < n; c++)
		{
			get_sn(r, c,0, "");
		}
	}

	/*for (auto v : sn_map)
	{
		cout << v.first << endl;
	}*/
	cout << sn_map.size() << endl;
	return 0;
}