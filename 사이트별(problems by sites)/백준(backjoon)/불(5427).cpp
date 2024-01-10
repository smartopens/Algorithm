#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <cstring>

using namespace std;

// 빌딩에 불이 났다.
// 매초마다 불은 특정 방향으로 인접하게 퍼진다.
// 불이 퍼지려는 칸에 상근이는 이동할 수 없다. (불은 상근이 전 위치로 가능)

int t;

int n, m;
char b_map[1002][1002];

bool c_out;
int min_tm;

int sr;
int sc;

struct p_no
{
	int r;
	int c;
};

vector<p_no> f_vec;

int dr[4] = { 0,0,1,-1 };
int dc[4] = { 1,-1,0,0 };

void s_run()
{
	//memset(vi, 0, sizeof(vi));
	int vi[1002][1002] = {};
	queue<p_no> fq = {};
	while (!f_vec.empty())
	{
		p_no now_f = f_vec.back();
		f_vec.pop_back();

		b_map[now_f.r][now_f.c] = '*';
		fq.push({ now_f.r, now_f.c });
		//cout << "!!" << endl;
	}

	queue<p_no> sq = {};
	sq.push({ sr,sc });
	vi[sr][sc] = 1;
	bool s_go = true;

	while (true)
	{
		// 다음 이동
		int tr, tc;
		// 불 퍼지기
		int q_size = fq.size();
		for (int qs = 0; qs < q_size; qs++)
		{
			p_no fv = fq.front();
			fq.pop();

			for (int i = 0; i < 4; i++)
			{
				tr = fv.r + dr[i];
				tc = fv.c + dc[i];

				if (0 > tr || n-1 < tr || 0 > tc || m-1 < tc) continue;
				if (b_map[tr][tc] == '*' || b_map[tr][tc] == '#') continue;
				
				b_map[tr][tc] = '*';
				fq.push({ tr,tc });
			}
		}

		// 상범 이동
		s_go = false;
		q_size = sq.size();
		for (int qs = 0; qs < q_size; qs++)
		{
			p_no sv = sq.front();
			sq.pop();

			// 탈출
			if (sv.r == 0 || sv.r == n - 1 || sv.c == 0 || sv.c == m - 1)
			{
				c_out = true;
				min_tm = vi[sv.r][sv.c];
			}

			for (int i = 0; i < 4; i++)
			{
				tr = sv.r + dr[i];
				tc = sv.c + dc[i];

				if (0 > tr || n - 1 < tr || 0 > tc || m - 1 < tc) continue;
				if (vi[tr][tc] != 0 || b_map[tr][tc] != '.') continue;

				s_go = true;
				vi[tr][tc] = vi[sv.r][sv.c] + 1;
				sq.push({ tr,tc });
			}
		}
		/*for (int r = 0; r < n; r++)
		{
			for (int c = 0; c < m; c++)
			{
				cout << b_map[r][c] << " ";
			}
			cout << endl;
		}
		cout << endl;


		for (int r = 0; r < n; r++)
		{
			for (int c = 0; c < m; c++)
			{
				cout << vi[r][c] << " ";
			}
			cout << endl;
		}
		cout << endl;*/

		if (c_out == true || s_go == false)
		{
			break;
		}
	}
}

int main()
{
	cin >> t;
	string in_b;
	for (int tc = 1; tc < t + 1; tc++)
	{
		c_out = false;
		min_tm = 21e8;
		f_vec.clear();
		cin >> m >> n;
		for (int r = 0; r < n; r++)
		{
			cin >> in_b;
			for (int c = 0; c < m; c++)
			{
				b_map[r][c] = in_b[c]; 
				if (b_map[r][c] == '@')
				{
					b_map[r][c] = '.';
					sr = r;
					sc = c;
				}
				else if (b_map[r][c] == '*')
				{
					f_vec.push_back({ r,c });
				}
			}
		}

		//cout << " " << sc << endl;
		s_run();
		if (c_out == false)
		{
			cout << "IMPOSSIBLE" << "\n";
		}
		else
		{
			cout << min_tm << "\n";
		}
	}
	return 0;
}