#include <iostream>
#include <string>

using namespace std;

int n, m;

char g_map[52][52];

bool cycle_empty;

int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };

int vi[52][52];
int g_vi[52][52];

void g_record(int r, int c)
{
	int tr, tc;
	// 사이클의 조건을 고려하기
	for (int di = 0; di < 4; di++)
	{
		tr = r + dr[di];
		tc = c + dc[di];

		// 예외요건1
		if (0 > tr || n - 1 < tr || 0 > tc || m - 1 < tc)
		{
			continue;
		}

		if (g_vi[tr][tc] != 0) continue;
		
		g_vi[tr][tc] = 1;
		g_record(tr, tc);
	}
	
}

void cycle_count(char b_dot, int sr, int sc, int r, int c, int dist)
{
	if (cycle_empty == true)
	{
		return;
	}

	int tr, tc;
	// 사이클의 조건을 고려하기
	for (int di = 0; di < 4; di++)
	{
		tr = r + dr[di];
		tc = c + dc[di];

		// 예외요건1
		if (0 > tr || n - 1 < tr || 0 > tc || m - 1 < tc)
		{
			continue;
		}

		// 예외요건2
		if (b_dot != g_map[tr][tc])
		{
			continue;
		}

		if (dist > 2 && tr == sr && tc == sc)
		{
			cycle_empty = true;
			return;
		}

		if (vi[tr][tc] != 0) continue;

		vi[tr][tc] = 1;
		cycle_count(b_dot, sr, sc, tr, tc, dist+1);
		vi[tr][tc] = 0;
	}
}

int main()
{
	cin >> n >> m;
	string in_g_map;
	for (int r = 0; r < n; r++)
	{
		cin >> in_g_map;
		for (int c = 0; c < m; c++)
		{
			g_map[r][c] = in_g_map[c];
		}
	}

	cycle_empty = false;
	char base_dot = 'A';
	bool min_cycle = false;
	for (int sr = 0; sr < n; sr++)
	{
		for (int sc = 0; sc < m; sc++)
		{
			if (g_vi[sr][sc] != 0) continue;

			base_dot = g_map[sr][sc];
			vi[sr][sc] = 1;
			cycle_count(base_dot, sr, sc, sr, sc,0);

		}
		if (cycle_empty == true) break;
	}

	if (cycle_empty == true)
	{
		cout << "Yes" << endl;
	}
	else
	{
		cout << "No" << endl;
	}
	return 0;
}