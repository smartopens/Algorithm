#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int n, m, t;

int f_map[102][102][2];
int vi[102][102][2];

bool can_save;

struct w_no
{
	int r;
	int c;
	int gn;
};

int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };

int min_tm;

void w_run()
{
	queue<w_no> q;
	q.push({ 1,1,0 });

	vi[1][1][0] = 1;

	while (!q.empty())
	{
		w_no wv = q.front();
		q.pop();
		
		if (wv.r == n && wv.c == m)
		{
			can_save = true;
			min_tm = min(min_tm, vi[wv.r][wv.c][wv.gn] - 1);
			//cout << min_tm << endl;
			return;
		}

		int tr, tc;
		int gn = wv.gn;
		for (int di = 0; di < 4; di++)
		{
			tr = wv.r + dr[di];
			tc = wv.c + dc[di];

			if (1 > tr || n < tr || 1 > tc || m < tc) continue;
			if (f_map[tr][tc][gn] == 1) continue;
			if (vi[tr][tc][gn] != 0) continue;

			if (vi[wv.r][wv.c][gn] > t)
			{
				continue;
			}

			// 무기를 획득한 경우
			if (f_map[tr][tc][gn] == 2)
			{
				//cout << vi[tr][tc][gn] + 1 << endl;
				//cout << tr << " " << tc << endl;
				vi[tr][tc][gn + 1] = vi[wv.r][wv.c][gn] + 1;
				q.push({ tr,tc,gn + 1 });
			}
			// 그냥 이동하는 경우
			else
			{
				vi[tr][tc][gn] = vi[wv.r][wv.c][gn] + 1;
				q.push({ tr,tc,gn });
			}
		}
	}
}

int main()
{
	cin >> n >> m >> t;
	for (int r = 1; r < n + 1; r++)
	{
		for (int c = 1; c < m + 1; c++)
		{
			cin >> f_map[r][c][0];
		}
	}

	can_save = false;
	min_tm = 21e8;
	w_run();

	if (can_save == false)
	{
		cout << "Fail\n";
	}
	else
	{
		cout << min_tm << endl;
	}
	return 0;
}