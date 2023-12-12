#include <iostream>
#include <cstring>

using namespace std;

// 시험관에 바이러스가 있다.
// 낮은 번호의 바이러스부터 초마다 증식한다. (서로 침범x)
// 시간복잡도: 4만 * 10000

// 시간 지나면서 vi를 표시한다.
// 숫자맵
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
	// 순차별 검사
	for (int r = 1; r < n + 1; r++)
	{
		for (int c = 1; c < n + 1; c++)
		{
			// 해당 영역에서 증식했는지를 검사하기
			if (v_map[r][c] == 0) continue;
			if (vi[r][c] != 0) continue;

			int now_v = v_map[r][c];
			// 검사 표기
			vi[r][c] = 1;
			cn += 1;

			// 바이러스 증식 표기
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