#define _CRT_SECURE_NO_WARNINGS

#include <queue>
#include <cstring>
#include <iostream>

using namespace std;

// 기본 벽돌판 정보
int n;
int w, h;
int board[15][15];
int tmp_board[15][15];

int visited[15][15];
vector<int> dolls;

int dr[4] = { -1,1,0,0 };
int dc[4] = { 0,0,-1,1 };

// 최종 남는 벽돌: total_num - max_bum
// 벽돌이 없어질 경우: is_max활용해 탐색을 종료함
int max_b_num = 0;
int total_num = 0;
bool is_max = false;

struct node {
	int r;
	int c;
};

void move(int r, int c) {
	int nr = r + 1;
	int nc = c;

	// 마지막까지 탐색하기
	while (nr + 1 < h) {
		if (board[nr][nc] != 0) break;
		nr += 1;
	}

	// 마지막 지점이고 블록이 0인 경우
	if (nr == h - 1 && board[nr][nc] == 0) {
		board[nr][nc] = board[r][c];
	}
	// 블록에 도달한 경우
	else if (board[nr][nc] != 0) {
		board[nr - 1][nc] = board[r][c];
	}

	board[r][c] = 0;
}

void gravity() {
	// 아래부터 위까지 탐색하기
	// 차례차례 벽돌들이 쌓인다.
	for (int r = h - 2; r > -1; r--) {
		for (int c = 0; c < w; c++) {
			if (board[r][c] > 0 && board[r + 1][c] == 0) {
				move(r, c);
			}
		}
	}

}

int put_dolls(int sc) {
	// 가장 위칸에서 구슬을 출발시킨다.
	int sr = 0;
	int b_num = 0;

	// 맨 마지막까지 벽돌을 탐색한다.
	while (sr + 1 < h) {
		if (board[sr][sc] != 0) break;
		sr += 1;
	}

	// 마지막 지점에 도달한 경우
	// 마지막 벽돌이 없다면 탐색할 필요가 없다.
	if (sr == h - 1 && board[sr][sc] == 0) return 0;

	memset(visited, 0, sizeof(visited));

	// 깰 수 있는 벽돌 정보를 탐색한다.
	queue<node> q = {};
	q.push({ sr,sc });

	while (!q.empty()) {
		node now = q.front();
		q.pop();

		int r, c;
		r = now.r;
		c = now.c;

		int k = board[r][c];
		visited[r][c] = 1;


		// k-1 거리만큼 탐색한다.
		for (int ki = 1; ki < k; ki++) {
			for (int i = 0; i < 4; i++) {
				int nr, nc;
				nr = r + dr[i] * ki;
				nc = c + dc[i] * ki;

				if (0 > nr || h <= nr || 0 > nc || w <= nc) continue;
				if (visited[nr][nc] != 0) continue;
				if (board[nr][nc] == 0) continue;

				q.push({ nr,nc });
			}
		}
	}

	// 벽돌판 정보, 깬 벽돌 수를 갱신한다.
	for (int r = 0; r < h; r++) {
		for (int c = 0; c < w; c++) {
			if (visited[r][c] == 0) continue;

			board[r][c] = 0;
			b_num += 1;
		}
	}

	// 벽돌판 중력 작용하기
	gravity();

	return b_num;
}

void dfs(int a) {
	// 모든 벽돌들을 깰 수 있는 경우
	// 이 후부터 더 볼 필요가 없다.
	if (is_max) {
		return;
	}
	// 경우의 수 완성
	if (a >= n) {
		int total_b_num = 0;

		// 구슬을 던지는 경우
		// 없앨 수 있는 벽돌 개수 세기
		for (int i = 0; i < dolls.size(); i++) {
			total_b_num += put_dolls(dolls[i]);
		}

		// 기존 벽돌맵 복구하기
		for (int r = 0; r < h; r++) {
			for (int c = 0; c < w; c++) {
				board[r][c] = tmp_board[r][c];
			}
		}

		// 최대 없어지는 벽돌 개수 갱신하기
		if (total_b_num > max_b_num) {
			max_b_num = total_b_num;

			if (max_b_num == total_num) {
				is_max = true;
			}
		}
		return;
	}


	// 구슬을 떨어뜨리는 경우의 수 탐색
	// 순서도 고려한다.
	for (int i = 0; i < w; i++) {
		dolls.push_back(i);
		dfs(a + 1);
		dolls.pop_back();
	}
}

int main() {
	int t = 0;
	cin >> t;

	for (int ti = 0; ti < t; ti++) {
		cin >> n >> w >> h;

		// 초기화
		max_b_num = 0;
		total_num = 0;
		is_max = false;

		// 벽돌판 정보 입력
		// 기존 벽돌들 개수 세기
		for (int r = 0; r < h; r++) {
			for (int c = 0; c < w; c++) {
				cin >> board[r][c];
				tmp_board[r][c] = board[r][c];

				if (board[r][c] > 0) {
					total_num += 1;
				}

			}
		}

		dfs(0);

		cout << "#" << ti + 1 << " " << total_num - max_b_num << endl;
	}

	return 0;
}
