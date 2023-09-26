#include <iostream>

using namespace std;

int n, m;
int new_p[1002][1002];
int vi[1002][1002];
int costs[1002][1002][3];

int dr[3] = { 0,1,0 };
int dc[3] = { 1,0,-1 };
int max_r;

// 바텀업 방식으로 생각하면 편하다.
// 저장소가 갱신될 경우, 이전 방향을 고려해 갱신된다.
// 시작지점(0,0)으로부터 세가지 방향으로 분기되고
// 가장 윗줄의 경우, 맨 왼쪽부터 갱신이 된다.
// 그 이후 방향에 맞게 dfs를 돌린다면, 모든 경로에서의
// 최대가치가 갱신된다.
int r_search(int now_r, int now_c, int p_di)
{
	if (now_r == n - 1 && now_c == m - 1)
	{
		return 0;
	}

	int& ret = costs[now_r][now_c][p_di];
	if (ret != -3e8)
	{
		return ret;
	}
	
	ret = -3e8;
	int to_r = 0;
	int to_c = 0;
	int max_c = -3e8;
	for (int i = 0; i < 3; i++)
	{
		to_r = now_r + dr[i];
		to_c = now_c + dc[i];
		if (0 > to_r || n-1 < to_r || 0 > to_c || m-1 < to_c) continue;
		if (vi[to_r][to_c] != 0) continue;
		
		vi[to_r][to_c] = 1;
		max_c = max(max_c, r_search(to_r, to_c, i) + new_p[to_r][to_c]);
		vi[to_r][to_c] = 0;
	}

	return ret = max_c;
}

int main()
{
	// 맵 정보 입력받기
	cin >> n >> m;
	for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < m; c++)
		{
			cin >> new_p[r][c];
		}
	}

	// 로봇 가치 저장소 초기화하기
	// 이동기록이 없게 되는 값으로 한다.
	for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < m; c++)
		{
			for (int k = 0; k < 3; k++)
			{
				costs[r][c][k] = -3e8;
			}
		}
	}

	// 경우 고려하기
	max_r = 0;
	max_r += new_p[0][0];
	vi[0][0] = 1;
	max_r += r_search(0,0,0);

	cout << max_r << endl;
	return 0;
}
