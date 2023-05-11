#define _CRT_SECURE_NO_WARNINGS

#include <cstring>
#include <iostream>

using namespace std;

// 지역 구 정보 설정
int n;
int board[20][20];
int last_area[20][20];

// 총 인구수, 선거구 인구 최소 경우 값 선언
int total_num = 0;
int min_gap = 21e8;

// 점수를 고려한다.
void count_score(int sr, int sc, int d1, int d2) {
	// sr, sc : 선거구 윗 지점 / sr_down, sc_down: 선거구 아랫지점 
	// 선거구 최대 인구 경우, 최소 인구 경우
	int sr_down, sc_down;
	int max_a_num = -21e8;
	int min_a_num = 21e8;

	sr_down = sr + d1 + d2;
	sc_down = sc - d1 + d2;

	// 선거구 1번지역 인구 고려하기
	int rest_num = 0;
	int tmp_s = 0;
	for (int r = 0; r < sr + d1; r++) {
		for (int c = 0; c < sc + 1; c++) {
			if (last_area[r][c] == 1) break;

			tmp_s += board[r][c];
			rest_num += board[r][c];
			last_area[r][c] = 1;
		}
	}
	if (tmp_s > max_a_num) max_a_num = tmp_s;
	if (tmp_s < min_a_num) min_a_num = tmp_s;

	// 선거구 2번지역 인구 고려하기
	tmp_s = 0;
	for (int r = 0; r < sr + d2 + 1; r++) {
		for (int c = n - 1; c > sc; c--) {
			if (last_area[r][c] == 1) break;

			tmp_s += board[r][c];
			rest_num += board[r][c];
			last_area[r][c] = 2;
		}
	}
	if (tmp_s > max_a_num) max_a_num = tmp_s;
	if (tmp_s < min_a_num) min_a_num = tmp_s;

	// 선거구 3번지역 인구 고려하기
	tmp_s = 0;
	for (int r = sr + d1; r < n; r++) {
		for (int c = 0; c < sc_down; c++) {
			if (last_area[r][c] == 1) break;

			tmp_s += board[r][c];
			rest_num += board[r][c];
			last_area[r][c] = 3;
		}
	}
	if (tmp_s > max_a_num) max_a_num = tmp_s;
	if (tmp_s < min_a_num) min_a_num = tmp_s;

	// 선거구 4번지역 인구 고려하기
	tmp_s = 0;
	for (int r = sr + d2 + 1; r < n; r++) {
		for (int c = n - 1; c > sc_down - 1; c--) {
			if (last_area[r][c] == 1) break;

			tmp_s += board[r][c];
			rest_num += board[r][c];
			last_area[r][c] = 4;
		}
	}
	if (tmp_s > max_a_num) max_a_num = tmp_s;
	if (tmp_s < min_a_num) min_a_num = tmp_s;

	// 마지막 선거구 인구 수 구하기
	int last_num = total_num - rest_num;
	if (last_num > max_a_num) max_a_num = last_num;
	if (last_num < min_a_num) min_a_num = last_num;

	// 최소 인구 경우를 갱신한다.
	if (max_a_num - min_a_num < min_gap) min_gap = max_a_num - min_a_num;

}

// 선거구를 나눈다.
// 가장 위 경계점을 시작점으로 생각한다.
// 시작점에서 d1, d2의 변화에 따라서 선거구를 나눈다.
void count_case() {
	// d1, d2가 1부터 증가한다.
	// 해당 경우에서 시작점으로부터 선거구를 설정한다.
	// 선거구가 정해지면 인구 수를 고려한다.

	// d1, d2의 최소 거리는 1이다.
	// d1, d2의 최대 거리는 n-2이다.
	for (int d1 = 1; d1 < n - 1; d1++) {
		for (int d2 = 1; d2 < n - 1; d2++) {

			for (int sr = 0; sr < n; sr++) {
				for (int sc = 0; sc < n; sc++) {
					// 선거구의 행의 경우와 열의 경우를 생각한다.
					// 행의 경우: 시작 지점부터 끝지점까지 구역안에 있다.
					// 열의 경우: 시작 지점부터 끝지점까지 구역안에 있다.

					if (sr + d1 + d2 > n - 1) continue;
					if (sc < d1 || sc > n - 1 - d2) continue;

					// 선거구 경계 정보 초기화하기
					memset(last_area, 0, sizeof(last_area));
					int r = sr;
					int c = sc;

					for (int di = 0; di < d1; di++) {
						r += 1;
						c -= 1;
						last_area[r][c] = 1;
					}

					for (int di = 0; di < d2; di++) {
						r += 1;
						c += 1;
						last_area[r][c] = 1;
					}

					for (int di = 0; di < d1; di++) {
						r -= 1;
						c += 1;
						last_area[r][c] = 1;
					}

					for (int di = 0; di < d2; di++) {
						r -= 1;
						c -= 1;
						last_area[r][c] = 1;
					}

					// 인구 수 고려하기
					count_score(sr, sc, d1, d2);

				}
			}

		}
	}
}

int main() {
	cin >> n;

	// 선거구 인구 정보 입력 받기
	// 총 인구수를 저장한다.
	for (int r = 0; r < n; r++) {
		for (int c = 0; c < n; c++) {
			cin >> board[r][c];
			total_num += board[r][c];
		}
	}

	// 선거구를 나눈다.
	count_case();

	// 선거구 최소 인구 경우 값 출력하기
	cout << min_gap << endl;

	return 0;
}
