#include <iostream>
#include <string>

using namespace std;

int n, m;

char c_map[602][602];
int vi[602][602];

int sr, sc;

bool meet_ok;
int mn;

int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };

void meet_people(int r, int c)
{
	int tr, tc;
	for (int di = 0; di < 4; di++)
	{
		tr = r + dr[di];
		tc = c + dc[di];

		if (0 > tr || n - 1 < tr || 0 > tc || m - 1 < tc) continue;
		if (c_map[tr][tc] == 'X') continue;
		if (vi[tr][tc] != 0) continue;

		if (c_map[tr][tc] == 'P')
		{
			mn += 1;
			meet_ok = true;
		}

		vi[tr][tc] = 1;
		meet_people(tr, tc);
	}
}

int main()
{
	cin >> n >> m;
	string info_c;
	for (int r = 0; r < n; r++)
	{
		cin >> info_c;
		for (int c = 0; c < m; c++)
		{
			c_map[r][c] = info_c[c];
		}
	}

	for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < m; c++)
		{
			if (c_map[r][c] == 'I')
			{
				sr = r;
				sc = c;
			}			
		}
	}

	meet_ok = false;
	mn = 0;
	vi[sr][sc] = 1;
	meet_people(sr, sc);

	if (meet_ok == false)
	{
		cout << "TT" << endl;
	}
	else
	{
		cout << mn << endl;
	}
	return 0;
}