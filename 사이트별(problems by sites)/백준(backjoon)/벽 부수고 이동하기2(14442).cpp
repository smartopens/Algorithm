#include <iostream>
#include <string>
#include <queue>

using namespace std;

int n, m;
int k;

int min_dist;

char w_map[1002][1002];
int vi[1002][1002][12];

struct p_no
{
	int r;
	int c;
	int kn;
};

int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };

void g_start()
{
	queue<p_no> q;
	q.push({ 0,0,0 });

	vi[0][0][0] = 1;

	if (0 == n - 1 && 0 == m - 1)
	{
		min_dist = vi[0][0][0];
		return;
	}

	while (!q.empty())
	{
		p_no mv = q.front();
		q.pop();

		int tr, tc;
		for (int di = 0; di < 4; di++)
		{
			tr = mv.r + dr[di];
			tc = mv.c + dc[di];
			
			// 벽을 부수는 경우
			if (0 > tr || n - 1 < tr || 0 > tc || m - 1 < tc) continue;
			if (w_map[tr][tc] == '1' && mv.kn < k && vi[tr][tc][mv.kn + 1] == 0)
			{
				/*cout << mv.r << " " << mv.c << " "  << mv.kn << "\n";
				cout << tr << " " << tc << "\n";*/

				vi[tr][tc][mv.kn + 1] = vi[mv.r][mv.c][mv.kn] + 1;
				
				if (tr == n - 1 && tc == m - 1)
				{
					min_dist = vi[tr][tc][mv.kn + 1];
					return;
				}
				q.push({ tr, tc, mv.kn + 1 });
			}

			if (w_map[tr][tc] == '1') continue;
			if (vi[tr][tc][mv.kn] != 0) continue;
			
			vi[tr][tc][mv.kn] = vi[mv.r][mv.c][mv.kn] + 1;
			if (tr == n - 1 && tc == m - 1)
			{
				min_dist = vi[tr][tc][mv.kn];
				return;
			}
			q.push({ tr,tc,mv.kn });
		}
	}
}

int main()
{
	cin >> n >> m;
	cin >> k;

	string in_map;
	for (int r = 0; r < n; r++)
	{
		cin >> in_map;
		for (int c = 0; c < m; c++)
		{
			w_map[r][c] = in_map[c];
		}
	}

	min_dist = 21e8;
	g_start();

	//for (int r = 0; r < n; r++)
	//{
	//	for (int c = 0; c < m; c++)
	//	{
	//		cout << vi[r][c][1] << " ";
	//	}
	//	cout << "\n";
	//}
	//cout << "\n";

	if (min_dist == 21e8)
	{
		cout << -1 << "\n";
	}
	else
	{
		cout << min_dist << "\n";
	}

	return 0;
}