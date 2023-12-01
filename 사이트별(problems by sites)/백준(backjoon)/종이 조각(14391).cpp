#include <iostream>
#include <string>

using namespace std;

// 가로나 세로 방향으로 합 구하기
int n, m;
char p_board[5][5];

int vi[5][5];

int dr[2] = { 0,1 };
int dc[2] = { 1,0 };

int max_ps;
int max_s;

void ps_count(int sr, int sc, int now_ps)
{
	if (sc > m - 1)
	{
		sr += 1;
		sc = 0;
	}

	if (sr > n - 1)
	{
		if (now_ps > max_ps)
		{
			max_ps = now_ps;
		}
		return;
	}
	int to_r, to_c;
	string to_ps;
	for (int di = 0; di < 2; di++)
	{
		// 열선, 후행
		to_ps = "";
		int tmp_mn = 0;
		for (int s = 0; s < max_s; s++)
		{
			to_r = sr + dr[di] * s;
			to_c = sc + dc[di] * s;

			if (0 > to_r || n - 1 < to_r || 0 > to_c || m - 1 < to_c) continue;
			if (vi[to_r][to_c] != 0) break;

			vi[to_r][to_c] = 1;
			to_ps += p_board[to_r][to_c];
			tmp_mn += 1;

			ps_count(sr, sc+1, now_ps+stoi(to_ps));
		}

		for (int s = 0; s < tmp_mn; s++)
		{
			to_r = sr + dr[di] * s;
			to_c = sc + dc[di] * s;

			if (0 > to_r || n - 1 < to_r || 0 > to_c || m - 1 < to_c) continue;
			vi[to_r][to_c] = 0;
		}
	}
	return;
}

int main()
{
	cin >> n >> m;
	max_s = max(n, m);

	string in_pv;
	for (int r = 0; r < n; r++)
	{
		cin >> in_pv;
		for (int c=0; c<m; c++)
		{
			p_board[r][c] = in_pv[c];
		}
	}

	ps_count(0,0,0);

	cout << max_ps << endl;
	return 0;
}