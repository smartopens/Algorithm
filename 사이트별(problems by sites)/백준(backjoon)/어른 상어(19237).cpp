#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

// 수족관에 상어가 m마리 있다.

int n, m, k;

vector<int> s_map[22][22];

struct s_no
{
	int r;
	int c;
	int di;
	bool is_live;
};

s_no s_info[402];

struct sm_no
{
	int s_id;
	int kn;
};

sm_no s_smell[22][22];

int dr[4] = { -1,1,0,0 };
int dc[4] = { 0,0,-1,1 };

int s_di[402][4][4];

int main()
{
	cin >> n >> m >> k;
	int s_id;
	for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < n; c++)
		{
			cin >> s_id;
			s_map[r][c].push_back(s_id);
			s_info[s_map[r][c][0]] = { r,c,0,true };
			s_smell[r][c] = { 0,0 };
		}
	}

	int sdi = 0;
	for (int sv = 1; sv < m+1; sv++)
	{
		cin >> sdi;
		sdi -= 1;
		s_info[sv].di = sdi;
	}

	// 상어 우선순위
	for (int sv = 1; sv < m + 1; sv++)
	{
		int d1, d2, d3, d4;
		for (int i = 0; i < 4; i++)
		{
			for (int di = 0; di < 4; di++)
			{
				cin >> d1;
				d1 -= 1;
				s_di[sv][i][di] = d1;
			}
		}
	}
	int now_k = 0;

	/*for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < n; c++)
		{
			if (!s_map[r][c].empty())
			{
				cout << s_map[r][c][0] << " ";
			}
			else {
				cout << 0 << " ";
			}
		}
		cout << endl;
	}
	cout << endl;*/

	while (now_k <= 1000)
	{
		// 상어는 각자의 위치에서 냄새를 남긴다. 
		for (int sv = 1; sv < m + 1; sv++)
		{
			if (s_info[sv].is_live == false) continue;
			s_smell[s_info[sv].r][s_info[sv].c] = { sv,k };
		}

		/*cout << now_k << endl;
		for (int r = 0; r < n; r++)
		{
			for (int c = 0; c < n; c++)
			{
				cout << s_smell[r][c].s_id << " ";
			}
			cout << endl;
		}
		cout << endl;*/

		// 모든 상어는 1초마다 이동한다.
		int to_r, to_c;
		int to_r2, to_c2;
		int to_r3, to_c3;
		int to_di2, to_di3;
		/*to_r3 = 0;
		to_c3 = 0;
		to_di3 = 0;*/
		bool can_go = false;
		bool can_go2 = false;

		memset(s_map, 0, sizeof(s_map));
		for (int sv = 1; sv < m + 1; sv++)
		{
			if (s_info[sv].is_live == false) continue;
			// 이동 우선순위(빈칸, 냄새) 고려
			can_go = false;
			can_go2 = false;
			for (int i = 0; i < 4; i++)
			{
				to_r = s_info[sv].r + dr[s_di[sv][s_info[sv].di][i]];
				to_c = s_info[sv].c + dc[s_di[sv][s_info[sv].di][i]];

				if (!(0 > to_r || n - 1 < to_r || 0 > to_c || n - 1 < to_c))
				{
					if (s_smell[to_r][to_c].s_id == 0 && can_go == false)
					{
						to_r2 = to_r;
						to_c2 = to_c;
						to_di2 = s_di[sv][s_info[sv].di][i];
						can_go = true;
					}
				}
				if (s_smell[to_r][to_c].s_id == sv && can_go2 == false)
				{
					to_r3 = to_r;
					to_c3 = to_c;
					to_di3 = s_di[sv][s_info[sv].di][i];
					can_go2 = true;
				}
			}

			// 빈칸으로 가는 경우
			if (can_go == true)
			{
				s_map[to_r2][to_c2].push_back(sv);
				s_info[sv].r = to_r2;
				s_info[sv].c = to_c2;
				s_info[sv].di = to_di2;
			}
			// 빈칸이 없는 경우
			else if (can_go == false)
			{
				s_map[to_r3][to_c3].push_back(sv);
				s_info[sv].r = to_r3;
				s_info[sv].c = to_c3;
				s_info[sv].di = to_di3;
			}
		}

		// 상어 정리
		for (int r = 0; r < n; r++)
		{
			for (int c = 0; c < n; c++)
			{
				// 이동 후 여러마리인 경우 고려
				if (s_map[r][c].size() > 1)
				{
					sort(s_map[r][c].begin(), s_map[r][c].end());
					int live_s = s_map[r][c][0];

					for (int s = 0; s < s_map[r][c].size(); s++)
					{
						if (s_map[r][c][s] == live_s) continue;
						s_info[s_map[r][c][s]].is_live = false;
					}
				}
			}
		}
		/*for (int r = 0; r < n; r++)
		{
			for (int c = 0; c < n; c++)
			{
				if (!s_map[r][c].empty())
				{
					cout << s_map[r][c][0] << " ";
				}
				else {
					cout << 0 << " ";
				}
			}
			cout << endl;
		}
		cout << endl;

		for (int sv = 1; sv < m + 1; sv++)
		{
			cout << sv << " " << s_info[sv].is_live << endl;
		}
		cout << endl;*/

		now_k += 1;

		// 냄새 제거
		for (int r = 0; r < n; r++)
		{
			for (int c = 0; c < n; c++)
			{
				if (s_smell[r][c].kn > 0)
				{
					s_smell[r][c].kn -= 1;
					if (s_smell[r][c].kn == 0)
					{
						s_smell[r][c].s_id = 0;
					}
				}
			}
		}

		bool one_live = true;
		for (int sv = 2; sv < m + 1; sv++)
		{
			if (s_info[sv].is_live == true)
			{
				one_live = false;
				break;
			}
		}
		
		if (one_live)
		{
			break;
		}
	}

	if (now_k > 1000)
	{
		cout << -1 << endl;
	}
	else {
		cout << now_k << endl;
	}
	return 0;
}