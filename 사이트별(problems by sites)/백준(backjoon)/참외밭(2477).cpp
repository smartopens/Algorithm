#include <iostream>

using namespace std;

// 육각형의 참외밭이 있다. (1m당 개수 주어짐)
// 참외밭의 각 길이와 방향이 주어진다. (동1,서2,남3,북4)

int k;
int max_sv;
int min_sv;

int max_h, max_w;

struct s_no
{
	int di;
	int len;
};

s_no s_info[6];

int main()
{
	cin >> k;
	int di, len;
	for (int i = 0; i < 6; i++)
	{
		cin >> di >> len;
		s_info[i] = { di, len };
	}

	int ndi, nlen;
	int to_di, to_len;
	for (int i = 0; i < 6; i++)
	{
		ndi = s_info[i].di;
		nlen = s_info[i].len;

		if (ndi == 1 || ndi == 2)
		{
			max_w = max(max_w, nlen);
		}
		if (ndi == 3 || ndi == 4)
		{
			max_h = max(max_h, nlen);
		}
	}

	for (int i = 0; i < 6; i++)
	{
		if (i == 5)
		{
			ndi = s_info[i].di;
			nlen = s_info[i].len;
			to_di = s_info[0].di;
			to_len = s_info[0].len;
		}
		else {
			ndi = s_info[i].di;
			nlen = s_info[i].len;
			to_di = s_info[i + 1].di;
			to_len = s_info[i + 1].len;
		}

		// 13, 32, 41, 24
		if (ndi == 1 && to_di == 3)
		{
			min_sv = nlen * to_len;
		}
		else if (ndi == 3 && to_di == 2)
		{
			min_sv = nlen * to_len;
		}
		else if (ndi == 4 && to_di == 1)
		{
			min_sv = nlen * to_len;
		}
		else if (ndi == 2 && to_di == 4)
		{
			min_sv = nlen * to_len;
		}
	}

	cout << (max_h * max_w - min_sv) * k << endl;

	return 0;
}