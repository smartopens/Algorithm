#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n, m;

int m_map[102][72];
int vi[102][72];

int dr[8] = { -1,0,1,0,-1,-1,1,1 };
int dc[8] = { 0,1,0,-1,-1,1,-1,1};

struct p_no
{
	int r;
	int c;
};

int hm_n;

void hm_sub_count(int sr, int sc)
{
	queue<p_no>q;
	q.push({ sr,sc });
	vi[sr][sc] = 1;

	int now_hm = m_map[sr][sc];

	while (!q.empty())
	{
		p_no mv = q.front();
		q.pop();

		int tr, tc;
		for (int di = 0; di < 8; di++)
		{
			tr = mv.r + dr[di];
			tc = mv.c + dc[di];

			// 작은 경우 탐색하기
			if (0 > tr || n - 1 < tr || 0 > tc || m - 1 < tc) continue;
			if (m_map[tr][tc] == 0) continue;
			
			if (now_hm == m_map[tr][tc] && vi[tr][tc] == 1)
			{
				vi[tr][tc] = 2;
				q.push({ tr,tc });
			}
			else if (now_hm != m_map[tr][tc] && m_map[mv.r][mv.c] > m_map[tr][tc]) {
				if (vi[tr][tc] != 0) continue;
				vi[tr][tc] = 1;
				q.push({ tr,tc });
			}
		}
	}
}

void hm_count(int sr, int sc)
{
	queue<p_no>q;
	q.push({ sr,sc });
	vi[sr][sc] = 1;

	int now_hm = m_map[sr][sc];

	while (!q.empty())
	{
		p_no mv = q.front();
		q.pop();

		int tr, tc;
		for (int di = 0; di < 8; di++)
		{
			tr = mv.r + dr[di];
			tc = mv.c + dc[di];

			// 산봉우리만 보기
			if (0 > tr || n - 1 < tr || 0 > tc || m - 1 < tc) continue;
			if (m_map[mv.r][mv.c] < m_map[tr][tc]) continue;
			if (vi[tr][tc] != 0) continue;
			
			vi[tr][tc] = 1;
			q.push({ tr,tc });
		}
	}
}
int main()
{
	cin >> n >> m;
	for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < m; c++)
		{
			cin >> m_map[r][c];
		}
	}

	hm_n = 0;
	vector<p_no> high_m;
	for (int m_h = 500; m_h > 0; m_h--)
	{
		for (int r = 0; r < n; r++)
		{
			for (int c = 0; c < m; c++)
			{
				if (m_map[r][c] != m_h) continue;
				if (vi[r][c] != 0) continue;

				hm_count(r,c);
				//hm_sub_count(r, c);
				hm_n += 1;
			}
		}
	}

	cout << hm_n << "\n";
	return 0;
}