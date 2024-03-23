#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

// 피자 반죽을 오븐에 넣기
// 오븐: D개의 층으로 이루어짐 (원판 층)
// 가장 최상단 피자의 깊이를 구하기

int d, n;

vector<int> p_oven;
queue<int> p_oven_tmp;
vector<int> p_info;

int vi[300002];

int main()
{
	cin >> d >> n;
	int p_in;
	for (int i = 0; i < d; i++)
	{
		cin >> p_in;
		p_oven.push_back(p_in);

		if (i == 0) continue;
		if (p_in > p_oven[i - 1])
		{
			p_oven[i] = p_oven[i - 1];
		}
	}

	int p_r;
	for (int s = 0; s < n; s++)
	{
		cin >> p_r;
		p_info.push_back(p_r);
	}

	// 층: 반대
	int o_id = d - 1;
	int p_id = 0;
	while (o_id > -1)
	{
		// 피자가 오븐보다 클 경우
		if (p_info[p_id] > p_oven[o_id])
		{
			o_id -= 1;
		}
		// 피자가 오븐에 들어가는 경우
		else
		{
			p_id += 1;
			o_id -= 1;
		}

		// 모든 피자를 채운 경우
		if (p_id == n)
		{
			o_id += 1;
			break;
		}
	}

	bool p_ok = false;

	if (p_id >= n)
	{
		p_ok = true;
	}

	if (p_ok == false)
	{
		cout << 0 << endl;
	}
	else
	{
		cout << o_id+1 << endl;
	}

	return 0;
}