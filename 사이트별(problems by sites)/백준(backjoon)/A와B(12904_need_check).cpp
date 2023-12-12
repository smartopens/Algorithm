#include <iostream>
#include <cstring>

using namespace std;

// ������� ���̷����� �ִ�.
// ���� ��ȣ�� ���̷������� �ʸ��� �����Ѵ�. (���� ħ��x)
// �ð����⵵: 4�� * 10000

// �ð� �����鼭 vi�� ǥ���Ѵ�.
// ���ڸ�
// 
// vi

int n, k;
int v_map[202][202];
int vi[202][202];

int v_map2[202][202];
int s, tr, tc;
int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };

int cn;

void v_expand()
{
	memcpy(v_map2, v_map, sizeof(v_map));
	// ������ �˻�
	for (int r = 1; r < n + 1; r++)
	{
		for (int c = 1; c < n + 1; c++)
		{
			// �ش� �������� �����ߴ����� �˻��ϱ�
			if (v_map[r][c] == 0) continue;
			if (vi[r][c] != 0) continue;

			int now_v = v_map[r][c];
			// �˻� ǥ��
			vi[r][c] = 1;
			cn += 1;

			// ���̷��� ���� ǥ��
			int to_r, to_c;
			for (int i = 0; i < 4; i++)
			{
				to_r = r + dr[i];
				to_c = c + dc[i];

				if (1 > to_r || n < to_r || 1 > to_c || n < to_c) continue;
				if (v_map[to_r][to_c] != 0) continue;

				if (v_map2[to_r][to_c] > now_v)
				{
					v_map2[to_r][to_c] = now_v;
				}
				else if (v_map2[to_r][to_c] == 0){
					v_map2[to_r][to_c] = now_v;
				}
			}

		}
	}

	memcpy(v_map, v_map2, sizeof(v_map));
	return;
}
int main()
{
	cin >> n >> k;
	for (int r = 1; r < n + 1; r++)
	{
		for (int c = 1; c < n + 1; c++)
		{
			cin >> v_map[r][c];
		}
	}

	cin >> s >> tr >> tc;
	
	for (int sv = 0; sv < s; sv++)
	{
		cn = 0;
		v_expand();
		if (cn >= n * n)
		{
			break;
		}
	}
	
	cout << v_map[tr][tc] << endl;
	return 0;
}