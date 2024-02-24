#include <iostream>
#include <algorithm>

using namespace std;

int n;
int w_val[100002];

int left_v, right_v;
int tar_sn;

int main()
{
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> w_val[i];
	}

	sort(w_val, w_val + n);

	left_v = 0;
	right_v = 0;
	tar_sn = 21e8;
	int l_id = 0;
	int r_id = n - 1;
	int w_sn = 0;

	while (l_id < r_id)
	{
		w_sn = w_val[l_id] + w_val[r_id];
		
		if (abs(w_sn) < tar_sn)
		{
			tar_sn = abs(w_sn);
			left_v = w_val[l_id];
			right_v = w_val[r_id];
		}

		if (w_sn >= 0)
		{
			r_id -= 1;
		}
		else
		{
			l_id += 1;
		}
	}

	cout << left_v << " " << right_v << endl;
	return 0;
}