#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// �ο��� �÷��̾���� ���� ��ȣ���� �����δ�.
// ���ڹ�: �ݴ����
// �̵� ���⿡ �÷��̾�x: �ش�ĭ�� ���� ���ݷ� ū ���� ��� �������� �д�.
// �̵� ���⿡ �÷��̾�o: ������ �Ѵ�.

// ������ ����: �ɷ�ġ+�� / �ʱ� �ɷ�ġ �켱
// �� ���: ���� �ΰ� ����ĭ���� �̵�(��������� ������, �ð� ����)
// �̱� ���: �ش� ĭ�� ���� ���ݷ� ū ���� ��� �������� �д�, ���� ȹ��(���� ����)

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
		// ��� �ִ� ���
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
			// ���� ����� �̱�� ���
			else if (now_pow > to_pow)
			{
				win_pn = pv;
				lose_pn = to_pn;

			}
			// ���� ����� �̱�� ���
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

			// �� ��� �� ����
			gun_map[to_r][to_c].push_back(wa_info[lose_pn].g_pow);

			// �̱� ��� �� ��ü �� ����
			p_sco[win_pn] += abs(now_pow - to_pow);

			// �� ��ü
			wa_gun = wa_info[win_pn].g_pow;
			if (gun_map[to_r][to_c].size() > 0)
			{
				sort(gun_map[to_r][to_c].begin(), gun_map[to_r][to_c].end());

				// ���� �ʵ� ���� �� ���� ���
				if (gun_map[to_r][to_c].size() > 0 &&
					wa_gun < gun_map[to_r][to_c][gun_map[to_r][to_c].size() - 1])
				{
					win_g_pow = gun_map[to_r][to_c][gun_map[to_r][to_c].size() - 1];
					gun_map[to_r][to_c].pop_back();
					gun_map[to_r][to_c].push_back(wa_gun);
				}
			}

			// �� ��� �̵��ϱ�
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

			// �� ��� �� ��ü
			lose_g_pow = 0;
			if (gun_map[to_r2][to_c2].size() > 0)
			{
				sort(gun_map[to_r2][to_c2].begin(), gun_map[to_r2][to_c2].end());
				lose_g_pow = gun_map[to_r2][to_c2][gun_map[to_r2][to_c2].size() - 1];
				gun_map[to_r2][to_c2].pop_back();
			}

			// ���� ����
			// �̱� ���
			wa_map[wa_info[pv].r][wa_info[pv].c] = 0;
			wa_map[to_r][to_c] = win_pn;
			wa_info[win_pn].g_pow = win_g_pow;
			wa_info[win_pn].dir = win_to_dir;
			wa_info[win_pn].r = to_r;
			wa_info[win_pn].c = to_c;

			// �� ���
			wa_map[to_r2][to_c2] = lose_pn;
			wa_info[lose_pn].g_pow = lose_g_pow;
			wa_info[lose_pn].dir = to_dir2;
			wa_info[lose_pn].r = to_r2;
			wa_info[lose_pn].c = to_c2;

		}
		// ��� ���� ���
		else
		{
			// �� ��ü
			wa_gun = wa_info[pv].g_pow;
			if (gun_map[to_r][to_c].size() > 0)
			{
				sort(gun_map[to_r][to_c].begin(), gun_map[to_r][to_c].end());

				// ���� �ʵ� ���� �� ���� ���
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