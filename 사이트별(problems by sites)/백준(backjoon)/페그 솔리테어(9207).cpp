#include <iostream>
#include <string>

using namespace std;

int n, m, t;
int ps;

char p_map[102][102];

int min_pn;
int min_mn;

struct p_no
{
	int r;
	int c;
	bool on;
};

p_no pins[8];

int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };

void p_move(int mn, int pn)
{
	if (pn < min_pn)
	{
		min_pn = pn;
		min_mn = mn;
	}
	else if (pn == min_pn)
	{
		if (mn < min_mn)
		{
			min_mn = mn;
		}
	}

	// ÇÉ ÀÌµ¿
	int r,c, tr, tc, tr2, tc2;
	for (int pv = 0; pv < ps; pv++)
	{
		if (pins[pv].on == false) continue;
		r = pins[pv].r;
		c = pins[pv].c;

		for (int i = 0; i < 4; i++)
		{
			tr = r + dr[i];
			tc = c + dc[i];
			if (0 > tr || n - 1 < tr || 0 > tc || m - 1 < tc) continue;
			if (p_map[tr][tc] != '#' && p_map[tr][tc] != '.')
			{
				
				tr2 = tr + dr[i];
				tc2 = tc + dc[i];
				char to_p = p_map[tr][tc];

				if (0 > tr2 || n - 1 < tr2 || 0 > tc2 || m - 1 < tc2) continue;
				if (p_map[tr2][tc2] != '.') continue;

				// ±âÁ¸ ÇÉ
				pins[p_map[tr][tc] - '0'].on = false;
				p_map[tr][tc] = '.';
				
				// ÀÌµ¿ ÇÉ
				pins[pv].r = tr2;
				pins[pv].c = tc2;
				p_map[tr2][tc2] = pv + '0';
				p_map[r][c] = '.';

				p_move(mn + 1, pn-1);

				// ±âÁ¸ ÇÉ
				pins[to_p - '0'].on = true;
				p_map[tr][tc] = to_p;

				// ÀÌµ¿ ÇÉ
				pins[pv].r = r;
				pins[pv].c = c;
				p_map[tr2][tc2] = '.';
				p_map[r][c] = pv+'0';
			}
		}
	}
}

int main()
{
	cin >> t;
	n = 5; m = 9;
	for (int tc = 0; tc < t; tc++)
	{
		string in_p;
		int p_id = 0;
		for (int r = 0; r < n; r++)
		{
			cin >> in_p;
			for (int c = 0; c < m; c++)
			{
				p_map[r][c] = in_p[c];
				if (p_map[r][c] == 'o')
				{
					pins[p_id] = { r,c,true };
					p_map[r][c] = p_id + '0';
					p_id += 1;
				}
			}
		}
		ps = p_id;

		min_pn = 21e8;
		min_mn = 21e8;

		p_move(0, ps);
		cout << min_pn << " " << min_mn << endl;
	}

	return 0;
}