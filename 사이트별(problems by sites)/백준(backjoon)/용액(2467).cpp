#include <iostream>

using namespace std;

int n;
int positions[100002];

int min_v;
int l_v;
int r_v;

// 용액들 중에서 합이 0에 가까워지는 경우를 찾는다.
// 이 때 n개의 경우에서 시작점을 차례로 줄여가며 찾기.
// 용액의 합이 0보다 크다면 합을 줄이는 경우로 인덱스를 조정한다.
// 반대의 경우는 합을 키우는 경우로 조정한다.
void z_find()
{
	int l_id = 0;
	int r_id = n - 1;
	int m_id = 0;
	int now_v = 21e8;

	while (l_id < r_id)
	{
		now_v = positions[l_id] + positions[r_id];

		if (abs(min_v) > abs(now_v))
		{
			l_v = positions[l_id];
			r_v = positions[r_id];
			min_v = abs(now_v);
		}

		if (now_v == 0)
		{
			return;
		}
		else if (now_v < 0)
		{
			l_id += 1;
		}
		else if (now_v > 0)
		{
			r_id -= 1;
		}
	}
}

int main()
{
	cin >> n;

	// 용액 값을 입력 받는다.
	for (int i = 0; i < n; i++)
	{
		cin >> positions[i];
	}

	// 최소 용액 합의 값을 초기화 하기
	// 문제조건을 고려한다.
	min_v = 21e8;

	// 용액의 합이 0에 가까워지는 경우를 찾는다.
	z_find();

	cout << l_v << " ";
	cout << r_v << endl;

	return 0;
}
