#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 싸움땅의 플레이어들은 작은 번호부터 움직인다.
// 격자밖: 반대방향
// 이동 방향에 플레이어x: 해당칸의 가장 공격력 큰 총을 들고 기존총을 둔다.
// 이동 방향에 플레이어o: 결투를 한다.

// 결투승 조건: 능력치+총 / 초기 능력치 우선
// 진 경우: 총을 두고 다음칸으로 이동(빈공간으로 가야함, 시계 방향)
// 이긴 경우: 해당 칸의 가장 공격력 큰 총을 들고 기존총을 둔다, 점수 획득(총합 차이)

int n, m, k;
vector<int> gun_map[20][20];

struct w_no
{
	int r;
	int c;
	int f_pow;
	int g_pow;
	int dir;
};

w_no wa_info[32];
int wa_map[20][20];

int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };

int p_sco[32];

void wa_move()
{
	int to_r, to_c, to_dir;
	int to_r2, to_c2, to_dir2;
	int wa_gun = 0;
	for (int pv = 1; pv < m + 1; pv++)
	{
		to_dir = wa_info[pv].dir;
		to_r = wa_info[pv].r + dr[to_dir];
		to_c = wa_info[pv].c + dc[to_dir];

		if (0 > to_r || n - 1 < to_r || 0 > to_c || n - 1 < to_c)
		{
			to_dir = (to_dir + 2) % 4;
			to_r = wa_info[pv].r + dr[to_dir];
			to_c = wa_info[pv].c + dc[to_dir];
		}

		int to_pow = wa_info[wa_map[to_r][to_c]].f_pow + wa_info[wa_map[to_r][to_c]].g_pow;
		int to_pn = wa_map[to_r][to_c];

		int now_pow = wa_info[pv].f_pow + wa_info[pv].g_pow;
		int now_f_pow = wa_info[pv].f_pow;
		int now_g_pow = wa_info[pv].g_pow;
		int now_to_dir = to_dir;
		wa_info[pv].dir = to_dir;

		int win_pn, lose_pn;
		// 사람 있는 경우
		if (wa_map[to_r][to_c] != 0)
		{
			if (now_pow == to_pow)
			{
				if (wa_info[pv].f_pow > wa_info[to_pn].f_pow)
				{
					win_pn = pv;
					lose_pn = to_pn;
				}
				else
				{
					win_pn = to_pn;
					lose_pn = pv;
				}
			}
			// 현재 사람이 이기는 경우
			else if (now_pow > to_pow)
			{
				win_pn = pv;
				lose_pn = to_pn;

			}
			// 기존 사람이 이기는 경우
			else if (now_pow < to_pow)
			{
				win_pn = to_pn;
				lose_pn = pv;
			}

			int win_f_pow = wa_info[win_pn].f_pow;
			int win_g_pow = wa_info[win_pn].g_pow;
			int win_to_dir = wa_info[win_pn].dir;

			int lose_f_pow = wa_info[lose_pn].f_pow;
			int lose_g_pow = wa_info[lose_pn].g_pow;
			int lose_to_dir = wa_info[lose_pn].dir;

			// 진 사람 총 놓기
			gun_map[to_r][to_c].push_back(wa_info[lose_pn].g_pow);

			// 이긴 사람 총 교체 및 점수
			p_sco[win_pn] += abs(now_pow - to_pow);

			// 총 교체
			wa_gun = wa_info[win_pn].g_pow;
			if (gun_map[to_r][to_c].size() > 0)
			{
				sort(gun_map[to_r][to_c].begin(), gun_map[to_r][to_c].end());

				// 기존 필드 총이 더 강한 경우
				if (gun_map[to_r][to_c].size() > 0 &&
					wa_gun < gun_map[to_r][to_c][gun_map[to_r][to_c].size() - 1])
				{
					win_g_pow = gun_map[to_r][to_c][gun_map[to_r][to_c].size() - 1];
					gun_map[to_r][to_c].pop_back();
					gun_map[to_r][to_c].push_back(wa_gun);
				}
			}

			// 진 사람 이동하기
			for (int i = 0; i < 4; i++)
			{
				to_dir2 = (lose_to_dir + i) % 4;
				to_r2 = to_r + dr[to_dir2];
				to_c2 = to_c + dc[to_dir2];

				if (0 > to_r2 || n - 1 < to_r2 || 0 > to_c2 || n - 1 < to_c2) continue;
				if ((to_r2 == wa_info[pv].r && to_c2 == wa_info[pv].c) || wa_map[to_r2][to_c2] == 0)
				{
					break;
				}
			}

			// 진 사람 총 교체
			lose_g_pow = 0;
			if (gun_map[to_r2][to_c2].size() > 0)
			{
				sort(gun_map[to_r2][to_c2].begin(), gun_map[to_r2][to_c2].end());
				lose_g_pow = gun_map[to_r2][to_c2][gun_map[to_r2][to_c2].size() - 1];
				gun_map[to_r2][to_c2].pop_back();
			}

			// 정보 갱신
			// 이긴 경우
			wa_map[wa_info[pv].r][wa_info[pv].c] = 0;
			wa_map[to_r][to_c] = win_pn;
			wa_info[win_pn].g_pow = win_g_pow;
			wa_info[win_pn].dir = win_to_dir;
			wa_info[win_pn].r = to_r;
			wa_info[win_pn].c = to_c;

			// 진 경우
			wa_map[to_r2][to_c2] = lose_pn;
			wa_info[lose_pn].g_pow = lose_g_pow;
			wa_info[lose_pn].dir = to_dir2;
			wa_info[lose_pn].r = to_r2;
			wa_info[lose_pn].c = to_c2;

		}
		// 사람 없는 경우
		else
		{
			// 총 교체
			wa_gun = wa_info[pv].g_pow;
			if (gun_map[to_r][to_c].size() > 0)
			{
				sort(gun_map[to_r][to_c].begin(), gun_map[to_r][to_c].end());

				// 기존 필드 총이 더 강한 경우
				if (gun_map[to_r][to_c].size() > 0 && wa_gun < gun_map[to_r][to_c][gun_map[to_r][to_c].size() - 1])
				{
					now_g_pow = gun_map[to_r][to_c][gun_map[to_r][to_c].size() - 1];
					gun_map[to_r][to_c].pop_back();
					gun_map[to_r][to_c].push_back(wa_gun);
				}
			}
			wa_map[to_r][to_c] = pv;
			wa_map[wa_info[pv].r][wa_info[pv].c] = 0;

			wa_info[pv].r = to_r;
			wa_info[pv].c = to_c;
			wa_info[pv].g_pow = now_g_pow;
			wa_info[pv].dir = now_to_dir;
		}
	}
}

int main()
{
	cin >> n >> m >> k;
	int in_g_pow;
	for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < n; c++)
		{
			cin >> in_g_pow;
			gun_map[r][c].push_back(in_g_pow);
		}
	}

	int in_r, in_c, in_d, in_s;
	for (int pv = 1; pv < m+1; pv++)
	{
		cin >> in_r >> in_c >> in_d >> in_s;
		wa_map[in_r - 1][in_c - 1] = pv;
		wa_info[pv] = { in_r-1,in_c-1, in_s, 0, in_d };
	}

	while (k > 0)
	{
		wa_move();
		k -= 1;
	} 

	for (int pv = 1; pv < m + 1; pv++)
	{
		cout << p_sco[pv] << " ";
	}

	return 0;
}