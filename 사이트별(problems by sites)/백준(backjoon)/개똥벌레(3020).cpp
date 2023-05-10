#define _CRT_SECURE_NO_WARNINGS

#include <iostream>

using namespace std;

// 석순과 종유석 기록
int n, h;
int top[500002];
int bottom[500002];

int main() {
	// 깊이와 높이 입력받기
	cin >> n >> h;

	// 장애물을 최소로 만나는 개수
	// 위의 경우의 수를 기록한다.
	int min_val = 21e8;
	int cnt = 0;

	// 짝수번에는 석순을, 홀수번에는 종유석을 기록한다.
	// 이 때, 각 물건들이 구간에 겹치는 경우를 세야한다.
	// 일일히 셀 경우 깊이와 높이가 너무 크기 때문에 시간이 부족하다.
	// 고로, 각 물건의 마지막 지점들을 기록한다.
	for (int i = 0; i < n; i++)
	{
		int num;
		cin >> num;

		if (i % 2 == 0) {
			bottom[num] += 1;
		}
		else if (i % 2 == 1) {
			top[h - num + 1] += 1;
		}
	}

	// 마지막 지점을 기준으로 구간의 개수를 더해준다.
	// 이렇게 하면 각 구간에서 막대를 만나는 경우를 알 수 있다.
	// 개념 자체는 누적합이라고 한다.

	// 석순
	for (int i = h; i > 1; i--)
	{
		bottom[i - 1] += bottom[i];
	}

	// 종유석
	for (int i = 1; i < h; i++)
	{
		top[i + 1] += top[i];
	}

	// 각 구간에서 최소 경우의 수를 고려한다.
	// 이때 숫자도 같이 센다.
	for (int i = 1; i < h + 1; i++)
	{
		if (bottom[i] + top[i] < min_val)
		{
			min_val = bottom[i] + top[i];
			cnt = 1;
		}
		else if (bottom[i] + top[i] == min_val)
		{
			cnt += 1;
		}
	}

	// 최소 경우, 해당 경우의 수 출력
	cout << min_val << " " << cnt << endl;
	return 0;
}
